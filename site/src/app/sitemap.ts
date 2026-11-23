import type { MetadataRoute } from "next";
import fs from "fs";
import path from "path";
import { pageIndex } from "@/lib/content";

export const dynamic = "force-static";

const SITE = process.env.NEXT_PUBLIC_SITE_URL || "https://deepmindq.github.io/DataQ";

/* Real last-modified dates from git (scripts/gen_lastmod.py runs before the
   build). Pages without a git date simply omit lastmod — no build-timestamp
   noise for crawlers (Top-20 #7). */
type LastmodMap = Record<string, string>;
let LASTMOD: LastmodMap = {};
try {
  LASTMOD = JSON.parse(
    fs.readFileSync(path.join(process.cwd(), "src", "content", "lastmod.json"), "utf8")
  ) as LastmodMap;
} catch {
  /* no git data in this environment — lastmod omitted */
}

function lastModified(fileKey: string | undefined): Date | undefined {
  if (!fileKey) return undefined;
  const raw = LASTMOD[fileKey];
  if (!raw) return undefined;
  const d = new Date(raw);
  return isNaN(d.getTime()) ? undefined : d;
}

export default function sitemap(): MetadataRoute.Sitemap {
  const rows = pageIndex();
  const extra = [
    { url: "/patented-intelligence/", priority: 0.8, key: "src/app/patented-intelligence/page.tsx" },
  ];
  return [
    ...rows.map((r) => {
      const priority =
        r.url === "/" ? 1.0 : r.template.endsWith("_hub") ? 0.8 : r.l4 ? 0.5 : 0.6;
      return {
        url: SITE + r.url,
        ...(lastModified(`src/content/pages/${r.file}.json`)
          ? { lastModified: lastModified(`src/content/pages/${r.file}.json`)! }
          : {}),
        changeFrequency: "monthly" as const,
        priority,
      };
    }),
    ...extra.map((e) => ({
      url: SITE + e.url,
      ...(lastModified(e.key) ? { lastModified: lastModified(e.key)! } : {}),
      changeFrequency: "monthly" as const,
      priority: e.priority,
    })),
  ];
}
