"use client";

/* ── HomeExecutive: steering pack (4 equal panels) + hero outcome console.
   All figures are illustrative composites, footnoted on every panel.
   Batch 2 of the 50% roadmap (P1 homepage rebuild). */

import { useEffect, useRef, useState } from "react";
import { BarChart2, LineArea2, StackBar, MiniTrend, Waterfall, BulletRow, MaturityScatter } from "./ChartsV2";

const FOOT = "Illustrative composite - replaced by your baseline at the value assessment.";

/* ── gate report table (panel 4 of the steering pack) ─────────────────── */
const GATE_ROWS: { metric: string; base: string; gates: [string, string, string]; owner: string }[] = [
  { metric: "Fraud decision cycle", base: "42 hrs", gates: ["28 hrs", "17 hrs", "11 hrs"], owner: "Head of Fraud Ops" },
  { metric: "Claims auto-adjudication", base: "34%", gates: ["48%", "62%", "71%"], owner: "COO, Claims" },
  { metric: "Unplanned downtime", base: "9.6 hrs/mo", gates: ["7.1 hrs/mo", "5.8 hrs/mo", "5.2 hrs/mo"], owner: "VP Manufacturing" },
  { metric: "Price refresh cycle", base: "64 hrs", gates: ["44 hrs", "30 hrs", "22 hrs"], owner: "VP Revenue Mgmt" },
];

function GateTable() {
  return (
    <div className="overflow-hidden rounded-xl border border-line">
      <table className="w-full border-separate border-spacing-0 text-[11px]">
        <thead>
          <tr className="bg-navy-800 text-white">
            <th className="px-3 py-2 text-left font-semibold">Metric</th>
            <th className="px-2 py-2 text-center font-semibold">Base</th>
            <th className="px-2 py-2 text-center font-semibold">G1</th>
            <th className="px-2 py-2 text-center font-semibold">G2</th>
            <th className="px-2 py-2 text-center font-semibold">G3</th>
            <th className="px-3 py-2 text-left font-semibold">Owner</th>
          </tr>
        </thead>
        <tbody>
          {GATE_ROWS.map((r, i) => (
            <tr key={r.metric} className={i % 2 ? "bg-mist/60" : "bg-white"}>
              <td className="border-b border-line px-3 py-2 text-left font-medium text-navy-800">{r.metric}</td>
              <td className="border-b border-line px-2 py-2 text-center tabular-nums text-slate-body/70">{r.base}</td>
              {r.gates.map((g, k) => (
                <td key={k} className="border-b border-line px-2 py-2 text-center tabular-nums text-navy-800">
                  {g}
                </td>
              ))}
              <td className="border-b border-line px-3 py-2 text-left text-slate-body/75">{r.owner}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

/* ── steering pack: 4 equal-height panels ─────────────────────────────── */
export function SteeringPack() {
  return (
    <div className="mt-8 grid gap-4 md:grid-cols-2 lg:items-stretch lg:auto-rows-fr">
      <BarChart2
        title="Decision latency after 90 days"
        caption="Sample engagement"
        labels={["Fraud triage", "Claims routing", "Demand plan", "Risk review"]}
        series={[
          { name: "Baseline", values: [42, 31, 64, 58] },
          { name: "Day 90", values: [11, 9, 22, 17] },
        ]}
        unit=" hrs"
        footnote={FOOT}
      />
      <LineArea2
        title="Autonomous resolution vs committed band"
        caption="12-week ramp"
        labels={Array.from({ length: 12 }, (_, i) => `W${i + 1}`)}
        series={[{ name: "Autonomous", values: [8, 12, 19, 27, 34, 41, 48, 55, 61, 66, 71, 76] }]}
        unit="%"
        band={{ min: 45, max: 75, label: "Committed band" }}
        footnote={FOOT}
      />
      <StackBar
        title="Where the value landed"
        caption="$ impact mix"
        segments={[
          { name: "Cost released", value: 38, note: "$1.2-1.8M per $10M program" },
          { name: "Revenue protected", value: 27, note: "$0.9-1.4M" },
          { name: "Risk reduced", value: 21, note: "control coverage" },
          { name: "Cycle time recovered", value: 14, note: "decision latency" },
        ]}
        footnote={FOOT}
      />
      <figure className="flex h-full flex-col overflow-hidden rounded-2xl border border-line bg-white shadow-2">
        <figcaption className="flex items-start justify-between gap-3 border-b border-line bg-mist/70 px-5 py-3">
          <span className="text-[13px] font-semibold leading-snug text-navy-800">Gate-by-gate delta, named owners</span>
          <span className="shrink-0 rounded-full bg-brand-tint px-2 py-0.5 text-[9.5px] font-bold uppercase tracking-[0.12em] text-brand-deep">
            Gate report
          </span>
        </figcaption>
        <div className="flex flex-1 flex-col px-5 pt-4">
          <GateTable />
          <p className="mt-auto pt-2 text-[10.5px] leading-snug text-slate-body/60">{FOOT}</p>
        </div>
      </figure>
      {/* second row: economics, risk posture, maturity-to-outcome (BG-040/042/044) */}
      <Waterfall
        title="Year-one run-cost walk, $10M program"
        caption="Value walk"
        steps={[
          { name: "Baseline run cost", value: 10.0, kind: "start", note: "steady-state cost before the program" },
          { name: "Cost released", value: -1.8, kind: "down", note: "automation of manual decision loops" },
          { name: "Revenue protected", value: -1.2, kind: "down", note: "fraud, waste and downtime avoided" },
          { name: "Reinvested", value: 0.6, kind: "up", note: "platform hardening and new use cases" },
          { name: "Net run cost", value: 7.6, kind: "end" },
        ]}
        unit=" $M"
        footnote={FOOT}
      />
      <BulletRow
        title="Control coverage vs committed target"
        caption="Risk posture"
        rows={[
          { name: "Identity & access", value: 92, target: 95 },
          { name: "Data estate", value: 88, target: 90 },
          { name: "Models & agents", value: 76, target: 85 },
          { name: "Supply chain", value: 64, target: 75 },
          { name: "Operations", value: 81, target: 85 },
        ]}
        footnote={FOOT}
      />
      <MaturityScatter
        title="AI maturity vs typical outcome, engagement composite"
        caption="350+ programs"
        xLabels={["Stage 1", "Stage 2", "Stage 3", "Stage 4", "Stage 5"]}
        points={[
          { x: 1, y: 6, w: 2, label: "Pilots, no owner" },
          { x: 2, y: 12, w: 4, label: "First use cases" },
          { x: 2, y: 18, w: 3, label: "Platform pilot" },
          { x: 3, y: 24, w: 7, label: "Decision hub live" },
          { x: 3, y: 31, w: 5, label: "Hub + governance" },
          { x: 4, y: 38, w: 6, label: "Agent fleet in prod" },
          { x: 4, y: 44, w: 4, label: "Fleet + control trail" },
          { x: 5, y: 52, w: 3, label: "Compounding estate" },
          { x: 5, y: 47, w: 2, label: "Compounding, weak ops" },
        ]}
        unit=" pts"
        footnote={FOOT}
      />
      <EngagementModels />
    </div>
  );
}

/* ── engagement-model comparison (panel 8, BG-045) ────────────────────── */
const MODELS = [
  {
    name: "Proof of value",
    tag: "4-6 weeks",
    desc: "A falsifiable PoC against your data, with the go/redirect/stop decision written before the first sprint.",
    spark: [0, 1, 2, 3, 5, 7],
    labels: ["W1", "W6"],
    band: undefined as { min: number; max: number; label: string } | undefined,
    unit: " pts",
  },
  {
    name: "Build",
    tag: "one quarter to stand-up",
    desc: "Named pod builds the decision hub, data contracts and control trail; your team co-owns from week two.",
    spark: [8, 14, 22, 31, 41, 52, 61, 70],
    labels: ["Q1", "Q2"],
    band: { min: 45, max: 75, label: "Committed band" },
    unit: "%",
  },
  {
    name: "Run",
    tag: "outcome-linked operations",
    desc: "We operate the estate against the signed metric — fees partially at risk against the committed band.",
    spark: [62, 64, 67, 69, 72, 75, 77, 79],
    labels: ["M1", "M8"],
    band: { min: 70, max: 85, label: "Committed band" },
    unit: "%",
  },
];

function EngagementModels() {
  return (
    <figure className="flex h-full flex-col overflow-hidden rounded-2xl border border-line bg-white shadow-2">
      <figcaption className="flex items-start justify-between gap-3 border-b border-line bg-mist/70 px-5 py-3">
        <span className="text-[13px] font-semibold leading-snug text-navy-800">Three ways in — each gates the next</span>
        <span className="shrink-0 rounded-full bg-brand-tint px-2 py-0.5 text-[9.5px] font-bold uppercase tracking-[0.12em] text-brand-deep">
          Engagement models
        </span>
      </figcaption>
      <div className="flex flex-1 flex-col justify-center gap-4 px-5 py-4">
        {MODELS.map((m, i) => (
          <div key={m.name} className="grid items-center gap-3 sm:grid-cols-[1fr_120px]">
            <div>
              <p className="flex flex-wrap items-center gap-2 text-[13px] font-semibold text-navy-800">
                {m.name}
                <span className="rounded-full bg-navy-800/5 px-2 py-0.5 text-[9.5px] font-bold uppercase tracking-[0.1em] text-navy-800/70">
                  {m.tag}
                </span>
              </p>
              <p className="mt-1 text-[11.5px] leading-snug text-slate-body/75">{m.desc}</p>
            </div>
            <div className="rounded-lg border border-line bg-mist/50 px-2.5 pb-1.5 pt-1">
              <MiniTrend values={m.spark} labels={m.labels} band={m.band} unit={m.unit} dark={false} />
            </div>
          </div>
        ))}
      </div>
      <div className="mt-auto border-t border-line px-5 py-2.5">
        <p className="text-[10.5px] leading-snug text-slate-body/60">{FOOT}</p>
      </div>
    </figure>
  );
}

/* ── hero outcome console ─────────────────────────────────────────────── */
type Scenario = {
  id: string;
  label: string;
  headline: string;
  kpis: { label: string; from: string; to: string; delta: string }[];
  trend: { label: string; values: number[]; labels: string[]; band: { min: number; max: number; label: string }; unit: string };
};

const SCENARIOS: Scenario[] = [
  {
    id: "banking",
    label: "Banking",
    headline: "Fraud and AML decisions, straight-through",
    kpis: [
      { label: "Fraud decision cycle", from: "42 hrs", to: "11 hrs", delta: "-74%" },
      { label: "Manual review load", from: "100%", to: "37%", delta: "-63%" },
    ],
    trend: {
      label: "Straight-through rate, weeks 1-8",
      values: [8, 14, 21, 30, 38, 45, 51, 57],
      labels: ["W1", "W8"],
      band: { min: 40, max: 70, label: "Committed band" },
      unit: "%",
    },
  },
  {
    id: "insurance",
    label: "Insurance",
    headline: "Claims routed before the adjuster opens the file",
    kpis: [
      { label: "Touch time per claim", from: "31 hrs", to: "9 hrs", delta: "-71%" },
      { label: "Auto-adjudication", from: "34%", to: "71%", delta: "+37 pts" },
    ],
    trend: {
      label: "Auto-adjudication rate, weeks 1-8",
      values: [12, 19, 27, 35, 44, 52, 60, 66],
      labels: ["W1", "W8"],
      band: { min: 45, max: 75, label: "Committed band" },
      unit: "%",
    },
  },
  {
    id: "manufacturing",
    label: "Manufacturing",
    headline: "Downtime caught before the line stops",
    kpis: [
      { label: "Unplanned downtime", from: "9.6 hrs/mo", to: "5.2 hrs/mo", delta: "-46%" },
      { label: "Scrap rate", from: "4.2%", to: "2.6%", delta: "-38%" },
    ],
    trend: {
      label: "Predictive intervention coverage, weeks 1-8",
      values: [10, 17, 26, 36, 47, 57, 66, 74],
      labels: ["W1", "W8"],
      band: { min: 40, max: 80, label: "Committed band" },
      unit: "%",
    },
  },
  {
    id: "retail",
    label: "Retail",
    headline: "Price and availability decisions at shelf speed",
    kpis: [
      { label: "Price refresh cycle", from: "64 hrs", to: "22 hrs", delta: "-66%" },
      { label: "Margin leakage", from: "baseline", to: "-28%", delta: "-28%" },
    ],
    trend: {
      label: "Automated pricing coverage, weeks 1-8",
      values: [6, 12, 20, 29, 39, 49, 58, 65],
      labels: ["W1", "W8"],
      band: { min: 35, max: 70, label: "Committed band" },
      unit: "%",
    },
  },
];

export function OutcomeConsole({ autoRotate = true }: { autoRotate?: boolean }) {
  const [idx, setIdx] = useState(0);
  const [paused, setPaused] = useState(false);
  const timer = useRef<number | null>(null);
  const reduced = useRef(false);

  useEffect(() => {
    reduced.current = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    return () => {
      if (timer.current) window.clearInterval(timer.current);
    };
  }, []);

  useEffect(() => {
    if (!autoRotate || paused || reduced.current) return;
    timer.current = window.setInterval(() => setIdx((i) => (i + 1) % SCENARIOS.length), 6000);
    return () => {
      if (timer.current) window.clearInterval(timer.current);
    };
  }, [autoRotate, paused]);

  const s = SCENARIOS[idx];
  return (
    <div
      className="overflow-hidden rounded-2xl border border-white/10 bg-white/[0.05] backdrop-blur"
      onMouseEnter={() => setPaused(true)}
      onMouseLeave={() => setPaused(false)}
      onFocus={() => setPaused(true)}
      onBlur={() => setPaused(false)}
    >
      <div className="flex flex-wrap items-center justify-between gap-2 border-b border-white/10 px-5 py-3">
        <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-brand-300">Executive outcome console</p>
        <p className="text-[9.5px] font-medium uppercase tracking-[0.12em] text-white/45">Illustrative scenarios</p>
      </div>

      {/* scenario tabs */}
      <div className="flex gap-1.5 overflow-x-auto px-4 pt-3" role="tablist" aria-label="Industry scenarios">
        {SCENARIOS.map((sc, i) => (
          <button
            key={sc.id}
            type="button"
            role="tab"
            aria-selected={i === idx}
            onClick={() => setIdx(i)}
            className={`whitespace-nowrap rounded-full px-3 py-1.5 text-[11px] font-semibold transition ${
              i === idx ? "bg-brand text-white" : "bg-white/10 text-white/65 hover:bg-white/15 hover:text-white"
            }`}
          >
            {sc.label}
          </button>
        ))}
      </div>

      <div className="grid gap-4 p-4 sm:grid-cols-2 sm:items-center">
        <div>
          <p className="text-[13.5px] font-semibold leading-snug text-white">{s.headline}</p>
          <div className="mt-3 space-y-2">
            {s.kpis.map((k) => (
              <div key={k.label} className="rounded-xl border border-white/10 bg-navy-900/60 px-3 py-2.5">
                <p className="text-[10.5px] font-medium uppercase tracking-[0.1em] text-white/50">{k.label}</p>
                <p className="mt-1 flex items-baseline gap-2 text-[13px] tabular-nums text-white">
                  <span className="text-white/45 line-through decoration-white/30">{k.from}</span>
                  <span aria-hidden="true" className="text-brand-300">-&gt;</span>
                  <span className="font-bold">{k.to}</span>
                  <span className="ml-auto rounded-md bg-brand/15 px-1.5 py-0.5 text-[11px] font-bold text-brand-300">{k.delta}</span>
                </p>
              </div>
            ))}
          </div>
        </div>
        <div className="rounded-xl border border-white/10 bg-navy-900/60 px-3 py-3">
          <MiniTrend values={s.trend.values} labels={s.trend.labels} band={s.trend.band} unit={s.trend.unit} label={s.trend.label} />
        </div>
      </div>

      <div className="flex items-center justify-between border-t border-white/10 px-5 py-2.5">
        <div className="flex gap-1.5">
          {SCENARIOS.map((sc, i) => (
            <button
              key={sc.id}
              type="button"
              aria-label={`Show ${sc.label} scenario`}
              onClick={() => setIdx(i)}
              className={`h-1.5 rounded-full transition-all ${i === idx ? "w-5 bg-brand" : "w-1.5 bg-white/25 hover:bg-white/50"}`}
            />
          ))}
        </div>
        <p className="max-w-[65%] text-right text-[10px] leading-snug text-white/45">
          Illustrative composites - your baseline replaces these figures at the value assessment.
        </p>
      </div>
    </div>
  );
}
