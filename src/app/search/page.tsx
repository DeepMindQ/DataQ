"use client";

import { Suspense, useEffect, useRef, useState } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { Search } from "lucide-react";

type PagefindDoc = {
  url: string;
  meta: { title?: string };
  excerpt?: string;
};
type PagefindHit = { id: string; data: Promise<PagefindDoc> };
type PagefindApi = {
  search: (q: string) => Promise<{ results: PagefindHit[] }>;
};

function SearchInner() {
  const params = useSearchParams();
  const initial = params.get("q") || "";
  const [query, setQuery] = useState(initial);
  const [results, setResults] = useState<PagefindDoc[] | null>(null);
  const [available, setAvailable] = useState<boolean | null>(null);
  const pfRef = useRef<PagefindApi | null>(null);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const pf = (await import(/* webpackIgnore: true */ "/pagefind/pagefind.js")) as unknown as PagefindApi;
        if (cancelled) return;
        pfRef.current = pf;
        setAvailable(true);
      } catch {
        if (!cancelled) setAvailable(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    const q = query.trim();
    if (!available || !pfRef.current) return;
    let cancelled = false;
    (async () => {
      if (!q) {
        setResults(null);
        return;
      }
      const res = await pfRef.current!.search(q);
      const docs = await Promise.all(res.slice(0, 20).map((r) => r.data));
      if (!cancelled) setResults(docs);
    })();
    return () => {
      cancelled = true;
    };
  }, [query, available]);

  return (
    <section className="container-dq max-w-4xl py-16">
      <h1 className="text-display-3 text-navy-800">Search</h1>
      <div className="relative mt-6">
        <Search className="absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-body/40" />
        <input
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search 630+ pages — services, industries, platforms, case studies…"
          className="w-full rounded-[10px] border border-line bg-white px-11 py-3.5 text-[14.5px] text-navy-800 shadow-1 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/50"
          aria-label="Search query"
        />
      </div>

      {available === false && (
        <div className="mt-8 rounded-xl border border-brand/30 bg-brand-tint p-5 text-[13.5px] text-slate-body/80">
          <p className="font-semibold text-navy-800">Search index activates with the production build.</p>
          <p className="mt-1">
            Pagefind indexes the site during static export. Until then, browse from{" "}
            <Link href="/services/" className="underline">Services</Link>,{" "}
            <Link href="/industries/" className="underline">Industries</Link> or{" "}
            <Link href="/html-sitemap/" className="underline">the full sitemap</Link>.
          </p>
        </div>
      )}

      {results && (
        <div className="mt-8 space-y-3">
          <p className="text-[12.5px] text-slate-body/60">
            {results.length === 0 ? "No results." : `${results.length} result${results.length === 1 ? "" : "s"}`}
          </p>
          {results.map((doc) => (
            <Link
              key={doc.url}
              href={doc.url}
              className="block rounded-xl border border-line bg-white p-4 transition hover:border-brand/60 shadow-1 hover:shadow-2"
            >
              <p className="text-[14px] font-semibold text-navy-800">{doc.meta?.title || doc.url}</p>
              {doc.excerpt && (
                <p
                  className="mt-1 text-[12.5px] leading-relaxed text-slate-body/70 [&_mark]:bg-brand/25 [&_mark]:rounded"
                  dangerouslySetInnerHTML={{ __html: doc.excerpt }}
                />
              )}
            </Link>
          ))}
        </div>
      )}
    </section>
  );
}

export default function SearchPage() {
  return (
    <Suspense fallback={<div className="mx-auto max-w-4xl px-6 py-16 text-slate-body">Loading…</div>}>
      <SearchInner />
    </Suspense>
  );
}
