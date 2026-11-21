import Link from "next/link";
import { ArrowUpRight, ChevronRight } from "lucide-react";
import { PageHero, Blocks, CardGrid, RelatedRail } from "./PageBlocks";
import { DashStyles } from "./ArchDash";
import { PatentStrip, OfficesMap } from "./PageAugment";
import { brandData, pageIndex } from "@/lib/content";
import type { Block, PageData } from "@/lib/content";

export { Breadcrumbs, PageHero, Blocks, CtaBand, CardGrid, Quote, RelatedRail, StatsStrip } from "./PageBlocks";

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
  tower_hub: { label: "Book a briefing", blurb: "45 minutes with the domain lead — your metric, our method.", url: "/book-a-briefing/" },
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
    tower_hub: "Expertise Domain",
    service_page: "Service",
    industry_hub: "Industry",
    subindustry_page: "Sub-industry",
    industry_capability: "Industry Capability",
    sub_capability: "Sub-Industry Capability",
    solution_page: "Solution",
    platform_overview: "Platform",
    platform_architecture: "Platform — Architecture & Trust",
    platform_usecases: "Platform — Industry Use Cases",
    case_study: "Case study — anonymized",
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
    cases_hub: "Evidence library",
    services_hub: "Services & Expertise",
    industries_hub: "Industries",
    solutions_hub: "Solutions",
    platforms_hub: "Proprietary Platforms",
    insights_hub: "Insights Library",
  };
  return map[page.template];
}

function cardsHeading(template: string): string {
  const map: Record<string, string> = {
    services_hub: "The eight expertise domains",
    industries_hub: "Twelve industries, one operating discipline",
    solutions_hub: "24 outcome-linked solutions",
    platforms_hub: "The Dataq platform portfolio",
    cases_hub: "The case index",
    insights_hub: "Insight categories",
    tower_hub: "Services in this expertise domain",
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
    cases_hub: "Indexed by industry and service area — every case carries its measured delta and the gates that governed the build.",
    insights_hub: "Practitioner theses from the delivery floor — published with vendor questions included.",
  };
  return map[template] ?? "";
}
