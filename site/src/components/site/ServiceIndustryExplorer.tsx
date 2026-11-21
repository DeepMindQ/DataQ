"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowRight, ArrowUpRight, Building2, ChevronRight } from "lucide-react";

/* ── ServiceIndustryExplorer — the service × industry lens ──────────────────
   A CXO lands on a service page from any of our 12 industries. This panel
   answers one question in their language: "what would you deliver for MY
   sector, and what would you hold yourself to?" All data is baked into the
   page JSON at build time (static-export safe, hydration-safe: the default
   selection is derived from props, never from Math.random / Date). */

export type ExplorerIndustry = {
  slug: string;
  name: string;
  flagship: boolean;
  hook: string;
  plays: string[];
  kpis: { label: string; value: string }[];
  capUrl: string;
};

export function ServiceIndustryExplorer({
  title,
  intro,
  service,
  practiceNote,
  industries,
}: {
  title: string;
  intro: string;
  service: string;
  practiceNote?: string;
  industries: ExplorerIndustry[];
}) {
  // deterministic default: first flagship, else first entry
  const defaultIdx = Math.max(
    0,
    industries.findIndex((i) => i.flagship),
  );
  const [active, setActive] = useState(defaultIdx);
  const sel = industries[active];
  if (!sel) return null;

  return (
    <section className="explorer mt-10" aria-label={`${service} across industries`}>
      <div className="overflow-hidden rounded-2xl border border-white/10 grad-navy-field shadow-3">
        {/* header */}
        <div className="flex flex-wrap items-center justify-between gap-2 border-b border-white/10 px-5 py-3.5 sm:px-6">
          <div>
            <p className="text-[13.5px] font-semibold text-white">{title}</p>
            <p className="mt-0.5 max-w-2xl text-[11.5px] leading-relaxed text-white/55">{intro}</p>
            {practiceNote && (
              <p className="mt-1.5 max-w-2xl text-[11.5px] font-medium leading-relaxed text-brand-300/90">{practiceNote}</p>
            )}
          </div>
          <span className="inline-flex items-center gap-1.5 rounded-full border border-brand/40 bg-brand/15 px-2.5 py-1 text-[10px] font-bold uppercase tracking-[0.14em] text-brand-300">
            <Building2 className="h-3 w-3" aria-hidden="true" />
            12 industries
          </span>
        </div>

        {/* industry chip row */}
        <div className="flex flex-wrap gap-2 px-5 pt-4 sm:px-6" role="tablist" aria-label="Choose your industry">
          {industries.map((ind, i) => (
            <button
              key={ind.slug}
              role="tab"
              aria-selected={i === active}
              onClick={() => setActive(i)}
              className={`group inline-flex items-center gap-1.5 rounded-full border px-3.5 py-1.5 text-[11.5px] font-medium transition ${
                i === active
                  ? "border-brand bg-brand text-white shadow-2"
                  : "border-white/15 bg-white/[0.05] text-white/70 hover:border-brand/50 hover:text-white"
              }`}
            >
              {ind.flagship && (
                <span
                  className={`inline-block h-1.5 w-1.5 rounded-full ${i === active ? "bg-white" : "bg-brand"}`}
                  aria-hidden="true"
                  title="Flagship sector for this service"
                />
              )}
              {ind.name}
            </button>
          ))}
        </div>

        {/* selected panel */}
        <div className="px-5 pb-5 pt-4 sm:px-6 sm:pb-6" role="tabpanel">
          <div className="grid gap-5 lg:grid-cols-[minmax(0,1.15fr)_minmax(0,1fr)]">
            {/* left — hook + plays */}
            <div className="rounded-xl border border-white/10 bg-white/[0.04] p-4 sm:p-5">
              <p className="text-[10.5px] font-bold uppercase tracking-[0.14em] text-brand-300">
                {service} in {sel.name}
              </p>
              <p className="mt-2 text-[13px] leading-relaxed text-white/80">{sel.hook}</p>
              <p className="mt-4 text-[10.5px] font-bold uppercase tracking-[0.14em] text-white/45">
                What we deliver here
              </p>
              <ul className="mt-2 space-y-2">
                {sel.plays.map((p, i) => (
                  <li
                    key={i}
                    className="flex items-start gap-2.5 text-[12.5px] leading-relaxed text-white/75"
                    style={{ animation: `dash-in 0.4s ${0.1 + i * 0.08}s both` }}
                  >
                    <ChevronRight className="mt-0.5 h-3.5 w-3.5 shrink-0 text-brand-300" aria-hidden="true" />
                    {p}
                  </li>
                ))}
              </ul>
            </div>

            {/* right — KPI targets + deep links */}
            <div className="flex flex-col gap-4">
              <div className="rounded-xl border border-white/10 bg-white/[0.04] p-4 sm:p-5">
                <p className="text-[10.5px] font-bold uppercase tracking-[0.14em] text-white/45">
                  Targets we sign for {sel.name} builds
                </p>
                <div className="mt-3 grid grid-cols-3 gap-2">
                  {sel.kpis.map((k, i) => (
                    <div
                      key={k.label}
                      className="rounded-lg border border-white/10 bg-navy-950/50 px-2.5 py-2.5 text-center"
                      style={{ animation: `dash-in 0.4s ${0.15 + i * 0.1}s both` }}
                    >
                      <p className="font-display text-[17px] font-bold leading-none tabular-nums text-brand-300 sm:text-[19px]">
                        {k.value}
                      </p>
                      <p className="mt-1.5 text-[9.5px] font-medium leading-tight text-white/55">{k.label}</p>
                    </div>
                  ))}
                </div>
              </div>
              <Link
                href={sel.capUrl}
                className="group flex items-center justify-between gap-3 rounded-xl border border-brand/35 bg-brand/10 px-4 py-3 transition hover:border-brand hover:bg-brand/20"
              >
                <span>
                  <span className="block text-[12.5px] font-semibold text-white">
                    {service} × {sel.name} — the full sector brief
                  </span>
                  <span className="mt-0.5 block text-[11px] text-white/55">
                    Workflows, controls and reference cases for this exact combination
                  </span>
                </span>
                <ArrowUpRight className="h-4.5 w-4.5 shrink-0 text-brand-300 transition group-hover:translate-x-0.5 group-hover:-translate-y-0.5" aria-hidden="true" />
              </Link>
            </div>
          </div>
        </div>

        {/* footer strip */}
        <div className="flex flex-wrap items-center justify-between gap-2 border-t border-white/10 px-5 py-3 text-[10.5px] text-white/45 sm:px-6">
          <span>
            Orange dot marks flagship sectors where {service} carries our deepest delivery record.
          </span>
          <Link href="/industries/" className="inline-flex items-center gap-1 font-semibold text-white/65 transition hover:text-brand-300">
            All industries <ArrowRight className="h-3 w-3" aria-hidden="true" />
          </Link>
        </div>
      </div>
    </section>
  );
}
