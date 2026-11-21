"use client";

import { useEffect, useState } from "react";

/* ── OpsConsole — the live operations console in the homepage hero ──────────
   An animated, believable operations view: KPI tiles, a streaming decision
   chart, gate bars and a live decision log that appends rows on a cadence.
   Purely presentational — values are framed as "reference program view",
   never as client results. Client component; reduced-motion aware. */

type LogRow = { t: string; tag: string; msg: string };

const SEED_LOG: LogRow[] = [
  { t: "14:02:11", tag: "DECISION", msg: "credit limit review — approved, policy v2.4.1, replay id 8f3c" },
  { t: "14:02:09", tag: "GATE", msg: "wave 3 gate passed — reconciliation delta 0.00%, signed" },
  { t: "14:01:58", tag: "AGENT", msg: "KYC file assembled — 14 sources cited, routed to analyst" },
  { t: "14:01:41", tag: "DECISION", msg: "fraud interdiction — blocked, challenge issued, evidence attached" },
  { t: "14:01:22", tag: "EVIDENCE", msg: "control coverage refreshed — 41/41 controls live" },
  { t: "14:01:03", tag: "MODEL", msg: "challenger promoted — task quality +3.1pts, serving cost -12%" },
];

const NEXT_LOG: LogRow[] = [
  { t: "14:02:3x", tag: "DECISION", msg: "pricing floor check — within guardrails, markdown cleared" },
  { t: "14:02:3x", tag: "GATE", msg: "baseline review — metric owner signed, evidence attached" },
  { t: "14:02:3x", tag: "AGENT", msg: "prior-auth package assembled — policy citations included" },
  { t: "14:02:3x", tag: "DECISION", msg: "maintenance window scheduled — RUL confidence 0.94" },
  { t: "14:02:3x", tag: "REPLAY", msg: "decision replay queried — 12ms p95, full trail" },
  { t: "14:02:3x", tag: "MODEL", msg: "drift monitor — stable, eval set refreshed" },
];

/* deterministic pseudo-random series so SSR/CSR markup matches */
function series(seed: number, n = 46): number[] {
  const out: number[] = [];
  let x = seed;
  for (let i = 0; i < n; i++) {
    x = (x * 9301 + 49297) % 233280;
    const r = x / 233280;
    const base = 46 + Math.sin(i / 6) * 14 + Math.sin(i / 2.2) * 6;
    out.push(Math.max(8, Math.min(96, base + (r - 0.5) * 18)));
  }
  return out;
}

function SparkPath(vals: number[], w: number, h: number, pad = 4): string {
  const step = (w - pad * 2) / (vals.length - 1);
  const pts = vals.map((v, i) => `${pad + i * step},${h - pad - (v / 100) * (h - pad * 2)}`);
  return `M ${pts.join(" L ")}`;
}

export default function OpsConsole() {
  const [log, setLog] = useState<LogRow[]>(SEED_LOG);
  const [tick, setTick] = useState(0);
  const s1 = series(11);
  const s2 = series(29);

  useEffect(() => {
    const iv = setInterval(() => {
      setTick((t) => t + 1);
    }, 2600);
    return () => clearInterval(iv);
  }, []);

  useEffect(() => {
    if (tick === 0) return;
    const nxt = NEXT_LOG[(tick - 1) % NEXT_LOG.length];
    setLog((cur) => {
      const stamped = { ...nxt, t: new Date().toLocaleTimeString("en-GB", { hour12: false }) };
      return [stamped, ...cur].slice(0, SEED_LOG.length);
    });
  }, [tick]);

  const bars = [
    { name: "Baseline", pct: 100 },
    { name: "Slice 1 live", pct: 82 },
    { name: "Slice 2 live", pct: 64 },
    { name: "Industrialized", pct: 41 },
  ];

  return (
    <div className="rounded-2xl border border-white/12 bg-navy-950/70 shadow-3 backdrop-blur">
      {/* window chrome */}
      <div className="flex items-center justify-between border-b border-white/10 px-4 py-2.5">
        <div className="flex items-center gap-2">
          <span className="h-2.5 w-2.5 rounded-full bg-white/15" />
          <span className="h-2.5 w-2.5 rounded-full bg-white/15" />
          <span className="h-2.5 w-2.5 rounded-full bg-brand/80" />
          <p className="ml-2 text-[12px] font-semibold text-white/85">Reference program view — decision operations</p>
        </div>
        <span className="inline-flex items-center gap-1.5 rounded-full border border-brand/40 bg-brand/15 px-2.5 py-0.5 text-[9.5px] font-bold uppercase tracking-[0.14em] text-brand-300">
          <span className="hv-pulse inline-block h-1.5 w-1.5 rounded-full bg-brand" aria-hidden="true" />
          Live view
        </span>
      </div>

      <div className="px-4 py-3.5">
        {/* KPI tiles */}
        <div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
          {[
            { label: "Decisions today", value: "1.9M", delta: "streaming", dir: "flat" },
            { label: "Under replay", value: "100%", delta: "audit-ready", dir: "up" },
            { label: "Autonomous share", value: "63%", delta: "+8pts", dir: "up" },
            { label: "Decision p95", value: "148ms", delta: "within SLO", dir: "flat" },
          ].map((k, i) => (
            <div key={k.label} className="rounded-lg border border-white/10 bg-white/[0.05] px-3 py-2.5" style={{ animation: `dash-in .5s ${i * 0.1}s both` }}>
              <p className="truncate text-[9.5px] font-bold uppercase tracking-[0.12em] text-white/40">{k.label}</p>
              <p className="mt-0.5 font-display text-[17px] font-bold tabular-nums text-white">
                {k.value}
                <span className={`ml-1.5 align-middle text-[10px] font-semibold ${k.dir === "up" ? "text-brand-300" : "text-white/45"}`}>{k.delta}</span>
              </p>
            </div>
          ))}
        </div>

        {/* streaming chart */}
        <div className="mt-3 rounded-lg border border-white/10 bg-white/[0.04] p-3">
          <div className="flex items-center justify-between">
            <p className="text-[9.5px] font-bold uppercase tracking-[0.14em] text-white/40">Decision volume & model confidence</p>
            <p className="text-[9.5px] text-white/35">last 24h</p>
          </div>
          <svg viewBox="0 0 320 84" className="mt-1.5 h-[84px] w-full" aria-hidden="true">
            {[21, 42, 63].map((y) => (
              <line key={y} x1="4" y1={y} x2="316" y2={y} stroke="rgba(255,255,255,0.07)" />
            ))}
            <path d={SparkPath(s2, 320, 84)} fill="none" stroke="rgba(255,255,255,0.28)" strokeWidth="1.2" />
            <path d={SparkPath(s1, 320, 84)} fill="none" stroke="#FE5722" strokeWidth="1.8" className="td-flow" strokeDasharray="200 0" />
          </svg>
        </div>

        {/* gate bars */}
        <div className="mt-3 space-y-2">
          {bars.map((b, i) => (
            <div key={b.name} className="flex items-center gap-2.5">
              <span className="w-24 shrink-0 text-[10px] font-medium text-white/55">{b.name}</span>
              <span className="h-1.5 flex-1 overflow-hidden rounded-full bg-white/10">
                <span
                  className="block h-full rounded-full"
                  style={{
                    width: `${b.pct}%`,
                    background: i === 0 ? "rgba(255,255,255,0.35)" : "rgba(254,87,34,0.6)",
                    animation: `dash-bar .9s ${0.3 + i * 0.15}s both`,
                  }}
                />
              </span>
              <span className="w-9 shrink-0 text-right text-[10px] font-semibold tabular-nums text-brand-300">{b.pct}%</span>
            </div>
          ))}
        </div>

        {/* decision log */}
        <div className="mt-3 rounded-lg border border-white/10 bg-black/30 p-2.5 font-mono">
          <p className="font-sans text-[9.5px] font-bold uppercase tracking-[0.14em] text-white/40">Decision log</p>
          <div className="mt-1.5 space-y-1">
            {log.map((r, i) => (
              <p key={`${r.t}-${i}-${r.msg.slice(0, 8)}`} className="flex flex-wrap items-baseline gap-x-1.5 truncate text-[9.5px] leading-relaxed text-white/65" style={{ animation: i === 0 && tick > 0 ? "dash-in .4s both" : undefined, opacity: 1 - i * 0.13 }}>
                <span className="text-white/30">{r.t}</span>
                <span className="rounded bg-brand/15 px-1 py-0.5 text-[8px] font-bold uppercase tracking-wider text-brand-300">{r.tag}</span>
                <span className="truncate">{r.msg}</span>
              </p>
            ))}
          </div>
        </div>
        <p className="mt-2.5 text-[9.5px] leading-relaxed text-white/35">
          Reference console — the same instrument panel every program reports against its own signed baseline.
        </p>
      </div>
    </div>
  );
}
