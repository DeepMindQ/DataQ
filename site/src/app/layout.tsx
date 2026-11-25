import type { Metadata, Viewport } from "next";
import { Sora, Inter } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";
import SiteHeader from "@/components/site/SiteHeader";
import SiteFooter from "@/components/site/SiteFooter";
import CookieConsent from "@/components/site/CookieConsent";
import ConsentAnalytics from "@/components/site/ConsentAnalytics";
import { ScrollProgress, BackToTop } from "@/components/site/Motion";
import MotionRuntime from "@/components/site/MotionRuntime";
import { brandData, navData } from "@/lib/content";

/* Self-hosted variable fonts with preload + display swap (Wave 1, CHG-099). */
const sora = Sora({
  subsets: ["latin"],
  variable: "--font-sora",
  display: "swap",
  weight: "variable",
});
const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
  weight: "variable",
});

/* og:image must be absolute, and the Pages base path must survive — build it
   from the same root the canonicals use (Top-20 #3/#4). */
const SITE_ROOT = (
  process.env.NEXT_PUBLIC_SITE_URL || "https://deepmindq.github.io/DataQ"
).replace(/\/$/, "");

export const metadata: Metadata = {
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL || "https://deepmindq.github.io/DataQ"),
  title: {
    default: "Dataq Software — IT services, consulting & business solutions | AI, cloud, data, security, ERP",
    template: "%s",
  },
  description:
    "Dataq Software is a global IT services and consulting partner. We build, run and modernize the ERP, cloud, data, AI and security systems enterprises depend on. SOC 2 Type II, ISO 27001.",
  robots: { index: true, follow: true },
  // Icons/manifest: Next 16 does NOT prefix metadata icon/manifest hrefs with
  // the router basePath, so on GitHub Pages "/manifest.json" would resolve to
  // deepmindq.github.io/manifest.json and 404. Prefix explicitly (Top-20 #18).
  manifest: `${process.env.NEXT_PUBLIC_BASE_PATH || ""}/manifest.json`,
  icons: {
    icon: [
      { url: `${process.env.NEXT_PUBLIC_BASE_PATH || ""}/icon.svg`, type: "image/svg+xml" },
      { url: `${process.env.NEXT_PUBLIC_BASE_PATH || ""}/favicon.ico`, sizes: "48x48", type: "image/x-icon" },
    ],
    apple: [{ url: `${process.env.NEXT_PUBLIC_BASE_PATH || ""}/apple-touch-icon.png`, sizes: "180x180" }],
  },
  openGraph: {
    type: "website",
    siteName: "Dataq Software",
    images: [{ url: SITE_ROOT + "/og/home.png", width: 1200, height: 630, alt: "Dataq Software — Intelligence, engineered for outcomes." }],
  },
  twitter: {
    card: "summary_large_image",
    images: [SITE_ROOT + "/og/home.png"],
  },
};

/* Mobile browser chrome carries the brand (CHG-006 / CHG-039). */
export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#18142D" },
    { media: "(prefers-color-scheme: dark)", color: "#0F0C20" },
  ],
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  const brand = brandData();
  const { nav, footer } = navData();
  const orgJsonLd = {
    "@context": "https://schema.org",
    "@type": "Organization",
    name: brand.legalName,
    alternateName: brand.name,
    url: brand.site,
    logo: `${brand.site}/logo.svg`,
    slogan: brand.tagline,
    description: brand.positioning,
    email: brand.emails.general,
    // sameAs: add LinkedIn/X/YouTube profile URLs here when the accounts are public.
    sameAs: [],
    address: brand.offices.map((o) => ({
      "@type": "PostalAddress",
      addressLocality: o.city,
    })),
  };
  const siteJsonLd = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: brand.name,
    url: brand.site,
    potentialAction: {
      "@type": "SearchAction",
      target: `${brand.site}/search?q={search_term_string}`,
      "query-input": "required name=search_term_string",
    },
  };
  return (
    <html lang="en" className={`${sora.variable} ${inter.variable}`}>
      <body className="min-h-screen flex flex-col bg-white antialiased">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(orgJsonLd) }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(siteJsonLd) }}
        />
        {/* Paint-time flag: all scroll choreography is scoped under .js-motion,
            so content stays fully visible when JS is unavailable. */}
        <script
          dangerouslySetInnerHTML={{
            __html: "try{document.documentElement.classList.add('js-motion')}catch(e){}",
          }}
        />
        <SiteHeader nav={nav} brand={brand} />
        <MotionRuntime />
        <ScrollProgress />
        <main id="main-content" className="flex-1">{children}</main>
        <SiteFooter brand={brand} footer={footer} />
        <BackToTop />
        <CookieConsent />
        <ConsentAnalytics />
        <Toaster />
      </body>
    </html>
  );
}
