import Link from "next/link";
import Image from "next/image";
import { ArrowRight, ArrowUpRight, ChevronRight, Info, Layers, Cog, Factory, FileBarChart2, BookOpen, Boxes, Building2, Compass, UserRound, Mail, Scale, Briefcase, Newspaper, Wrench, MapPin, Handshake, ShieldCheck, FileText } from "lucide-react";
import Reveal from "./Reveal";
import { CountUp } from "./Motion";
import { PatentStrip, OfficesMap } from "./PageAugment";
import { pick as pickImagery } from "./PageImagery";
import { TechDiagram, DIAGRAM_KINDS, type DiagramKind } from "./TechDiagrams";
import { ArchGraph, MetricsDash, DashStyles } from "./ArchDash";
import { brandData, pageIndex } from "@/lib/content";
import type { Block, Card, Crumb, PageData } from "@/lib/content";

/* ── Breadcrumbs (CHG-062): chevrons, deep-path truncation, orange current ── */
export function Breadcrumbs({ crumbs, dark = false }: { crumbs: Crumb[]; dark?: boolean }) {
  // deep capability paths (4+ levels): keep first + last two, collapse the middle
  const truncated = crumbs.length > 4;
  const shown = truncated
    ? [crumbs[0], { name: "…", url: undefined } as Crumb, ...crumbs.slice(-2)]
    : crumbs;
  return (
    <nav aria-label="Breadcrumb" className={`text-[12px] ${dark ? "text-white/55" : "text-slate-body/60"}`}>
      <ol className="flex flex-wrap items-center gap-x-1 gap-y-1">
        {shown.map((c, i) => {
          const last = i === shown.length - 1;
          const collapsed = c.name === "…" && truncated;
          const label = (
            <span
              className={
                last
                  ? dark
                    ? "text-brand-300 font-medium"
                    : "text-brand-deep font-medium"
                  : undefined
              }
            >
              {c.name}
            </span>
          );
          return (
            <li key={`${c.name}-${i}`} className="flex items-center gap-1">
              {c.url && !last ? (
                <Link href={c.url} className={`hover:underline ${dark ? "hover:text-white/85" : "hover:text-navy-800"}`}>
                  {label}
                </Link>
              ) : (
                label
              )}
              {!last && <ChevronRight aria-hidden="true" className="h-3 w-3 opacity-40" />}
            </li>
          );
        })}
      </ol>
    </nav>
  );
}

/* ── Template kicker icon + v2 hero chrome (CHG-288/289/290/344) ─────── */
const KICKER_ICON: Record<string, React.ComponentType<{ className?: string }>> = {
  tower_hub: Layers,
  service_page: Cog,
  industry_hub: Factory,
  subindustry_page: Factory,
  industry_capability: Wrench,
  sub_capability: Wrench,
  solution_page: Handshake,
  platform_overview: Boxes,
  platform_architecture: ShieldCheck,
  platform_usecases: MapPin,
  case_study: FileBarChart2,
  insight_article: BookOpen,
  insights_category: BookOpen,
  company_page: Building2,
  approach_page: Compass,
  legal_page: Scale,
  contact_page: Mail,
  leadership_profile: UserRound,
  partner_page: Handshake,
  careers_page: Briefcase,
  newsroom_article: Newspaper,
};

/* Template-specific secondary hero CTA (CHG-290); empty = hide CTAs */
function heroSecondaryCta(page: PageData): { label: string; url: string } | null {
  switch (page.template) {
    case "case_study":
      return { label: "Run the same diagnostic", url: "/value-assessment/" };
    case "insight_article":
    case "newsroom_article":
      return { label: "Discuss with the practice lead", url: "/contact/" };
    case "careers_page":
      return { label: "See open positions", url: "/careers/open-positions/" };
    case "platform_architecture":
      return { label: "Talk to the platform team", url: "/contact/" };
    default:
      return { label: "Request a Value Assessment", url: "/value-assessment/" };
  }
}
const NO_HERO_CTA = new Set(["contact_page", "legal_page", "leadership_profile", "search_page"]);

/* Per-template micro-chips shown ON the hero image (wave-2 hero redesign).
   Two short, factual lines — never repeated copy, just template semantics. */
const HERO_CHIP: Record<string, { head: string; sub: string }> = {
  tower_hub: { head: "8 services · 2 platforms", sub: "Tower evidence pack" },
  service_page: { head: "Baseline → audited delta", sub: "Weekly evidence cadence" },
  sub_capability: { head: "Composable delivery", sub: "Signed baseline metric" },
  industry_capability: { head: "Sector-calibrated", sub: "Regime-aware controls" },
  subindustry_page: { head: "Workflow-level scope", sub: "Five priority capabilities" },
  industry_hub: { head: "8 capability lanes", sub: "Regulatory posture mapped" },
  solution_page: { head: "Composed architecture", sub: "Named prerequisites" },
  platform_overview: { head: "Production rails", sub: "Deployment under NDA" },
  platform_architecture: { head: "Three-plane design", sub: "Audit evidence ready" },
  platform_usecases: { head: "Proven scenarios", sub: "Reference flows" },
  case_study: { head: "Baseline audited", sub: "Method under NDA" },
  insight_article: { head: "Field-tested practice", sub: "No vendor theater" },
  newsroom_article: { head: "Company release", sub: "Press contact inside" },
  company_page: { head: "Operating detail", sub: "Named owners" },
  approach_page: { head: "Method, not slideware", sub: "Gates that bind" },
  partner_page: { head: "Certified delivery", sub: "Joint reference stack" },
  leadership_profile: { head: "Practice leader", sub: "Direct line to team" },
  careers_page: { head: "Hiring now", sub: "Human process" },
  legal_page: { head: "Plain-language terms", sub: "Effective date inside" },
  contact_page: { head: "Named inboxes", sub: "Response within 1 business day" },
};

/* ── Split hero v3 (wave-2): copy left, live visual INSIDE the title block ──
   The image is no longer a detached figure under the band — it is a framed
   panel of the hero grid itself, with beam sweep, telemetry chip and ring. */
export function PageHero({
  page,
  kicker,
  lede,
  children,
}: {
  page: PageData;
  kicker?: string;
  lede?: string;
  children?: React.ReactNode;
}) {
  const intro =
    lede ??
    (page.blocks.find((b) => b.t === "hero") as { x: string } | undefined)?.x ??
    page.blocks.find((b) => b.t === "p")?.x ??
    "";
  const Icon = KICKER_ICON[page.template];
  const secondary = heroSecondaryCta(page);
  const chips = [page.l1, page.l2, page.l3].filter(Boolean) as string[];
  const showVisual = page.url !== "/search" && page.url !== "/style-guide";
  const im = showVisual ? pickImagery(page) : null;
  const chip = HERO_CHIP[page.template];
  const priority = page.template === "tower_hub" || page.template === "industry_hub";
  return (
    <section className="dq-hero relative overflow-hidden grad-navy-field text-white">
      <div className="absolute inset-0 dot-grid" aria-hidden="true" />
      <div className="absolute inset-0 grad-orange-glow" aria-hidden="true" />
      <div className="relative container-dq pb-12 pt-10 sm:pb-16 sm:pt-14">
        <div className="hero-stagger grid gap-8 lg:grid-cols-[minmax(0,1fr)_minmax(0,30rem)] lg:items-center lg:gap-12">
          {/* left column — the copy */}
          <div className="min-w-0">
            <Breadcrumbs crumbs={page.crumbs} dark />
            <div className="measure mt-6">
              {kicker && (
                <p className="kicker-bar-dark flex items-center gap-2 text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-300">
                  {Icon && <Icon className="h-4 w-4" aria-hidden="true" />}
                  {kicker}
                </p>
              )}
              <h1 data-split className="text-display-2 mt-2 max-w-3xl text-white">{page.title}</h1>
              {intro && <p className="mt-4 text-[15px] leading-relaxed text-white/70">{intro}</p>}
            </div>
            {chips.length > 0 && (
              <div className="mt-5 flex flex-wrap items-center gap-2">
                {chips.map((c, i) => (
                  <span
                    key={c + i}
                    className="rounded-full border border-white/15 bg-white/[0.06] px-3 py-1 text-[11px] font-medium text-white/70"
                  >
                    {c}
                  </span>
                ))}
                {page.template === "case_study" && (
                  <span className="rounded-full border border-brand/40 bg-brand/15 px-3 py-1 text-[11px] font-semibold text-brand-300">
                    Identity withheld · Baseline audited · Method under NDA
                  </span>
                )}
              </div>
            )}
            {children}
            {!NO_HERO_CTA.has(page.template) && (
              <div className="mt-7 flex flex-wrap gap-3">
                <Link
                  href="/book-a-briefing/"
                  className="btn-sheen inline-flex items-center gap-2 rounded-[10px] bg-brand px-5 py-2.5 text-[13px] font-semibold text-white transition hover:bg-brand-hover"
                >
                  Book an Executive Briefing <ArrowRight className="h-4 w-4" />
                </Link>
                {secondary && (
                  <Link
                    href={secondary.url}
                    className="inline-flex items-center rounded-[10px] border border-white/25 px-5 py-2.5 text-[13px] font-medium text-white/85 transition hover:border-brand-300 hover:text-brand-300"
                  >
                    {secondary.label}
                  </Link>
                )}
              </div>
            )}
          </div>

          {/* right column — the visual, INSIDE the title block */}
          {im && (
            <figure className="hv-figure group relative m-0 aspect-[16/11] w-full overflow-hidden rounded-2xl border border-white/15 bg-navy-900 shadow-3 lg:aspect-[4/3]">
              <Image
                src={im.src}
                alt={im.alt}
                fill
                sizes="(max-width: 1024px) 100vw, 480px"
                className="object-cover hv-img"
                priority={priority}
              />
              {/* legibility + brand grading */}
              <div aria-hidden="true" className="pointer-events-none absolute inset-0 bg-gradient-to-t from-navy-950/85 via-navy-950/15 to-transparent" />
              <div aria-hidden="true" className="pointer-events-none absolute inset-0 grad-orange-glow-soft opacity-60 mix-blend-screen" />
              {/* animated beam sweep */}
              <div aria-hidden="true" className="hv-beam pointer-events-none absolute inset-0 overflow-hidden">
                <span />
              </div>
              {/* corner brackets */}
              <svg aria-hidden="true" className="pointer-events-none absolute inset-0 h-full w-full text-brand-300/70" viewBox="0 0 100 100" preserveAspectRatio="none">
                <path d="M3 12 V3 H12" fill="none" stroke="currentColor" strokeWidth="0.8" vectorEffect="non-scaling-stroke" />
                <path d="M88 3 H97 V12" fill="none" stroke="currentColor" strokeWidth="0.8" vectorEffect="non-scaling-stroke" />
                <path d="M97 88 V97 H88" fill="none" stroke="currentColor" strokeWidth="0.8" vectorEffect="non-scaling-stroke" />
                <path d="M12 97 H3 V88" fill="none" stroke="currentColor" strokeWidth="0.8" vectorEffect="non-scaling-stroke" />
              </svg>
              {/* template badge — top right */}
              {kicker && (
                <figcaption className="absolute right-3 top-3 rounded-full border border-white/20 bg-navy-950/55 px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.16em] text-white/80 backdrop-blur-sm">
                  {kicker}
                </figcaption>
              )}
              {/* telemetry chip — bottom left, rises on hover */}
              {chip && (
                <div className="hv-chip absolute bottom-3 left-3 rounded-xl border border-white/15 bg-navy-950/65 px-3.5 py-2.5 backdrop-blur-md">
                  <p className="text-[12.5px] font-semibold leading-none text-white">{chip.head}</p>
                  <p className="mt-1 flex items-center gap-1.5 text-[10.5px] leading-none text-brand-300">
                    <span className="hv-pulse inline-block h-1.5 w-1.5 rounded-full bg-brand" aria-hidden="true" />
                    {chip.sub}
                  </p>
                </div>
              )}
              <div aria-hidden="true" className="pointer-events-none absolute inset-0 rounded-2xl ring-1 ring-inset ring-white/10" />
            </figure>
          )}
        </div>
      </div>
    </section>
  );
}

/* ── Block renderer ───────────────────────────────────────────────────── */
export function Blocks({ blocks, skip = [] }: { blocks: Block[]; skip?: string[] }) {
  const out: React.ReactNode[] = [];
  let h2Index = 0;
  for (const b of blocks) {
    if (skip.includes(b.t)) continue;
    if (b.t === "p") {
      out.push(
        <Reveal key={`p-${out.length}`}>
          <p className="measure text-[15px] leading-[1.8] text-slate-body">{b.x}</p>
        </Reveal>,
      );
    } else if (b.t === "diagram") {
      out.push(
        <TechDiagram
          key={`d-${out.length}`}
          kind={(DIAGRAM_KINDS as string[]).includes(b.kind) ? (b.kind as DiagramKind) : "pipeline"}
          labels={b.labels}
          note={b.note}
          title={b.title}
        />,
      );
    } else if (b.t === "arch") {
      out.push(
        <ArchGraph
          key={`a-${out.length}`}
          title={b.title}
          lanes={b.lanes}
          nodes={b.nodes}
          edges={b.edges}
          note={b.note}
        />,
      );
    } else if (b.t === "dash") {
      out.push(
        <MetricsDash
          key={`m-${out.length}`}
          title={b.title}
          kpis={b.kpis}
          gates={b.gates}
          log={b.log}
          caption={b.note}
        />,
      );
    } else if (b.t === "h2") {
      h2Index += 1;
      const anchorId = `sec-${h2Index}`;
      out.push(
        <Reveal key={`h2-${h2Index}`}>
          <h2
            id={anchorId}
            className="dq-h2 group measure mt-12 flex scroll-mt-28 items-baseline gap-3 font-display text-[22px] font-semibold text-navy-800 sm:text-[24px]"
          >
            {b.x}
            {/* anchor link on hover (CHG-328) */}
            <a
              href={`#${anchorId}`}
              aria-label={`Link to section ${b.x}`}
              className="text-[13px] font-medium text-slate-body/30 opacity-0 transition group-hover:opacity-100 hover:text-brand-deep"
            >
              #
            </a>
          </h2>
        </Reveal>,
      );
    } else if (b.t === "bullets") {
      if (!b.items || b.items.length === 0) continue; // never render empty card grids
      out.push(
        <Reveal key={`b-${out.length}`}>
          <ul data-stagger className="mt-5 grid gap-3 sm:grid-cols-2">
            {b.items.map(([title, desc], i) => (
              <li
                key={i}
                className="card-sheen tilt-card group rounded-xl border border-line bg-white p-4 transition hover:-translate-y-0.5 hover:border-brand/50 shadow-1 hover:shadow-2"
              >
                <p className="text-[13.5px] font-semibold text-navy-800">{title}</p>
                <p className="mt-1 text-[12.5px] leading-relaxed text-slate-body/80">{desc}</p>
              </li>
            ))}
          </ul>
        </Reveal>,
      );
    } else if (b.t === "table") {
      out.push(
        <Reveal key={`t-${out.length}`}>
          <figure className="mt-8 overflow-hidden rounded-xl border border-line shadow-1">
            {b.caption && (
              <figcaption className="border-b border-line bg-mist px-4 py-3 text-[13px] font-semibold text-navy-800">
                {b.caption}
              </figcaption>
            )}
            <div className="overflow-x-auto">
              <table className="w-full min-w-[480px] text-left text-[13px]">
                <thead>
                  <tr className="bg-navy-800 text-white">
                    {b.headers.map((h) => (
                      <th key={h} className="px-4 py-2.5 font-semibold">
                        {h}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {b.rows.map((row, ri) => (
                    <tr key={ri} className={ri % 2 ? "bg-mist/60" : "bg-white hover:bg-brand-tint/60"}>
                      {row.map((cell, ci) => (
                        <td
                          key={ci}
                          className={`px-4 py-2.5 align-top ${
                            ci === 0
                              ? "sticky left-0 bg-inherit font-semibold text-navy-800 min-w-[132px]"
                              : "text-slate-body/85"
                          }`}
                        >
                          {cell}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </figure>
        </Reveal>,
      );
    } else if (b.t === "note") {
      out.push(
        <Reveal key={`n-${out.length}`}>
          <p className="mt-6 flex items-start gap-2.5 rounded-xl border border-brand/30 bg-brand-tint px-4 py-3 text-[12.5px] leading-relaxed text-slate-body/90">
            <Info className="mt-0.5 h-4 w-4 shrink-0 text-brand-deep" aria-hidden="true" />
            {b.x}
          </p>
        </Reveal>,
      );
    } else if (b.t === "cta") {
      out.push(<CtaBand key={`c-${out.length}`} message={b.x} />);
    } else if (b.t === "hero") {
      // rendered inside PageHero
      continue;
    }
  }
  return <div className="space-y-4">{out}</div>;
}

/* ── CTA band v2 — navy gradient + texture + orange actions (CHG-071) ──── */
export function CtaBand({ message }: { message: string }) {
  return (
    <Reveal className="mt-12">
      <div className="cta-glow-band relative overflow-hidden rounded-2xl grad-navy-field px-6 py-10 text-white shadow-3 sm:px-10">
        <div className="orb-field" aria-hidden="true">
          <span className="orb" />
          <span className="orb" />
          <span className="orb" />
        </div>
        <div className="absolute inset-0 dot-grid" aria-hidden="true" />
        <div className="absolute inset-0 grad-orange-glow" aria-hidden="true" />
        <div className="absolute inset-0 pattern-noise" aria-hidden="true" />
        <div className="relative flex flex-col gap-6 md:flex-row md:items-center md:justify-between">
          <p className="max-w-2xl font-display text-[19px] font-medium leading-snug sm:text-[21px]">{message}</p>
          <div className="flex flex-wrap gap-3">
            <Link
              href="/book-a-briefing/"
              className="btn-sheen inline-flex items-center gap-2 rounded-[10px] bg-brand px-5 py-2.5 text-[13px] font-semibold text-white hover:bg-brand-hover"
            >
              Book a briefing <ArrowUpRight className="h-4 w-4" />
            </Link>
            <Link
              href="/contact/"
              className="inline-flex items-center rounded-[10px] border border-white/25 px-5 py-2.5 text-[13px] font-medium text-white/85 hover:border-brand-300 hover:text-brand-300"
            >
              Contact us
            </Link>
          </div>
        </div>
      </div>
    </Reveal>
  );
}

/* ── Card grid (CHG-058 base card contract) ───────────────────────────── */
export function CardGrid({ cards, heading, sub }: { cards: Card[]; heading?: string; sub?: string }) {
  if (!cards.length) return null;
  return (
    <Reveal className="mt-14">
      <div className="flex items-end justify-between gap-4">
        <div>
          {heading && <h2 className="font-display text-[22px] font-semibold text-navy-800 sm:text-[24px]">{heading}</h2>}
          {sub && <p className="mt-1 text-[13.5px] text-slate-body/70">{sub}</p>}
        </div>
      </div>
      <div data-stagger className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {cards.map((c) => (
          <Link
            key={c.url + c.title}
            href={c.url}
            className="tilt-card group flex flex-col rounded-2xl border border-line bg-white p-5 transition hover:-translate-y-0.5 hover:border-brand/60 shadow-1 hover:shadow-2"
          >
            <span className="inline-flex w-fit rounded-full bg-brand-tint px-2.5 py-0.5 text-[10.5px] font-semibold uppercase tracking-wider text-brand-deep">
              {c.tag}
            </span>
            <p className="mt-3 font-display text-[15.5px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
              {c.title}
            </p>
            <p className="mt-1.5 flex-1 text-[12.5px] leading-relaxed text-slate-body/75">{c.desc}</p>
            <span className="mt-4 inline-flex items-center gap-1 text-[12px] font-semibold text-brand-deep">
              Explore <ArrowRight className="h-3.5 w-3.5 transition group-hover:translate-x-0.5" />
            </span>
          </Link>
        ))}
      </div>
    </Reveal>
  );
}

/* ── Pull-quote slab (CHG-070): navy field, oversized orange quote glyph ── */
export function Quote({
  text,
  attribution,
  role,
}: {
  text: string;
  attribution: string;
  role?: string;
}) {
  return (
    <Reveal>
      <figure className="quote-fade relative overflow-hidden rounded-2xl grad-navy-field px-6 py-10 text-white shadow-3 sm:px-12 sm:py-12">
        <div className="absolute inset-0 dot-grid" aria-hidden="true" />
        <div className="absolute inset-0 grad-orange-glow-soft" aria-hidden="true" />
        <span
          aria-hidden="true"
          className="quote-mark relative block select-none font-display text-[88px] leading-[0.7] text-brand sm:text-[112px]"
        >
          &ldquo;
        </span>
        <blockquote className="relative mt-4 max-w-3xl font-display text-[19px] font-medium leading-snug sm:text-[23px]">
          {text}
        </blockquote>
        <figcaption className="relative mt-6 flex items-center gap-3">
          <span aria-hidden="true" className="h-8 w-[3px] rounded-full bg-brand" />
          <span className="text-[13px]">
            <span className="block font-semibold text-white">{attribution}</span>
            {role && <span className="mt-0.5 block text-white/60">{role}</span>}
          </span>
        </figcaption>
      </figure>
    </Reveal>
  );
}

/* ── Related rail ─────────────────────────────────────────────────────── */
export function RelatedRail({ links }: { links: Card[] }) {
  if (!links.length) return null;
  return (
    <Reveal className="mt-14">
      <h2 className="font-display text-[20px] font-semibold text-navy-800">Related pages</h2>
      <div className="mt-5 grid gap-3 md:grid-cols-2">
        {links.map((l) => (
          <Link
            key={l.url + l.title}
            href={l.url}
            className="group flex items-start justify-between gap-4 rounded-xl border border-line bg-mist/50 px-4 py-3.5 transition hover:border-brand/60 hover:bg-white"
          >
            <span>
              <span className="block text-[13.5px] font-semibold text-navy-800 group-hover:text-brand-deep">
                {l.title}
              </span>
              {l.desc && <span className="mt-0.5 block text-[12px] text-slate-body/70">{l.desc}</span>}
            </span>
            <ArrowRight className="mt-1 h-4 w-4 shrink-0 text-brand-deep transition group-hover:translate-x-0.5" />
          </Link>
        ))}
      </div>
    </Reveal>
  );
}

/* ── Stats strip (CHG-069: tabular numerals, brand values) ────────────── */
export function StatsStrip({ stats }: { stats: { value: string; label: string }[] }) {
  return (
    <div data-stagger className="stat-flip grid grid-cols-2 gap-px overflow-hidden rounded-xl border border-white/10 bg-white/10 sm:grid-cols-4">
      {stats.map((s) => (
        <div key={s.label} className="bg-navy-800/70 px-4 py-5 text-center backdrop-blur">
          <p className="font-display text-[22px] font-bold tabular-nums text-brand sm:text-[26px]">
            <CountUp value={s.value} />
          </p>
          <p className="mt-1 text-[11px] leading-snug text-white/60">{s.label}</p>
        </div>
      ))}
    </div>
  );
}

/* ── Sibling paging + hub (CHG-329/330) + next-step map (CHG-337) ─────── */
function siblingPages(page: PageData) {
  const rows = pageIndex();
  const key = page.l2 || page.l1;
  const group = rows.filter((r) => (r.l2 || r.l1) === key && r.template === page.template);
  const idx = group.findIndex((r) => r.url === page.url);
  if (group.length < 2 || idx === -1) return null;
  const at = (i: number) => group[(i + group.length) % group.length];
  return { prev: at(idx - 1), next: at(idx + 1), position: idx + 1, total: group.length };
}
const NEXT_STEP: Record<string, { label: string; blurb: string; url: string }> = {
  consulting_service: { label: "Book a practice briefing", blurb: "45 minutes with the practice lead — your estate, the method, a straight feasibility read.", url: "/book-a-briefing/" },
  service_page: { label: "Value assessment", blurb: "Price the delta in your estate before anything is signed.", url: "/value-assessment/" },
  tower_hub: { label: "Book a briefing", blurb: "45 minutes with the tower lead — your metric, our method.", url: "/book-a-briefing/" },
  solution_page: { label: "Book a briefing", blurb: "Map this solution to the metric you own.", url: "/book-a-briefing/" },
  case_study: { label: "Run the same diagnostic", blurb: "The diagnostic that locked this baseline takes two weeks.", url: "/value-assessment/" },
  insight_article: { label: "Talk to the practice lead", blurb: "Bring your context — the thesis meets your data.", url: "/contact/" },
  platform_overview: { label: "See the platform live", blurb: "A working session on your use case, not a demo script.", url: "/book-a-briefing/" },
};

function faqJsonLd(page: PageData): object | null {
  if (page.template !== "service_page" && page.template !== "tower_hub") return null;
  const bullets = page.blocks
    .filter((b) => b.t === "bullets")
    .flatMap((b) => (b as { items: [string, string][] }).items.slice(0, 4));
  if (bullets.length < 3) return null;
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: bullets.map(([q, a]) => ({
      "@type": "Question",
      name: q,
      acceptedAnswer: { "@type": "Answer", text: a },
    })),
  };
}

/* ── Universal content page (all templates except home) ───────────────── */
export function ContentPage({ page }: { page: PageData }) {
  const kicker = sectionKicker(page);
  const siblings = siblingPages(page);
  const nextStep = NEXT_STEP[page.template];
  const faq = faqJsonLd(page);
  return (
    <>
      {faq && <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faq) }} />}
      <DashStyles />
      <PageHero page={page} kicker={kicker}>
        {page.published && (
          <p className="mt-3 inline-flex rounded-full border border-white/20 px-3 py-1 text-[11.5px] text-white/70">
            Published {page.published}
          </p>
        )}
        {page.profile && (
          <div className="mt-5 flex flex-wrap items-center gap-3">
            {/* navy-orange monogram (CHG-066) until photos exist */}
            <span className="flex h-12 w-12 items-center justify-center rounded-full bg-gradient-to-br from-navy-700 to-brand font-display text-[15px] font-bold text-white shadow-2">
              {page.profile.name
                .split(" ")
                .map((w) => w[0])
                .slice(0, 3)
                .join("")}
            </span>
            <div>
              <p className="text-[14.5px] font-semibold text-white">{page.profile.name}</p>
              <p className="text-[12px] text-white/55">{page.profile.role}</p>
            </div>
            <span className="ml-2 rounded-full border border-white/20 px-2.5 py-0.5 text-[10.5px] uppercase tracking-wider text-white/50">
              Profile
            </span>
          </div>
        )}
      </PageHero>
      <div className="container-dq py-12">
        {/* Phase 1 editorial layout: ONE centered article column. The old
            232px "On this page" rail and the duplicate back-to-hub link were
            removed — they produced the term-paper structure the redesign bans.
            Section wayfinding = breadcrumbs (hero) + hover anchors (headings)
            + the related/next-step rails at the end. */}
        <article className="dq-article mx-auto w-full max-w-[1080px]">
          <Blocks blocks={page.blocks} skip={["hero"]} />

          {/* in-narrative exploration cards ("Services in this tower", hubs…) */}
          <CardGrid
            cards={page.cards}
            heading={cardsHeading(page.template)}
            sub={cardsSub(page.template)}
          />

          {/* the patented methods underneath — factual, patent-mapped */}
          <PatentStrip page={page} />

          {page.profile && page.profile.focus.length > 0 && (
            <div className="mt-6 flex flex-wrap gap-2">
              {page.profile.focus.map((f) => (
                <span key={f} className="rounded-full border border-line bg-mist px-3 py-1 text-[12px] font-medium text-navy-800">
                  {f}
                </span>
              ))}
            </div>
          )}
          <RelatedRail links={page.related} />
          {/* prev / next sibling paging (CHG-330) */}
          {siblings && (
            <nav aria-label="Sibling pages" className="mt-12 grid gap-3 border-t border-line pt-6 sm:grid-cols-2">
              <Link
                href={siblings.prev.url}
                className="group rounded-xl border border-line bg-mist/50 px-4 py-3.5 transition hover:border-brand/60 hover:bg-white"
              >
                <span className="text-[10.5px] font-bold uppercase tracking-[0.14em] text-slate-body/50">
                  Previous · {siblings.position - 1 < 1 ? siblings.total : siblings.position - 1} of {siblings.total}
                </span>
                <span className="mt-0.5 flex items-center gap-1.5 text-[13.5px] font-semibold text-navy-800 group-hover:text-brand-deep">
                  <ChevronRight className="h-3.5 w-3.5 rotate-180" aria-hidden="true" /> {siblings.prev.title}
                </span>
              </Link>
              <Link
                href={siblings.next.url}
                className="group rounded-xl border border-line bg-mist/50 px-4 py-3.5 text-right transition hover:border-brand/60 hover:bg-white"
              >
                <span className="text-[10.5px] font-bold uppercase tracking-[0.14em] text-slate-body/50">
                  Next · {siblings.position + 1 > siblings.total ? 1 : siblings.position + 1} of {siblings.total}
                </span>
                <span className="mt-0.5 flex items-center justify-end gap-1.5 text-[13.5px] font-semibold text-navy-800 group-hover:text-brand-deep">
                  {siblings.next.title} <ChevronRight className="h-3.5 w-3.5" aria-hidden="true" />
                </span>
              </Link>
            </nav>
          )}
          {/* contextual next-step (CHG-337) */}
          {nextStep && (
            <Link
              href={nextStep.url}
              className="group mt-10 flex flex-col gap-3 rounded-2xl grad-navy-field px-6 py-6 text-white shadow-3 transition hover:shadow-2 sm:flex-row sm:items-center sm:justify-between"
            >
              <span>
                <span className="text-[11px] font-bold uppercase tracking-[0.16em] text-brand-300">Next step</span>
                <span className="mt-1 block font-display text-[17px] font-semibold text-white">{nextStep.label}</span>
                <span className="mt-0.5 block text-[12.5px] text-white/65">{nextStep.blurb}</span>
              </span>
              <span className="inline-flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-brand text-white transition group-hover:scale-105">
                <ArrowUpRight className="h-4.5 w-4.5" aria-hidden="true" />
              </span>
            </Link>
          )}
          <p className="mt-8 border-t border-line pt-4 text-[11px] text-slate-body/55">
            Maintained by the Dataq Software practice council · Last reviewed 2026-11 ·
            {" "}
            <Link href="/html-sitemap/" className="hover:text-brand-deep">
              Sitemap
            </Link>
          </p>
        </article>
        {page.url === "/global-offices/" && (
          <div className="mt-10">
            <OfficesMap offices={brandData().offices} />
          </div>
        )}
      </div>
    </>
  );
}

function sectionKicker(page: PageData): string | undefined {
  const map: Record<string, string> = {
    tower_hub: "Deep Technology Tower",
    service_page: "Service",
    industry_hub: "Industry",
    subindustry_page: "Sub-industry",
    industry_capability: "Industry Capability",
    sub_capability: "Sub-Industry Capability",
    solution_page: "Solution",
    platform_overview: "Platform",
    platform_architecture: "Platform — Architecture & Trust",
    platform_usecases: "Platform — Industry Use Cases",
    case_study: "Case Study — Anonymized",
    insight_article: "Insight",
    insights_category: "Insights Library",
    company_page: "Company",
    approach_page: "Our Approach",
    consulting_hub: "Consulting Services",
    consulting_service: "Consulting Practice",
    legal_page: "Legal & Compliance",
    contact_page: "Contact",
    leadership_profile: "Leadership",
    partner_page: "Partner Ecosystem — Alliance in validation",
    careers_page: "Careers",
    newsroom_article: "Newsroom",
    cases_hub: "Evidence",
    services_hub: "Deep Technology Towers",
    industries_hub: "Industries",
    solutions_hub: "Solutions",
    platforms_hub: "Proprietary Platforms",
    insights_hub: "Insights Library",
  };
  return map[page.template];
}

function cardsHeading(template: string): string {
  const map: Record<string, string> = {
    services_hub: "Eight deep technology towers",
    industries_hub: "Twelve industries, one operating discipline",
    solutions_hub: "24 outcome-linked solutions",
    platforms_hub: "The Dataq platform portfolio",
    cases_hub: "36 anonymized engagements",
    insights_hub: "Insight categories",
    tower_hub: "Services in this tower",
    industry_hub: "Sub-industries",
    subindustry_page: "Capabilities for this sub-industry",
    industry_capability: "Sub-industry depth",
    solution_page: "Related solutions",
    platforms_hub_alt: "",
  };
  return map[template] ?? "Explore further";
}

function cardsSub(template: string): string {
  const map: Record<string, string> = {
    cases_hub: "Identity withheld under confidentiality; measurement methods available under NDA.",
    insights_hub: "Practitioner theses from the delivery floor — published with vendor questions included.",
  };
  return map[template] ?? "";
}
