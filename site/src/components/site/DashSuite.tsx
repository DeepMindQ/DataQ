"use client";

import { useState } from "react";
import { DashWidgetView, KpiStrip } from "./DashWidgets";
import type { DashWidget, DashKpiSpec } from "./DashWidgets";

/* ═══════════════════════════════════════════════════════════════════════════
   DashSuite — the interactive delivery console that anchors every service
   page. A tabbed operations dashboard: KPI strip with sparklines on top,
   tabbed widget area below. Each page feeds its own KPIs, tabs and widgets
   from the page JSON, so no two consoles look or behave alike.

   Static-export safe: all data baked into props. Hydration-safe: initial
   tab derived from props, never from Date/Math.random.
   ═══════════════════════════════════════════════════════════════════════════ */

export type DashTab = { name: string; widgets: DashWidget[] };

export function DashSuite({
  title,
  badge,
  kpis,
  tabs,
  note,
}: {
  title: string;
  badge?: string;
  kpis: DashKpiSpec[];
  tabs: DashTab[];
  note?: string;
}) {
  const [tab, setTab] = useState(0);
  const active = tabs[Math.min(tab, tabs.length - 1)];
  if (!active) return null;
  return (
    <section className="dash-suite mt-6" aria-label={title}>
      <div className="overflow-hidden rounded-2xl border border-white/10 grad-navy-field shadow-3">
        {/* console header */}
        <div className="flex flex-wrap items-center justify-between gap-2 border-b border-white/10 px-5 py-3">
          <div className="flex items-center gap-2.5">
            <span className="relative flex h-2.5 w-2.5">
              <span className="hv-pulse absolute inline-flex h-full w-full rounded-full bg-brand opacity-60" />
              <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-brand" />
            </span>
            <p className="text-[13px] font-semibold text-white">{title}</p>
          </div>
          {badge && (
            <span className="rounded-full border border-brand/40 bg-brand/15 px-3 py-1 text-[10px] font-bold uppercase tracking-[0.14em] text-brand-300">
              {badge}
            </span>
          )}
          {/* E-05: provenance chip — every numeric panel states its source */}
          <span className="rounded-full border border-white/20 bg-white/[0.06] px-3 py-1 text-[9.5px] font-bold uppercase tracking-[0.14em] text-white/55">
            Illustrative · reference program
          </span>
        </div>

        {/* KPI strip */}
        <div className="px-4 pt-4 sm:px-5">
          <KpiStrip kpis={kpis} />
        </div>

        {/* tab bar */}
        <div className="mt-4 flex gap-1.5 overflow-x-auto border-b border-white/10 px-4 pb-0 sm:px-5" role="tablist" aria-label="Console views">
          {tabs.map((t, i) => (
            <button
              key={t.name}
              role="tab"
              aria-selected={i === tab}
              onClick={() => setTab(i)}
              className={`whitespace-nowrap rounded-t-lg border-x border-t px-4 py-2 text-[11.5px] font-semibold transition ${
                i === tab
                  ? "border-white/10 border-b-transparent bg-white/[0.08] text-white"
                  : "border-transparent text-white/50 hover:text-white/85"
              }`}
            >
              {t.name}
            </button>
          ))}
        </div>

        {/* tab body */}
        <div className="px-4 py-4 sm:px-5" role="tabpanel">
          <div className={`grid gap-4 ${active.widgets.length > 1 ? "xl:grid-cols-2" : ""}`}>
            {active.widgets.map((w, i) => (
              <div
                key={`${active.name}-${i}`}
                className="min-w-0"
                style={{ animation: `dash-in .45s ${0.08 * i}s both` }}
              >
                <DashWidgetView w={w} />
              </div>
            ))}
          </div>
        </div>

        {note && (
          <p className="border-t border-white/10 px-5 py-2.5 text-[11px] leading-relaxed text-white/45">{note}</p>
        )}
      </div>
    </section>
  );
}
