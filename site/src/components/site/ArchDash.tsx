import Reveal from "./Reveal";
import { CountUp } from "./Motion";

/* ── ArchDash — data-driven deep-tech visuals ───────────────────────────────
   Two components, both fed from the page JSON so every page renders its OWN
   architecture / dashboard (no shared template imagery):

   1. ArchGraph   — a real architecture graph: lanes + nodes + edges passed
                    from content. Each (tower × industry × variant) renders a
                    different topology with that sector's actual systems.
   2. MetricsDash — an operations-console mock: KPI tiles, gate-by-gate bar
                    chart, decision-log ticker. Values are the page's own
                    measured outcomes (case studies) or named program
                    metrics — never invented figures.

   Pure SVG + CSS animation, static-export safe, reduced-motion aware. */

const CL = {
  bg: "rgba(255,255,255,0.045)",
  bg2: "rgba(255,255,255,0.09)",
  stroke: "rgba(255,255,255,0.26)",
  edge: "rgba(255,255,255,0.20)",
  hot: "rgba(254,87,34,0.18)",
  hotStroke: "rgba(254,87,34,0.75)",
  orange: "#FE5722",
  txt: "rgba(255,255,255,0.95)",
  dim: "rgba(255,255,255,0.60)",
  lane: "rgba(255,255,255,0.05)",
};

export type ArchNode = { id: string; lane: number; label: string; hot?: boolean };
export type ArchEdge = { a: string; b: string; label?: string };

function wrapLabel(label: string, max = 20): string[] {
  const words = label.split(/\s+/);
  const lines: string[] = [];
  let cur = "";
  for (const w of words) {
    if ((cur + " " + w).trim().length > max && cur) {
      lines.push(cur);
      cur = w;
    } else {
      cur = (cur + " " + w).trim();
    }
  }
  if (cur) lines.push(cur);
  return lines.slice(0, 2).length ? lines.slice(0, 2) : [label];
}

export function ArchGraph({
  title,
  note,
  lanes,
  nodes,
  edges,
}: {
  title: string;
  note?: string;
  lanes: string[];
  nodes: ArchNode[];
  edges: ArchEdge[];
}) {
  const COL_W = 178;
  const GAP = 64;
  const NODE_W = 158;
  const NODE_H = 44;
  const TOP = 66;
  const ROW_GAP = 58;
  const W = lanes.length * COL_W + (lanes.length - 1) * GAP + 32;
  const maxRows = Math.max(2, ...lanes.map((_, li) => nodes.filter((n) => n.lane === li).length));
  const H = TOP + maxRows * (NODE_H + ROW_GAP) + 26;

  // lane x origins
  const laneX = (li: number) => 16 + li * (COL_W + GAP);
  // node positions per lane, stacked
  const pos: Record<string, { x: number; y: number }> = {};
  const perLaneCount: number[] = lanes.map(() => 0);
  for (const n of nodes) {
    const row = perLaneCount[n.lane]++;
    const laneNodeCount = nodes.filter((m) => m.lane === n.lane).length;
    const totalH = laneNodeCount * NODE_H + (laneNodeCount - 1) * ROW_GAP;
    const startY = TOP + (maxRows * (NODE_H + ROW_GAP) - ROW_GAP - totalH) / 2;
    pos[n.id] = { x: laneX(n.lane) + (COL_W - NODE_W) / 2, y: startY + row * (NODE_H + ROW_GAP) };
  }

  const anchor = (id: string, side: "l" | "r") => {
    const p = pos[id];
    if (!p) return { x: 0, y: 0 };
    return { x: side === "l" ? p.x : p.x + NODE_W, y: p.y + NODE_H / 2 };
  };

  return (
    <Reveal className="mt-6">
      <figure className="overflow-hidden rounded-2xl border border-white/10 grad-navy-field shadow-3">
        <div className="flex flex-wrap items-center justify-between gap-2 border-b border-white/10 px-5 py-3">
          <p className="text-[12.5px] font-semibold text-white">{title}</p>
          <span className="rounded-full border border-brand/40 bg-brand/15 px-2.5 py-0.5 text-[10px] font-bold uppercase tracking-[0.14em] text-brand-300">
            Architecture
          </span>
        </div>
        <div className="overflow-x-auto px-2 py-3">
          <svg viewBox={`0 0 ${W} ${H}`} className="h-auto w-full min-w-[720px]" role="img" aria-label={title}>
            {/* lane bands + headers */}
            {lanes.map((lane, li) => (
              <g key={lane}>
                <rect
                  x={laneX(li)}
                  y={14}
                  width={COL_W}
                  height={H - 30}
                  rx={12}
                  fill={li % 2 ? CL.lane : "rgba(255,255,255,0.02)"}
                  stroke="rgba(255,255,255,0.07)"
                />
                <text
                  x={laneX(li) + COL_W / 2}
                  y={36}
                  fontSize={10.5}
                  fontWeight={800}
                  fill="rgba(254,87,34,0.9)"
                  textAnchor="middle"
                  letterSpacing="0.14em"
                >
                  {lane.toUpperCase()}
                </text>
              </g>
            ))}
            {/* edges */}
            {edges.map((e, i) => {
              const a = anchor(e.a, "r");
              const b = anchor(e.b, "l");
              if (!a || !b) return null;
              const mx = (a.x + b.x) / 2;
              const d = `M ${a.x} ${a.y} C ${mx} ${a.y}, ${mx} ${b.y}, ${b.x} ${b.y}`;
              return (
                <g key={`e${i}`}>
                  <path d={d} fill="none" stroke={CL.edge} strokeWidth={1.4} />
                  <path
                    className="td-flow"
                    d={d}
                    fill="none"
                    stroke={CL.orange}
                    strokeWidth={1.8}
                    strokeDasharray="4 12"
                    strokeLinecap="round"
                    style={{ animationDelay: `${(i % 6) * 0.35}s`, animationDuration: `${2 + (i % 4) * 0.4}s`, opacity: 0.85 }}
                  />
                  {e.label && (
                    <text x={mx} y={(a.y + b.y) / 2 - 5} fontSize={9.5} fill={CL.dim} textAnchor="middle">
                      {e.label}
                    </text>
                  )}
                </g>
              );
            })}
            {/* nodes */}
            {nodes.map((n) => {
              const p = pos[n.id];
              if (!p) return null;
              const lines = wrapLabel(n.label);
              return (
                <g key={n.id}>
                  <rect
                    x={p.x}
                    y={p.y}
                    width={NODE_W}
                    height={NODE_H}
                    rx={9}
                    fill={n.hot ? CL.hot : CL.bg}
                    stroke={n.hot ? CL.hotStroke : CL.stroke}
                    strokeWidth={n.hot ? 1.5 : 1.1}
                  />
                  {lines.map((ln, k) => (
                    <text
                      key={k}
                      x={p.x + NODE_W / 2}
                      y={p.y + NODE_H / 2 + 4 + (k - (lines.length - 1) / 2) * 13}
                      fontSize={10.5}
                      fontWeight={600}
                      fill={n.hot ? "rgba(255,255,255,0.97)" : CL.txt}
                      textAnchor="middle"
                    >
                      {ln}
                    </text>
                  ))}
                </g>
              );
            })}
          </svg>
        </div>
        {note && (
          <figcaption className="border-t border-white/10 px-5 py-2.5 text-[11.5px] leading-relaxed text-white/55">
            {note}
          </figcaption>
        )}
      </figure>
    </Reveal>
  );
}

/* ── MetricsDash — the operations console ─────────────────────────────────── */

export type DashKpi = { label: string; value: string; delta?: string; dir?: "up" | "down" | "flat" };
export type DashGate = { name: string; pct: number };
export type DashLog = { t: string; msg: string; tag: string };

export function MetricsDash({
  title,
  kpis,
  gates,
  log,
  caption,
}: {
  title: string;
  kpis: DashKpi[];
  gates?: DashGate[];
  log?: DashLog[];
  caption?: string;
}) {
  return (
    <Reveal className="mt-6">
      <figure className="overflow-hidden rounded-2xl border border-white/10 grad-navy-field shadow-3">
        {/* console header */}
        <div className="flex items-center justify-between border-b border-white/10 px-5 py-3">
          <div className="flex items-center gap-2">
            <span className="h-2.5 w-2.5 rounded-full bg-white/20" />
            <span className="h-2.5 w-2.5 rounded-full bg-white/20" />
            <span className="h-2.5 w-2.5 rounded-full bg-brand/70" />
            <p className="ml-2 text-[12.5px] font-semibold text-white">{title}</p>
          </div>
          <span className="inline-flex items-center gap-1.5 rounded-full border border-brand/40 bg-brand/15 px-2.5 py-0.5 text-[10px] font-bold uppercase tracking-[0.14em] text-brand-300">
            <span className="hv-pulse inline-block h-1.5 w-1.5 rounded-full bg-brand" aria-hidden="true" />
            Program view
          </span>
        </div>
        <div className="px-5 py-4">
          {/* KPI tiles */}
          <div className="grid grid-cols-2 gap-2.5 sm:grid-cols-4">
            {kpis.map((k, i) => (
              <div
                key={k.label}
                className="rounded-xl border border-white/10 bg-white/[0.05] px-3.5 py-3 backdrop-blur"
                style={{ animation: `dash-in 0.5s ${0.12 * i}s both` }}
              >
                <p className="truncate text-[10.5px] font-bold uppercase tracking-[0.12em] text-white/45">{k.label}</p>
                <p className="mt-1 font-display text-[20px] font-bold tabular-nums text-white">
                  {k.value}
                  {k.delta && (
                    <span
                      className={`ml-2 align-middle text-[11.5px] font-semibold ${
                        k.dir === "down" ? "text-emerald-400" : k.dir === "flat" ? "text-white/50" : "text-brand-300"
                      }`}
                    >
                      {k.delta}
                    </span>
                  )}
                </p>
              </div>
            ))}
          </div>
          {/* gate bars */}
          {gates && gates.length > 0 && (
            <div className="mt-4 rounded-xl border border-white/10 bg-white/[0.04] px-4 py-3.5">
              <p className="text-[10.5px] font-bold uppercase tracking-[0.14em] text-white/45">Gate-by-gate position</p>
              <div className="mt-3 space-y-2.5">
                {gates.map((g, i) => (
                  <div key={g.name} className="flex items-center gap-3">
                    <span className="w-36 shrink-0 truncate text-[11px] font-medium text-white/70">{g.name}</span>
                    <span className="h-2 flex-1 overflow-hidden rounded-full bg-white/10">
                      <span
                        className="block h-full rounded-full"
                        style={{
                          width: `${Math.max(4, Math.min(100, g.pct))}%`,
                          background: i === gates.length - 1 ? CL.orange : "rgba(254,87,34,0.55)",
                          animation: `dash-bar 0.9s ${0.25 + 0.15 * i}s both`,
                        }}
                      />
                    </span>
                    <span className="w-10 shrink-0 text-right text-[11px] font-semibold tabular-nums text-brand-300">
                      {g.pct}%
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}
          {/* decision log */}
          {log && log.length > 0 && (
            <div className="mt-4 rounded-xl border border-white/10 bg-navy-950/60 px-4 py-3 font-mono">
              <p className="font-sans text-[10.5px] font-bold uppercase tracking-[0.14em] text-white/45">Decision log</p>
              <div className="mt-2.5 space-y-1.5">
                {log.map((r, i) => (
                  <p
                    key={i}
                    className="flex flex-wrap items-baseline gap-x-2 text-[11px] leading-relaxed text-white/70"
                    style={{ animation: `dash-in 0.5s ${0.5 + 0.18 * i}s both` }}
                  >
                    <span className="text-white/35">{r.t}</span>
                    <span className="rounded bg-brand/15 px-1.5 py-0.5 text-[9.5px] font-bold uppercase tracking-wider text-brand-300">
                      {r.tag}
                    </span>
                    <span>{r.msg}</span>
                  </p>
                ))}
              </div>
            </div>
          )}
        </div>
        {caption && (
          <figcaption className="border-t border-white/10 px-5 py-2.5 text-[11.5px] leading-relaxed text-white/55">
            {caption}
          </figcaption>
        )}
      </figure>
    </Reveal>
  );
}

/* keyframes injected once (used by tiles/bars/log rows) */
export function DashStyles() {
  return (
    <style>{`
      @keyframes dash-in { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: none; } }
      @keyframes dash-bar { from { width: 4% !important; } }
      @media (prefers-reduced-motion: reduce) {
        [style*="dash-in"], [style*="dash-bar"] { animation: none !important; }
      }
    `}</style>
  );
}
