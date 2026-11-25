import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { ContentPage } from "@/components/site/PagePieces";
import HomeView from "@/components/site/HomeView";
import { CaseHubView, CaseStudyView } from "@/components/site/CaseStudies";
import { brandData, fileForUrl, pageIndex, readPage, urlToSlugSegments, type PageData } from "@/lib/content";
import { ogImageFor } from "@/lib/og";

export const dynamicParams = false;

export function generateStaticParams(): { slug: string[] }[] {
  return pageIndex().map((r) => ({ slug: urlToSlugSegments(r.url) }));
}

const HOME_META: Metadata = {
  title: "Dataq Software — IT services, consulting & business solutions | AI, cloud, data, security, ERP",
  description:
    "Dataq Software is a global IT services and consulting partner. We build, run and modernize the ERP, cloud, data, AI and security systems enterprises depend on. SOC 2 Type II, ISO 27001.",
  alternates: { canonical: "/" },
  openGraph: {
    title: "Dataq Software — IT services, consulting & business solutions",
    description:
      "We build, run and modernize the systems your business depends on: ERP, cloud, data, AI and security, delivered on patented platforms in 40+ countries.",
    url: "/",
    siteName: "Dataq Software",
    type: "website",
    images: [{ url: ogImageFor("/"), width: 1200, height: 630, alt: "Dataq Software — enterprise AI, data and automation delivered with proof." }],
  },
  twitter: {
    card: "summary_large_image",
    title: "Dataq Software — IT services, consulting & business solutions",
    description: "We build, run and modernize the systems your business depends on.",
    images: [ogImageFor("/")],
  },
};

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug?: string[] }>;
}): Promise<Metadata> {
  const { slug = [] } = await params;
  if (slug.length === 0) return HOME_META;
  const url = "/" + slug.join("/") + "/";
  const rows = pageIndex();
  const row = rows.find((r) => r.url === url);
  if (!row) return {};
  const brand = brandData();
  const title = row.seoTitle || row.title;
  const description = row.metaDescription || brand.positioning;
  return {
    title,
    description,
    alternates: { canonical: url },
    openGraph: {
      title,
      description,
      url,
      siteName: brand.name,
      type: "website",
      images: [{ url: ogImageFor(url), width: 1200, height: 630, alt: title }],
    },
    twitter: {
      card: "summary_large_image",
      title,
      description,
      images: [ogImageFor(url)],
    },
  };
}

function breadcrumbJsonLd(page: PageData) {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: page.crumbs.map((c, i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: c.name,
      ...(c.url ? { item: brandData().site + c.url } : {}),
    })),
  };
}

function pageJsonLd(page: PageData): object | null {
  const brand = brandData();
  const base = { "@context": "https://schema.org" };
  switch (page.template) {
    case "service_page":
    case "expertise_hub":
      return {
        ...base,
        "@type": "Service",
        name: page.title,
        description: page.meta_description,
        provider: { "@type": "Organization", name: brand.legalName, url: brand.site },
        url: brand.site + page.url,
      };
    case "case_study":
    case "insight_article":
      return {
        ...base,
        "@type": "Article",
        headline: page.title,
        description: page.meta_description,
        author: { "@type": "Organization", name: brand.name },
        publisher: { "@type": "Organization", name: brand.legalName },
        url: brand.site + page.url,
      };
    case "newsroom_article":
      return {
        ...base,
        "@type": "NewsArticle",
        headline: page.title,
        description: page.meta_description,
        datePublished: page.published,
        author: { "@type": "Organization", name: brand.name },
        publisher: { "@type": "Organization", name: brand.legalName },
        url: brand.site + page.url,
      };
    case "leadership_profile":
      return {
        ...base,
        "@type": "ProfilePage",
        name: page.profile?.role || page.title,
        url: brand.site + page.url,
        about: { "@type": "Organization", name: brand.legalName },
      };
    default:
      return null;
  }
}

export default async function CatchAllPage({ params }: { params: Promise<{ slug?: string[] }> }) {
  const { slug = [] } = await params;
  if (slug.length === 0) return <HomeView />;
  const url = "/" + slug.join("/") + "/";
  const file = fileForUrl(url);
  const page = file ? readPage(file) : null;
  if (!page) notFound();

  const bc = breadcrumbJsonLd(page);
  const extra = pageJsonLd(page);
  if (page.template === "cases_hub") {
    return (
      <>
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(bc) }} />
        {extra && <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(extra) }} />}
        <CaseHubView page={page} />
      </>
    );
  }
  if (page.template === "case_study") {
    const hubFile = fileForUrl("/case-studies/");
    const hub = hubFile ? readPage(hubFile) : null;
    return (
      <>
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(bc) }} />
        {extra && <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(extra) }} />}
        <CaseStudyView page={page} hub={hub} />
      </>
    );
  }
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(bc) }} />
      {extra && <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(extra) }} />}
      <ContentPage page={page} />
    </>
  );
}
