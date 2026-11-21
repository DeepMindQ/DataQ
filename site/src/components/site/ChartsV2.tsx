"use client";

/* ── ChartsV2: executive chart system (Batch 2)
   ChartFrame v2 with title / caption / footnote slots and equal-height contract.
   SVG-rendered axes, nice-number ticks, gridlines, SVG tooltips, reduced-motion
   safe (globals kill switch). Data is deterministic + illustrative, footnoted. */

import { useState } from "react";
import { useInView } from "./Motion";

export const BRAND = "#FE5722";
export const NAVY = "#18142D";
const NAVY_SOFT = "#3A3358";

type Dark = { dark?: boolean };

function niceMax(v: number): number {
  if (v <= 0) return 1;
  const exp = Math.floor(Math.log10(v));
  const base = Math.pow(10, exp);
  const f = v / base;
  const nf = f <= 1 ? 1 : f <= 2 ? 2 : f <= 2.5 ? 2.5 : f <= 5 ? 5 : 10;
  return nf * base;
}

const fmt = (n: number) => n.toLocaleString("en-US");

/* ── ChartFrame v2 ────────────────────────────────────────────────────── */
export function ChartFrame({
  title,
  caption,
  footnote,
  dark,
  children,
}: {
  title: string;
  caption?: string;
  footnote?: string;
  dark?: boolean;
  children: React.ReactNode;
}) {
  return (
    <figure
      className={`flex h-full flex-col overflow-hidden rounded-2xl border shadow-2 ${
        dark ? "border-white/10 bg-white/[0.05] backdrop-blur" : "border-line bg-white"
      }`}
    >
      <figcaption
        className={`flex items-start justify-between gap-3 border-b px-5 py-3 ${
          dark ? "border-white/10" : "border-line bg-mist/70"
        }`}
      >
        <span className={`text-[13px] font-semibold leading-snug ${dark ? "text-white" : "text-navy-800"}`}>
          {title}
        </span>
        {caption && (
          <span
            className={`shrink-0 rounded-full px-2 py-0.5 text-[9.5px] font-bold uppercase tracking-[0.12em] ${
              dark ? "bg-brand/20 text-brand-300" : "bg-brand-tint text-brand-deep"
            }`}
          >
            {caption}
          </span>
        )}
      </figcaption>
      <div className="flex flex-1 flex-col px-5 pt-4">{children}</div>
      <div className={`mt-auto border-t px-5 py-2.5 ${dark ? "border-white/10" : "border-line"}`}>
        <p className={`text-[10.5px] leading-snug ${dark ? "text-white/50" : "text-slate-body/60"}`}>
          {footnote ?? "Illustrative composite - replaced by your baseline at the value assessment."}
        </p>
      </div>
    </figure>
  );
}

function AxisUnit({ unit, dark }: { unit: string; dark?: boolean }) {
  if (!unit) return null;
  return (
    <text x={46} y={12} fontSize="9" fontWeight="600" fill={dark ? "rgba(255,255,255,.55)" : "#6B6580"}>
      {unit.trim()}
    </text>
  );
}

function YTicks({ max, H, pad, unit, dark }: { max: number; H: number; pad: { l: number; r: number; t: number; b: number }; unit: string; dark?: boolean }) {
  const ticks = [0, 0.25, 0.5, 0.75, 1];
  const grid = dark ? "rgba(255,255,255,.12)" : "#E7E3F0";
  const label = dark ? "rgba(255,255,255,.55)" : "#6B6580";
  return (
    <g>
      {ticks.map((t) => {
        const y = pad.t + (1 - t) * (H - pad.t - pad.b);
        const v = max * t;
        return (
          <g key={t}>
            <line x1={pad.l} x2={560 - pad.r} y1={y} y2={y} stroke={t === 0 ? grid : grid} strokeWidth="1" />
            <text x={pad.l - 6} y={y + 3} textAnchor="end" fontSize="9" fill={label}>
              {t === 0 ? "0" : fmt(Math.round(v))}
            </text>
          </g>
        );
      })}
      <AxisUnit unit={unit} dark={dark} />
    </g>
  );
}

function Legend({ series, dark, base }: { series: { name: string; color?: string }[]; dark?: boolean; base?: string }) {
  return (
    <div className="mt-2 flex flex-wrap gap-x-4 gap-y-1.5">
      {series.map((s, si) => (
        <span key={s.name} className={`flex items-center gap-1.5 text-[11px] ${dark ? "text-white/70" : "text-slate-body/80"}`}>
          <span aria-hidden="true" className="h-2 w-2 rounded-[3px]" style={{ background: s.color ?? (si === 0 ? base ?? NAVY : BRAND) }} />
          {s.name}
        </span>
      ))}
    </div>
  );
}

/* ── BarChart v2: SVG grouped bars, y-axis, tooltips, dim-on-hover ────── */
export function BarChart2({
  title,
  labels,
  series,
  unit = "",
  caption,
  footnote,
  dark,
}: {
  title: string;
  labels: string[];
  series: { name: string; values: number[]; color?: string }[];
  unit?: string;
  caption?: string;
  footnote?: string;
} & Dark) {
  const { ref, inView } = useInView<HTMLDivElement>(0.3);
  const [hover, setHover] = useState<{ gi: number; si: number } | null>(null);
  const W = 560;
  const H = 232;
  const pad = { l: 46, r: 8, t: 20, b: 30 };
  const max = niceMax(Math.max(...series.flatMap((s) => s.values), 1));
  const plotW = W - pad.l - pad.r;
  const plotH = H - pad.t - pad.b;
  const gw = plotW / labels.length;
  const barW = Math.min(30, (gw - 10) / series.length - 3);
  const colorOf = (si: number, s: { color?: string }) => s.color ?? (si === 0 ? NAVY_SOFT : BRAND);
  const y = (v: number) => pad.t + (1 - v / max) * plotH;

  return (
    <div ref={ref}>
      <ChartFrame title={title} caption={caption} footnote={footnote} dark={dark}>
        <svg viewBox={`0 0 ${W} ${H}`} className="w-full" role="img" aria-label={title}>
          <YTicks max={max} H={H} pad={pad} unit={unit} dark={dark} />
          {labels.map((lb, gi) => {
            const gx = pad.l + gi * gw;
            return (
              <g key={lb}>
                <rect
                  x={gx}
                  y={pad.t}
                  width={gw}
                  height={plotH}
                  fill="transparent"
                  onMouseEnter={() => setHover({ gi, si: -1 })}
                  onMouseLeave={() => setHover(null)}
                />
                {series.map((s, si) => {
                  const v = s.values[gi] ?? 0;
                  const bx = gx + gw / 2 - (series.length * barW + (series.length - 1) * 4) / 2 + si * (barW + 4);
                  const by = y(v);
                  const dim = hover && hover.gi === gi && hover.si !== -1 && hover.si !== si;
                  return (
                    <g key={si}>
                      <rect
                        x={bx}
                        y={by}
                        width={barW}
                        height={Math.max(2, pad.t + plotH - by)}
                        rx={3}
                        fill={colorOf(si, s)}
                        opacity={dim ? 0.3 : 1}
                        onMouseEnter={() => setHover({ gi, si })}
                        style={{
                          transformBox: "fill-box",
                          transformOrigin: "bottom",
                          transform: inView ? "scaleY(1)" : "scaleY(0)",
                          transition: `transform 750ms cubic-bezier(.22,1,.36,1) ${si * 90 + gi * 70}ms, opacity 200ms ease`,
                        }}
                      />
                      <text
                        x={bx + barW / 2}
                        y={by - 5}
                        textAnchor="middle"
                        fontSize="9.5"
                        fontWeight="600"
                        className="tabular-nums"
                        fill={dark ? "rgba(255,255,255,.85)" : NAVY}
                        style={{
                          opacity: inView ? (hover && hover.gi === gi && hover.si !== -1 && hover.si !== si ? 0.25 : 1) : 0,
                          transition: `opacity 400ms ease ${si * 90 + gi * 70 + 320}ms`,
                        }}
                      >
                        {fmt(v)}
                      </text>
                    </g>
                  );
                })}
                <text x={gx + gw / 2} y={H - 10} textAnchor="middle" fontSize="9.5" fill={dark ? "rgba(255,255,255,.55)" : "#6B6580"}>
                  {lb}
                </text>
                {hover && hover.gi === gi && hover.si === -1 && (
                  <rect x={gx + 1} y={pad.t} width={gw - 2} height={plotH} fill={BRAND} opacity={0.06} />
                )}
              </g>
            );
          })}
          {hover && hover.si >= 0 && (
            <g>
              {(() => {
                const gi = hover.gi;
                const si = hover.si;
                const s = series[si];
                const gx = pad.l + gi * gw;
                const bx = gx + gw / 2 - (series.length * barW + (series.length - 1) * 4) / 2 + si * (barW + 4);
                const v = s.values[gi] ?? 0;
                const ty = Math.max(24, y(v) - 8);
                const label = `${s.name}: ${fmt(v)}${unit}`;
                const tw = Math.max(96, label.length * 5.6 + 16);
                const tx = Math.min(W - pad.r - tw, Math.max(pad.l, bx + barW / 2 - tw / 2));
                return (
                  <g pointerEvents="none">
                    <rect x={tx} y={ty - 16} width={tw} height={20} rx={5} fill={dark ? "rgba(24,20,45,.94)" : "rgba(24,20,45,.94)"} />
                    <text x={tx + 8} y={ty - 2} fontSize="9.5" fill="#fff" fontWeight="600">
                      {label}
                    </text>
                  </g>
                );
              })()}
            </g>
          )}
        </svg>
        <div
          onMouseEnter={() => setHover(null)}
        >
          <Legend series={series} dark={dark} />
        </div>
      </ChartFrame>
    </div>
  );
}

/* ── LineArea v2: axes, target band, crosshair tooltip, end annotation ── */
export function LineArea2({
  title,
  labels,
  series,
  unit = "",
  caption,
  footnote,
  band,
  dark,
  compact = false,
}: {
  title: string;
  labels: string[];
  series: { name: string; values: number[]; color?: string }[];
  unit?: string;
  caption?: string;
  footnote?: string;
  band?: { min: number; max: number; label: string };
  compact?: boolean;
} & Dark) {
  const { ref, inView } = useInView<HTMLDivElement>(0.3);
  const [hoverIdx, setHoverIdx] = useState<number | null>(null);
  const W = 560;
  const H = compact ? 180 : 232;
  const pad = { l: 46, r: 14, t: 20, b: 28 };
  const all = series.flatMap((s) => s.values).concat(band ? [band.min, band.max] : []);
  const max = niceMax(Math.max(...all, 1));
  const plotW = W - pad.l - pad.r;
  const plotH = H - pad.t - pad.b;
  const x = (i: number, n: number) => pad.l + (i * plotW) / Math.max(1, n - 1);
  const y = (v: number) => pad.t + (1 - v / max) * plotH;
  const n = series[0]?.values.length ?? 0;

  return (
    <div ref={ref}>
      <ChartFrame title={title} caption={caption} footnote={footnote} dark={dark}>
        <svg
          viewBox={`0 0 ${W} ${H}`}
          className="w-full"
          role="img"
          aria-label={title}
          onMouseLeave={() => setHoverIdx(null)}
        >
          {band && (
            <g>
              <rect x={pad.l} y={y(band.max)} width={plotW} height={Math.max(2, y(band.min) - y(band.max))} fill={BRAND} opacity={0.08} />
              <line x1={pad.l} x2={W - pad.r} y1={y(band.max)} y2={y(band.max)} stroke={BRAND} strokeWidth="1" strokeDasharray="4 3" opacity={0.55} />
              <line x1={pad.l} x2={W - pad.r} y1={y(band.min)} y2={y(band.min)} stroke={BRAND} strokeWidth="1" strokeDasharray="4 3" opacity={0.55} />
              <text x={pad.l + 6} y={y(band.max) + 12} textAnchor="start" fontSize="8.5" fontWeight="600" fill={dark ? "#FE9C77" : "#C2410C"}>
                {band.label}
              </text>
            </g>
          )}
          <YTicks max={max} H={H} pad={pad} unit={unit} dark={dark} />
          {series.map((s, si) => {
            const pts = s.values.map((v, i) => `${x(i, s.values.length)},${y(v)}`).join(" ");
            const line = `M${pts}`;
            const area = `${line} L${x(s.values.length - 1, s.values.length)},${H - pad.b} L${x(0, s.values.length)},${H - pad.b} Z`;
            const color = s.color ?? BRAND;
            const last = s.values[s.values.length - 1];
            return (
              <g key={si}>
                <path d={area} fill={color} opacity={inView ? 0.12 : 0} style={{ transition: "opacity 900ms ease 500ms" }} />
                <path
                  d={line}
                  fill="none"
                  stroke={color}
                  strokeWidth="2.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  pathLength={1}
                  strokeDasharray={1}
                  strokeDashoffset={inView ? 0 : 1}
                  style={{ transition: `stroke-dashoffset 1300ms cubic-bezier(.4,0,.2,1) ${si * 180}ms` }}
                />
                {s.values.map((v, i) => (
                  <circle
                    key={i}
                    cx={x(i, s.values.length)}
                    cy={y(v)}
                    r={hoverIdx === i ? 4 : 2.4}
                    fill={hoverIdx === i ? color : dark ? "#0F0C20" : "#fff"}
                    stroke={color}
                    strokeWidth="1.6"
                    opacity={inView ? 1 : 0}
                    style={{ transition: `opacity 300ms ease ${700 + i * 50 + si * 180}ms, r 120ms ease` }}
                  />
                ))}
                {!compact && (
                  <g opacity={inView ? 1 : 0} style={{ transition: "opacity 500ms ease 1200ms" }}>
                    <circle cx={x(s.values.length - 1, s.values.length)} cy={y(last)} r={4.5} fill={color} />
                    <text
                      x={x(s.values.length - 1, s.values.length) - 6}
                      y={y(last) - 8}
                      textAnchor="end"
                      fontSize="10"
                      fontWeight="700"
                      className="tabular-nums"
                      fill={dark ? "#fff" : NAVY}
                    >
                      {fmt(last)}
                      {unit}
                    </text>
                  </g>
                )}
              </g>
            );
          })}
          {labels.map((lb, i) =>
            compact || labels.length <= 12 || i % 2 === 0 || i === labels.length - 1 ? (
              <text key={i} x={x(i, labels.length)} y={H - 8} textAnchor="middle" fontSize="8.5" fill={dark ? "rgba(255,255,255,.5)" : "#6B6580"}>
                {lb}
              </text>
            ) : null,
          )}
          {hoverIdx !== null && n > 0 && (
            <g pointerEvents="none">
              <line x1={x(hoverIdx, n)} x2={x(hoverIdx, n)} y1={pad.t} y2={H - pad.b} stroke={dark ? "rgba(255,255,255,.3)" : "rgba(24,20,45,.25)"} strokeWidth="1" />
              {(() => {
                const rows = series.map((s, si) => ({ name: s.name, v: s.values[hoverIdx] ?? 0, si }));
                const head = `${labels[hoverIdx] ?? ""}`;
                const w = Math.max(120, ...rows.map((r) => (r.name.length + String(fmt(r.v)).length) * 5.4)) + 20;
                const hgt = 18 + rows.length * 14 + 6;
                const tx = Math.min(W - pad.r - w, Math.max(pad.l, x(hoverIdx, n) + 10));
                const ty = pad.t + 4;
                return (
                  <g>
                    <rect x={tx} y={ty} width={w} height={hgt} rx={6} fill="rgba(24,20,45,.94)" />
                    <text x={tx + 9} y={ty + 14} fontSize="9" fontWeight="700" fill="#FE9C77">
                      {head}
                    </text>
                    {rows.map((r, k) => (
                      <text key={k} x={tx + 9} y={ty + 30 + k * 14} fontSize="9.5" fill="#fff">
                        <tspan fill="rgba(255,255,255,.7)">{r.name}</tspan>
                        <tspan dx="6" fontWeight="700" className="tabular-nums">
                          {fmt(r.v)}
                          {unit}
                        </tspan>
                      </text>
                    ))}
                  </g>
                );
              })()}
            </g>
          )}
          <rect
            x={pad.l}
            y={pad.t}
            width={plotW}
            height={plotH}
            fill="transparent"
            onMouseMove={(e) => {
              const box = (e.target as SVGRectElement).getBoundingClientRect();
              const rel = (e.clientX - box.left) / box.width;
              setHoverIdx(Math.max(0, Math.min(n - 1, Math.round(rel * (n - 1)))));
            }}
          />
        </svg>
        {series.length > 1 && <Legend series={series} dark={dark} base={BRAND} />}
      </ChartFrame>
    </div>
  );
}

/* ── StackBar: horizontal composition with $-mapped legend ────────────── */
export function StackBar({
  title,
  caption,
  footnote,
  segments,
  dark,
}: {
  title: string;
  caption?: string;
  footnote?: string;
  segments: { name: string; value: number; note?: string; color?: string }[];
} & Dark) {
  const { ref, inView } = useInView<HTMLDivElement>(0.3);
  const [hover, setHover] = useState<number | null>(null);
  const total = segments.reduce((a, s) => a + s.value, 0) || 1;
  const palette = [BRAND, NAVY, "#FE9C77", NAVY_SOFT];
  let acc = 0;
  return (
    <div ref={ref}>
      <ChartFrame title={title} caption={caption} footnote={footnote} dark={dark}>
        <div className={`relative h-[34px] w-full overflow-hidden rounded-lg ${dark ? "bg-white/10" : "bg-mist"}`}>
          {segments.map((s, i) => {
            const frac = s.value / total;
            const left = (acc / total) * 100;
            acc += s.value;
            const color = s.color ?? palette[i % palette.length];
            return (
              <div
                key={s.name}
                onMouseEnter={() => setHover(i)}
                onMouseLeave={() => setHover(null)}
                className="absolute bottom-0 top-0"
                style={{
                  width: `${frac * 100}%`,
                  transform: inView ? "scaleX(1)" : "scaleX(0)",
                  transformOrigin: "left",
                  opacity: hover === null || hover === i ? 1 : 0.45,
                  transition: `transform 800ms cubic-bezier(.22,1,.36,1) ${i * 130}ms, opacity 200ms ease`,
                  background: color,
                  left: `${left}%`,
                }}
              >
                {frac > 0.13 && (
                  <span className="absolute inset-0 flex items-center justify-center text-[11px] font-bold tabular-nums text-white">
                    {Math.round(frac * 100)}%
                  </span>
                )}
              </div>
            );
          })}
        </div>
        <div className="mt-3 space-y-2">
          {segments.map((s, i) => (
            <div
              key={s.name}
              className={`flex items-start justify-between gap-3 text-[11.5px] leading-snug`}
              onMouseEnter={() => setHover(i)}
              onMouseLeave={() => setHover(null)}
            >
              <span className={`flex items-center gap-2 ${dark ? "text-white/80" : "text-slate-body/90"}`}>
                <span aria-hidden="true" className="mt-0.5 h-2.5 w-2.5 shrink-0 rounded-full" style={{ background: s.color ?? palette[i % palette.length] }} />
                {s.name}
                {s.note && <span className={dark ? "text-white/45" : "text-slate-body/55"}> - {s.note}</span>}
              </span>
              <span className={`shrink-0 font-bold tabular-nums ${dark ? "text-white" : "text-navy-800"}`}>{Math.round((s.value / total) * 100)}%</span>
            </div>
          ))}
        </div>
      </ChartFrame>
    </div>
  );
}

/* ── Waterfall: year-one run-cost walk (baseline -> releases -> reinvest -> net) ── */
export function Waterfall({
  title,
  caption,
  footnote,
  steps,
  unit = " $M",
  dark,
}: {
  title: string;
  caption?: string;
  footnote?: string;
  steps: { name: string; value: number; kind?: "start" | "down" | "up" | "end"; note?: string }[];
  unit?: string;
} & Dark) {
  const { ref, inView } = useInView<HTMLDivElement>(0.3);
  const [hover, setHover] = useState<number | null>(null);
  const W = 560;
  const H = 232;
  const pad = { l: 46, r: 8, t: 20, b: 34 };
  const plotW = W - pad.l - pad.r;
  const plotH = H - pad.t - pad.b;
  // cumulative levels (end bar spans 0 -> net value)
  let acc = 0;
  const bars = steps.map((s) => {
    const from = s.kind === "end" ? 0 : acc;
    const to = s.kind === "end" ? s.value : acc + s.value;
    if (s.kind !== "end") acc = to;
    return { ...s, from, to };
  });
  const max = niceMax(Math.max(...bars.flatMap((b) => [b.from, b.to]), 1));
  const gw = plotW / bars.length;
  const barW = Math.min(46, gw - 18);
  const y = (v: number) => pad.t + (1 - v / max) * plotH;
  const colorOf = (b: (typeof bars)[number]) =>
    b.kind === "down" ? BRAND : b.kind === "up" ? NAVY_SOFT : NAVY;
  return (
    <div ref={ref}>
      <ChartFrame title={title} caption={caption} footnote={footnote} dark={dark}>
        <svg viewBox={`0 0 ${W} ${H}`} className="w-full" role="img" aria-label={title}>
          <YTicks max={max} H={H} pad={pad} unit={unit} dark={dark} />
          {bars.map((b, i) => {
            const cx = pad.l + i * gw + gw / 2;
            const top = y(Math.max(b.from, b.to));
            const bot = y(Math.min(b.from, b.to));
            const label = `${b.kind === "end" ? fmt(b.value) : `${b.value > 0 ? "+" : ""}${fmt(b.value)}`}${unit}`;
            return (
              <g key={b.name}>
                {/* connector to next bar */}
                {i < bars.length - 1 && (
                  <line
                    x1={cx + barW / 2}
                    x2={pad.l + (i + 1) * gw + gw / 2 - barW / 2}
                    y1={y(b.to)}
                    y2={y(b.to)}
                    stroke={dark ? "rgba(255,255,255,.3)" : "#B9B3CC"}
                    strokeDasharray="3 3"
                    opacity={inView ? 1 : 0}
                    style={{ transition: `opacity 500ms ease ${400 + i * 160}ms` }}
                  />
                )}
                <rect
                  x={cx - barW / 2}
                  y={top}
                  width={barW}
                  height={Math.max(3, bot - top)}
                  rx={3}
                  fill={colorOf(b)}
                  opacity={hover === null || hover === i ? 1 : 0.4}
                  onMouseEnter={() => setHover(i)}
                  onMouseLeave={() => setHover(null)}
                  style={{
                    transformBox: "fill-box",
                    transformOrigin: "bottom",
                    transform: inView ? "scaleY(1)" : "scaleY(0)",
                    transition: `transform 700ms cubic-bezier(.22,1,.36,1) ${i * 150}ms, opacity 200ms ease`,
                  }}
                />
                <text
                  x={cx}
                  y={top - 6}
                  textAnchor="middle"
                  fontSize="9.5"
                  fontWeight="700"
                  className="tabular-nums"
                  fill={dark ? "#fff" : NAVY}
                  style={{ opacity: inView ? 1 : 0, transition: `opacity 400ms ease ${300 + i * 150}ms` }}
                >
                  {label}
                </text>
                <text x={cx} y={H - 12} textAnchor="middle" fontSize="9" fill={dark ? "rgba(255,255,255,.55)" : "#6B6580"}>
                  {b.name.length > 14 ? b.name.slice(0, 13) + "…" : b.name}
                </text>
                {hover === i && b.note && (
                  <g pointerEvents="none">
                    <rect x={Math.min(W - 190, Math.max(pad.l, cx - 90))} y={pad.t + 2} width={180} height={22} rx={5} fill="rgba(24,20,45,.94)" />
                    <text x={Math.min(W - 190, Math.max(pad.l, cx - 90)) + 9} y={pad.t + 17} fontSize="9.5" fill="#fff">
                      {b.note}
                    </text>
                  </g>
                )}
              </g>
            );
          })}
        </svg>
      </ChartFrame>
    </div>
  );
}

/* ── BulletRow: control coverage vs committed target (risk strip) ─────── */
export function BulletRow({
  title,
  caption,
  footnote,
  rows,
  dark,
}: {
  title: string;
  caption?: string;
  footnote?: string;
  rows: { name: string; value: number; target: number }[];
  dark?: boolean;
}) {
  const { ref, inView } = useInView<HTMLDivElement>(0.3);
  const [hover, setHover] = useState<string | null>(null);
  return (
    <div ref={ref}>
      <ChartFrame title={title} caption={caption} footnote={footnote} dark={dark}>
        <div className="flex flex-1 flex-col justify-center gap-3 pb-1">
          {rows.map((r, i) => (
            <div
              key={r.name}
              className="group"
              onMouseEnter={() => setHover(r.name)}
              onMouseLeave={() => setHover(null)}
            >
              <div className="flex items-baseline justify-between gap-2 text-[11.5px]">
                <span className={dark ? "text-white/80" : "text-slate-body/90"}>{r.name}</span>
                <span className={`tabular-nums font-bold ${r.value >= r.target ? (dark ? "text-emerald-300" : "text-emerald-700") : dark ? "text-brand-300" : "text-brand-deep"}`}>
                  {r.value}%
                  <span className={`ml-1 font-medium ${dark ? "text-white/40" : "text-slate-body/55"}`}>/ {r.target}%</span>
                </span>
              </div>
              <div className={`relative mt-1 h-[10px] w-full rounded-full ${dark ? "bg-white/10" : "bg-mist"}`}>
                <div
                  className="absolute inset-y-0 left-0 rounded-full"
                  style={{
                    width: `${r.value}%`,
                    background: r.value >= r.target ? "#10B981" : BRAND,
                    transform: inView ? "scaleX(1)" : "scaleX(0)",
                    transformOrigin: "left",
                    opacity: hover === null || hover === r.name ? 1 : 0.55,
                    transition: `transform 800ms cubic-bezier(.22,1,.36,1) ${i * 120}ms, opacity 200ms ease`,
                  }}
                />
                {/* target marker */}
                <div
                  aria-hidden="true"
                  className="absolute top-[-3px] h-[16px] w-[2px] rounded-full"
                  style={{
                    left: `${r.target}%`,
                    background: dark ? "rgba(255,255,255,.65)" : NAVY,
                    opacity: inView ? 1 : 0,
                    transition: `opacity 400ms ease ${500 + i * 120}ms`,
                  }}
                />
              </div>
            </div>
          ))}
          <div className={`flex items-center gap-4 pt-1 text-[10px] ${dark ? "text-white/50" : "text-slate-body/60"}`}>
            <span className="flex items-center gap-1.5">
              <span aria-hidden="true" className="h-2 w-4 rounded-full" style={{ background: BRAND }} /> coverage
            </span>
            <span className="flex items-center gap-1.5">
              <span aria-hidden="true" className="h-3 w-[2px]" style={{ background: dark ? "rgba(255,255,255,.65)" : NAVY }} /> committed target
            </span>
            <span className="flex items-center gap-1.5">
              <span aria-hidden="true" className="h-2 w-4 rounded-full bg-emerald-500" /> target met
            </span>
          </div>
        </div>
      </ChartFrame>
    </div>
  );
}

/* ── MaturityScatter: maturity stage vs typical outcome, sized by volume ── */
export function MaturityScatter({
  title,
  caption,
  footnote,
  points,
  xLabels,
  unit = " pts",
  dark,
}: {
  title: string;
  caption?: string;
  footnote?: string;
  points: { x: number; y: number; w?: number; label: string; sector?: string }[];
  xLabels: string[];
  unit?: string;
} & Dark) {
  const { ref, inView } = useInView<HTMLDivElement>(0.3);
  const [hover, setHover] = useState<number | null>(null);
  const W = 560;
  const H = 232;
  const pad = { l: 46, r: 10, t: 20, b: 30 };
  const plotW = W - pad.l - pad.r;
  const plotH = H - pad.t - pad.b;
  const maxY = niceMax(Math.max(...points.map((p) => p.y), 1));
  const n = xLabels.length;
  const x = (v: number) => pad.l + ((v - 0.5) * plotW) / n;
  const y = (v: number) => pad.t + (1 - v / maxY) * plotH;
  const rOf = (p: (typeof points)[number]) => 5 + Math.min(9, (p.w ?? 1) * 1.4);
  // median guides
  const medX = x(n / 2 + 0.5);
  const medY = y(maxY * 0.5);
  return (
    <div ref={ref}>
      <ChartFrame title={title} caption={caption} footnote={footnote} dark={dark}>
        <svg viewBox={`0 0 ${W} ${H}`} className="w-full" role="img" aria-label={title} onMouseLeave={() => setHover(null)}>
          <YTicks max={maxY} H={H} pad={pad} unit={unit} dark={dark} />
          {/* median guides split the field into quadrants */}
          <line x1={medX} x2={medX} y1={pad.t} y2={H - pad.b} stroke={dark ? "rgba(255,255,255,.2)" : "#D8D3E6"} strokeDasharray="4 4" />
          <line x1={pad.l} x2={W - pad.r} y1={medY} y2={medY} stroke={dark ? "rgba(255,255,255,.2)" : "#D8D3E6"} strokeDasharray="4 4" />
          <text x={W - pad.r - 4} y={pad.t + 12} textAnchor="end" fontSize="8.5" fontWeight="600" fill={dark ? "#FE9C77" : "#C2410C"}>
            fast lane
          </text>
          {points.map((p, i) => (
            <g key={i}>
              <circle
                cx={x(p.x)}
                cy={y(p.y)}
                r={hover === i ? rOf(p) + 2 : rOf(p)}
                fill={i % 2 ? NAVY_SOFT : BRAND}
                opacity={hover === null || hover === i ? 0.78 : 0.3}
                onMouseEnter={() => setHover(i)}
                style={{
                  transformBox: "fill-box",
                  transformOrigin: "center",
                  transform: inView ? "scale(1)" : "scale(0)",
                  transition: `transform 600ms cubic-bezier(.22,1,.36,1) ${i * 90}ms, r 140ms ease, opacity 200ms ease`,
                }}
              />
            </g>
          ))}
          {hover !== null && (
            <g pointerEvents="none">
              {(() => {
                const p = points[hover];
                const label = `${p.label}: +${p.y}${unit}`;
                const w = Math.max(110, label.length * 5.8 + 16);
                const tx = Math.min(W - pad.r - w, Math.max(pad.l, x(p.x) + 10));
                return (
                  <g>
                    <rect x={tx} y={y(p.y) - 24} width={w} height={20} rx={5} fill="rgba(24,20,45,.94)" />
                    <text x={tx + 8} y={y(p.y) - 10} fontSize="9.5" fill="#fff" fontWeight="600">
                      {label}
                    </text>
                  </g>
                );
              })()}
            </g>
          )}
          {xLabels.map((lb, i) => (
            <text key={lb} x={x(i + 1)} y={H - 10} textAnchor="middle" fontSize="9" fill={dark ? "rgba(255,255,255,.55)" : "#6B6580"}>
              {lb}
            </text>
          ))}
        </svg>
      </ChartFrame>
    </div>
  );
}

/* ── Radar2: maturity scorecard with rings, labeled axes, legend ──────── */
export function Radar2({
  title,
  caption,
  footnote,
  axes,
  series,
  dark,
}: {
  title: string;
  caption?: string;
  footnote?: string;
  axes: string[];
  series: { name: string; values: number[]; color?: string }[];
} & Dark) {
  const { ref, inView } = useInView<HTMLDivElement>(0.3);
  const W = 560;
  const H = 300;
  const cx = W / 2;
  const cy = H / 2 + 4;
  const R = 108;
  const n = axes.length;
  const angle = (i: number) => (Math.PI * 2 * i) / n - Math.PI / 2;
  const pt = (i: number, v: number) => `${cx + Math.cos(angle(i)) * (v / 100) * R},${cy + Math.sin(angle(i)) * (v / 100) * R}`;
  const rings = [25, 50, 75, 100];
  const colors = [NAVY_SOFT, BRAND, "#8B85A6"];
  return (
    <div ref={ref}>
      <ChartFrame title={title} caption={caption} footnote={footnote} dark={dark}>
        <svg viewBox={`0 0 ${W} ${H}`} className="w-full" role="img" aria-label={title}>
          {rings.map((r) => (
            <polygon
              key={r}
              points={axes.map((_, i) => pt(i, r)).join(" ")}
              fill="none"
              stroke={dark ? "rgba(255,255,255,.12)" : "#E7E3F0"}
              strokeWidth="1"
            />
          ))}
          {axes.map((_, i) => (
            <line key={i} x1={cx} y1={cy} x2={cx + Math.cos(angle(i)) * R} y2={cy + Math.sin(angle(i)) * R} stroke={dark ? "rgba(255,255,255,.12)" : "#E7E3F0"} />
          ))}
          {series.map((s, si) => (
            <polygon
              key={s.name}
              points={s.values.map((v, i) => pt(i, Math.min(100, Math.max(0, v)))).join(" ")}
              fill={s.color ?? colors[si % colors.length]}
              fillOpacity={inView ? 0.16 : 0}
              stroke={s.color ?? colors[si % colors.length]}
              strokeWidth="2.2"
              strokeLinejoin="round"
              style={{
                transformBox: "fill-box",
                transformOrigin: "center",
                transform: inView ? "scale(1)" : "scale(0.55)",
                opacity: inView ? 1 : 0,
                transition: `transform 800ms cubic-bezier(.22,1,.36,1) ${si * 180}ms, opacity 500ms ease ${si * 180}ms`,
              }}
            />
          ))}
          {axes.map((a, i) => {
            const lx = cx + Math.cos(angle(i)) * (R + 26);
            const ly = cy + Math.sin(angle(i)) * (R + 18);
            return (
              <g key={a}>
                <text x={lx} y={ly - 3} textAnchor="middle" fontSize="10" fontWeight="700" fill={dark ? "#fff" : NAVY}>
                  {a}
                </text>
                <text x={lx} y={ly + 9} textAnchor="middle" fontSize="8.5" fill={dark ? "rgba(255,255,255,.5)" : "#6B6580"} className="tabular-nums">
                  {series[0]?.values[i]}
                  {series[1] ? ` → ${series[1].values[i]}` : ""}
                </text>
              </g>
            );
          })}
        </svg>
        <Legend series={series} dark={dark} />
      </ChartFrame>
    </div>
  );
}

/* ── Gauge2: half-arc assurance gauge with target tick ────────────────── */
export function Gauge2({
  title,
  caption,
  footnote,
  value,
  target,
  unit = "%",
  dark,
}: {
  title: string;
  caption?: string;
  footnote?: string;
  value: number;
  target?: number;
  unit?: string;
} & Dark) {
  const { ref, inView } = useInView<HTMLDivElement>(0.3);
  const W = 560;
  const H = 232;
  const cx = W / 2;
  const cy = 172;
  const R = 118;
  const a = (v: number) => Math.PI * (1 - Math.min(100, Math.max(0, v)) / 100);
  const pt = (v: number, r: number) => `${cx + Math.cos(a(v)) * r},${cy - Math.sin(a(v)) * r}`;
  const arc = (v1: number, v2: number, r: number) => `M${pt(v1, r)} A${r},${r} 0 ${v2 - v1 > 50 ? 1 : 0} 1 ${pt(v2, r)}`;
  const big = Math.round(value);
  return (
    <div ref={ref}>
      <ChartFrame title={title} caption={caption} footnote={footnote} dark={dark}>
        <svg viewBox={`0 0 ${W} ${H}`} className="w-full" role="img" aria-label={title}>
          <path d={arc(0, 100, R)} fill="none" stroke={dark ? "rgba(255,255,255,.14)" : "#E7E3F0"} strokeWidth="16" strokeLinecap="round" />
          <path
            d={arc(0, Math.max(0.5, value), R)}
            fill="none"
            stroke={BRAND}
            strokeWidth="16"
            strokeLinecap="round"
            pathLength={1}
            strokeDasharray={1}
            strokeDashoffset={inView ? 0 : 1}
            style={{ transition: "stroke-dashoffset 1100ms cubic-bezier(.4,0,.2,1) 150ms" }}
          />
          {[0, 25, 50, 75, 100].map((t) => (
            <text key={t} x={cx + Math.cos(a(t)) * (R + 20)} y={cy - Math.sin(a(t)) * (R + 20) + 3} textAnchor="middle" fontSize="9" fill={dark ? "rgba(255,255,255,.5)" : "#6B6580"}>
              {t}
            </text>
          ))}
          {target !== undefined && (
            <g opacity={inView ? 1 : 0} style={{ transition: "opacity 500ms ease 900ms" }}>
              <line
                x1={cx + Math.cos(a(target)) * (R - 14)}
                y1={cy - Math.sin(a(target)) * (R - 14)}
                x2={cx + Math.cos(a(target)) * (R + 12)}
                y2={cy - Math.sin(a(target)) * (R + 12)}
                stroke={NAVY}
                strokeWidth="2.5"
              />
              <text x={cx + Math.cos(a(target)) * (R + 20)} y={cy - Math.sin(a(target)) * (R + 20) + 12} textAnchor="middle" fontSize="8.5" fontWeight="600" fill={dark ? "#FE9C77" : "#C2410C"}>
                target {target}
                {unit}
              </text>
            </g>
          )}
          <text x={cx} y={cy - 28} textAnchor="middle" fontSize="40" fontWeight="800" fill={dark ? "#fff" : NAVY} className="tabular-nums">
            {big}
            <tspan fontSize="16" fontWeight="600" fill={dark ? "rgba(255,255,255,.6)" : "#6B6580"}>
              {unit}
            </tspan>
          </text>
          <text x={cx} y={cy - 6} textAnchor="middle" fontSize="9.5" fill={dark ? "rgba(255,255,255,.55)" : "#6B6580"}>
            of decision paths reproducible byte-for-byte
          </text>
        </svg>
      </ChartFrame>
    </div>
  );
}

/* ── Funnel2: adoption funnel with stage conversion ───────────────────── */
export function Funnel2({
  title,
  caption,
  footnote,
  stages,
  dark,
}: {
  title: string;
  caption?: string;
  footnote?: string;
  stages: { name: string; value: number }[];
} & Dark) {
  const { ref, inView } = useInView<HTMLDivElement>(0.3);
  const [hover, setHover] = useState<number | null>(null);
  const max = Math.max(...stages.map((s) => s.value), 1);
  return (
    <div ref={ref}>
      <ChartFrame title={title} caption={caption} footnote={footnote} dark={dark}>
        <div className="flex flex-1 flex-col justify-center gap-1.5 pb-1">
          {stages.map((s, i) => {
            const w = (s.value / max) * 100;
            const conv = i > 0 ? Math.round((s.value / Math.max(1, stages[i - 1].value)) * 100) : null;
            return (
              <div key={s.name} className="group relative" onMouseEnter={() => setHover(i)} onMouseLeave={() => setHover(null)}>
                <div className="flex items-center gap-2">
                  <div
                    className="relative flex h-[26px] items-center rounded-md"
                    style={{
                      width: `${Math.max(18, w)}%`,
                      background: i === 0 ? NAVY : i === stages.length - 1 ? BRAND : `color-mix(in srgb, ${BRAND} ${30 + i * 14}%, ${NAVY})`,
                      opacity: hover === null || hover === i ? 1 : 0.5,
                      transform: inView ? "scaleX(1)" : "scaleX(0)",
                      transformOrigin: "left",
                      transition: `transform 700ms cubic-bezier(.22,1,.36,1) ${i * 110}ms, opacity 200ms ease`,
                    }}
                  >
                    <span className="truncate px-2.5 text-[10.5px] font-semibold text-white">{s.name}</span>
                  </div>
                  <span className={`shrink-0 text-[11px] font-bold tabular-nums ${dark ? "text-white/85" : "text-navy-800"}`}>{fmt(s.value)}</span>
                  {conv !== null && (
                    <span className={`shrink-0 text-[10px] font-semibold tabular-nums ${conv >= 60 ? (dark ? "text-emerald-300" : "text-emerald-700") : dark ? "text-brand-300" : "text-brand-deep"}`}>
                      {conv}%
                    </span>
                  )}
                </div>
              </div>
            );
          })}
          <p className={`pt-1 text-[10px] ${dark ? "text-white/45" : "text-slate-body/55"}`}>Right column: stage-to-stage conversion on the reference rollout.</p>
        </div>
      </ChartFrame>
    </div>
  );
}

/* ── Heatmap2: priority matrix with ramp legend + hover values ────────── */
export function Heatmap2({
  title,
  caption,
  footnote,
  rows,
  cols,
  matrix,
  dark,
}: {
  title: string;
  caption?: string;
  footnote?: string;
  rows: string[];
  cols: string[];
  matrix: number[][];
} & Dark) {
  const { ref, inView } = useInView<HTMLDivElement>(0.3);
  const [hover, setHover] = useState<string | null>(null);
  const shade = (v: number) => {
    const t = Math.max(0, Math.min(1, (v - 35) / 60));
    const from = dark ? [255, 255, 255] : [24, 20, 45];
    const to = [254, 87, 34];
    const mix = from.map((f, i) => Math.round(f + (to[i] - f) * t));
    return `rgb(${mix[0]} ${mix[1]} ${mix[2]})`;
  };
  return (
    <div ref={ref}>
      <ChartFrame title={title} caption={caption} footnote={footnote} dark={dark}>
        <div className="flex flex-1 flex-col justify-center pb-1">
          <table className="w-full border-separate border-spacing-[3px] text-center">
            <thead>
              <tr>
                <th aria-hidden="true" />
                {cols.map((c) => (
                  <th key={c} className={`pb-1 text-[10px] font-bold uppercase tracking-wider ${dark ? "text-white/55" : "text-slate-body/60"}`}>
                    {c}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {rows.map((r, ri) => (
                <tr key={r}>
                  <td className={`pr-1.5 text-right text-[10.5px] font-semibold ${dark ? "text-white/75" : "text-slate-body/75"}`}>{r}</td>
                  {cols.map((c, ci) => {
                    const v = matrix[ri]?.[ci] ?? 0;
                    const key = `${r}-${c}`;
                    return (
                      <td key={c}>
                        <div
                          onMouseEnter={() => setHover(key)}
                          onMouseLeave={() => setHover(null)}
                          className="relative flex h-[34px] items-center justify-center rounded-md text-[11px] font-bold tabular-nums text-white"
                          style={{
                            background: shade(v),
                            opacity: inView ? (hover === null || hover === key ? 1 : 0.55) : 0,
                            transition: `opacity 500ms ease ${(ri * cols.length + ci) * 45}ms, transform 400ms ease`,
                          }}
                        >
                          {v}
                          {hover === key && (
                            <span className="pointer-events-none absolute -top-7 left-1/2 z-10 -translate-x-1/2 whitespace-nowrap rounded-md bg-[rgba(24,20,45,.94)] px-2 py-1 text-[9.5px] font-semibold text-white">
                              {r} · {c}: {v}/100
                            </span>
                          )}
                        </div>
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
          <div className={`mt-2.5 flex items-center gap-2 text-[10px] ${dark ? "text-white/50" : "text-slate-body/55"}`}>
            <span>lower priority</span>
            <span aria-hidden="true" className="h-2 w-24 rounded-full" style={{ background: "linear-gradient(90deg, rgb(24 20 45), rgb(254 87 34))" }} />
            <span>act first</span>
          </div>
        </div>
      </ChartFrame>
    </div>
  );
}

/* ── MiniTrend: compact banded trend for the hero console ─────────────── */
export function MiniTrend({
  values,
  labels,
  band,
  unit = "",
  dark = true,
  label,
}: {
  values: number[];
  labels: string[];
  band?: { min: number; max: number; label: string };
  unit?: string;
  dark?: boolean;
  label?: string;
}) {
  const { ref, inView } = useInView<HTMLDivElement>(0.4);
  const W = 300;
  const H = 120;
  const pad = { l: 8, r: 8, t: 10, b: 16 };
  const all = values.concat(band ? [band.min, band.max] : []);
  const max = niceMax(Math.max(...all, 1));
  const plotW = W - pad.l - pad.r;
  const plotH = H - pad.t - pad.b;
  const x = (i: number) => pad.l + (i * plotW) / Math.max(1, values.length - 1);
  const y = (v: number) => pad.t + (1 - v / max) * plotH;
  const pts = values.map((v, i) => `${x(i)},${y(v)}`).join(" ");
  const line = `M${pts}`;
  const area = `${line} L${x(values.length - 1)},${H - pad.b} L${x(0)},${H - pad.b} Z`;
  const last = values[values.length - 1];
  return (
    <div ref={ref}>
      {label && <p className={`text-[10.5px] font-semibold uppercase tracking-[0.14em] ${dark ? "text-brand-300" : "text-brand-deep"}`}>{label}</p>}
      <svg viewBox={`0 0 ${W} ${H}`} className="mt-1 w-full" role="img" aria-label={label ?? "Trend"}>
        {band && (
          <rect x={pad.l} y={y(band.max)} width={plotW} height={Math.max(2, y(band.min) - y(band.max))} fill={BRAND} opacity={0.12} />
        )}
        <path d={area} fill={BRAND} opacity={inView ? 0.15 : 0} style={{ transition: "opacity 800ms ease 400ms" }} />
        <path
          d={line}
          fill="none"
          stroke={BRAND}
          strokeWidth="2.2"
          strokeLinecap="round"
          pathLength={1}
          strokeDasharray={1}
          strokeDashoffset={inView ? 0 : 1}
          style={{ transition: "stroke-dashoffset 1100ms cubic-bezier(.4,0,.2,1)" }}
        />
        <circle cx={x(values.length - 1)} cy={y(last)} r={3.6} fill={BRAND} opacity={inView ? 1 : 0} style={{ transition: "opacity 400ms ease 1000ms" }} />
        <text x={x(values.length - 1) - 5} y={y(last) - 7} textAnchor="end" fontSize="10.5" fontWeight="700" className="tabular-nums" fill={dark ? "#fff" : NAVY}>
          {fmt(last)}
          {unit}
        </text>
        {labels.map((lb, i) =>
          i === 0 || i === labels.length - 1 ? (
            <text key={i} x={x(i)} y={H - 3} textAnchor={i === 0 ? "start" : "end"} fontSize="8" fill={dark ? "rgba(255,255,255,.45)" : "#6B6580"}>
              {lb}
            </text>
          ) : null,
        )}
      </svg>
    </div>
  );
}
