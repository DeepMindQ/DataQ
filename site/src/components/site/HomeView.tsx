import Link from "next/link";
import { ArrowRight, BrainCircuit, Bot, Database, ShieldCheck, CloudCog, Atom, Blocks, Radar, Crosshair, UserCheck, Gauge as GaugeIcon, Wrench, Handshake } from "lucide-react";
import Reveal from "@/components/site/Reveal";
import { Marquee } from "@/components/site/Motion";
import { PATENTS } from "@/lib/patents";
import { SpotlightSlider, IndustryFinder, PlatformTabs } from "@/components/site/Wave3";
import NewsletterForm from "./NewsletterForm";
import { CtaBand, Quote, StatsStrip } from "@/components/site/PagePieces";
import { readPage, fileForUrl, type PageData } from "@/lib/content";
import OpsConsole from "@/components/site/OpsConsole";

const PILLARS = [
  {
    icon: Crosshair,
    title: "A named business metric",
    desc: "Every engagement starts with the number you need to move — signed before delivery begins, reported every fortnight.",
  },
  {
    icon: UserCheck,
    title: "A named control owner",
    desc: "One accountable name on each control — not a committee. Regulators can walk the trail from gate to owner.",
  },
  {
    icon: GaugeIcon,
    title: "A named risk budget",
    desc: "The envelope of acceptable risk is fixed up front. Innovation inside it moves fast; nothing outside it ships.",
  },
];

const DOMAIN_ICONS = [BrainCircuit, Bot, Database, ShieldCheck, CloudCog, Atom, Blocks, Radar];

/* consulting groups — mirrored from the consulting data (4 groups × practices) */
const CONSULTING_GROUPS = [
  { name: "Data & Analytics", services: [
    { name: "Data Analytics & Decision Products" }, { name: "Data Migration & Platform Moves" }, { name: "Digital Transformation Programs" },
  ] },
  { name: "Engineering & Quality", services: [
    { name: "Software Development & Engineering Pods" }, { name: "Testing & Quality Engineering" }, { name: "Application Services & Modernization" }, { name: "UI/UX Design & Product Experience" },
  ] },
  { name: "Cloud & Operations", services: [
    { name: "Cloud Development & Azure Services" }, { name: "IT Services & Managed Operations" }, { name: "IT Support & End-User Services" },
  ] },
  { name: "Advisory & Enterprise", services: [
    { name: "IT Consulting & Managed Capacity" }, { name: "Cybersecurity Consulting & Zero-Trust" }, { name: "ERP Services & Enterprise Core" },
  ] },
];
const ConsultIcons = [Database, Wrench, CloudCog, Handshake];

/* the eight reporting panels of the steering pack — what leadership receives,
   described in words. No sample figures: the pack is generated from the
   client's own signed baseline, so inventing numbers would be dishonest. */
const STEERING_PANELS: { name: string; desc: string }[] = [
  { name: "Decision latency", desc: "How long the decision takes, end to end, against the baseline signed in week two." },
  { name: "Autonomous coverage", desc: "Which decisions now run without a human touch — and which deliberately keep one." },
  { name: "Where the value lands", desc: "Cost released, revenue protected, risk reduced — attributed line by line." },
  { name: "Gate-by-gate delta", desc: "The measured move at every delivery gate, with the evidence behind each figure." },
  { name: "Year-one cost walk", desc: "Run cost before, during and after — so finance sees the same numbers delivery does." },
  { name: "Control coverage", desc: "Controls live and tested versus the committed target, owned by a named person." },
  { name: "Maturity to outcome", desc: "Where the estate sits on the maturity curve and what the next gate requires." },
  { name: "Engagement model", desc: "Who is on the program, what they own, and how the team changes as value scales." },
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
  const hubCards = (hubPage?.cards ?? []) as { industry: string; industry_url: string; service?: string; service_url?: string }[];
  const CASE_COUNT = hubCards.length;
  const indSeen = new Map<string, string>();
  for (const c of hubCards) if (!indSeen.has(c.industry)) indSeen.set(c.industry, c.industry_url);
  const CASE_INDUSTRIES = [...indSeen.keys()].map((name) => ({
    name, count: hubCards.filter((c) => c.industry === name).length,
  }));
  const svcSeen = new Map<string, string>();
  for (const c of hubCards) if (c.service && !svcSeen.has(c.service)) svcSeen.set(c.service, c.service_url ?? "/services/");
  const CASE_SERVICES = [...svcSeen.keys()].map((name) => ({
    name, count: hubCards.filter((c) => c.service === name).length,
  }));

  return (
    <>
      {/* split hero — choreographed text + live intelligence-mesh visual (CHG-234/235) */}
      <section id="top" className="relative overflow-hidden grad-navy-field text-white">
        <div className="bg-field-drift absolute inset-0 dot-grid" aria-hidden="true" />
        <div className="bg-glow-pulse absolute inset-0 grad-orange-glow" aria-hidden="true" />
        <div className="absolute inset-0 pattern-noise" aria-hidden="true" />
        <div className="relative container-dq grid gap-10 pb-14 pt-16 sm:pt-24 lg:grid-cols-[minmax(0,7fr)_minmax(0,5fr)] lg:items-center">
          <div>
            <Reveal className="hero-choreo">
              <p className="rise-item text-[12px] font-semibold uppercase tracking-[0.22em] text-brand-300" style={{ ["--rise-delay" as string]: "40ms" }}>
                Global IT services &amp; consulting
              </p>
              <h1 className="text-display-1 mt-4 max-w-3xl text-white">
                <span className="line-mask block" style={{ ["--rise-delay" as string]: "120ms" }}>
                  <span className="line-mask-inner block">We build the systems institutions</span>
                </span>
                <span className="line-mask block" style={{ ["--rise-delay" as string]: "260ms" }}>
                  <span className="line-mask-inner block">
                    run on — <span className="grad-text">and prove every decision.</span>
                  </span>
                </span>
              </h1>
              <p className="rise-item measure mt-5 text-body-lg leading-relaxed text-white/70" style={{ ["--rise-delay" as string]: "560ms" }}>
                Fraud decided in milliseconds with the evidence attached. KYC backlogs cleared by governed agents.
                Data estates your auditors can walk alone. We build, run and prove the intelligence layer of the
                enterprise — eight proprietary platforms in production, every engagement gated on a metric your
                board already tracks.
              </p>
              <div className="rise-item mt-8 flex flex-wrap gap-3" style={{ ["--rise-delay" as string]: "680ms" }}>
                <Link
                  href="/book-a-briefing/"
                  className="btn-sheen inline-flex items-center gap-2 rounded-[10px] bg-brand px-6 py-3 text-[14px] font-semibold text-white transition hover:bg-brand-hover"
                >
                  Book an Executive Briefing <ArrowRight className="h-4 w-4" />
                </Link>
                <Link
                  href="/services/"
                  className="inline-flex items-center rounded-[10px] border border-white/25 px-6 py-3 text-[14px] font-medium text-white/85 transition hover:border-brand-300 hover:text-brand-300"
                >
                  Explore the capability map
                </Link>
              </div>
              {/* compliance line (kept lean — company figures live in the stats band below) */}
              <p className="rise-item mt-7 flex flex-wrap items-center gap-x-5 gap-y-2 text-[12px] text-white/55" style={{ ["--rise-delay" as string]: "780ms" }}>
                <span className="inline-flex items-center gap-1.5">
                  <ShieldCheck className="h-3.5 w-3.5 text-brand-300" aria-hidden="true" /> SOC 2 Type II · ISO 27001 · ISO 9001
                </span>
                <span className="inline-flex items-center gap-1.5">GDPR &amp; CCPA aligned delivery</span>
              </p>
            </Reveal>
            <div className="mt-10 lg:hidden">
              <StatsStrip stats={brand.stats} />
            </div>
          </div>
          {/* the operations console — what a program reports, rendered live */}
          <div className="hidden lg:block">
            <Reveal delay={400}>
              <OpsConsole />
            </Reveal>
          </div>
        </div>
        <div className="relative container-dq hidden pb-12 lg:block">
          <StatsStrip stats={brand.stats} />
        </div>
      </section>

      {/* credentials + platform marquee (CHG-124/125) */}
      <div className="border-b border-line bg-navy-900/95">
        <Marquee
          dark
          className="marquee-dark container-dq"
          items={[
            "SOC 2 Type II", "ISO 27001", "ISO 9001", "GDPR & CCPA aligned", "Zero-exposure delivery",
            "Dataq Nexus", "Dataq Forge", "Dataq Swarm", "Dataq Sentinel", "Dataq Twinverse", "Dataq Quanta", "Dataq Ledger", "Dataq Compass",
            "8 patented method families", "4 global delivery centers",
          ]}
        />
      </div>

      {/* steering pack — dark executive band: the delivery output, board-grade (Batch 2) */}
      <section id="output" className="vignette-section relative scroll-mt-24 overflow-hidden grad-navy-field text-white">
        <div className="orb-field" aria-hidden="true">
          <span className="orb" />
          <span className="orb" />
        </div>
        <div className="bg-field-drift absolute inset-0 dot-grid" aria-hidden="true" />
        <div className="absolute inset-0 pattern-noise" aria-hidden="true" />
        <div className="relative container-dq section-y-sm">
          <Reveal>
            <p className="kicker-bar-dark text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-300">What delivery produces</p>
            <h2 className="text-display-3 mt-1 max-w-4xl text-white sm:text-[28px]">
              Leadership reads the same panel every fortnight — against your baseline, not our brochure
            </h2>
            <p className="mt-2 max-w-4xl text-[14.5px] leading-relaxed text-white/65">
              Eight panels, one per decision surface: latency, autonomous coverage, where the value lands,
              gate-by-gate deltas, the cost walk, control coverage, maturity, and who owns what. Generated
              from your estate — so week two already reads like your business.
            </p>
          </Reveal>
          <div className="mt-8 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
            {STEERING_PANELS.map((p, i) => (
              <Reveal key={p.name} delay={i * 40}>
                <div className="h-full rounded-xl border border-white/10 bg-white/[0.04] p-5 backdrop-blur transition hover:border-brand/40 hover:bg-white/[0.07]">
                  <p className="font-display text-[11px] font-bold text-brand-300/90">{String(i + 1).padStart(2, "0")}</p>
                  <p className="mt-2 text-[14.5px] font-semibold text-white">{p.name}</p>
                  <p className="mt-1.5 text-[12.5px] leading-relaxed text-white/55">{p.desc}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* the eight expertise domains */}
      <section id="services" className="scroll-mt-24 border-y border-line bg-mist/60 dot-grid-light">
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Services
                </p>
                <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[30px]">
                  Eight domains. One engineering standard.
                </h2>
                <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                  Applied AI, agentic automation, data platforms, cybersecurity, cloud, quantum,
                  digital trust and IoT — each domain carries named services, an architecture you can
                  interrogate, and gates that stop the program when the evidence is missing.
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
              return (
                <Reveal key={t.url} delay={i * 40}>
                  <Link
                    href={t.url}
                    className="tilt-card group flex h-full flex-col rounded-2xl border border-line bg-white p-5 transition hover:-translate-y-0.5 hover:border-brand/60 shadow-1 hover:shadow-2"
                  >
                    <span className="flex items-center justify-between">
                      <span className="flex h-10 w-10 items-center justify-center rounded-xl bg-navy-800 text-brand-300 transition group-hover:bg-brand group-hover:text-white">
                        <Icon className="h-5 w-5" aria-hidden="true" />
                      </span>
                      <span className="font-display text-[12px] font-bold text-brand-deep/70">
                        {String(i + 1).padStart(2, "0")}
                      </span>
                    </span>
                    <p className="mt-3 font-display text-[15.5px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
                      {t.name}
                    </p>
                    <p className="mt-2 flex-1 text-[12.5px] leading-relaxed text-slate-body/75">{t.desc}</p>
                    <span className="mt-4 inline-flex items-center gap-1 text-[12px] font-semibold text-brand-deep">
                      Enter domain <ArrowRight className="h-3.5 w-3.5 transition group-hover:translate-x-0.5" />
                    </span>
                  </Link>
                </Reveal>
              );
            })}
          </div>
        </div>
      </section>

      {/* consulting practices (new section) */}
      <section id="consulting" className="scroll-mt-24 border-y border-line bg-white">
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Consulting practices
                </p>
                <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                  Thirteen practices for the work every enterprise still has to do
                </h2>
                <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                  Data migration without a lost row. Software that ships into your controls. Quality
                  engineered in, not tested after. Azure estates end to end. ERP programs that land
                  process and controls. Same contract everywhere: two-week diagnostic, signed baseline, evidence or stop.
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
                  className="tilt-card group flex h-full flex-col rounded-2xl border border-line bg-mist/60 p-5 transition hover:-translate-y-0.5 hover:border-brand/60 hover:bg-white shadow-1 hover:shadow-2"
                >
                  <span className="flex items-center justify-between">
                    <span className="flex h-10 w-10 items-center justify-center rounded-xl bg-navy-800 text-brand-300 transition group-hover:bg-brand group-hover:text-white">
                      {(() => { const Ic = ConsultIcons[i % ConsultIcons.length]; return <Ic className="h-5 w-5" aria-hidden="true" />; })()}
                    </span>
                    <span className="font-display text-[12px] font-bold text-brand-deep/70">
                      {String(i + 1).padStart(2, "0")}
                    </span>
                  </span>
                  <p className="mt-3 font-display text-[15.5px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
                    {g.name}
                  </p>
                  <p className="mt-2 flex-1 text-[12.5px] leading-relaxed text-slate-body/75">
                    {g.services.map((sv) => sv.name).join(" · ")}
                  </p>
                  <span className="mt-4 inline-flex items-center gap-1 text-[12px] font-semibold text-brand-deep">
                    Open the group <ArrowRight className="h-3.5 w-3.5 transition group-hover:translate-x-0.5" />
                  </span>
                </Link>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      {/* patented intelligence band (Wave 2 + patent directive) */}
      <section id="patents" className="scroll-mt-24 container-dq section-y-sm">
        <Reveal>
          <div className="flex flex-wrap items-end justify-between gap-4">
            <div>
              <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                Patented intelligence
              </p>
              <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                Eight patented method families behind every delivery
              </h2>
              <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                Graph-native contextual intelligence, quantum-inspired optimization, federated trust,
                validated ethical decisions and self-evolving learning — developed by our research programme and
                in production use inside named platforms.
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
        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
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
                <p className="mt-2 flex-1 text-[12.5px] leading-relaxed text-slate-body/75">
                  {p.oneLiner}
                </p>
                <span className="mt-4 inline-flex items-center gap-1 text-[12px] font-semibold text-brand-deep">
                  Read the method <ArrowRight className="h-3.5 w-3.5 transition group-hover:translate-x-0.5" />
                </span>
              </Link>
            </Reveal>
          ))}
        </div>
      </section>

      {/* industries */}
      <section id="industries" className="scroll-mt-24 border-y border-line bg-mist/60 dot-grid-light">
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Industries
                </p>
                <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                  Built where you operate — under the rules you are held to
                </h2>
                <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                  DORA in banking. HIPAA in health. IEC 62443 on the plant floor. Every industry hub
                  maps its regulatory reality and decision pressure to the expertise domains, with named workflows
                  and the systems of record your programs will touch.
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
          <div className="mt-4 flex flex-wrap gap-2.5">
            {brand.industries.map((ind) => (
              <Link
                key={ind.url}
                href={ind.url}
                className="rounded-full border border-line bg-white px-4 py-2 text-[13px] font-medium text-navy-800 transition hover:border-brand hover:bg-brand-tint hover:text-brand-deep"
              >
                {ind.name}
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* three-pillar operating discipline (CHG-239) */}
      <section id="value" className="scroll-mt-24 border-y border-line bg-mist/60 dot-grid-light">
        <div className="container-dq section-y-sm">
          <Reveal>
            <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">The operating discipline</p>
            <h2 className="text-display-3 mt-1 max-w-3xl text-navy-800 sm:text-[28px]">
              Three names signed before delivery begins — the engagement charter
            </h2>
          </Reveal>
          <div className="mt-8 grid gap-4 md:grid-cols-3">
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
        </div>
      </section>

      {/* platforms — interactive showcase tabs (CHG-240/241) */}
      <section id="platforms" className="scroll-mt-24 container-dq section-y-sm">
        <Reveal>
          <div className="flex flex-wrap items-end justify-between gap-4">
            <div>
              <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                Platforms
              </p>
              <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                Eight proprietary platforms in production
              </h2>
              <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                Decision hubs, data contracts, agent fleets, zero-trust estates, digital twins,
                quantum readiness, digital trust and field intelligence — each with architecture and
                evidence trails a regulator can walk.
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
      </section>

      {/* featured cases — spotlight slider (CHG-244/245/266) + dual index (Phase 2) */}
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
                  The numbers are the client&rsquo;s. The method is on the page.
                </h2>
                <p className="mt-2 max-w-2xl text-[14.5px] text-white/65">
                  {CASE_COUNT} anonymized engagements, indexed by industry and by service area — each with
                  the measured delta, the system that produced it, and the gates that governed the build.
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
          <div className="mt-8">
            <SpotlightSlider slides={brand.cases} />
          </div>
          {/* dual index teaser — industries with counts, linking into the library */}
          <Reveal>
            <div className="mt-9 grid gap-5 lg:grid-cols-[minmax(0,3fr)_minmax(0,2fr)]">
              <div>
                <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-white/45">By industry</p>
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
                <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-white/45">By service area</p>
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

      {/* insights */}
      <section className="container-dq section-y-sm">
        <Reveal>
          <div className="flex flex-wrap items-end justify-between gap-4">
            <div>
              <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                Insights
              </p>
              <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                From the delivery floor
              </h2>
              <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                Practitioner theses on the retrieval layer, decision hubs, policy envelopes and the
                economics of GenAI — with the vendor questions you should be asking.
              </p>
            </div>
            <Link
              href="/insights/"
              className="link-animated inline-flex items-center gap-1.5 text-[13.5px] font-semibold text-brand-deep"
            >
              Insights library <ArrowRight className="h-4 w-4" />
            </Link>
          </div>
        </Reveal>
        <div className="mt-8 grid gap-4 md:grid-cols-3">
          {brand.insights.map((it, i) => (
            <Reveal key={it.url} delay={i * 60}>
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
              </Link>
            </Reveal>
          ))}
        </div>
      </section>

      {/* engagement charter pull-quote (CHG-070) + testimonial band (CHG-248) */}
      <section className="container-dq pt-12">
        <Quote
          text="Every engagement anchored to a named business metric, a named control owner and a named risk budget."
          attribution="The Dataq engagement charter"
          role="Signed before delivery begins — measured at every gate"
        />
      </section>

      {/* newsletter band (CHG-254) */}
      <section className="container-dq pt-12">
        <Reveal>
          <div className="grid gap-6 rounded-2xl border border-line bg-mist/60 px-6 py-8 shadow-1 sm:px-10 md:grid-cols-[1fr_320px] md:items-center">
            <div>
              <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-brand-deep">Intelligence briefing</p>
              <p className="mt-1.5 max-w-lg font-display text-[18px] font-semibold leading-snug text-navy-800">
                One briefing a month — the delivery-floor thesis, the vendor questions, no noise.
              </p>
            </div>
            <NewsletterForm />
          </div>
        </Reveal>
      </section>

      {/* closing CTA */}
      <section className="container-dq pb-16 pt-12">
        <CtaBand message="Book an executive briefing — 45 minutes with a practice lead, your metric, and three reference engagements." />
      </section>
    </>
  );
}
