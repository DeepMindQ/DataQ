import Link from "next/link";
import {
  ArrowRight,
  ArrowLeftRight,
  Atom,
  Blocks,
  Bot,
  BrainCircuit,
  Building2,
  CloudCog,
  Cog,
  Compass,
  Crosshair,
  Database,
  FileSearch,
  FileSignature,
  Gauge as GaugeIcon,
  Handshake,
  Network,
  Radar,
  RefreshCw,
  Scale,
  ShieldCheck,
  Smartphone,
  Sparkles,
  UserCheck,
  Wrench,
} from "lucide-react";
import Reveal from "@/components/site/Reveal";
import { Marquee, CountUp } from "@/components/site/Motion";
import { PATENTS } from "@/lib/patents";
import {
  SpotlightSlider,
  PlatformTabs,
  SectionRail,
  EvidenceGrid,
  type EvidenceCard,
} from "@/components/site/Wave3";
import { Accordion } from "@/components/site/ui-bits";
import NewsletterForm from "./NewsletterForm";
import { CtaBand, Quote, StatsStrip } from "@/components/site/PagePieces";
import { readPage, fileForUrl, pageIndex, type PageData } from "@/lib/content";
import OpsConsole from "@/components/site/OpsConsole";

/* ── Home rewrite: calm, factual, TCS-register. Plain sentences, real
   facts, no invented jargon ("engagement notes", "gates", "regimes"),
   no repeated proof points, one stat strip, one offer per section. ──── */

/* company facts for the identity section — animated on reveal */
const IDENTITY_STATS = [
  { value: "4", label: "global delivery centers, one delivery standard" },
  { value: "24x7", label: "managed operations behind every program" },
  { value: "2400+", label: "engineers, consultants and domain specialists" },
];

/* the enterprise-systems practice: maintain · upgrade · migrate */
const ENTERPRISE_SYSTEMS = [
  { icon: Database, name: "Data analytics", desc: "Decision-ready reporting and analytics on the estate you already run.", url: "/services/data-analytics-lakehouse/" },
  { icon: Smartphone, name: "Mobility", desc: "Mobile front-ends that put enterprise systems in every pocket.", url: "/consulting/software-development/" },
  { icon: RefreshCw, name: "SAP upgrades", desc: "SAP 3.x and 7.0 lifted to SAP BI 7.3 without freezing the business.", url: "/consulting/erp-services/" },
  { icon: ArrowLeftRight, name: "BW to HANA", desc: "BW objects migrated onto HANA with parity proven object by object.", url: "/consulting/erp-services/" },
  { icon: Network, name: "EAI migrations", desc: "Enterprise application integration carried forward, interface by interface.", url: "/consulting/it-services/" },
];

/* the delivery bridge: onsite command ↔ offshore pods, one standard */
const BRIDGE_NODES = [
  {
    icon: Building2,
    t: "Your onsite team",
    points: ["Direct collaboration in your time zones", "Business context stays with your teams", "One accountable counterpart per program"],
  },
  {
    icon: Network,
    t: "Our offshore pods",
    points: ["Engineers who plug into your teams as extra capacity", "Capacity that scales without new overhead", "Coverage across four delivery centers"],
  },
  {
    icon: Scale,
    t: "One delivery standard",
    points: ["Named owners and audited SLAs", "The same quality checks on both sides", "Handovers that hold across every geography"],
  },
];

/* RPA lifecycle delivered with our Automation Anywhere partnership */
const RPA_STAGES = [
  { icon: FileSearch, t: "Process analysis", d: "We measure which processes are worth automating before anything is built." },
  { icon: Compass, t: "Vision & strategy", d: "Where robots pay for themselves first, and how the program scales from there." },
  { icon: Sparkles, t: "Proof of concept", d: "A working robot on a real process, with the business case proven on live data." },
  { icon: Cog, t: "Implementation", d: "Bots deployed into production under the same release checks as every build." },
  { icon: ShieldCheck, t: "24x7 managed support", d: "Bots monitored, maintained and improved around the clock." },
];

/* the regulations each industry answers to — real regimes, no invented words */
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

/* consulting groups — mirrored from the consulting practice pages */
const CONSULTING_GROUPS = [
  {
    name: "Data & analytics",
    desc: "Migration factories, decision products and platform moves for the classic data estate.",
    services: ["Data analytics & decision products", "Data migration & platform moves", "Digital transformation programs"],
  },
  {
    name: "Engineering & quality",
    desc: "Engineering pods that ship inside your controls, with quality designed in from the start.",
    services: ["Software development & engineering pods", "Testing & quality engineering", "Application services & modernization", "UI/UX design"],
  },
  {
    name: "Cloud & operations",
    desc: "Azure estates end to end, and managed operations with SLAs you can audit.",
    services: ["Cloud development & Azure services", "IT services & managed operations", "IT support & end-user services"],
  },
  {
    name: "Advisory & enterprise",
    desc: "ERP programs that land process and controls, managed capacity that scales, and security advisory.",
    services: ["IT consulting & managed capacity", "Cybersecurity consulting", "ERP services & enterprise core"],
  },
];
const ConsultIcons = [Database, Wrench, CloudCog, Handshake];

/* the questions a buyer asks before the final CTA */
const HOME_FAQ = [
  {
    q: "What happens if the two-week diagnostic says we should not build it?",
    a: "Then it paid for itself. Some ideas should not be built, and the cheapest place to learn that is a two-week diagnostic, not a year-long program. You get the evidence behind the verdict and the alternative path we scored, in writing.",
  },
  {
    q: "How do you keep programs from shipping work that is not ready?",
    a: "Nothing ships until its agreed measurement moves and the proof reconciles. Migrations are checked by reconciliation, decision systems by replaying past decisions, models by evaluation scores, security controls by live drills. Missing evidence stops a release before it reaches production.",
  },
  {
    q: "Who decides what success is measured against?",
    a: "Your side does. Your metric owner signs the baseline in week two, it stays in your estate, and we report against it every fortnight. If the owner changes, the baseline is re-signed before work continues.",
  },
  {
    q: "How does the patented IP work commercially?",
    a: "The platforms and method families are licensed inside the engagement fee, so there is nothing extra to buy. Accelerators built specifically for you can carry co-ownership terms, and your data and audit trail stay in your estate throughout.",
  },
];

export default function HomeView() {
  const page: PageData | null = fileForUrl("/") ? readPage(fileForUrl("/")!) : null;
  const brand = page?.extras;
  if (!page || !brand) {
    return <div className="container-dq py-20 text-navy-800">Content not generated yet.</div>;
  }

  /* case-library index — read once from the case-studies hub */
  const hubFile = fileForUrl("/case-studies/");
  const hubPage = hubFile ? readPage(hubFile) : null;
  const hubCards = (hubPage?.cards ?? []) as unknown as {
    title: string; url: string; industry: string; industry_url: string;
    desc: string; service?: string; service_url?: string; region?: string;
  }[];
  const indSeen = new Map<string, string>();
  for (const c of hubCards) if (!indSeen.has(c.industry)) indSeen.set(c.industry, c.industry_url);
  const CASE_INDUSTRIES = [...indSeen.entries()].map(([name, url]) => ({
    name, url, count: hubCards.filter((c) => c.industry === name).length,
  }));

  /* practice index — named practices per domain */
  const rows = pageIndex();
  const practicesOf = (name: string) =>
    rows.filter((r) => r.template === "service_page" && r.l2 === name).map((r) => ({ label: r.title, url: r.url }));

  /* flagship case card per industry */
  const evidenceCards: EvidenceCard[] = [];
  const seenInd = new Set<string>();
  for (const c of hubCards) {
    if (seenInd.has(c.industry)) continue;
    seenInd.add(c.industry);
    evidenceCards.push({
      title: c.title, url: c.url, desc: c.desc, tag: c.industry,
      industry: c.industry, service: c.service, service_url: c.service_url,
    });
  }

  /* hero stat strip: the four company facts, in one calm row */
  const pick = (prefix: string, fallbackIdx: number) =>
    brand.stats.find((s) => s.label.startsWith(prefix)) ?? brand.stats[fallbackIdx];
  const HERO_STATS = [
    pick("enterprise engagements", 3),
    pick("countries served", 4),
    pick("engineers", 7),
    pick("proprietary platforms", 5),
  ].filter(Boolean) as { value: string; label: string }[];

  /* insight read time */
  const wordsByUrl = new Map(rows.map((r) => [r.url, r.words] as const));
  const insightMeta = (url: string) => {
    const w = wordsByUrl.get(url) ?? 0;
    return `${Math.max(2, Math.ceil(w / 200))} min read`;
  };

  const SECTION_NAV = [
    { id: "identity", label: "Who we are" },
    { id: "services", label: "What we do" },
    { id: "delivery", label: "Delivery model" },
    { id: "rpa", label: "Automation" },
    { id: "patents", label: "Platforms & IP" },
    { id: "evidence", label: "Case studies" },
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

      {/* ── hero: one promise, two actions, one proof line, four facts ── */}
      <section id="top" className="relative overflow-hidden grad-navy-field text-white">
        <div className="bg-field-drift absolute inset-0 dot-grid" aria-hidden="true" />
        <div className="bg-glow-pulse absolute inset-0 grad-orange-glow" aria-hidden="true" />
        <div className="absolute inset-0 pattern-noise" aria-hidden="true" />
        <span className="dq-beam" aria-hidden="true" />
        <span className="dq-beam dq-beam-2" aria-hidden="true" />
        <div className="relative container-dq grid gap-10 pb-14 pt-16 sm:pt-24 lg:grid-cols-[minmax(0,7fr)_minmax(0,5fr)] lg:items-center">
          <div>
            <Reveal className="hero-choreo">
              <p className="rise-item text-[12px] font-semibold uppercase tracking-[0.22em] text-brand-300" style={{ ["--rise-delay" as string]: "40ms" }}>
                IT services · consulting · business solutions
              </p>
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
              <p className="rise-item measure mt-5 text-body-lg leading-relaxed text-white/70" style={{ ["--rise-delay" as string]: "560ms" }}>
                Dataq Software is a global IT services and consulting firm. From ERP and cloud to data, AI and
                security, we take on the programs enterprises depend on — and report every result against the
                business metric the program was funded to move.
              </p>
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
              <p className="rise-item mt-6 flex flex-wrap items-center gap-x-2 gap-y-1 text-[13px] text-white/65" style={{ ["--rise-delay" as string]: "780ms" }}>
                <ShieldCheck className="h-3.5 w-3.5 shrink-0 text-brand-300" aria-hidden="true" />
                <span>
                  Recent results: 38% lower fraud losses at a top-10 European bank · OEE +7.2 points across 14
                  plants · claims settled 55% faster.
                </span>
                <Link href="/case-studies/" className="link-animated font-semibold text-brand-300">
                  Read the case studies <ArrowRight className="inline h-3 w-3" />
                </Link>
              </p>
            </Reveal>
          </div>
          <div className="hidden lg:block">
            <Reveal delay={400}>
              <OpsConsole />
            </Reveal>
          </div>
        </div>
        <div className="relative container-dq pb-12">
          <StatsStrip stats={HERO_STATS} />
        </div>
      </section>

      {/* credentials + partnership marquee */}
      <div className="border-b border-line bg-navy-900/95">
        <Marquee
          dark
          className="marquee-dark container-dq"
          items={[
            "SOC 2 Type II", "ISO 27001", "ISO 9001", "GDPR & CCPA aligned",
            "SAP upgrades & BW on HANA", "Automation Anywhere partner",
            "24x7 managed operations", "4 global delivery centers",
          ]}
        />
      </div>

      {/* ── who we are ── */}
      <section id="identity" className="scroll-mt-24 border-b border-line bg-white">
        <div className="container-dq section-y-sm">
          <div className="grid gap-10 lg:grid-cols-[minmax(0,7fr)_minmax(0,5fr)] lg:items-start">
            <Reveal>
              <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">Who we are</p>
              <h2 className="text-display-3 mt-1 max-w-3xl text-navy-800 sm:text-[30px]">
                The systems large companies run are the systems we work on.
              </h2>
              <div className="mt-5 space-y-4 text-[15px] leading-relaxed text-slate-body/80">
                <p className="rise-item" style={{ ["--rise-delay" as string]: "300ms" }}>
                  Dataq Software works on the estate enterprises actually run: SAP and ERP cores, enterprise data
                  platforms and integrations, cloud infrastructure, and the AI now being layered on top of them.
                  We advise, we build, and we run what we build.
                </p>
                <p className="rise-item" style={{ ["--rise-delay" as string]: "420ms" }}>
                  Delivery teams work onsite and offshore under one standard, managed operations run around the
                  clock behind every program, and results are reported against the numbers agreed at the start.
                  Eight proprietary platforms and eight patented method families give every engagement a
                  configured starting point, so your budget goes to the work that is genuinely yours.
                </p>
              </div>
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
            <div className="grid gap-4">
              <Reveal delay={140}>
                <figure className="card-sheen relative overflow-hidden rounded-2xl border border-brand/25 bg-brand-tint/50 p-6 shadow-1">
                  <blockquote className="font-display text-[18px] font-semibold leading-snug text-navy-800">
                    &ldquo;We maintain what runs, upgrade what lags, and modernize what holds the business
                    back. That is the job, done as day-to-day work.&rdquo;
                  </blockquote>
                  <figcaption className="mt-4 text-[11.5px] font-bold uppercase tracking-[0.16em] text-brand-deep">
                    Dataq Software, company positioning
                  </figcaption>
                </figure>
              </Reveal>
              <Reveal delay={230}>
                <div className="rounded-2xl border border-line bg-mist/70 p-5">
                  <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-slate-body/55">How an engagement runs</p>
                  <ul className="mt-3 space-y-2.5 text-[13.5px] leading-relaxed text-slate-body/80">
                    <li className="flex items-start gap-2.5">
                      <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-brand" aria-hidden="true" />
                      Your onsite team stays in command, with direct collaboration in your time zones.
                    </li>
                    <li className="flex items-start gap-2.5">
                      <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-brand" aria-hidden="true" />
                      Offshore pods extend capacity under one delivery standard.
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

      {/* ── what we do: eight domains + the consulting practice ── */}
      <section id="services" className="scroll-mt-24 border-y border-line bg-mist/60 dot-grid-light">
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  What we do
                </p>
                <h2 className="text-display-3 mt-1 max-w-4xl text-navy-800 sm:text-[30px]">
                  Eight expertise domains and a full consulting practice
                </h2>
                <p className="mt-2 max-w-2xl text-[15px] leading-relaxed text-slate-body/75">
                  Each domain pairs named practices with the platform they run on. Whichever door you enter,
                  delivery follows the same rules: a named owner, a measurable result, and reporting against
                  your own numbers.
                </p>
              </div>
              <Link
                href="/services/"
                className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-deep"
              >
                All services <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
          </Reveal>
          <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            {brand.domains.map((t, i) => {
              const Icon = DOMAIN_ICONS[i % DOMAIN_ICONS.length];
              const practices = practicesOf(t.name).slice(0, 2);
              return (
                <Reveal key={t.url} delay={i * 40}>
                  <Link
                    href={t.url}
                    className="tilt-card group flex h-full flex-col rounded-2xl border border-line bg-white p-5 transition hover:-translate-y-0.5 hover:border-brand/60 shadow-1 hover:shadow-2"
                  >
                    <span className="flex h-10 w-10 items-center justify-center rounded-xl bg-navy-800 text-brand-300 transition group-hover:bg-brand group-hover:text-white">
                      <Icon className="h-5 w-5" aria-hidden="true" />
                    </span>
                    <p className="mt-3 font-display text-[16px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
                      {t.name}
                    </p>
                    <p className="mt-2 flex-1 text-[13px] leading-relaxed text-slate-body/75">{t.desc}</p>
                    <span className="mt-2.5 flex flex-wrap gap-1.5">
                      {practices.map((p) => (
                        <span key={p.url} className="rounded-full border border-line bg-mist/70 px-2 py-0.5 text-[11px] font-medium text-navy-800/85">
                          {p.label}
                        </span>
                      ))}
                    </span>
                    {t.plat && (
                      <span className="mt-2 text-[11px] font-medium text-slate-body/55">
                        Runs on {t.plat}
                      </span>
                    )}
                    <span className="mt-3 inline-flex items-center gap-1 text-[12px] font-semibold text-brand-deep">
                      Explore the practices <ArrowRight className="h-3.5 w-3.5 transition group-hover:translate-x-0.5" />
                    </span>
                  </Link>
                </Reveal>
              );
            })}
          </div>
        </div>

        {/* consulting & IT services — one band, plain language */}
        <div className="container-dq section-y-sm border-t border-line">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Consulting &amp; IT services
                </p>
                <h3 className="mt-1 font-display text-[24px] font-semibold text-navy-800">
                  Consulting that ends in delivery
                </h3>
                <p className="mt-2 max-w-2xl text-[15px] leading-relaxed text-slate-body/75">
                  Transformation programs, migration factories, engineering pods, quality engineering, Azure
                  estates, ERP cores, managed operations and end-user support. The team that advises you is the
                  team that builds it.
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
            {CONSULTING_GROUPS.map((g, i) => (
              <Reveal key={g.name} delay={i * 40}>
                <Link
                  href="/consulting/"
                  className="tilt-card group flex h-full flex-col rounded-2xl border border-line bg-white p-5 transition hover:-translate-y-0.5 hover:border-brand/60 shadow-1 hover:shadow-2"
                >
                  <span className="flex h-10 w-10 items-center justify-center rounded-xl bg-navy-800 text-brand-300 transition group-hover:bg-brand group-hover:text-white">
                    {(() => { const Ic = ConsultIcons[i % ConsultIcons.length]; return <Ic className="h-5 w-5" aria-hidden="true" />; })()}
                  </span>
                  <p className="mt-3 font-display text-[16px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
                    {g.name}
                  </p>
                  <p className="mt-2 flex-1 text-[13px] leading-relaxed text-slate-body/75">{g.desc}</p>
                  <span className="mt-2.5 space-y-1">
                    {g.services.slice(0, 3).map((s) => (
                      <span key={s} className="block text-[11.5px] leading-snug text-slate-body/60">{s}</span>
                    ))}
                  </span>
                </Link>
              </Reveal>
            ))}
          </div>
          {/* enterprise systems — maintain · upgrade · migrate */}
          <Reveal>
            <div className="mt-10 rounded-2xl border border-line bg-white p-5 sm:p-6">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <p className="text-[14px] font-semibold text-navy-800">
                  Enterprise systems — the work we are known for
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
                    <p className="mt-1 flex-1 text-[12px] leading-relaxed text-slate-body/70">{s.desc}</p>
                  </Link>
                ))}
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ── global delivery model ── */}
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
                  Onsite command, offshore scale, one delivery standard
                </h2>
              </div>
              <Link
                href="/consulting/it-services/"
                className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-300"
              >
                IT services &amp; managed operations <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
            <p className="rise-item mt-3 max-w-3xl text-[15px] leading-relaxed text-white/70" style={{ ["--rise-delay" as string]: "420ms" }}>
              Our teams work as one delivery organization: engineers who plug into your teams as extra capacity,
              while business ownership stays on your side. The same quality checks apply on both sides, so
              handovers stay clean across every geography.
            </p>
          </Reveal>
          <div className="relative mt-10">
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
                    <p className="mt-4 font-display text-[17px] font-semibold text-white">{n.t}</p>
                    <ul className="mt-3 space-y-2 text-[13.5px] leading-relaxed text-white/70">
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
          <Reveal>
            <div className="mt-8 grid gap-4 lg:grid-cols-[minmax(0,2fr)_minmax(0,3fr)] lg:items-center">
              <div className="grid grid-cols-3 gap-3">
                {[
                  { value: "4", label: "global delivery centers" },
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
              <p className="text-[14px] leading-relaxed text-white/65">
                Application maintenance is a transferable discipline. Our support teams have carried estates
                from one industry to another, through EAI migrations and a broad range of development tools —
                every pod backed by 24x7 managed operations.
              </p>
            </div>
          </Reveal>
        </div>
      </section>

      {/* ── automation partnership ── */}
      <section id="rpa" className="scroll-mt-24 border-b border-line bg-white">
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Automation partnership
                </p>
                <h2 className="text-display-3 mt-1 max-w-4xl text-navy-800 sm:text-[30px]">
                  RPA programs delivered end to end, with Automation Anywhere
                </h2>
                <p className="mt-2 max-w-3xl text-[15px] leading-relaxed text-slate-body/75">
                  Global implementations delivered through five owned stages — from the first process
                  measurement to round-the-clock support of the robots in production.
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
          <div className="relative mt-10">
            <Reveal className="absolute left-[6%] right-[6%] top-6 hidden lg:block">
              <div className="w9-step-line h-0.5 w-full rounded-full bg-brand/40" aria-hidden="true" />
            </Reveal>
            <ol className="grid gap-7 sm:grid-cols-2 lg:grid-cols-5 lg:gap-4">
              {RPA_STAGES.map((st, i) => (
                <li key={st.t} className="relative flex h-full flex-col">
                  <Reveal delay={i * 120} className="flex h-full flex-col">
                    <span className="relative z-10 flex h-12 w-12 items-center justify-center rounded-full border border-brand/40 bg-white text-brand-deep shadow-1 transition duration-300 hover:scale-110 hover:bg-brand hover:text-white">
                      <st.icon className="h-5 w-5" aria-hidden="true" />
                    </span>
                    <p className="mt-3 font-display text-[10.5px] font-bold uppercase tracking-[0.16em] text-brand-deep/70">
                      Stage {i + 1}
                    </p>
                    <p className="mt-0.5 text-[15px] font-semibold text-navy-800">{st.t}</p>
                    <p className="mt-1 flex-1 text-[13px] leading-relaxed text-slate-body/75">{st.d}</p>
                  </Reveal>
                </li>
              ))}
            </ol>
          </div>
        </div>
      </section>

      {/* ── platforms & patented methods ── */}
      <section id="patents" className="scroll-mt-24 container-dq section-y-sm">
        <Reveal>
          <div className="flex flex-wrap items-end justify-between gap-4">
            <div>
              <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                Platforms &amp; patented methods
              </p>
              <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                Every engagement starts from configured IP
              </h2>
              <p className="mt-2 max-w-3xl text-[15px] leading-relaxed text-slate-body/75">
                Eight platforms, one job each: Nexus runs decisions, Forge runs data, Swarm runs agents,
                Sentinel guards access, Twinverse mirrors operations, Quanta readies compute, Ledger anchors
                trust and Compass keeps AI inspectable. Licensing is included in the engagement fee — and
                accelerators built specifically for you can carry co-ownership terms.
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
        <Reveal>
          <div className="mt-10 flex flex-wrap items-end justify-between gap-4 border-t border-line pt-8">
            <h3 className="font-display text-[22px] font-semibold text-navy-800">
              The patented methods underneath
            </h3>
            <Link
              href="/patented-intelligence/"
              className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-deep"
            >
              The method map <ArrowRight className="h-4 w-4" />
            </Link>
          </div>
        </Reveal>
        <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {PATENTS.slice(0, 4).map((p, i) => (
            <Reveal key={p.ref} delay={i * 50}>
              <Link
                href="/patented-intelligence/"
                className="tilt-card group flex h-full flex-col rounded-2xl border border-line bg-white p-5 transition hover:-translate-y-0.5 hover:border-brand/60 shadow-1 hover:shadow-2"
              >
                <span className="w-fit rounded-full bg-brand-tint px-2.5 py-0.5 text-[10.5px] font-bold uppercase tracking-wider text-brand-deep">
                  {p.ref}
                </span>
                <p className="mt-3 flex-1 font-display text-[15px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
                  {p.title}
                </p>
                <p className="mt-2.5 rounded-lg bg-brand-tint/60 px-3 py-2 text-[12.5px] font-medium leading-snug text-brand-deep">
                  {p.outcome.replace(/^Means:\s*/, "")}
                </p>
              </Link>
            </Reveal>
          ))}
        </div>
      </section>

      {/* ── case studies ── */}
      <section id="evidence" className="scroll-mt-24 relative overflow-hidden border-y border-line grad-navy-field text-white">
        <div className="bg-field-drift absolute inset-0 dot-grid" aria-hidden="true" />
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar-dark text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-300">
                  Case studies
                </p>
                <h2 className="text-display-3 mt-1 text-white sm:text-[28px]">
                  Client outcomes, with the numbers left in
                </h2>
                <p className="mt-2 max-w-2xl text-[15px] text-white/65">
                  Every case study states what changed, by how much, and where it ran. Filter by industry, then
                  read the full note.
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
          <EvidenceGrid cards={evidenceCards} industries={CASE_INDUSTRIES} />
          <Reveal>
            <div className="mt-8">
              <SpotlightSlider slides={brand.cases} />
            </div>
          </Reveal>
        </div>
      </section>

      {/* ── how an engagement starts ── */}
      <section id="value" className="scroll-mt-24 border-y border-line bg-mist/60 dot-grid-light">
        <div className="container-dq section-y-sm">
          <Reveal>
            <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">Before delivery begins</p>
            <h2 className="text-display-3 mt-1 max-w-3xl text-navy-800 sm:text-[28px]">
              How an engagement starts
            </h2>
            <p className="mt-2 max-w-2xl text-[15px] leading-relaxed text-slate-body/75">
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
            <Reveal delay={120}>
              <div className="flex h-full flex-col rounded-2xl border border-line bg-white p-6 shadow-2">
                <p className="flex items-center gap-2 text-[11px] font-bold uppercase tracking-[0.14em] text-brand-deep">
                  <FileSignature className="h-4 w-4" aria-hidden="true" /> Program charter — one page
                </p>
                <div className="mt-3 space-y-2.5 text-[13px] leading-relaxed">
                  <p className="rounded-lg border border-line bg-mist/60 px-3 py-2">
                    <span className="font-semibold text-navy-800">Metric:</span>{" "}
                    <span className="text-slate-body/80">the number the program must move, signed as baseline</span>
                  </p>
                  <p className="rounded-lg border border-line bg-mist/60 px-3 py-2">
                    <span className="font-semibold text-navy-800">Control owner:</span>{" "}
                    <span className="text-slate-body/80">one accountable name per control</span>
                  </p>
                  <p className="rounded-lg border border-line bg-mist/60 px-3 py-2">
                    <span className="font-semibold text-navy-800">Risk boundary:</span>{" "}
                    <span className="text-slate-body/80">a fixed envelope, agreed with you at the start</span>
                  </p>
                </div>
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

      {/* ── industries ── */}
      <section id="industries" className="scroll-mt-24 border-b border-line bg-mist/60 dot-grid-light">
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Industries
                </p>
                <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                  Where we work — and the rules you answer to
                </h2>
                <p className="mt-2 max-w-2xl text-[15px] text-slate-body/75">
                  Twelve sectors, each brief mapping the regulations, systems and workflows your programs will
                  touch.
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
          <div className="mt-6 grid gap-2.5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            {brand.industries.map((ind) => {
              const notes = CASE_INDUSTRIES.find((c) => c.name === ind.name)?.count ?? 0;
              return (
                <Link
                  key={ind.url}
                  href={ind.url}
                  className="group flex items-center justify-between gap-2 rounded-xl border border-line bg-white px-4 py-3 transition hover:border-brand hover:shadow-1"
                >
                  <span className="min-w-0">
                    <span className="flex flex-wrap items-center gap-1.5 text-[13.5px] font-semibold text-navy-800 group-hover:text-brand-deep">
                      {ind.name}
                      {INDUSTRY_REGIME[ind.name] && (
                        <span className="rounded-full bg-brand-tint px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider text-brand-deep">
                          {INDUSTRY_REGIME[ind.name]}
                        </span>
                      )}
                    </span>
                    <span className="mt-0.5 block text-[11.5px] text-slate-body/60">
                      {notes} case {notes === 1 ? "study" : "studies"} published
                    </span>
                  </span>
                  <ArrowRight className="h-3.5 w-3.5 shrink-0 text-brand-deep transition group-hover:translate-x-0.5" aria-hidden="true" />
                </Link>
              );
            })}
          </div>
        </div>
      </section>

      {/* ── insights ── */}
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
              <p className="mt-2 max-w-2xl text-[15px] text-slate-body/75">
                What we are learning on live programs — retrieval layers, decision hubs, agent guardrails and
                the economics of GenAI — with the questions worth asking any vendor.
              </p>
            </div>
            <Link
              href="/insights/"
              className="inline-flex items-center gap-1.5 rounded-[10px] border border-line bg-white px-4 py-2 text-[13px] font-semibold text-navy-800 transition hover:border-brand hover:text-brand-deep"
            >
              Insights library <ArrowRight className="h-3.5 w-3.5" />
            </Link>
          </div>
        </Reveal>
        <div className="mt-8 grid gap-4 md:grid-cols-3">
          {brand.insights.slice(0, 3).map((it, i) => (
            <Reveal key={it.url} delay={i * 50}>
              <Link
                href={it.url}
                className="group flex h-full flex-col rounded-2xl border border-line bg-white p-5 transition hover:-translate-y-0.5 hover:border-brand/60 shadow-1 hover:shadow-2"
              >
                <span className="w-fit rounded-full bg-brand-tint px-2.5 py-0.5 text-[10.5px] font-semibold uppercase tracking-wider text-brand-deep">
                  {it.tag}
                </span>
                <p className="mt-3 font-display text-[16px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
                  {it.title}
                </p>
                <p className="mt-2 flex-1 text-[13px] leading-relaxed text-slate-body/75">{it.desc}</p>
                <span className="mt-3 text-[11.5px] font-medium text-slate-body/55">{insightMeta(it.url)}</span>
              </Link>
            </Reveal>
          ))}
        </div>
      </section>

      {/* client voice */}
      <section className="container-dq pt-12">
        <Quote
          text="Their controls went straight into our audit pack. Nothing needed translating."
          attribution="COO, European retail bank"
          role="Real-time fraud decisioning on instant payments"
        />
      </section>

      {/* newsletter */}
      <section className="container-dq pt-12">
        <Reveal>
          <div className="grid gap-6 rounded-2xl border border-line bg-mist/60 px-6 py-8 shadow-1 sm:px-10 md:grid-cols-[1fr_320px] md:items-center">
            <div>
              <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-brand-deep">The Delivery Floor, monthly</p>
              <p className="mt-1.5 max-w-lg font-display text-[18px] font-semibold leading-snug text-navy-800">
                One email a month from live programs. What worked, what did not, and the questions worth asking
                any vendor.
              </p>
            </div>
            <NewsletterForm />
          </div>
        </Reveal>
      </section>

      {/* FAQ */}
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
        <CtaBand message="Tell us the outcome you need to move. We will show you the method, the platform and the plan we would sign against it." />
      </section>
    </>
  );
}
