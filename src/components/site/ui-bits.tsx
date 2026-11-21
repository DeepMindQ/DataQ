"use client";

import { useId, useRef, useState } from "react";

/* ── Wave 1 design-system primitives (CHG-059/060/061/064/065/073/074/
   075/078/083/084/085/094). Shared by page templates built in Waves 2-4.
   All motion respects prefers-reduced-motion via globals.css tokens. ──── */

/* Tabs with sliding orange indicator (CHG-059) */
export function Tabs({
  items,
}: {
  items: { id: string; label: string; content: React.ReactNode }[];
}) {
  const [active, setActive] = useState(items[0]?.id);
  const refs = useRef<Record<string, HTMLButtonElement | null>>({});
  function onKeyDown(e: React.KeyboardEvent) {
    const idx = items.findIndex((i) => i.id === active);
    if (e.key === "ArrowRight") {
      const next = items[(idx + 1) % items.length];
      setActive(next.id);
      refs.current[next.id]?.focus();
    } else if (e.key === "ArrowLeft") {
      const prev = items[(idx - 1 + items.length) % items.length];
      setActive(prev.id);
      refs.current[prev.id]?.focus();
    }
  }
  return (
    <div>
      <div role="tablist" aria-label="Content sections" className="relative flex gap-1 border-b border-line" onKeyDown={onKeyDown}>
        {items.map((it) => (
          <button
            key={it.id}
            ref={(el) => {
              refs.current[it.id] = el;
            }}
            role="tab"
            aria-selected={active === it.id}
            tabIndex={active === it.id ? 0 : -1}
            onClick={() => setActive(it.id)}
            className={`relative px-4 py-2.5 text-[13px] font-medium transition-colors ${
              active === it.id ? "text-brand-deep" : "text-slate-body hover:text-navy-800"
            }`}
          >
            {it.label}
            {/* sliding indicator: every tab has one, only the active is scaled */}
            <span
              aria-hidden="true"
              className={`absolute inset-x-3 -bottom-px h-0.5 rounded-full bg-brand transition-transform duration-300 ${
                active === it.id ? "scale-x-100" : "scale-x-0"
              }`}
            />
          </button>
        ))}
      </div>
      {items.map((it) => (
        <div key={it.id} role="tabpanel" hidden={active !== it.id} className="pt-5 text-[14px] leading-relaxed text-slate-body">
          {it.content}
        </div>
      ))}
    </div>
  );
}

/* Accordion with height animation + plus/minus morph (CHG-060) */
export function Accordion({
  items,
  singleOpen = true,
}: {
  items: { q: string; a: React.ReactNode }[];
  singleOpen?: boolean;
}) {
  const [open, setOpen] = useState<Set<string>>(new Set(items[0] ? [items[0].q] : []));
  function toggle(q: string) {
    setOpen((prev) => {
      const next = new Set(singleOpen && !prev.has(q) ? [] : prev);
      if (next.has(q)) next.delete(q);
      else next.add(q);
      return next;
    });
  }
  return (
    <div className="divide-y divide-line rounded-2xl border border-line bg-white shadow-1">
      {items.map((it) => {
        const isOpen = open.has(it.q);
        return (
          <div key={it.q}>
            <button
              onClick={() => toggle(it.q)}
              aria-expanded={isOpen}
              className="flex w-full items-center justify-between gap-4 px-5 py-4 text-left"
            >
              <span className="text-[14px] font-semibold text-navy-800">{it.q}</span>
              <span aria-hidden="true" className="relative h-4 w-4 shrink-0">
                <span className="absolute left-1/2 top-0 h-4 w-0.5 -translate-x-1/2 rounded bg-brand transition-transform duration-300" style={{ transform: isOpen ? "translateX(-50%) rotate(90deg)" : "translateX(-50%)" }} />
                <span className="absolute left-0 top-1/2 h-0.5 w-4 -translate-y-1/2 rounded bg-brand" />
              </span>
            </button>
            <div
              className="grid transition-[grid-template-rows] duration-300"
              style={{ gridTemplateRows: isOpen ? "1fr" : "0fr" }}
            >
              <div className="overflow-hidden">
                <div className="px-5 pb-4 text-[13.5px] leading-relaxed text-slate-body/85">{it.a}</div>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}

/* Tooltip: navy, arrow, 200ms delay, works on light and dark (CHG-061) */
export function Tooltip({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <span className="group/tip relative inline-flex">
      {children}
      <span
        role="tooltip"
        className="pointer-events-none absolute bottom-full left-1/2 z-40 mb-2 -translate-x-1/2 whitespace-nowrap rounded-lg bg-navy-800 px-2.5 py-1.5 text-[11.5px] font-medium text-white opacity-0 shadow-2 transition-opacity duration-200 [transition-delay:200ms] group-hover/tip:opacity-100 group-focus-within/tip:opacity-100"
      >
        {label}
        <span aria-hidden="true" className="absolute left-1/2 top-full -translate-x-1/2 border-4 border-transparent border-t-navy-800" />
      </span>
    </span>
  );
}

/* Pagination for search results and long lists (CHG-064) */
export function Pagination({
  page,
  total,
  onPage,
}: {
  page: number;
  total: number;
  onPage?: (p: number) => void;
}) {
  if (total <= 1) return null;
  const nums: (number | "…")[] = [];
  for (let i = 1; i <= total; i++) {
    if (i === 1 || i === total || Math.abs(i - page) <= 1) nums.push(i);
    else if (nums[nums.length - 1] !== "…") nums.push("…");
  }
  return (
    <nav aria-label="Pagination" className="mt-8 flex items-center justify-center gap-1.5">
      {nums.map((n, i) =>
        n === "…" ? (
          <span key={`e${i}`} className="px-1.5 text-[13px] text-slate-body/50">…</span>
        ) : (
          <button
            key={n}
            aria-current={n === page ? "page" : undefined}
            onClick={() => onPage?.(n)}
            className={`h-9 min-w-9 rounded-[10px] px-2.5 text-[13px] font-medium transition ${
              n === page
                ? "bg-brand text-white"
                : "border border-line text-navy-800 hover:border-brand hover:text-brand-deep"
            }`}
          >
            {n}
          </button>
        ),
      )}
    </nav>
  );
}

/* Skeleton shimmer in navy neutrals (CHG-065) */
export function Skeleton({ className = "" }: { className?: string }) {
  return (
    <div
      aria-hidden="true"
      className={`animate-pulse rounded-xl bg-navy-800/10 ${className}`}
    />
  );
}

/* Numbered process 01-04 with connector (CHG-073; scroll-draw motion lands in Wave 2) */
export function NumberedProcess({ steps }: { steps: { title: string; desc: string }[] }) {
  return (
    <ol className="relative grid gap-8 md:grid-cols-4">
      <span aria-hidden="true" className="absolute left-0 right-0 top-5 hidden h-px bg-line md:block" />
      {steps.map((s, i) => (
        <li key={s.title} className="relative">
          <span className="relative z-10 inline-flex h-10 w-10 items-center justify-center rounded-full border-2 border-brand bg-white font-display text-[13px] font-bold tabular-nums text-brand-deep">
            {String(i + 1).padStart(2, "0")}
          </span>
          <p className="mt-3 text-[14px] font-semibold text-navy-800">{s.title}</p>
          <p className="mt-1 text-[12.5px] leading-relaxed text-slate-body/80">{s.desc}</p>
        </li>
      ))}
    </ol>
  );
}

/* Timeline for company story / case timelines (CHG-074) */
export function Timeline({ events }: { events: { date: string; title: string; desc?: string }[] }) {
  return (
    <ol className="relative space-y-6 border-l-2 border-line pl-6">
      {events.map((e) => (
        <li key={e.date + e.title} className="relative">
          <span aria-hidden="true" className="absolute -left-[31px] top-1 h-3.5 w-3.5 rounded-full border-2 border-brand bg-white" />
          <p className="text-[11.5px] font-semibold uppercase tracking-wider text-brand-deep tabular-nums">{e.date}</p>
          <p className="mt-0.5 text-[14px] font-semibold text-navy-800">{e.title}</p>
          {e.desc && <p className="mt-1 text-[13px] leading-relaxed text-slate-body/80">{e.desc}</p>}
        </li>
      ))}
    </ol>
  );
}

/* Logo wall: grayscale text lockups colorize on hover (CHG-075).
   Uses certification/alliance names, never third-party logos. */
export function LogoWall({ entries }: { entries: string[] }) {
  return (
    <div className="flex flex-wrap items-center gap-x-10 gap-y-4">
      {entries.map((e) => (
        <span
          key={e}
          className="font-display text-[14px] font-bold tracking-wide text-slate-body/45 grayscale transition hover:text-navy-800 hover:grayscale-0"
        >
          {e}
        </span>
      ))}
    </div>
  );
}

/* Glossary tooltip: dotted-underline term with definition popover (CHG-084) */
export function GlossaryTip({ term, def }: { term: string; def: string }) {
  const id = useId();
  return (
    <Tooltip label={def}>
      <button
        type="button"
        aria-describedby={id}
        className="border-b border-dotted border-brand-deep font-medium text-navy-800"
      >
        {term}
        <span id={id} className="sr-only">: {def}</span>
      </button>
    </Tooltip>
  );
}

/* Divider with centered label (CHG-085) */
export function Divider({ label }: { label?: string }) {
  if (!label) return <hr className="my-10 border-line" />;
  return (
    <div className="my-10 flex items-center gap-4" role="separator" aria-label={label}>
      <span className="h-px flex-1 bg-line" />
      <span className="text-[11.5px] font-semibold uppercase tracking-[0.18em] text-slate-body/55">{label}</span>
      <span className="h-px flex-1 bg-line" />
    </div>
  );
}

/* Progress bar + stepper for multi-step forms (CHG-083) */
export function ProgressBar({ value, max = 100 }: { value: number; max?: number }) {
  const pct = Math.min(100, Math.round((value / max) * 100));
  return (
    <div
      role="progressbar"
      aria-valuenow={pct}
      aria-valuemin={0}
      aria-valuemax={100}
      className="h-1.5 w-full overflow-hidden rounded-full bg-mist"
    >
      <div className="h-full rounded-full bg-brand transition-[width] duration-500" style={{ width: `${pct}%` }} />
    </div>
  );
}

export function Stepper({ steps, current }: { steps: string[]; current: number }) {
  return (
    <ol className="flex items-center gap-2" aria-label={`Step ${current + 1} of ${steps.length}`}>
      {steps.map((s, i) => (
        <li key={s} className="flex items-center gap-2">
          <span
            className={`inline-flex h-6 w-6 items-center justify-center rounded-full text-[11px] font-bold tabular-nums ${
              i < current
                ? "bg-brand text-white"
                : i === current
                  ? "border-2 border-brand text-brand-deep"
                  : "border border-line text-slate-body/50"
            }`}
          >
            {i < current ? "✓" : i + 1}
          </span>
          <span className={`text-[12px] ${i === current ? "font-semibold text-navy-800" : "text-slate-body/60"}`}>{s}</span>
          {i < steps.length - 1 && <span aria-hidden="true" className="mx-1 h-px w-6 bg-line" />}
        </li>
      ))}
    </ol>
  );
}

/* Language/region selector stub (CHG-078): en-US active, structure ready */
export function LanguageSelector() {
  const [lang, setLang] = useState("en-US");
  const langs = ["en-US", "en-GB"];
  return (
    <label className="inline-flex items-center gap-1.5 text-[12px] text-slate-body/70">
      <span className="sr-only">Language and region</span>
      <select
        value={lang}
        onChange={(e) => setLang(e.target.value)}
        className="rounded-lg border border-line bg-white px-2 py-1 text-[12px] text-navy-800 focus:outline-none focus:ring-2 focus:ring-brand/70"
      >
        {langs.map((l) => (
          <option key={l} value={l}>
            {l}
          </option>
        ))}
      </select>
    </label>
  );
}
