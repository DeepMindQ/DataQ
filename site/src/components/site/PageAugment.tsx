import { PageData } from "@/lib/content";
import { PATENTS, patentsForPage, Patent } from "@/lib/patents";
import { mulberry32, hashStr } from "@/lib/seeded";
import Link from "next/link";
import { ShieldCheck } from "lucide-react";
/* Charts: ChartsV2 executive system (y-axes, ticks, tooltips, draw-in).
   ArchitectureFlow + WorldPins remain in DataVisuals (diagram + map). */
import { BarChart2, LineArea2, Radar2, Gauge2, Funnel2, Heatmap2, StackBar } from "./ChartsV2";
import { ArchitectureFlow, WorldPins } from "./DataVisuals";

/* ── PageAugment (Wave 2 + output-graphs directive) ─────────────────────
   Server-side, template-aware augmentation: every internal page receives a
   deterministic, page-seeded "output telemetry" panel (illustrative sample
   engagement data) plus the patents that power it. No per-page JSON edits. */

type Rng = () => number;

const TOWER_KPI: Record<string, { names: string[]; unit: string; trend: string; trendUnit: string }> = {
  "applied-ai-generative-ai": {
    names: ["Decision accuracy", "Time-to-answer", "Content ops cost", "Manual review hrs"],
    unit: "%",
    trend: "Assisted decisions per day",
    trendUnit: "",
  },
  "agentic-ai-hyperautomation": {
    names: ["Straight-through rate", "Cycle time", "Touches per case", "Backlog age"],
    unit: "%",
    trend: "Cases resolved autonomously / week",
    trendUnit: "",
  },
  "data-analytics-lakehouse": {
    names: ["Query latency p95", "Pipeline failures", "Freshness lag", "Cost per TB"],
    unit: "%",
    trend: "Governed queries served / day",
    trendUnit: "",
  },
  "cybersecurity-zero-trust": {
    names: ["MTTD", "MTTR", "Policy violations", "Open audit findings"],
    unit: "%",
    trend: "Threat signals correlated / hour",
    trendUnit: "",
  },
  "cloud-edge-platform-engineering": {
    names: ["Deploy frequency", "Change failure rate", "Cost per workload", "Incidents / mo"],
    unit: "%",
    trend: "Workloads orchestrated / day",
    trendUnit: "",
  },
  "quantum-advanced-compute": {
    names: ["Optimality gap", "Solve time", "Scenario coverage", "Energy per solve"],
    unit: "%",
    trend: "Scenarios explored / run",
    trendUnit: "",
  },
  "blockchain-digital-trust": {
    names: ["Reconciliation time", "Verification cost", "Dispute rate", "Provenance coverage"],
    unit: "%",
    trend: "Assets verified on-ledger / day",
    trendUnit: "",
  },
  "iot-digital-twin-robotics": {
    names: ["Unplanned downtime", "OEE uplift", "Defect escape rate", "Sensor coverage"],
    unit: "%",
    trend: "Twin sync events / minute",
    trendUnit: "",
  },
};

function towerOf(page: PageData): string {
  const seg = page.url.split("/").filter(Boolean);
  const towers = Object.keys(TOWER_KPI);
  for (const s of seg) if (towers.includes(s)) return s;
  return "applied-ai-generative-ai";
}

function baselineVsAfter(rng: Rng, names: string[]): { base: number[]; after: number[] } {
  // Improvement magnitudes per KPI: 22–58% better than baseline
  const base = names.map(() => Math.round(38 + rng() * 50));
  const after = base.map((b) => Math.max(6, Math.round(b * (1 - (0.22 + rng() * 0.36)))));
  return { base, after };
}

/* ── Output telemetry panel — per-template deterministic charts ───────── */
/* ── Output telemetry — curated, CXO-meaningful program views ────────────
   Every figure below is an explicitly authored composite: the typical
   starting position and the 90-day/12-month target shape our pattern
   library plans against. Not client data, not RNG — a planning baseline
   the reader can interrogate. Captions state exactly what each chart is. */
export function OutputTelemetry({ page }: { page: PageData }) {
  const t = page.template;
  const tower = towerOf(page);
  const kpi = TOWER_KPI[tower];
  const dark = t === "case_study";
  const wrap = (children: React.ReactNode, note?: string) => (
    <section className="container-dq pt-2">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <p className={`text-[12px] font-semibold uppercase tracking-[0.2em] ${dark ? "text-brand-300" : "text-brand-deep"}`}>
            Program economics
          </p>
          <h2 className={`mt-1 font-display text-[21px] font-semibold sm:text-[23px] ${dark ? "text-white" : "text-navy-800"}`}>
            What a program of this type targets
          </h2>
          <p className={`mt-1.5 max-w-2xl text-[13px] ${dark ? "text-white/60" : "text-slate-body/70"}`}>
            Composite planning figures from our delivery pattern library — the starting position
            is measured and signed in weeks 1–2; the target shape is agreed at the design gate.
            Your numbers replace these at the value assessment.
          </p>
        </div>
      </div>
      {children}
      {note && (
        <p className={`mt-3 flex items-start gap-2 text-[12px] leading-relaxed ${dark ? "text-white/55" : "text-slate-body/70"}`}>
          <span aria-hidden="true" className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-brand" />
          {note}
        </p>
      )}
    </section>
  );

  /* curated per-tower KPI figures: [typical starting point, 90-day target] */
  const TOWER_FIGS: Record<string, { names: string[]; base: number[]; target: number[]; unit: string; read: string }> = {
    "applied-ai-generative-ai": {
      names: ["Decision accuracy", "Time-to-answer (min)", "Content ops cost (idx)", "Manual review (hrs/wk)"],
      base: [72, 45, 100, 60], target: [88, 12, 62, 18],
      unit: "",
      read: "Read: accuracy gains come from retrieval and evaluation discipline, not model swaps. Cost index is rebased to 100 at baseline.",
    },
    "agentic-ai-hyperautomation": {
      names: ["Straight-through rate", "Cycle time (hrs)", "Touches per case", "Backlog age (days)"],
      base: [42, 9, 5, 12], target: [78, 3, 2, 2],
      unit: "",
      read: "Read: straight-through rate is the compounding metric — every point moves cost and cycle time together. Exceptions keep human checkpoints.",
    },
    "data-analytics-lakehouse": {
      names: ["Query p95 (sec)", "Pipeline failures/mo", "Freshness lag (hrs)", "Cost per TB (idx)"],
      base: [180, 9, 24, 100], target: [8, 1, 1, 58],
      unit: "",
      read: "Read: freshness lag is the metric that decides whether decisions use this data. Cost index falls with storage tiering and query pruning, not headcount.",
    },
    "cybersecurity-zero-trust": {
      names: ["MTTD (min)", "MTTR (hrs)", "Policy violations/mo", "Open audit findings"],
      base: [240, 26, 31, 14], target: [15, 4, 6, 2],
      unit: "",
      read: "Read: MTTD/MTTR only move when detection, identity and response are engineered as one pipeline — tool counts are not the goal.",
    },
    "cloud-edge-platform-engineering": {
      names: ["Deploy freq (/wk)", "Change failure rate", "Cost per workload (idx)", "Sev-2 incidents/mo"],
      base: [1, 18, 100, 7], target: [9, 6, 64, 2],
      unit: "",
      read: "Read: deploy frequency and change failure rate move inversely by design — the platform absorbs the risk manual releases used to carry.",
    },
    "quantum-advanced-compute": {
      names: ["Optimality gap", "Solve time (min)", "Scenario coverage", "Energy per solve (idx)"],
      base: [14, 90, 40, 100], target: [3, 11, 92, 47],
      unit: "",
      read: "Read: every quantum-inspired run is benchmarked against the best classical solver; we only ship where the gap is real and measured.",
    },
    "blockchain-digital-trust": {
      names: ["Reconciliation (days)", "Verification cost (idx)", "Dispute rate", "Provenance coverage"],
      base: [5, 100, 8, 35], target: [0.2, 31, 1, 96],
      unit: "",
      read: "Read: provenance coverage is the adoption metric — the ledger only pays back when counterparties actually write to it.",
    },
    "iot-digital-twin-robotics": {
      names: ["Unplanned downtime (%)", "OEE (pts)", "Defect escape (kPPM)", "Sensor coverage"],
      base: [7, 61, 4200, 42], target: [2.4, 74, 1500, 92],
      unit: "",
      read: "Read: OEE points are worth 5-12x their weight in margin at plant scale; downtime cuts land first, yield follows.",
    },
  };
  const figs = TOWER_FIGS[tower] ?? TOWER_FIGS["applied-ai-generative-ai"];

  /* program economics: cumulative value vs cumulative cost, 12 months */
  const months = Array.from({ length: 12 }, (_, i) => `M${i + 1}`);
  const cumValue = [0, 4, 12, 26, 44, 66, 92, 118, 142, 164, 184, 202];
  const cumCost = [14, 28, 42, 56, 70, 82, 92, 101, 109, 116, 122, 128];

  if (t === "service_page" || t === "sub_capability" || t === "industry_capability") {
    return wrap(
      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        <BarChart2
          title="Typical starting position vs 90-day target"
          caption="Pattern-library composite"
          labels={figs.names}
          series={[
            { name: "Typical starting point", values: figs.base },
            { name: "90-day target", values: figs.target, color: "#FE5722" },
          ]}
          dark={dark}
        />
        <LineArea2
          title="Cumulative value vs cumulative cost — 12 months"
          caption="Illustrative program shape"
          labels={months}
          series={[
            { name: "Cumulative value", values: cumValue },
            { name: "Cumulative cost", values: cumCost, color: "#3A3358" },
          ]}
          dark={dark}
        />
      </div>,
      figs.read + " The value line crosses the cost line in month 6 on this composite — payback timing is set by the baseline audit, not assumed.",
    );
  }

  if (t === "tower_hub") {
    return wrap(
      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        <BarChart2
          title="Typical starting position vs 90-day target"
          caption="Pattern-library composite"
          labels={figs.names}
          series={[
            { name: "Typical starting point", values: figs.base },
            { name: "90-day target", values: figs.target, color: "#FE5722" },
          ]}
        />
        <Radar2
          title="Operating maturity — current vs design gate"
          caption="5-point scale x20"
          axes={["Speed", "Precision", "Resilience", "Governance", "Scale"]}
          series={[
            { name: "Typical current state", values: [38, 42, 35, 30, 45], color: "#3A3358" },
            { name: "Design-gate target", values: [82, 78, 86, 90, 76], color: "#FE5722" },
          ]}
        />
      </div>,
      figs.read,
    );
  }

  if (t === "platform_overview") {
    return wrap(
      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        <Radar2
          title="Platform capability scorecard"
          caption="Reference deployment"
          axes={["Throughput", "Precision", "Resilience", "Governance", "Time-to-value"]}
          series={[{ name: "Reference benchmark", values: [84, 80, 88, 92, 74], color: "#FE5722" }]}
        />
        <LineArea2
          title="Cumulative value vs cumulative cost — 12 months"
          caption="Illustrative program shape"
          labels={months}
          series={[
            { name: "Cumulative value", values: cumValue },
            { name: "Cumulative cost", values: cumCost, color: "#3A3358" },
          ]}
        />
      </div>,
      "Read: the platform's pre-built controls compress the cost curve — most programs cross breakeven a quarter earlier than greenfield builds.",
    );
  }

  if (t === "platform_architecture") {
    const layers = PLATFORM_LAYERS[keyOf(page.url)] ?? PLATFORM_LAYERS.nexus;
    return wrap(
      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        <ArchitectureFlow title="Reference architecture — trust layers" caption="Method-family aligned" layers={layers} />
        <Gauge2 title="Deterministic verification coverage" caption="Runtime assurance" value={94} unit="%" />
      </div>,
      "Read: verification coverage is the share of decision paths whose outputs are reproducible byte-for-byte — the property auditors test first.",
    );
  }

  if (t === "platform_usecases") {
    return wrap(
      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        <Funnel2
          title="Enterprise adoption funnel — reference rollout"
          caption="How deployments scale"
          stages={[
            { name: "Value assessment", value: 120 },
            { name: "Pilot scoped", value: 64 },
            { name: "Production pilot", value: 38 },
            { name: "Scaled rollout", value: 26 },
            { name: "Enterprise standard", value: 18 },
          ]}
        />
        <BarChart2
          title="Where the value lands — impact mix"
          caption="Composite of delivered programs"
          labels={["Cost released", "Revenue protected", "Risk reduced", "Cycle time"]}
          series={[{ name: "Share of value", values: [38, 27, 21, 14] }]}
        />
      </div>,
      "Read: cost release usually funds the program; revenue protection and risk reduction are where CFOs find the second business case.",
    );
  }

  if (t === "case_study") {
    return wrap(
      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        <BarChart2
          title="Signed baseline vs audited outcome"
          caption="Method under NDA"
          labels={figs.names}
          dark
          series={[
            { name: "Signed baseline", values: figs.base },
            { name: "Audited outcome", values: figs.target, color: "#FE5722" },
          ]}
        />
        <StackBar
          title="Where the value landed"
          caption="Composite impact mix"
          dark
          segments={[
            { name: "Cost released", value: 38 },
            { name: "Revenue protected", value: 27 },
            { name: "Risk reduced", value: 21 },
            { name: "Cycle-time recovered", value: 14 },
          ]}
        />
      </div>,
      "Read: every case page shows the shape of the measurement — the client's actual figures stay under NDA and are shown at the briefing.",
    );
  }

  if (t === "industry_hub" || t === "subindustry_page") {
    return wrap(
      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        <Heatmap2
          title="Program priority matrix — capability by quarter"
          caption="Planning view"
          rows={["AMER", "EMEA", "APAC", "MEASA"]}
          cols={["Q1", "Q2", "Q3", "Q4"]}
          matrix={[
            [62, 74, 81, 86],
            [55, 68, 79, 84],
            [48, 61, 74, 80],
            [40, 52, 66, 75],
          ]}
        />
        <LineArea2
          title="Cumulative value vs cumulative cost — 12 months"
          caption="Illustrative program shape"
          labels={months}
          series={[
            { name: "Cumulative value", values: cumValue },
            { name: "Cumulative cost", values: cumCost, color: "#3A3358" },
          ]}
        />
      </div>,
      "Read: the heatmap is a planning view of where enterprise programs in this sector concentrate by quarter and region — use it to time your pilot.",
    );
  }

  if (t === "solution_page") {
    return wrap(
      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        <Funnel2
          title="Decision pipeline — from signal to executed action"
          caption="Reference flow"
          stages={[
            { name: "Signals ingested", value: 4800 },
            { name: "Contextualized", value: 2400 },
            { name: "Decisions proposed", value: 960 },
            { name: "Human-approved", value: 640 },
            { name: "Automated execution", value: 520 },
          ]}
        />
        <BarChart2
          title="Typical starting position vs 90-day target"
          caption="Pattern-library composite"
          labels={figs.names}
          series={[
            { name: "Typical starting point", values: figs.base },
            { name: "90-day target", values: figs.target, color: "#FE5722" },
          ]}
        />
      </div>,
      figs.read,
    );
  }

  if (t === "insight_article") {
    return wrap(
      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        <LineArea2
          title="The adoption curve this thesis tracks"
          caption="Composite signal"
          labels={months}
          series={[{ name: "Index", values: cumValue }]}
        />
        <StackBar
          title="Where programs stall"
          caption="Field pattern"
          segments={[
            { name: "Data contracts", value: 34 },
            { name: "Decision ownership", value: 26 },
            { name: "Model operations", value: 22 },
            { name: "Change management", value: 18 },
          ]}
        />
      </div>,
      "Read: the stall mix is the field pattern behind the thesis — most programs fail on contracts and ownership long before they fail on models.",
    );
  }

  if (t === "approach_page" || t === "company_page") {
    return wrap(
      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        <ArchitectureFlow
          title="The Dataq Method — gate structure"
          caption="Outcome-anchored"
          layers={[
            { name: "Diagnose — metric lock", nodes: ["Named metric", "Baseline audit", "Control owner"] },
            { name: "Design — risk budget", nodes: ["Risk envelope", "Control mapping", "Gate criteria"] },
            { name: "Prove — measured pilot", nodes: ["Bounded scope", "Evidence trail", "Gate review"] },
            { name: "Industrialize — scale", nodes: ["Runbooks", "Enablement", "Quarterly re-audit"] },
          ]}
        />
        <LineArea2
          title="Cumulative value vs cumulative cost — 12 months"
          caption="Illustrative program shape"
          labels={months}
          series={[
            { name: "Cumulative value", values: cumValue },
            { name: "Cumulative cost", values: cumCost, color: "#3A3358" },
          ]}
        />
      </div>,
      "Read: the gate structure is what keeps the value line above the cost line — a phase that misses its evidence stops, and the ledger shows it.",
    );
  }

  return null;
}
function weeksRamp(rng: Rng): number[] {
  const start = 180 + Math.round(rng() * 400);
  return Array.from({ length: 12 }, (_, i) => Math.round(start + i * i * (1.4 + rng() * 1.8) + i * (4 + rng() * 10)));
}
function keyOf(url: string): string {
  const m = url.match(/platforms\/([a-z-]+)\//);
  return m ? m[1] : "nexus";
}

/* Patent-aligned reference architectures per platform (from the specs) */
export const PLATFORM_LAYERS: Record<string, { name: string; nodes: string[] }[]> = {
  nexus: [
    { name: "Ingestion & fusion", nodes: ["Multi-modal intake", "Normalization", "Context tensors"] },
    { name: "Graph intelligence core", nodes: ["Dynamic graphs", "Hypergraph tensors", "Spectral analysis"] },
    { name: "Decision hub", nodes: ["Contextual scoring", "Anomaly detection", "Deterministic streaming"] },
    { name: "Delivery & audit", nodes: ["APIs", "Dashboards", "Evidence trail"] },
  ],
  forge: [
    { name: "Workload intake", nodes: ["Task graphs", "Constraint capture", "Cost envelopes"] },
    { name: "Tensor decomposition", nodes: ["SVD / low-rank", "Manifold encoding", "Energy profiling"] },
    { name: "Quantum-walk optimizer", nodes: ["State exploration", "Amplitude amplification", "Route synthesis"] },
    { name: "Execution fabric", nodes: ["TPU / FPGA dispatch", "Grid-aware sync", "Verification"] },
  ],
  swarm: [
    { name: "Task graph synthesis", nodes: ["Dependency mapper", "Blueprint generator", "Temporal logic"] },
    { name: "Agent fleet", nodes: ["MARL policies", "Swarm clusters", "Shared rewards"] },
    { name: "Orchestration", nodes: ["Scheduler", "Conflict resolver", "Resource arbiter"] },
    { name: "Validated execution", nodes: ["zk-SNARK checks", "Blockchain log", "Rollback"] },
  ],
  sentinel: [
    { name: "Telemetry estate", nodes: ["Identity signals", "Network fabric", "Data posture"] },
    { name: "Encrypted computation", nodes: ["ZHNE homomorphic ops", "Secure aggregation", "Key governance"] },
    { name: "Consensus & trust", nodes: ["MABC protocol", "Byzantine isolation", "Compliance monitors"] },
    { name: "Resilient response", nodes: ["Self-healing ledger", "Workload redistribution", "Forensics"] },
  ],
  twinverse: [
    { name: "Sensor fabric", nodes: ["IoT streams", "Vision feeds", "Edge gateways"] },
    { name: "Multimodal perception", nodes: ["Quantum-enhanced NN", "Ensemble scoring", "Noise suppression"] },
    { name: "Twin synchronization", nodes: ["State estimator", "Curvature transforms", "What-if simulation"] },
    { name: "Actuation", nodes: ["Maintenance plans", "Autonomous control", "Operator HMI"] },
  ],
  quanta: [
    { name: "Problem encoding", nodes: ["Objective capture", "Constraint tensors", "Hilbert-space map"] },
    { name: "Spectral decomposition", nodes: ["Laplacian eigensets", "Band isolation", "Phase estimation"] },
    { name: "Quantum-inspired solver", nodes: ["Quantum walks", "Amplitude amplification", "Annealing"] },
    { name: "Verified result", nodes: ["Optimality bound", "Reproducibility check", "Explain report"] },
  ],
  ledger: [
    { name: "Event capture", nodes: ["Signed events", "Stream validation", "Schema contracts"] },
    { name: "Consensus ledger", nodes: ["DAG ordering", "Byzantine tolerance", "Immutable log"] },
    { name: "Provenance graph", nodes: ["Lineage links", "Attribution", "Retention policy"] },
    { name: "Trust delivery", nodes: ["Audit API", "Regulator views", "Disclosures"] },
  ],
  compass: [
    { name: "Signal lake", nodes: ["Temporal streams", "Spatial context", "Semantic layer"] },
    { name: "Adaptive learning loop", nodes: ["DRLF policies", "NAS refinement", "POMDP policies"] },
    { name: "Decision intelligence", nodes: ["Knowledge-graph DSS", "Explainability", "Fairness checks"] },
    { name: "Outcome tracking", nodes: ["Metric ledger", "Raft coherence", "Board reporting"] },
  ],
};

/* ── Patent strip — powers-this-page band ─────────────────────────────── */
export function PatentStrip({ page, dark }: { page: PageData; dark?: boolean }) {
  const patents = patentsForPage(page.url, page.title);
  if (!patents.length) return null;
  return (
    <section className="container-dq pt-6">
      <div className={`rounded-2xl border px-5 py-4 ${dark ? "border-white/10 bg-white/[0.05]" : "border-line bg-mist/60"}`}>
        <p className={`text-[11px] font-bold uppercase tracking-[0.18em] ${dark ? "text-brand-300" : "text-brand-deep"}`}>
          Patented method underneath
        </p>
        <div className="mt-3 grid gap-3 md:grid-cols-3">
          {patents.map((p) => (
            <div key={p.ref} className="flex items-start gap-2.5">
              <ShieldCheck className="mt-0.5 h-4 w-4 shrink-0 text-brand" aria-hidden="true" />
              <div>
                <p className={`text-[12.5px] font-semibold leading-snug ${dark ? "text-white" : "text-navy-800"}`}>{p.title}</p>
                <Link
                  href="/patented-intelligence/"
                  className={`text-[11px] font-medium hover:underline ${dark ? "text-brand-300" : "text-brand-deep"}`}
                >
                  {p.ref} — see the patent map
                </Link>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ── Patented-intelligence full grid (used by /patented-intelligence/) ── */
export function PatentGrid() {
  return (
    <div className="container-dq pb-4">
      <div className="grid gap-4 md:grid-cols-2">
        {PATENTS.map((p: Patent, i) => (
          <article
            key={p.ref}
            className="group flex flex-col rounded-2xl border border-line bg-white p-6 shadow-1 transition hover:-translate-y-0.5 hover:border-brand/60 hover:shadow-2"
          >
            <div className="flex items-center justify-between gap-3">
              <span className="inline-flex items-center gap-1.5 rounded-full bg-brand-tint px-2.5 py-1 text-[10.5px] font-bold uppercase tracking-[0.12em] text-brand-deep">
                <ShieldCheck className="h-3.5 w-3.5" aria-hidden="true" /> Patented method
              </span>
              <span className="font-display text-[12px] font-bold text-brand-deep/60">{String(i + 1).padStart(2, "0")}</span>
            </div>
            <h2 className="mt-3 font-display text-[17px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
              {p.title}
            </h2>
            <p className="mt-2 text-[13px] leading-relaxed text-slate-body/80">{p.oneLiner}</p>
            <ul className="mt-3 space-y-1.5">
              {p.capabilities.slice(0, 4).map((c) => (
                <li key={c} className="flex items-start gap-2 text-[12.5px] leading-snug text-slate-body/85">
                  <span aria-hidden="true" className="mt-[7px] h-1.5 w-1.5 shrink-0 rounded-full bg-brand" />
                  {c}
                </li>
              ))}
            </ul>
            <div className="mt-4 flex flex-wrap gap-1.5 border-t border-line pt-3">
              <span className="text-[10.5px] font-semibold uppercase tracking-wider text-slate-body/50">Powers</span>
              {[...p.platforms.map((x) => `/platforms/${x}/`), ...p.towers.map((x) => `/services/${x}/`)].map((u) => (
                <Link
                  key={u}
                  href={u}
                  className="rounded-md border border-line bg-mist px-2 py-0.5 text-[11px] font-medium text-navy-800 transition hover:border-brand hover:text-brand-deep"
                >
                  {u.replace(/\//g, " ").trim()}
                </Link>
              ))}
            </div>
          </article>
        ))}
      </div>
    </div>
  );
}

/* ── Offices world map (CHG-186) — consumed by global-offices via template */
export function OfficesMap({ offices }: { offices: { city: string }[] }) {
  const coords: Record<string, { x: number; y: number }> = {
    "United States": { x: 0.268, y: 0.375 },
    "Tysons Corner": { x: 0.268, y: 0.375 },
    "New York": { x: 0.26, y: 0.36 },
    "United Kingdom": { x: 0.46, y: 0.3 },
    London: { x: 0.46, y: 0.3 },
    India: { x: 0.69, y: 0.56 },
    Bengaluru: { x: 0.685, y: 0.575 },
    "Kingdom of Saudi Arabia": { x: 0.575, y: 0.455 },
    "Saudi Arabia": { x: 0.575, y: 0.455 },
    Riyadh: { x: 0.575, y: 0.455 },
    Dubai: { x: 0.585, y: 0.47 },
    Singapore: { x: 0.755, y: 0.6 },
  };
  const pins = offices
    .map((o) => {
      const city = o.city.split(",")[0].split("(")[0].split("—")[0].split(" — ")[0].trim();
      const c = coords[city];
      return c ? { id: city, ...c } : null;
    })
    .filter(Boolean) as { id: string; x: number; y: number }[];
  if (!pins.length) return null;
  return <WorldPins title="Four global delivery centers, one delivery standard" caption="Global delivery" pins={pins} />;
}
