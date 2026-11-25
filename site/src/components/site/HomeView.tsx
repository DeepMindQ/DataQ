import Link from "next/link";
import { ArrowRight, ArrowLeftRight, BrainCircuit, Building2, Bot, Cog, Compass, Database, FileSearch, Network, ShieldCheck, Smartphone, Sparkles, RefreshCw, CloudCog, Atom, Blocks, Radar, Crosshair, UserCheck, Gauge as GaugeIcon, Wrench, Handshake, FileSignature, Scale } from "lucide-react";
import Reveal from "@/components/site/Reveal";
import { Marquee, CountUp } from "@/components/site/Motion";
import { PATENTS } from "@/lib/patents";
import {
  SpotlightSlider,
  IndustryFinder,
  PlatformTabs,
  RotatingProof,
  SectionRail,
  DomainRouter,
  EvidenceGrid,
  HomeIndustryExplorer,
  type RouterOption,
  type EvidenceCard,
  type HomeExplorerIndustry,
} from "@/components/site/Wave3";
import { Accordion } from "@/components/site/ui-bits";
import NewsletterForm from "./NewsletterForm";
import { CtaBand, Quote, StatsStrip } from "@/components/site/PagePieces";
import { readPage, fileForUrl, pageIndex, type PageData } from "@/lib/content";
import OpsConsole from "@/components/site/OpsConsole";

/* ── A-01..A-58 homepage rebuild (Wave 1 of the change register) ────────── */

/* domain hub display names by slug — used for patent reinforces links (A-31) */
const HUB_BY_SLUG: Record<string, string> = {
  "data-analytics-lakehouse": "Data, Analytics & Lakehouse",
  "applied-ai-generative-ai": "Applied AI & Generative AI",
  "quantum-advanced-compute": "Quantum & Advanced Compute",
  "cloud-edge-platform-engineering": "Cloud, Edge & Platform Engineering",
  "cybersecurity-zero-trust": "Cybersecurity & Zero-Trust",
  "iot-digital-twin-robotics": "IoT, Digital Twin & Robotics",
  "agentic-ai-hyperautomation": "Agentic AI & Hyperautomation",
  "blockchain-digital-trust": "Blockchain & Digital Trust",
};

/* Wave 7 — company identity facts, animated with CountUp on reveal.
   Deliberately different facts from the hero strip, so the page adds
   information instead of repeating itself. */
const IDENTITY_STATS = [
  { value: "4", label: "global delivery centers, one delivery standard" },
  { value: "24x7", label: "managed operations behind every program" },
  { value: "630+", label: "published delivery playbooks across industries" },
];

/* Wave 7 — the enterprise-systems practice: the maintained IT-services suite */
const ENTERPRISE_SYSTEMS = [
  { icon: Database, name: "Data Analytics", desc: "Decision-ready reporting and analytics on the estate you already run.", url: "/services/data-analytics-lakehouse/" },
  { icon: Smartphone, name: "Mobility", desc: "Mobile front-ends that put enterprise systems in every pocket.", url: "/services/" },
  { icon: RefreshCw, name: "SAP upgrades", desc: "SAP 3.X or 7.0 lifted to SAP BI 7.3, without freezing the business.", url: "/consulting/erp-services/" },
  { icon: ArrowLeftRight, name: "BW → HANA", desc: "BW objects migrated and transformed onto HANA, with parity proven.", url: "/consulting/erp-services/" },
  { icon: Network, name: "EAI migrations", desc: "Enterprise application integration carried forward, interface by interface.", url: "/consulting/it-services/" },
];

/* Wave 7 — the global delivery bridge: onsite command, offshore capability,
   one governance standard across the span. */
const BRIDGE_NODES = [
  {
    icon: Building2,
    t: "Your onsite team",
    points: ["Direct collaboration in your time zones", "Business context stays with your teams", "One accountable counterpart per program"],
  },
  {
    icon: Network,
    t: "Dataq offshore pods",
    points: ["Qualified engineers who plug into your teams", "Capacity that scales without new overhead", "24x7 coverage across the delivery centers"],
  },
  {
    icon: Scale,
    t: "One delivery standard",
    points: ["Named owners and audited SLAs", "The same quality checks on both sides of the bridge", "Handovers that hold across every geography"],
  },
];

/* Wave 7 — the end-to-end RPA lifecycle delivered with our Automation
   Anywhere partnership */
const RPA_STAGES = [
  { icon: FileSearch, t: "Process Analysis", d: "We measure which processes are worth automating before anything is built." },
  { icon: Compass, t: "RPA Vision & Strategy", d: "Where robots pay for themselves first, and how the program scales from there." },
  { icon: Sparkles, t: "Proof of Concept", d: "A working robot on a real process, with the business case proven on live data." },
  { icon: Cog, t: "Implementation", d: "Bots deployed into production under the same release checks as every build." },
  { icon: ShieldCheck, t: "24x7 Managed Support", d: "Bots monitored, maintained and improved around the clock, across geographies." },
];

/* A-33: the regime each industry is held to — sourced from the industry hubs */
const INDUSTRY_REGIME: Record<string, string> = {
  "Banking & Financial Services": "DORA",
  "Insurance & Risk": "Solvency II",
  "Healthcare & Life Sciences": "HIPAA · GxP",
  "Manufacturing & Industrial": "IEC 62443",
  "Energy & Utilities": "NERC CIP",
  "Telecom, Media & Entertainment": "NIS2",
  "Retail & Consumer Goods": "PCI DSS",
  "Technology & SaaS": "SOC 2 · ISO 27001",
  "Logistics & Supply Chain": "C-TPAT",
  "Agriculture & Food Systems": "FSMA",
  "Public Sector & Government": "FedRAMP",
  "Education & Research": "GDPR",
};

/* A-41: the release-gate pair each engagement note was governed by —
   the site's own gate vocabulary, keyed by the delivering domain */
/* the release checks each engagement note was governed by, in plain words */
const GATE_BY_SERVICE: Record<string, string> = {
  "Data, Analytics & Lakehouse": "Replay-tested decisions · freshness SLA",
  "Agentic AI & Hyperautomation": "Guardrails · human checkpoints",
  "Applied AI & Generative AI": "Eval scores · PoC kill rate",
  "Cybersecurity & Zero-Trust": "Live response drills · audit trail",
  "Cloud, Edge & Platform Engineering": "Reconciliation checks · rollback plan",
  "IoT, Digital Twin & Robotics": "Twin accuracy · safe updates",
  "Blockchain & Digital Trust": "Ledger parity · audit trail",
  "Quantum & Advanced Compute": "Honest benchmarks · classical parity",
};

/* A-52: the three-question router — pain surface → domain + two practices */
const ROUTER_OPTIONS: RouterOption[] = [
  {
    key: "decisions",
    label: "Decisions",
    blurb: "Decisions too slow to defend, or too opaque to audit.",
    domain: { label: "Agentic AI & Hyperautomation", url: "/services/agentic-ai-hyperautomation/" },
    practices: [
      { label: "Decision Intelligence Systems", url: "/services/agentic-ai-hyperautomation/decision-intelligence-systems/" },
      { label: "Agentic Process Automation", url: "/services/agentic-ai-hyperautomation/agentic-process-automation/" },
    ],
  },
  {
    key: "data",
    label: "Data",
    blurb: "Data nobody trusts, disputes nobody resolves.",
    domain: { label: "Data, Analytics & Lakehouse", url: "/services/data-analytics-lakehouse/" },
    practices: [
      { label: "Real-Time Streaming & Event-Driven Decisioning", url: "/services/data-analytics-lakehouse/realtime-streaming-decisioning/" },
      { label: "Lakehouse Architecture & Migration", url: "/services/data-analytics-lakehouse/lakehouse-architecture/" },
    ],
  },
  {
    key: "risk",
    label: "Risk",
    blurb: "Risk you can sense but cannot evidence to a regulator.",
    domain: { label: "Cybersecurity & Zero-Trust", url: "/services/cybersecurity-zero-trust/" },
    practices: [
      { label: "Zero-Trust Architecture & Implementation", url: "/services/cybersecurity-zero-trust/zero-trust-architecture/" },
      { label: "AI Security & Model Protection", url: "/services/cybersecurity-zero-trust/ai-security-model-protection/" },
    ],
  },
  {
    key: "estate",
    label: "Estate",
    blurb: "An estate that will not move without breaking something.",
    domain: { label: "Cloud, Edge & Platform Engineering", url: "/services/cloud-edge-platform-engineering/" },
    practices: [
      { label: "Cloud-Native & Legacy Modernization", url: "/services/cloud-edge-platform-engineering/cloud-native-modernization/" },
      { label: "Hybrid & Multicloud Architecture", url: "/services/cloud-edge-platform-engineering/hybrid-multicloud-architecture/" },
    ],
  },
  {
    key: "operations",
    label: "Operations",
    blurb: "Capacity, cutover, ERP cores or a helpdesk that has to answer.",
    domain: { label: "Consulting & IT Services", url: "/consulting/" },
    practices: [
      { label: "IT Services & Managed Operations", url: "/consulting/it-services/" },
      { label: "ERP Services & Enterprise Core", url: "/consulting/erp-services/" },
    ],
  },
];

const PILLARS = [
  {
    icon: Crosshair,
    title: "A named business metric",
    desc: "Every engagement starts with the number you need to move. It is agreed before work begins and reported every fortnight.",
  },
  {
    icon: UserCheck,
    title: "A named control owner",
    desc: "One accountable person on each control, never a committee. When your auditor asks who signed, the trail has a name.",
  },
  {
    icon: GaugeIcon,
    title: "A named risk boundary",
    desc: "The boundaries of acceptable risk are fixed at the start. Inside them, teams move fast. Outside them, nothing ships.",
  },
];

const DOMAIN_ICONS = [Database, Bot, BrainCircuit, ShieldCheck, CloudCog, Radar, Blocks, Atom];

/* consulting groups — mirrored from the consulting data (4 groups × practices) */
const CONSULTING_GROUPS = [
  {
    name: "Data & Analytics",
    desc: "Migration factories, decision products and platform moves for the classic data estate, all under one delivery discipline.",
    services: [
      { name: "Data Analytics & Decision Products" }, { name: "Data Migration & Platform Moves" }, { name: "Digital Transformation Programs" },
    ],
  },
  {
    name: "Engineering & Quality",
    desc: "Engineering pods that ship inside your controls, with quality designed in rather than tested afterwards.",
    services: [
      { name: "Software Development & Engineering Pods" }, { name: "Testing & Quality Engineering" }, { name: "Application Services & Modernization" }, { name: "UI/UX Design & Product Experience" },
    ],
  },
  {
    name: "Cloud & Operations",
    desc: "Azure estates end to end, and managed operations with SLAs you can audit.",
    services: [
      { name: "Cloud Development & Azure Services" }, { name: "IT Services & Managed Operations" }, { name: "IT Support & End-User Services" },
    ],
  },
  {
    name: "Advisory & Enterprise",
    desc: "ERP programs that land process and controls, managed capacity that scales, and zero-trust advisory.",
    services: [
      { name: "IT Consulting & Managed Capacity" }, { name: "Cybersecurity Consulting & Zero-Trust" }, { name: "ERP Services & Enterprise Core" },
    ],
  },
];
const ConsultIcons = [Database, Wrench, CloudCog, Handshake];

/* A-58: the objections a buyer raises before the final CTA, in plain words */
const HOME_FAQ = [
  {
    q: "What happens if the two-week diagnostic says we should not build it?",
    a: "Then it paid for itself. Some ideas should not be built, and the cheapest place to learn that is a two-week diagnostic, not a year-long program. You get the evidence that led to the verdict and the cheaper alternative path we scored, in writing.",
  },
  {
    q: "What stops a program from shipping something that is not ready?",
    a: "A release gate. Nothing ships until its measurement moves against the numbers agreed at the start and the proof reconciles. Migrations are checked by reconciliation, decision systems by replaying past decisions, models by evaluation scores, security controls by live drills. Missing evidence stops a release at the gate, not in production.",
  },
  {
    q: "Who decides what success is measured against?",
    a: "Your side does. Your metric owner signs the baseline in week two, it stays in your estate, and we report against it every fortnight. If the owner changes, the baseline is re-signed before work continues, and the audit trail records every signature.",
  },
  {
    q: "How does the patented IP work commercially?",
    a: "The platforms and method families are licensed inside the engagement fee, so there is nothing extra to buy to get started. Accelerators we build specifically for you can carry co-ownership terms, and your data, baselines and audit trail stay in your estate throughout.",
  },
];

export default function HomeView() {
  const page: PageData | null = fileForUrl("/") ? readPage(fileForUrl("/")!) : null;
  const brand = page?.extras;
  if (!page || !brand) {
    return <div className="container-dq py-20 text-navy-800">Content not generated yet.</div>;
  }

  /* case-library index counts — read once from the case-studies hub */
  const hubFile = fileForUrl("/case-studies/");
  const hubPage = hubFile ? readPage(hubFile) : null;
  const hubCards = (hubPage?.cards ?? []) as {
    title: string; url: string; industry: string; industry_url: string;
    desc: string; service?: string; service_url?: string; region?: string;
  }[];
  const CASE_COUNT = hubCards.length;
  const indSeen = new Map<string, string>();
  for (const c of hubCards) if (!indSeen.has(c.industry)) indSeen.set(c.industry, c.industry_url);
  const CASE_INDUSTRIES = [...indSeen.entries()].map(([name, url]) => ({
    name, url, count: hubCards.filter((c) => c.industry === name).length,
  }));
  const svcSeen = new Map<string, string>();
  for (const c of hubCards) if (c.service && !svcSeen.has(c.service)) svcSeen.set(c.service, c.service_url ?? "/services/");
  const CASE_SERVICES = [...svcSeen.keys()].map((name) => ({
    name, count: hubCards.filter((c) => c.service === name).length,
  }));

  /* practice index — counts + named practices per domain (A-20/22), insight read times (A-44) */
  const rows = pageIndex();
  const domainSlug = (name: string) => {
    for (const [slug, hubName] of Object.entries(HUB_BY_SLUG)) if (hubName === name) return slug;
    return "";
  };
  const practicesOf = (name: string) =>
    rows.filter((r) => r.template === "service_page" && r.l2 === name).map((r) => ({ label: r.title, url: r.url }));
  const domainCount = (name: string) => practicesOf(name).length;

  /* A-40: 12-card evidence grid — one flagship note per industry */
  const evidenceCards: EvidenceCard[] = [];
  const seenInd = new Set<string>();
  for (const c of hubCards) {
    if (seenInd.has(c.industry)) continue;
    seenInd.add(c.industry);
    evidenceCards.push({
      title: c.title, url: c.url, desc: c.desc, tag: c.industry,
      industry: c.industry, service: c.service, service_url: c.service_url,
      gate: c.service ? GATE_BY_SERVICE[c.service] : undefined,
    });
  }

  /* A-56: industry → top practices by published notes in that sector */
  const explorerIndustries: HomeExplorerIndustry[] = CASE_INDUSTRIES.map((ind) => {
    const cards = hubCards.filter((c) => c.industry === ind.name);
    const svcCount = new Map<string, number>();
    for (const c of cards) if (c.service) svcCount.set(c.service, (svcCount.get(c.service) ?? 0) + 1);
    const top = [...svcCount.entries()].sort((a, b) => b[1] - a[1]).slice(0, 3);
    const practices = top.map(([svc]) => {
      const hit = hubCards.find((c) => c.service === svc);
      return { label: svc, url: hit?.service_url ?? "/services/" };
    });
    return { name: ind.name, url: ind.url, regime: INDUSTRY_REGIME[ind.name] ?? "", notes: ind.count, practices };
  });

  /* A-44: read-time meta per insight card */
  const wordsByUrl = new Map(rows.map((r) => [r.url, r.words] as const));
  const insightMeta = (url: string) => {
    const w = wordsByUrl.get(url) ?? 0;
    return `${Math.max(2, Math.ceil(w / 200))} min read · practice desk`;
  };

  /* A-49/50 metadata lives in HOME_META + layout; home.json carries the same strings */

  const SECTION_NAV = [
    { id: "identity", label: "Who we are" },
    { id: "services", label: "What we do" },
    { id: "delivery", label: "Delivery model" },
    { id: "rpa", label: "Automation" },
    { id: "patents", label: "IP & platforms" },
    { id: "evidence", label: "Results" },
    { id: "value", label: "Charter" },
    { id: "industries", label: "Industries" },
    { id: "insights", label: "Insights" },
    { id: "faq", label: "FAQ" },
  ];

  const faqJsonLd = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: HOME_FAQ.map((f) => ({
      "@type": "Question",
      name: f.q,
      acceptedAnswer: { "@type": "Answer", text: f.a },
    })),
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqJsonLd) }} />
      <SectionRail items={SECTION_NAV} />

      {/* split hero — buyer + proof in the first three seconds (A-01..A-05) */}
      <section id="top" className="relative overflow-hidden grad-navy-field text-white">
        <div className="bg-field-drift absolute inset-0 dot-grid" aria-hidden="true" />
        <div className="bg-glow-pulse absolute inset-0 grad-orange-glow" aria-hidden="true" />
        <div className="absolute inset-0 pattern-noise" aria-hidden="true" />
        {/* light beams sweeping the hero — ambient motion, GPU-cheap */}
        <span className="dq-beam" aria-hidden="true" />
        <span className="dq-beam dq-beam-2" aria-hidden="true" />
        <div className="relative container-dq grid gap-10 pb-14 pt-16 sm:pt-24 lg:grid-cols-[minmax(0,7fr)_minmax(0,5fr)] lg:items-center">
          <div>
            <Reveal className="hero-choreo">
              {/* A-02: category chips, TCS-boilerplate vocabulary — the descriptor lives here, not in the H1 */}
              <p className="rise-item text-[12px] font-semibold uppercase tracking-[0.22em] text-brand-300" style={{ ["--rise-delay" as string]: "40ms" }}>
                IT services · consulting · business solutions
              </p>
              {/* A-01: brand line that says what we do — the category chip above carries the descriptor */}
              <h1 className="text-display-1 mt-4 max-w-3xl text-white">
                <span className="line-mask block" style={{ ["--rise-delay" as string]: "120ms" }}>
                  <span className="line-mask-inner block">We build, run and modernize</span>
                </span>
                <span className="line-mask block" style={{ ["--rise-delay" as string]: "260ms" }}>
                  <span className="line-mask-inner block">
                    the <span className="grad-text">systems</span> your business depends on.
                  </span>
                </span>
              </h1>
              {/* A-03: one promise sentence + one proof sentence, in plain words */}
              <p className="rise-item measure mt-5 text-body-lg leading-relaxed text-white/70" style={{ ["--rise-delay" as string]: "560ms" }}>
                Dataq Software is a global IT services and consulting firm. We deliver ERP, cloud, data, AI and
                security programs for enterprises in 40+ countries, starting from patented platforms and reporting
                every result against the metric your board already tracks.
              </p>
              {/* A-03: the three delivery vignettes, as a rotating proof line */}
              <div className="rise-item" style={{ ["--rise-delay" as string]: "620ms" }}>
                <RotatingProof
                  lines={[
                    "A top-10 European bank cut fraud losses 38% with real-time decisioning.",
                    "A global insurer settles claims 55% faster with document intelligence.",
                    "OEE up 7.2 points across 14 plants at a global automotive OEM.",
                    "SAP and BW estates upgraded and migrated to HANA, with parity proven.",
                    "Global RPA programs delivered end to end with Automation Anywhere.",
                  ]}
                />
              </div>
              {/* A-04: the ask, with what the buyer leaves with */}
              <div className="rise-item mt-8 flex flex-wrap items-center gap-3" style={{ ["--rise-delay" as string]: "680ms" }}>
                <Link
                  href="/book-a-briefing/"
                  className="btn-sheen inline-flex items-center gap-2 rounded-[10px] bg-brand px-6 py-3 text-[14px] font-semibold text-white transition hover:bg-brand-hover"
                >
                  Book a 45-minute briefing <ArrowRight className="h-4 w-4" />
                </Link>
                <Link
                  href="/services/"
                  className="inline-flex items-center rounded-[10px] border border-white/25 px-6 py-3 text-[14px] font-medium text-white/85 transition hover:border-brand-300 hover:text-brand-300"
                >
                  Explore what we do
                </Link>
              </div>
              <p className="rise-item mt-2 text-[12px] text-white/45" style={{ ["--rise-delay" as string]: "720ms" }}>
                A working session with a practice lead. Bring your problem, leave with a plan.
              </p>
              {/* A-05: outcome proof instead of compliance badges, linking to the evidence */}
              <p className="rise-item mt-6 flex flex-wrap items-center gap-x-4 gap-y-2 text-[12.5px] text-white/65" style={{ ["--rise-delay" as string]: "780ms" }}>
                <Link href="#evidence" className="inline-flex flex-wrap items-center gap-x-2 gap-y-1 hover:text-brand-300">
                  <ShieldCheck className="h-3.5 w-3.5 text-brand-300" aria-hidden="true" />
                  <span className="font-semibold text-white/80">38% lower fraud losses, OEE up 7.2 pts, claims 55% faster</span>
                  <span className="text-white/45">in the published engagement notes</span>
                </Link>
                <span className="rounded-full border border-white/15 px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wider text-white/45">
                  Published results
                </span>
              </p>
            </Reveal>
          </div>
          {/* the operations console — what a program reports (A-06/51/55 in OpsConsole) */}
          <div className="hidden lg:block">
            <Reveal delay={400}>
              <OpsConsole />
            </Reveal>
          </div>
        </div>
        {/* A-07: the stat strip renders ONCE · A-08/09/10/11 reconciled content · E-05 provenance note */}
        <div className="relative container-dq pb-12">
          <StatsStrip stats={brand.stats} />
          <p className="mt-2 text-right text-[10.5px] text-white/35">
            Operating metrics from the illustrative reference program. Engagement counts are delivery to date.
          </p>
        </div>
      </section>

      {/* credentials + platform marquee */}
      <div className="border-b border-line bg-navy-900/95">
        <Marquee
          dark
          className="marquee-dark container-dq"
          items={[
            "SOC 2 Type II", "ISO 27001", "ISO 9001", "GDPR & CCPA aligned", "24x7 managed operations",
            "SAP upgrades & BW on HANA", "RPA with Automation Anywhere", "Global delivery centers",
            "Dataq Nexus", "Dataq Forge", "Dataq Swarm", "Dataq Sentinel", "Dataq Twinverse", "Dataq Quanta", "Dataq Ledger", "Dataq Compass",
          ]}
        />
      </div>

      {/* Wave 7 — who we are: the company's positioning statement, in first person */}
      <section id="identity" className="scroll-mt-24 border-b border-line bg-white">
        <div className="container-dq section-y-sm">
          <div className="grid gap-10 lg:grid-cols-[minmax(0,7fr)_minmax(0,5fr)] lg:items-start">
            <Reveal>
              <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">Who we are</p>
              <h2 className="text-display-3 mt-1 max-w-3xl text-navy-800 sm:text-[30px]">
                <span className="line-mask block">
                  <span className="line-mask-inner block">The systems large companies run</span>
                </span>
                <span className="line-mask block" style={{ ["--rise-delay" as string]: "160ms" }}>
                  <span className="line-mask-inner block">
                    are the systems we <span className="grad-text">maintain, upgrade and modernize</span>.
                  </span>
                </span>
              </h2>
              <div className="mt-5 space-y-4 text-[14.5px] leading-relaxed text-slate-body/80">
                <p className="rise-item" style={{ ["--rise-delay" as string]: "300ms" }}>
                  Dataq Software is a technology consulting organization built for application transformation. We work
                  on the estate enterprises actually run: SAP and ERP cores, BW and enterprise integrations, data
                  estates, cloud platforms, and the AI now being layered on top of them.
                </p>
                <p className="rise-item" style={{ ["--rise-delay" as string]: "420ms" }}>
                  The portfolio pairs a full suite of maintained IT services with eight proprietary platforms, each
                  the productized form of a patented method family. Clients use them as a running start: configured
                  controls, delivery patterns and reporting from day one, so budget goes to the work that is
                  genuinely theirs.
                </p>
                <p className="rise-item" style={{ ["--rise-delay" as string]: "540ms" }}>
                  We advise, we build, and we run what we build. Delivery teams work on site and offshore under one
                  standard, managed operations run 24x7 behind every program, and results are reported against the
                  numbers agreed at the start. The technology carries the weight; your people keep the decisions.
                </p>
              </div>
              {/* identity facts — count up on reveal */}
              <div className="mt-7 grid max-w-xl grid-cols-3 gap-4">
                {IDENTITY_STATS.map((s, i) => (
                  <div
                    key={s.value}
                    className="rise-item rounded-xl border border-line bg-mist/70 px-4 py-3"
                    style={{ ["--rise-delay" as string]: `${620 + i * 90}ms` }}
                  >
                    <p className="font-display text-[22px] font-bold leading-none text-navy-800">
                      <CountUp value={s.value} />
                    </p>
                    <p className="mt-1.5 text-[11.5px] leading-snug text-slate-body/65">{s.label}</p>
                  </div>
                ))}
              </div>
            </Reveal>
            {/* right column — the positioning quote + how an engagement runs */}
            <div className="grid gap-4">
              <Reveal delay={140}>
                <figure className="card-sheen relative overflow-hidden rounded-2xl border border-brand/25 bg-brand-tint/50 p-6 shadow-1">
                  <svg aria-hidden="true" viewBox="0 0 48 48" className="float-slow h-9 w-9 text-brand-deep/25">
                    <path
                      fill="currentColor"
                      d="M10 34c-2.2 0-4-1.8-4-4V22c0-6.6 4.4-12 10-14l1.6 3.2c-3.2 1.4-5.4 4-5.9 7.3.5-.2 1.1-.3 1.8-.3 3.1 0 5.5 2.5 5.5 5.9S16.6 34 10 34Zm18 0c-2.2 0-4-1.8-4-4V22c0-6.6 4.4-12 10-14l1.6 3.2c-3.2 1.4-5.4 4-5.9 7.3.5-.2 1.1-.3 1.8-.3 3.1 0 5.5 2.5 5.5 5.9S31.6 34 28 34Z"
                    />
                  </svg>
                  <blockquote className="mt-3 font-display text-[17.5px] font-semibold leading-snug text-navy-800">
                    &ldquo;We maintain what runs, upgrade what lags, and modernize what holds the business back.
                    That is application transformation, done as day-to-day work rather than a slogan.&rdquo;
                  </blockquote>
                  <figcaption className="mt-4 text-[11.5px] font-bold uppercase tracking-[0.16em] text-brand-deep">
                    Dataq Software, company positioning
                  </figcaption>
                </figure>
              </Reveal>
              <Reveal delay={230}>
                <div className="rounded-2xl border border-line bg-mist/70 p-5">
                  <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-slate-body/55">How an engagement runs</p>
                  <ul className="mt-3 space-y-2.5 text-[13px] leading-relaxed text-slate-body/80">
                    <li className="flex items-start gap-2.5">
                      <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-brand" aria-hidden="true" />
                      Your onsite team stays in command, with direct collaboration in your time zones.
                    </li>
                    <li className="flex items-start gap-2.5">
                      <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-brand" aria-hidden="true" />
                      Qualified offshore pods extend capacity under one delivery standard.
                    </li>
                    <li className="flex items-start gap-2.5">
                      <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-brand" aria-hidden="true" />
                      Named owners and audited SLAs govern every program.
                    </li>
                  </ul>
                  <Link
                    href="#delivery"
                    className="link-animated mt-4 inline-flex items-center gap-1.5 text-[12.5px] font-semibold text-brand-deep"
                  >
                    See the delivery model <ArrowRight className="h-3.5 w-3.5" />
                  </Link>
                </div>
              </Reveal>
            </div>
          </div>
        </div>
      </section>

      {/* the expertise domains (A-17..A-22 + A-52 router) */}
      <section id="services" className="scroll-mt-24 border-y border-line bg-mist/60 dot-grid-light">
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Services &amp; consulting
                </p>
                {/* A-17 */}
                <h2 className="text-display-3 mt-1 max-w-4xl text-navy-800 sm:text-[30px]">
                  Eight deep-tech domains and a full consulting practice
                </h2>
                {/* A-18 */}
                <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                  Enter through any door; the same discipline governs the build. Named owners, measured results and
                  every outcome reported against your own numbers. The consulting practice follows the same rule:
                  the team that recommends is the team that builds.
                </p>
              </div>
              <div className="flex flex-col items-start gap-1.5">
                <Link
                  href="/services/"
                  className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-deep"
                >
                  All services <ArrowRight className="h-4 w-4" />
                </Link>
              </div>
            </div>
          </Reveal>
          <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {brand.domains.map((t, i) => {
              const Icon = DOMAIN_ICONS[i % DOMAIN_ICONS.length];
              const practices = practicesOf(t.name).slice(0, 3);
              return (
                <Reveal key={t.url} delay={i * 40}>
                  <Link
                    href={t.url}
                    className="tilt-card group flex h-full flex-col rounded-2xl border border-line bg-white p-5 transition hover:-translate-y-0.5 hover:border-brand/60 shadow-1 hover:shadow-2"
                  >
                    <span className="flex items-center justify-between">
                      <span className="float-slow flex h-10 w-10 items-center justify-center rounded-xl bg-navy-800 text-brand-300 transition group-hover:bg-brand group-hover:text-white group-hover:animate-none">
                        <Icon className="h-5 w-5" aria-hidden="true" />
                      </span>
                      {/* A-21: entry-intent tag on the two most-entered domains */}
                      {t.start && (
                        <span className="rounded-full bg-brand-tint px-2.5 py-0.5 text-[10px] font-bold uppercase tracking-wider text-brand-deep">
                          Start here
                        </span>
                      )}
                    </span>
                    <p className="mt-3 font-display text-[15.5px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
                      {t.name}
                    </p>
                    <p className="mt-2 flex-1 text-[12.5px] leading-relaxed text-slate-body/75">{t.desc}</p>
                    {/* A-19: the managed-on metric + flagship outcome */}
                    {t.metric && (
                      <p className="mt-2.5 rounded-md bg-navy-800 px-2.5 py-1.5 font-display text-[11.5px] font-semibold text-white">
                        {t.metric}
                      </p>
                    )}
                    {/* A-22: three named practices per card */}
                    <span className="mt-2.5 flex flex-wrap gap-1.5">
                      {practices.map((p) => (
                        <span key={p.url} className="rounded-full border border-line bg-mist/70 px-2 py-0.5 text-[11px] font-medium text-navy-800/85">
                          {p.label}
                        </span>
                      ))}
                    </span>
                    {/* A-39: the platform pairing */}
                    {t.plat && (
                      <span className="mt-2 text-[11px] font-medium text-slate-body/55">
                        Pairs with Dataq {t.plat.replace("Dataq ", "")}
                      </span>
                    )}
                    {/* A-20: count CTA */}
                    <span className="mt-3 inline-flex items-center gap-1 text-[12px] font-semibold text-brand-deep">
                      Explore practices <ArrowRight className="h-3.5 w-3.5 transition group-hover:translate-x-0.5" />
                    </span>
                  </Link>
                </Reveal>
              );
            })}
          </div>
          {/* A-52: the self-qualification router */}
          <DomainRouter options={ROUTER_OPTIONS} />
        </div>

        {/* consulting practices (A-23..A-27) — merged into the services band */}
        <div className="container-dq section-y-sm border-t border-line">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Consulting &amp; IT services
                </p>
                {/* A-23 */}
                <h3 className="mt-1 font-display text-[22px] font-semibold text-navy-800">
                  Consulting that ends in delivery
                </h3>
                {/* A-24 */}
                <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                  Transformation programs, migration factories, engineering pods, quality engineering, Azure estates,
                  ERP cores, managed operations and end-user support. The team that recommends is the team that
                  builds it, so nothing is lost between the deck and the build.
                </p>
              </div>
              <Link
                href="/consulting/"
                className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-deep"
              >
                All consulting practices <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
          </Reveal>
          <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {CONSULTING_GROUPS.slice(0, 4).map((g, i) => (
              <Reveal key={g.name} delay={i * 40}>
                <Link
                  href="/consulting/"
                  className="tilt-card group flex h-full flex-col rounded-2xl border border-line bg-white p-5 transition hover:-translate-y-0.5 hover:border-brand/60 shadow-1 hover:shadow-2"
                >
                  <span className="flex items-center justify-between">
                    <span className="flex h-10 w-10 items-center justify-center rounded-xl bg-navy-800 text-brand-300 transition group-hover:bg-brand group-hover:text-white">
                      {(() => { const Ic = ConsultIcons[i % ConsultIcons.length]; return <Ic className="h-5 w-5" aria-hidden="true" />; })()}
                    </span>
                    <ArrowRight className="h-4 w-4 text-brand-deep/40 transition group-hover:translate-x-0.5 group-hover:text-brand-deep" aria-hidden="true" />
                  </span>
                  <p className="mt-3 font-display text-[15.5px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
                    {g.name}
                  </p>
                  {/* A-25: a real description, not a name list */}
                  <p className="mt-2 flex-1 text-[12.5px] leading-relaxed text-slate-body/75">{g.desc}</p>
                  {/* A-26: CTA names the action, not the count */}
                  <span className="mt-3 inline-flex items-center gap-1 text-[12px] font-semibold text-brand-deep">
                    Explore the practices <ArrowRight className="h-3.5 w-3.5 transition group-hover:translate-x-0.5" />
                  </span>
                </Link>
              </Reveal>
            ))}
          </div>
          {/* Wave 7 — the enterprise-systems practice: maintain · upgrade · migrate */}
          <Reveal>
            <div className="mt-10 rounded-2xl border border-line bg-white p-5 sm:p-6">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Enterprise systems practice · maintain · upgrade · migrate
                </p>
                <Link
                  href="/consulting/erp-services/"
                  className="link-animated inline-flex items-center gap-1.5 text-[12.5px] font-semibold text-brand-deep"
                >
                  ERP &amp; enterprise core <ArrowRight className="h-3.5 w-3.5" />
                </Link>
              </div>
              <div className="mt-4 grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
                {ENTERPRISE_SYSTEMS.map((s, i) => (
                  <Link
                    key={s.name}
                    href={s.url}
                    className="tilt-card group flex h-full flex-col rounded-xl border border-line bg-white p-4 transition hover:-translate-y-0.5 hover:border-brand/60 shadow-1 hover:shadow-2"
                    style={{ transitionDelay: `${i * 30}ms` }}
                  >
                    <span className="flex h-9 w-9 items-center justify-center rounded-lg bg-navy-800 text-brand-300 transition group-hover:bg-brand group-hover:text-white">
                      <s.icon className="h-4.5 w-4.5" aria-hidden="true" />
                    </span>
                    <p className="mt-2.5 text-[13.5px] font-semibold text-navy-800 group-hover:text-brand-deep">{s.name}</p>
                    <p className="mt-1 flex-1 text-[11.5px] leading-relaxed text-slate-body/70">{s.desc}</p>
                  </Link>
                ))}
              </div>
            </div>
          </Reveal>
          {/* A-27: the bridge between the two taxonomies */}
          <Reveal>
            <p className="mt-6 flex flex-wrap items-center gap-1.5 text-[13px] text-slate-body/70">
              <Scale className="h-4 w-4 shrink-0 text-brand-deep" aria-hidden="true" />
              <span className="font-semibold text-navy-800">Where consulting meets expertise:</span>
              <span>platform moves land in</span>
              <Link href="/services/cloud-edge-platform-engineering/" className="link-animated font-semibold text-brand-deep">
                Cloud, Edge &amp; Platform Engineering
              </Link>
              <span>· decision products in</span>
              <Link href="/services/data-analytics-lakehouse/" className="link-animated font-semibold text-brand-deep">
                Data, Analytics &amp; Lakehouse
              </Link>
              <span>· zero-trust advisory in</span>
              <Link href="/services/cybersecurity-zero-trust/" className="link-animated font-semibold text-brand-deep">
                Cybersecurity &amp; Zero-Trust
              </Link>
            </p>
          </Reveal>
        </div>
      </section>

      {/* Wave 7 — global delivery model: the offshore capability headline, verbatim */}
      <section id="delivery" className="scroll-mt-24 relative overflow-hidden border-y border-line grad-navy-field text-white">
        <div className="bg-field-drift absolute inset-0 dot-grid" aria-hidden="true" />
        <div className="bg-glow-pulse absolute inset-0 grad-orange-glow-soft" aria-hidden="true" />
        <div className="absolute inset-0 pattern-noise" aria-hidden="true" />
        <div className="relative container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar-dark text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-300">
                  Global delivery model
                </p>
                <h2 className="text-display-3 mt-1 max-w-4xl text-white sm:text-[30px]">
                  <span className="line-mask block">
                    <span className="line-mask-inner block">Onsite command, offshore scale,</span>
                  </span>
                  <span className="line-mask block" style={{ ["--rise-delay" as string]: "170ms" }}>
                    <span className="line-mask-inner block">
                      one <span className="grad-text">delivery standard</span>
                    </span>
                  </span>
                </h2>
              </div>
              <Link
                href="/consulting/it-services/"
                className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-300"
              >
                IT services &amp; managed operations <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
            <p className="rise-item mt-3 max-w-3xl text-[14.5px] leading-relaxed text-white/70" style={{ ["--rise-delay" as string]: "420ms" }}>
              Teams at onshore and offshore locations work as one delivery organization: qualified engineers who
              plug into your organization as extra capacity, while business ownership stays on your side of the
              bridge. The same quality checks apply on both sides, so handovers stay clean across every geography.
            </p>
          </Reveal>
          {/* the delivery bridge — onsite command ↔ offshore pods, one standard across the span */}
          <div className="relative mt-10">
            {/* animated connector — desktop only, travels behind the node row */}
            <div className="absolute left-[8%] right-[8%] top-10 hidden lg:block" aria-hidden="true">
              <div className="w9-bridge-line w-full" />
              <div className="w9-travel-dot absolute inset-x-0 top-0 h-0" />
            </div>
            <div className="grid gap-4 lg:grid-cols-3">
              {BRIDGE_NODES.map((n, i) => (
                <Reveal key={n.t} delay={i * 140}>
                  <div className="relative flex h-full flex-col rounded-2xl border border-white/10 bg-white/[0.04] p-6 backdrop-blur transition hover:border-brand/50 hover:bg-white/[0.07]">
                    <span className="relative z-10 flex h-12 w-12 items-center justify-center rounded-2xl bg-brand text-white shadow-2">
                      <n.icon className="h-5.5 w-5.5" aria-hidden="true" />
                    </span>
                    <p className="mt-4 font-display text-[16.5px] font-semibold text-white">{n.t}</p>
                    <ul className="mt-3 space-y-2 text-[13px] leading-relaxed text-white/70">
                      {n.points.map((pt) => (
                        <li key={pt} className="flex items-start gap-2.5">
                          <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-brand-300" aria-hidden="true" />
                          {pt}
                        </li>
                      ))}
                    </ul>
                  </div>
                </Reveal>
              ))}
            </div>
          </div>
          {/* cross-industry AMS proof point — carried across sectors via EAI + tooling */}
          <Reveal>
            <div className="mt-8 grid gap-4 lg:grid-cols-[minmax(0,2fr)_minmax(0,3fr)] lg:items-center">
              <div className="grid grid-cols-3 gap-3">
                {[
                  { value: "4", label: "global delivery centers, one standard" },
                  { value: "24x7", label: "operations coverage" },
                  { value: "40+", label: "countries served" },
                ].map((s, i) => (
                  <div
                    key={s.label}
                    className="rise-item rounded-xl border border-white/10 bg-white/[0.05] px-3.5 py-3 text-center backdrop-blur"
                    style={{ ["--rise-delay" as string]: `${i * 90}ms` }}
                  >
                    <p className="font-display text-[20px] font-bold leading-none text-white">
                      <CountUp value={s.value} />
                    </p>
                    <p className="mt-1.5 text-[10.5px] leading-snug text-white/55">{s.label}</p>
                  </div>
                ))}
              </div>
              <p className="text-[13.5px] leading-relaxed text-white/65">
                Complex application maintenance is a transferable discipline. Our support teams have carried
                estates from one industry to another, through EAI migrations and a broad range of application
                development tools, and every pod is backed by 24x7 managed operations.
              </p>
            </div>
          </Reveal>
        </div>
      </section>

      {/* Wave 7 — RPA partnership: Automation Anywhere, end to end */}
      <section id="rpa" className="scroll-mt-24 border-b border-line bg-white">
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Automation partnership
                </p>
                <h2 className="text-display-3 mt-1 max-w-4xl text-navy-800 sm:text-[30px]">
                  Automation that ends in managed support
                </h2>
                <p className="mt-2 max-w-3xl text-[14.5px] leading-relaxed text-slate-body/75">
                  Our Automation Anywhere partnership has delivered global RPA implementations: robots put to work
                  where they pay back fastest, every stage owned and measured, and every handover documented.
                </p>
              </div>
              <Link
                href="/services/agentic-ai-hyperautomation/"
                className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-deep"
              >
                Agentic AI &amp; hyperautomation <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
          </Reveal>
          {/* the five-stage lifecycle — connected line draws itself on reveal */}
          <div className="relative mt-10">
            <Reveal className="absolute left-[6%] right-[6%] top-6 hidden lg:block">
              <div className="w9-step-line h-0.5 w-full rounded-full bg-brand/40" aria-hidden="true" />
            </Reveal>
            <ol className="grid gap-7 sm:grid-cols-2 lg:grid-cols-5 lg:gap-4">
              {RPA_STAGES.map((st, i) => (
                /* Reveal INSIDE the li: a wrapper div between <ol> and <li>
                   breaks list semantics (axe listitem rule, Lighthouse a11y). */
                <li key={st.t} className="relative flex h-full flex-col">
                  <Reveal delay={i * 120} className="flex h-full flex-col">
                    <span className="relative z-10 flex h-12 w-12 items-center justify-center rounded-full border border-brand/40 bg-white text-brand-deep shadow-1 transition duration-300 hover:scale-110 hover:bg-brand hover:text-white">
                      <st.icon className="h-5 w-5" aria-hidden="true" />
                    </span>
                    <p className="mt-3 font-display text-[10.5px] font-bold uppercase tracking-[0.16em] text-brand-deep/70">
                      Stage {i + 1}
                    </p>
                    <p className="mt-0.5 text-[14.5px] font-semibold text-navy-800">{st.t}</p>
                    <p className="mt-1 flex-1 text-[12.5px] leading-relaxed text-slate-body/75">{st.d}</p>
                  </Reveal>
                </li>
              ))}
            </ol>
          </div>
        </div>
      </section>

      {/* patented intelligence (A-28..A-32) */}
      <section id="patents" className="scroll-mt-24 container-dq section-y-sm">
        <Reveal>
          <div className="flex flex-wrap items-end justify-between gap-4">
            <div>
              <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                The IP differential
              </p>
              <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                Ambition is common. Proof is not.
              </h2>
              {/* A-32: the platforms named · A-28: the four-of-eight affordance */}
              <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                Every engagement starts from configured IP rather than a blank page and a staffing plan. Graph-native
                contextual intelligence, quantum-inspired optimization, federated trust, validated ethical decisions
                and self-evolving learning are developed by our research programme and run in production inside the
                platforms.{" "}
                <Link href="/patented-intelligence/" className="link-animated font-semibold text-brand-deep">
                  The method map lists every family with its controls.
                </Link>
              </p>
            </div>
            <Link
              href="/patented-intelligence/"
              className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-deep"
            >
              The method map <ArrowRight className="h-4 w-4" />
            </Link>
          </div>
        </Reveal>
        {/* the three IP strategies — how the differential lands commercially */}
        <div className="mt-8 grid gap-4 md:grid-cols-3">
          {[
            {
              t: "Start from configured IP",
              d: "Method families arrive pre-configured inside our platforms: controls, reporting and delivery patterns already in place. Budget goes to the 20% that is genuinely yours.",
            },
            {
              t: "Fewer hours to the same outcome",
              d: "With the heavy lifting in licensed IP, teams start near 80% ready, and the delta is measured against your own numbers. Speed you can check, not a claim.",
            },
            {
              t: "IP models that fit the deal",
              d: "License, embed or co-develop. Accelerators built specifically for you can carry co-ownership terms, so the advantage compounds on your side of the table too.",
            },
          ].map((s) => (
            <Reveal key={s.t}>
              <div className="h-full rounded-2xl border border-brand/25 bg-brand-tint/40 p-5">
                <p className="font-display text-[15px] font-semibold text-navy-800">{s.t}</p>
                <p className="mt-2 text-[12.5px] leading-relaxed text-slate-body/75">{s.d}</p>
              </div>
            </Reveal>
          ))}
        </div>
        <div className="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {PATENTS.slice(0, 4).map((p, i) => (
            <Reveal key={p.ref} delay={i * 50}>
              <Link
                href="/patented-intelligence/"
                className="tilt-card group flex h-full flex-col rounded-2xl border border-line bg-white p-5 transition hover:-translate-y-0.5 hover:border-brand/60 shadow-1 hover:shadow-2"
              >
                <span className="w-fit rounded-full bg-brand-tint px-2.5 py-0.5 text-[10.5px] font-bold uppercase tracking-wider text-brand-deep">
                  {p.ref}
                </span>
                <p className="mt-3 font-display text-[14.5px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
                  {p.title}
                </p>
                <p className="mt-2 flex-1 text-[12.5px] leading-relaxed text-slate-body/75">{p.oneLiner}</p>
                {/* A-29: the outcome line — what the method buys you */}
                <p className="mt-2.5 rounded-lg bg-brand-tint/60 px-3 py-2 text-[12px] font-medium leading-snug text-brand-deep">
                  {p.outcome}
                </p>
                {/* A-31: the service pages the family reinforces */}
                <span className="mt-2.5 flex flex-wrap gap-1.5">
                  {p.expertise.slice(0, 2).map((slug) => (
                    <span key={slug} className="rounded-full border border-line bg-mist/70 px-2 py-0.5 text-[10.5px] font-medium text-navy-800/80">
                      reinforces: {HUB_BY_SLUG[slug] ?? slug}
                    </span>
                  ))}
                </span>
                {/* A-30: CTA names the family */}
                <span className="mt-3 inline-flex items-center gap-1 text-[12px] font-semibold text-brand-deep">
                  Read {p.ref} <ArrowRight className="h-3.5 w-3.5 transition group-hover:translate-x-0.5" />
                </span>
              </Link>
            </Reveal>
          ))}
        </div>

          {/* platforms (A-37/38/39 in PlatformTabs) — merged into the IP band */}
          <div className="mt-10 border-t border-line pt-8">
            <Reveal>
              <div className="flex flex-wrap items-end justify-between gap-4">
                <div>
                  <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                    Platforms
                  </p>
                  <h3 className="mt-1 font-display text-[22px] font-semibold text-navy-800">
                    Eight platforms, one job each
                  </h3>
                  <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                    Nexus runs decisions · Forge runs data · Swarm runs agents · Sentinel guards access · Twinverse
                    mirrors operations · Quanta readies compute · Ledger anchors trust · Compass keeps AI inspectable.
                  </p>
                </div>
                <Link
                  href="/platforms/"
                  className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-deep"
                >
                  Platform portfolio <ArrowRight className="h-4 w-4" />
                </Link>
              </div>
            </Reveal>
          <div className="mt-8">
            <PlatformTabs platforms={brand.platforms} />
          </div>
          </div>
      </section>

      {/* evidence library (A-40..A-43, A-53) — proof, after the two offer tracks */}
      <section id="evidence" className="scroll-mt-24 relative overflow-hidden border-y border-line grad-navy-field text-white">
        <div className="bg-field-drift absolute inset-0 dot-grid" aria-hidden="true" />
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar-dark text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-300">
                  Evidence library
                </p>
                <h2 className="text-display-3 mt-1 text-white sm:text-[28px]">
                  Published results, with the numbers left in
                </h2>
                {/* A-08: reconciled count language */}
                <p className="mt-2 max-w-2xl text-[14.5px] text-white/65">
                  Every published engagement note carries the measured result, the system that produced it and the
                  industry it ran in. Filter by sector, then read the full note.
                </p>
              </div>
              <Link
                href="/case-studies/"
                className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-300"
              >
                Browse the full index <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
          </Reveal>
          {/* A-40/41/43: filterable grid with gates + delivering practice */}
          <EvidenceGrid cards={evidenceCards} industries={CASE_INDUSTRIES} />
          <Reveal>
            <div className="mt-8">
              <SpotlightSlider slides={brand.cases} />
            </div>
            {/* A-42: the lists carry their real name */}
            <div className="mt-9 grid gap-5 lg:grid-cols-[minmax(0,3fr)_minmax(0,2fr)]">
              <div>
                <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-white/45">Published engagement notes — by industry</p>
                <div className="mt-2.5 flex flex-wrap gap-2">
                  {CASE_INDUSTRIES.map((ind) => (
                    <Link
                      key={ind.name}
                      href="/case-studies/#by-industry"
                      className="rounded-full border border-white/15 bg-white/[0.05] px-3.5 py-1.5 text-[12.5px] font-medium text-white/75 transition hover:border-brand-300 hover:text-brand-300"
                    >
                      {ind.name} <span className="text-white/40">{ind.count}</span>
                    </Link>
                  ))}
                </div>
              </div>
              <div>
                <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-white/45">Published engagement notes — by service area</p>
                <div className="mt-2.5 flex flex-wrap gap-2">
                  {CASE_SERVICES.map((svc) => (
                    <Link
                      key={svc.name}
                      href="/case-studies/#by-service"
                      className="rounded-full border border-white/15 bg-white/[0.05] px-3.5 py-1.5 text-[12.5px] font-medium text-white/75 transition hover:border-brand-300 hover:text-brand-300"
                    >
                      {svc.name} <span className="text-white/40">{svc.count}</span>
                    </Link>
                  ))}
                </div>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* the engagement charter — with a redacted artifact (A-35/36) */}
      <section id="value" className="scroll-mt-24 border-y border-line bg-mist/60 dot-grid-light">
        <div className="container-dq section-y-sm">
          <Reveal>
            <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">Before delivery begins</p>
            <h2 className="text-display-3 mt-1 max-w-3xl text-navy-800 sm:text-[28px]">
              How an engagement starts
            </h2>
            <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
              One page, signed in week two: the metric the program must move, the owner of each control, and the
              boundaries of acceptable risk. Your board and your auditors read the same page delivery runs on.
            </p>
          </Reveal>
          <div className="mt-8 grid gap-4 lg:grid-cols-[minmax(0,3fr)_minmax(0,2fr)]">
            <div className="grid gap-4 md:grid-cols-3">
              {PILLARS.map((p, i) => (
                <Reveal key={p.title} delay={i * 70}>
                  <div className="h-full rounded-2xl border border-line bg-white p-6 shadow-1 transition hover:-translate-y-0.5 hover:border-brand/60 hover:shadow-2">
                    <span className="flex h-11 w-11 items-center justify-center rounded-xl bg-navy-800 text-brand-300">
                      <p.icon className="h-5 w-5" aria-hidden="true" />
                    </span>
                    <p className="mt-4 font-display text-[16px] font-semibold text-navy-800">{p.title}</p>
                    <p className="mt-2 text-[13px] leading-relaxed text-slate-body/75">{p.desc}</p>
                  </div>
                </Reveal>
              ))}
            </div>
            {/* A-35: the charter you sign, three fields filled */}
            <Reveal delay={120}>
              <div className="flex h-full flex-col rounded-2xl border border-line bg-white p-6 shadow-2">
                <p className="flex items-center gap-2 text-[11px] font-bold uppercase tracking-[0.14em] text-brand-deep">
                  <FileSignature className="h-4 w-4" aria-hidden="true" /> Program charter — one page
                </p>
                <div className="mt-3 space-y-2.5 text-[12.5px] leading-relaxed">
                  <p className="rounded-lg border border-line bg-mist/60 px-3 py-2">
                    <span className="font-semibold text-navy-800">Metric:</span>{" "}
                    <span className="text-slate-body/80">fraud losses per approved volume, signed as baseline and reported fortnightly</span>
                  </p>
                  <p className="rounded-lg border border-line bg-mist/60 px-3 py-2">
                    <span className="font-semibold text-navy-800">Control owner:</span>{" "}
                    <span className="text-slate-body/80">one accountable name per control, the trail a regulator walks</span>
                  </p>
                  <p className="rounded-lg border border-line bg-mist/60 px-3 py-2">
                    <span className="font-semibold text-navy-800">Risk boundary:</span>{" "}
                    <span className="text-slate-body/80">a fixed envelope, agreed with you at the start</span>
                  </p>
                </div>
                {/* A-36: inline CTA inside the section */}
                <Link
                  href="/book-a-briefing/"
                  className="link-animated mt-4 inline-flex items-center gap-1.5 text-[12.5px] font-semibold text-brand-deep"
                >
                  Your charter is drafted in the two-week diagnostic <ArrowRight className="h-3.5 w-3.5" />
                </Link>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* industries — regime chips + sector explorer (A-33/34/42/56) */}
      <section id="industries" className="scroll-mt-24 border-y border-line bg-mist/60 dot-grid-light">
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Industries
                </p>
                <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                  Built where you operate, under the rules you are held to
                </h2>
                {/* A-42: the list is named for what it is */}
                <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                  Each sector brief maps the industry&rsquo;s regulatory reality to our expertise domains, with named
                  workflows and the systems of record your programs will touch.
                </p>
              </div>
              <Link
                href="/industries/"
                className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-deep"
              >
                All industries <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
          </Reveal>
          <div className="mt-6 max-w-md">
            <IndustryFinder industries={brand.industries} />
          </div>
          {/* A-33/34: regime chip + engagement-note count on every tile */}
          <div className="mt-4 grid gap-2.5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            {brand.industries.map((ind) => {
              const notes = CASE_INDUSTRIES.find((c) => c.name === ind.name)?.count ?? 0;
              return (
                <Link
                  key={ind.url}
                  href={ind.url}
                  className="group flex items-center justify-between gap-2 rounded-xl border border-line bg-white px-4 py-3 transition hover:border-brand hover:shadow-1"
                >
                  <span className="min-w-0">
                    <span className="flex flex-wrap items-center gap-1.5 text-[13px] font-semibold text-navy-800 group-hover:text-brand-deep">
                      {ind.name}
                      {INDUSTRY_REGIME[ind.name] && (
                        <span className="rounded-full bg-brand-tint px-2 py-0.5 text-[9.5px] font-bold uppercase tracking-wider text-brand-deep">
                          {INDUSTRY_REGIME[ind.name]}
                        </span>
                      )}
                    </span>
                    {/* A-34: the second line, with the real count */}
                    <span className="mt-0.5 block text-[11px] text-slate-body/60">
                      {notes} published engagement {notes === 1 ? "note" : "notes"}
                    </span>
                  </span>
                  <ArrowRight className="h-3.5 w-3.5 shrink-0 text-brand-deep transition group-hover:translate-x-0.5" aria-hidden="true" />
                </Link>
              );
            })}
          </div>
          {/* A-56: industry → top practices explorer */}
          <HomeIndustryExplorer industries={explorerIndustries} />
        </div>
      </section>

      {/* insights (A-44/45) */}
      <section id="insights" className="container-dq scroll-mt-24 section-y-sm">
        <Reveal>
          <div className="flex flex-wrap items-end justify-between gap-4">
            <div>
              <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                Insights
              </p>
              <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                Field notes from live programs
              </h2>
              <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                What we are learning on live programs: retrieval layers, decision hubs, agent guardrails and the
                economics of GenAI, with the vendor questions worth asking.
              </p>
            </div>
            {/* A-45: the library button is a visible button */}
            <Link
              href="/insights/"
              className="inline-flex items-center gap-1.5 rounded-[10px] border border-line bg-white px-4 py-2 text-[13px] font-semibold text-navy-800 transition hover:border-brand hover:text-brand-deep"
            >
              Insights library <ArrowRight className="h-3.5 w-3.5" />
            </Link>
          </div>
        </Reveal>
        <div className="mt-8 grid gap-4 md:grid-cols-3">
          {brand.insights.map((it, i) => (
            <Reveal key={it.url} delay={i * 50}>
              <Link
                href={it.url}
                className="group flex h-full flex-col rounded-2xl border border-line bg-white p-5 transition hover:-translate-y-0.5 hover:border-brand/60 shadow-1 hover:shadow-2"
              >
                <span className="w-fit rounded-full bg-brand-tint px-2.5 py-0.5 text-[10.5px] font-semibold uppercase tracking-wider text-brand-deep">
                  {it.tag}
                </span>
                <p className="mt-3 font-display text-[15.5px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
                  {it.title}
                </p>
                <p className="mt-2 flex-1 text-[12.5px] leading-relaxed text-slate-body/75">{it.desc}</p>
                {/* A-44: depth meta line */}
                <span className="mt-3 text-[11px] font-medium text-slate-body/55">{insightMeta(it.url)}</span>
              </Link>
            </Reveal>
          ))}
        </div>
      </section>

      {/* A-46: a client voice, anonymized from a published engagement note */}
      <section className="container-dq pt-12">
        <Quote
          text="Their controls went straight into our audit pack. Nothing needed translating."
          attribution="COO, European retail bank"
          role="Published engagement note, real-time fraud decisioning on instant rails"
        />
      </section>

      {/* newsletter band (A-47) */}
      <section className="container-dq pt-12">
        <Reveal>
          <div className="grid gap-6 rounded-2xl border border-line bg-mist/60 px-6 py-8 shadow-1 sm:px-10 md:grid-cols-[1fr_320px] md:items-center">
            <div>
              <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-brand-deep">The Delivery Floor, monthly</p>
              <p className="mt-1.5 max-w-lg font-display text-[18px] font-semibold leading-snug text-navy-800">
                One email a month from live programs. What worked, what did not, and the questions worth asking any
                vendor.
              </p>
            </div>
            <NewsletterForm />
          </div>
        </Reveal>
      </section>

      {/* A-58: objection handling before the final CTA */}
      <section id="faq" className="container-dq scroll-mt-24 pt-12">
        <Reveal>
          <div className="max-w-3xl">
            <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">Before you commit</p>
            <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">The questions every buyer asks</h2>
          </div>
        </Reveal>
        <Reveal delay={80}>
          <div className="mx-auto mt-6 max-w-3xl text-left">
            <Accordion items={HOME_FAQ.map((f) => ({ q: f.q, a: f.a }))} />
          </div>
        </Reveal>
      </section>

      {/* closing CTA */}
      <section className="container-dq pb-16 pt-12">
        <CtaBand message="Bring the number you need to move. A practice lead will show you the method, the platform and the plan we would sign against it." />
      </section>
    </>
  );
}
