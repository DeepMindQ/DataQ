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

/* Top-20 #16: section taxonomy for grouping + filter pills. */
const SECTION_RULES: [RegExp, string][] = [
  [/^\/services/, "Services"],
  [/^\/consulting/, "Consulting"],
  [/^\/industries/, "Industries"],
  [/^\/solutions/, "Solutions"],
  [/^\/platforms/, "Platforms"],
  [/^\/case-studies/, "Case studies"],
  [/^\/insights/, "Insights"],
  [/^\/newsroom/, "Newsroom"],
  [/^\/(about-us|why-dataq|careers|leadership|global-offices|values-culture|contact|book-a-briefing|partner-ecosystem)/, "Company"],
];

function sectionOf(url: string): string {
  for (const [re, name] of SECTION_RULES) if (re.test(url)) return name;
  return "Other";
}

const SECTION_ORDER = ["Services", "Consulting", "Industries", "Solutions", "Platforms", "Case studies", "Insights", "Newsroom", "Company", "Other"];

/* Pagefind v1 auto-prefixes result URLs with its own directory's parent path
   (on the GitHub Pages project site, the configured base path) — but <Link>
   applies the base path AGAIN, doubling it. Strip it here; Link re-adds. */
const PF_BP = process.env.NEXT_PUBLIC_BASE_PATH || "";
function stripBasePath(u: string): string {
  return PF_BP && u.startsWith(PF_BP + "/") ? u.slice(PF_BP.length) : u;
}

function SearchInner() {
  const params = useSearchParams();
  const initial = params.get("q") || "";
  const [query, setQuery] = useState(initial);
  const [results, setResults] = useState<PagefindDoc[] | null>(null);
  const [available, setAvailable] = useState<boolean | null>(null);
  const [filter, setFilter] = useState<string>("All");
  const pfRef = useRef<PagefindApi | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        // Pagefind indexes at the site root during static export. The import
        // must respect the GitHub Pages base path — a root-absolute
        // "/pagefind/..." 404s on project sites and search silently breaks.
        const base = process.env.NEXT_PUBLIC_BASE_PATH || "";
        const pf = (await import(/* webpackIgnore: true */ `${base}/pagefind/pagefind.js`)) as unknown as PagefindApi;
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
      // pagefind v1.6: r.data is a FUNCTION returning a promise — call it.
      // Passing the bare reference yields functions as "docs", whose .url is
      // undefined and crashes <Link> at formatUrl (production hard-crash).
      // Also drop any doc without a usable URL string as extra armor.
      const docs = (await Promise.all(res.results.slice(0, 20).map((r) => r.data())))
        .filter((d) => typeof d.url === "string" && d.url.length > 0)
        .map((d) => ({ ...d, url: stripBasePath(d.url) }));
      if (!cancelled) {
        setResults(docs);
        // consent-gated analytics: fires only when Plausible is active
        import("@/components/site/ConsentAnalytics").then(({ trackEvent }) =>
          trackEvent("Search", { query: q.slice(0, 80), results: String(docs.length) })
        );
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [query, available]);

  const shown = results?.filter((d) => filter === "All" || sectionOf(d.url) === filter) ?? null;
  const sections = results
    ? SECTION_ORDER.filter((s) => results.some((d) => sectionOf(d.url) === s))
    : [];

  return (
    <section className="container-dq max-w-4xl py-16">
      <h1 className="text-display-3 text-navy-800">Search</h1>
      <div className="relative mt-6">
        <Search className="absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-body/40" />
        <input
          ref={inputRef}
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Escape") {
              setQuery("");
              inputRef.current?.focus();
            }
          }}
          placeholder="Search 700+ pages — services, industries, platforms, case studies…"
          className="w-full rounded-[10px] border border-line bg-white px-11 py-3.5 text-[14.5px] text-navy-800 shadow-1 focus:border-brand focus:outline-none focus:ring-2 focus:ring-brand/50"
          aria-label="Search query"
          aria-describedby="search-hint"
        />
        <p id="search-hint" className="sr-only">
          Press Escape to clear the query.
        </p>
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

      {results && results.length > 0 && (
        <div className="mt-6 flex flex-wrap gap-2" role="group" aria-label="Filter results by section">
          {["All", ...sections].map((s) => (
            <button
              key={s}
              type="button"
              onClick={() => setFilter(s)}
              aria-pressed={filter === s}
              className={`rounded-full border px-3.5 py-1.5 text-[12.5px] font-medium transition ${
                filter === s
                  ? "border-brand bg-brand text-white"
                  : "border-line bg-white text-navy-800/80 hover:border-brand/60"
              }`}
            >
              {s}
              {s === "All" && <span className="ml-1 opacity-60">{results.length}</span>}
            </button>
          ))}
        </div>
      )}

      {shown && (
        <div className="mt-8 space-y-3" aria-live="polite">
          <p className="text-[12.5px] text-slate-body/60">
            {shown.length === 0
              ? `No results${filter !== "All" ? " in " + filter : ""}.`
              : `${shown.length} result${shown.length === 1 ? "" : "s"}${filter !== "All" ? " in " + filter : ""}`}
          </p>
          {shown.map((doc) => (
            <Link
              key={doc.url}
              href={doc.url}
              className="block rounded-xl border border-line bg-white p-4 transition hover:border-brand/60 shadow-1 hover:shadow-2"
            >
              <p className="text-[10.5px] font-bold uppercase tracking-[0.14em] text-brand-deep">{sectionOf(doc.url)}</p>
              <p className="mt-1 text-[14px] font-semibold text-navy-800">{doc.meta?.title || doc.url}</p>
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
