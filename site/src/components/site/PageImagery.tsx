import Image from "next/image";
import Reveal from "./Reveal";

/* ── PageImagery (Wave 2 visuals overhaul) ─────────────────────────
   Deterministic, template-aware brand illustration under the hero.
   Animated brand SVGs (self-animating via SMIL — no JS needed).
   IMPORTANT: next/image does NOT prefix src under unoptimized+basePath,
   so every raw asset path must go through withBasePath(). */

const BP = process.env.NEXT_PUBLIC_BASE_PATH || "";

type Img = { src: string; alt: string };

const img = (file: string, alt: string): Img => ({
  src: `${BP}/images/${file}`,
  alt,
});

const TOWER_IMG: Record<string, Img> = {
  "applied-ai-generative-ai": img("ai-neural-mesh.svg", "Pulsing neural mesh — applied and generative AI in production"),
  "agentic-ai-hyperautomation": img("agent-swarm-flow.svg", "Agent packets streaming through orchestration lanes"),
  "data-analytics-lakehouse": img("lakehouse-streams.svg", "Layered lakehouse platforms receiving live data streams"),
  "cybersecurity-zero-trust": img("zero-trust-radar.svg", "Zero-trust radar sweeping a monitored threat surface"),
  "cloud-edge-platform-engineering": img("edge-lattice.svg", "Isometric edge lattice with live uplinks to the core"),
  "quantum-advanced-compute": img("quantum-orbits.svg", "Quantum orbit rings around a compute core"),
  "blockchain-digital-trust": img("ledger-chain.svg", "Chained ledger blocks passing signed pulses of trust"),
  "iot-digital-twin-robotics": img("twin-mirror.svg", "Industrial twin mirroring the physical floor"),
};

const PLATFORM_IMG: Record<string, Img> = {
  nexus: img("decision-bars.svg", "Decision mesh surfacing ranked, governed decisions"),
  forge: img("platform-strata.svg", "Platform strata — layered estate with flowing pipelines"),
  swarm: img("fleet-formation.svg", "Agent fleet in coordinated formation"),
  sentinel: img("sentinel-grid.svg", "Sentinel wall of monitored control cells"),
  twinverse: img("mirror-city.svg", "Mirrored operations city — the twinverse skyline"),
  quanta: img("orbit-converge.svg", "Optimizer orbits converging on the best schedule"),
  ledger: img("trust-graph.svg", "Distributed trust graph verifying every exchange"),
  compass: img("governance-compass.svg", "Governance compass steering regulated delivery"),
};

/* Industry motifs, matched by keyword anywhere in the page path. */
const INDUSTRY_RULES: [RegExp, Img][] = [
  [/banking|financial|insurance|fintech|capital-markets|payments/, img("capital-flow.svg", "Value streams compounding across a financial estate")],
  [/healthcare|pharma|life-science|medical/, img("health-pulse.svg", "Live clinical signal drawn across a monitoring line")],
  [/retail|consumer|e-?commerce|cpg/, img("retail-demand.svg", "Demand curve rising across channels with live nodes")],
  [/manufacturing|energy|utilit|industrial|automotive|logistics|supply/, img("energy-grid.svg", "Industrial grid with power flowing between control points")],
  [/government|public-sector|education|defense/, img("public-dome.svg", "Public-service dome with governed service arcs")],
  [/telecom|media|travel|hospitality|sports/, img("global-arcs.svg", "Global mesh linking markets through animated arcs")],
];

const INDUSTRY_IMG = img("global-arcs.svg", "Global delivery mesh in the Dataq brand");

const SOLUTION_RULES: [RegExp, Img][] = [
  [/workflow|orchestr|agent|swarm|hyperautomat|automation/, img("agent-swarm-flow.svg", "Orchestrated agents moving work through lanes")],
  [/decision|intelligen|insight|nexus|forecast/, img("decision-bars.svg", "Decision mesh surfacing ranked, governed decisions")],
  [/data|lakehouse|estate|govern|migrat|quality|master/, img("lakehouse-streams.svg", "Lakehouse layers receiving governed data streams")],
  [/securit|zero-trust|threat|sentinel|soc|compliance/, img("zero-trust-radar.svg", "Zero-trust radar sweeping the threat surface")],
  [/quantum|optimi|schedul|route/, img("quantum-orbits.svg", "Quantum-inspired optimization rings")],
  [/blockchain|ledger|trust|chain/, img("ledger-chain.svg", "Ledger chain passing signed pulses")],
  [/twin|iot|robot|sensor|simulat/, img("twin-mirror.svg", "Digital twin mirroring physical operations")],
  [/cloud|edge|infrastruc|platform-engineer|sre|devops/, img("edge-lattice.svg", "Edge lattice uplinking to the core")],
  [/compass|risk|regulat|audit|ethical/, img("governance-compass.svg", "Governance compass steering delivery")],
  [/generative|gen-?ai|copilot|knowledge|document/, img("ai-neural-mesh.svg", "Generative mesh composing knowledge")],
];

const HUB_IMG: Record<string, Img> = {
  "/services": img("platform-strata.svg", "Service platform strata in the Dataq brand"),
  "/solutions": img("ai-neural-mesh.svg", "Solution mesh composing intelligence"),
  "/industries": img("global-arcs.svg", "Global industry mesh"),
  "/platforms": img("platform-strata.svg", "Eight platforms, one governed stack"),
  "/case-studies": img("decision-bars.svg", "Outcomes surfaced as decision bars"),
  "/insights": img("lakehouse-streams.svg", "Insight streams from the knowledge estate"),
  "/newsroom": img("global-arcs.svg", "Dataq newsroom, worldwide"),
  "/careers": img("fleet-formation.svg", "Teams in formation — careers at Dataq"),
  "/about-us": img("global-arcs.svg", "Dataq across four global delivery centers"),
  "/why-dataq-soft": img("governance-compass.svg", "The Dataq edge — governed, outcome-linked delivery"),
  "/our-approach": img("platform-strata.svg", "The Dataq method, layer by layer"),
  "/patented-intelligence": img("orbit-converge.svg", "Patent-pending families converging into delivery"),
  "/partner-ecosystem": img("trust-graph.svg", "Partner trust graph"),
  "/global-offices": img("global-arcs.svg", "Four global delivery centers"),
  "/contact": img("global-arcs.svg", "Talk to Dataq Software"),
  "/values-culture": img("governance-compass.svg", "Values that steer every engagement"),
  "/book-a-briefing": img("decision-bars.svg", "Bring your baseline — leave with a plan"),
};

const DEFAULT_IMG = img("ai-neural-mesh.svg", "Dataq Software — intelligence, engineered for outcomes");

function firstRule(rules: [RegExp, Img][], haystack: string): Img | null {
  for (const [re, im] of rules) if (re.test(haystack)) return im;
  return null;
}

function pick(page: { url: string; template: string; l1?: string | null; l2?: string | null }): Img {
  const url = page.url || "/";
  const hay = `${url} ${page.l1 ?? ""} ${page.l2 ?? ""}`.toLowerCase();

  // hub + company pages first (exact-ish prefixes)
  for (const prefix of Object.keys(HUB_IMG).sort((a, b) => b.length - a.length)) {
    if (url === prefix || url.startsWith(prefix + "/") || url.startsWith(prefix)) {
      // only treat as hub when it's the hub root or a company section root
      if (url === prefix) return HUB_IMG[prefix];
      if (["/about-us", "/why-dataq-soft", "/our-approach", "/careers", "/newsroom", "/insights", "/case-studies", "/patented-intelligence", "/partner-ecosystem", "/global-offices", "/contact", "/values-culture", "/book-a-briefing"].some((c) => url.startsWith(c)))
        return HUB_IMG[prefix];
    }
  }

  const segs = url.split("/").filter(Boolean);
  if (segs[0] === "services") {
    for (const s of segs) if (TOWER_IMG[s]) return TOWER_IMG[s];
    const r = firstRule(SOLUTION_RULES, hay);
    if (r) return r;
    return TOWER_IMG["applied-ai-generative-ai"];
  }
  if (segs[0] === "platforms") {
    return PLATFORM_IMG[segs[segs.length - 1]] ?? PLATFORM_IMG.nexus;
  }
  if (segs[0] === "solutions") {
    return firstRule(SOLUTION_RULES, hay) ?? DEFAULT_IMG;
  }
  if (segs[0] === "industries") {
    return firstRule(INDUSTRY_RULES, hay) ?? INDUSTRY_IMG;
  }
  const r = firstRule(SOLUTION_RULES, hay) ?? firstRule(INDUSTRY_RULES, hay);
  return r ?? DEFAULT_IMG;
}

export function PageImagery({
  page,
}: {
  page: { url: string; template: string; l1?: string | null; l2?: string | null };
}) {
  if (page.url === "/search" || page.url === "/style-guide") return null;
  const im = pick(page);
  const priority = page.template === "tower_hub" || page.template === "industry_hub";
  return (
    <Reveal className="container-dq pt-2" delay={60}>
      <figure className="pi-figure overflow-hidden rounded-2xl border border-line bg-white shadow-1">
        <div className="relative aspect-[21/8] w-full overflow-hidden bg-navy-900">
          <Image
            src={im.src}
            alt={im.alt}
            fill
            sizes="(max-width: 768px) 100vw, 1200px"
            className="object-cover pi-img"
            priority={priority}
          />
          <div aria-hidden="true" className="absolute inset-0 bg-gradient-to-t from-navy-950/70 via-transparent to-transparent" />
        </div>
      </figure>
    </Reveal>
  );
}
