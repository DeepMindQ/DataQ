/* Per-section OpenGraph image routing (Top-20 #4).
   Absolute URLs are required for og:image, and path-absolute values would drop
   the Pages base path when resolved against metadataBase — so the site root
   (brand.site) is always prepended here. Longest prefix wins. */
import { brandData } from "@/lib/content";

const OG_BY_PREFIX: Array<[string, string]> = [
  ["/services/applied-ai-generative-ai", "/og/services-applied-ai-generative-ai.png"],
  ["/services/agentic-ai-hyperautomation", "/og/services-agentic-ai-hyperautomation.png"],
  ["/services/data-analytics-lakehouse", "/og/services-data-analytics-lakehouse.png"],
  ["/services/cybersecurity-zero-trust", "/og/services-cybersecurity-zero-trust.png"],
  ["/services/cloud-edge-platform-engineering", "/og/services-cloud-edge-platform-engineering.png"],
  ["/services/quantum-advanced-compute", "/og/services-quantum-advanced-compute.png"],
  ["/services/blockchain-digital-trust", "/og/services-blockchain-digital-trust.png"],
  ["/services/iot-digital-twin-robotics", "/og/services-iot-digital-twin-robotics.png"],
  ["/services", "/og/services.png"],
  ["/industries/banking-financial-services", "/og/industries-banking-financial-services.png"],
  ["/industries/insurance", "/og/industries-insurance.png"],
  ["/industries/healthcare-life-sciences", "/og/industries-healthcare-life-sciences.png"],
  ["/industries/manufacturing", "/og/industries-manufacturing.png"],
  ["/industries/retail-consumer-goods", "/og/industries-retail-consumer-goods.png"],
  ["/industries/telecom-media", "/og/industries-telecom-media.png"],
  ["/industries/energy-utilities", "/og/industries-energy-utilities.png"],
  ["/industries/logistics-supply-chain", "/og/industries-logistics-supply-chain.png"],
  ["/industries/public-sector", "/og/industries-public-sector.png"],
  ["/industries/education-research", "/og/industries-education-research.png"],
  ["/industries/technology-saas", "/og/industries-technology-saas.png"],
  ["/industries/agriculture-food", "/og/industries-agriculture-food.png"],
  ["/industries", "/og/industries.png"],
  ["/platforms/nexus", "/og/platforms-nexus.png"],
  ["/platforms/forge", "/og/platforms-forge.png"],
  ["/platforms/swarm", "/og/platforms-swarm.png"],
  ["/platforms/sentinel", "/og/platforms-sentinel.png"],
  ["/platforms/twinverse", "/og/platforms-twinverse.png"],
  ["/platforms/quanta", "/og/platforms-quanta.png"],
  ["/platforms/ledger", "/og/platforms-ledger.png"],
  ["/platforms/compass", "/og/platforms-compass.png"],
  ["/platforms", "/og/platforms.png"],
  ["/solutions", "/og/solutions.png"],
  ["/case-studies", "/og/case-studies.png"],
  ["/insights", "/og/insights.png"],
  ["/consulting", "/og/consulting.png"],
  ["/patented-intelligence", "/og/patented-intelligence.png"],
  ["/about-us", "/og/company.png"],
  ["/careers", "/og/company.png"],
  ["/why-dataq", "/og/company.png"],
  ["/leadership", "/og/company.png"],
  ["/global-offices", "/og/company.png"],
  ["/newsroom", "/og/company.png"],
  ["/values-culture", "/og/company.png"],
  ["/accessibility", "/og/company.png"],
  ["/privacy-policy", "/og/company.png"],
  ["/cookie-policy", "/og/company.png"],
  ["/terms-of-use", "/og/company.png"],
];

/** Site root used to build absolute og:image URLs (env wins over brand.json). */
function siteRoot(): string {
  const env = process.env.NEXT_PUBLIC_SITE_URL;
  if (env) return env.replace(/\/$/, "");
  try {
    return brandData().site.replace(/\/$/, "");
  } catch {
    // module-scope evaluation safety when fs/cwd are unavailable
    return "https://deepmindq.github.io/DataQ";
  }
}

/** Absolute og:image URL for a page URL (longest matching section prefix). */
export function ogImageFor(url: string): string {
  for (const [prefix, file] of OG_BY_PREFIX) {
    if (url.startsWith(prefix)) {
      return siteRoot() + file;
    }
  }
  return siteRoot() + "/og/home.png";
}
