#!/usr/bin/env python3
"""Homepage copy pass 2: plain-English stat labels + clean SEO strings.
Edits src/content/pages/home.json (extras.stats, seo_title, meta_description)
and the "/" row in src/content/index.json. Idempotent."""

import json, pathlib

SITE = pathlib.Path("/home/z/my-project/site")

# value -> new label (matched on value, applied in order)
STAT_LABELS = {
    "1.9M": "decisions a day under management (illustrative reference program)",
    "148 ms": "decision latency p95, within SLO (reference program)",
    "100%": "of releases pass the evidence check before they ship",
    "350+": "enterprise engagements delivered",
    "40+": "countries served from 4 global delivery centers",
    "8": "proprietary platforms in production with clients",
    "2,400+": "engineers, consultants and domain specialists",
}

SEO_TITLE = "Dataq Software | IT Services, Consulting & Business Solutions"
META_DESC = (
    "Dataq Software is a global IT services and consulting partner. We build, run and "
    "modernize the ERP, cloud, data, AI and security systems enterprises depend on, in 40+ "
    "countries, on patented delivery platforms. SOC 2 Type II, ISO 27001."
)

def main():
    home_p = SITE / "src/content/pages/home.json"
    home = json.loads(home_p.read_text())
    stats = home["extras"]["stats"]
    seen8 = False
    changed = 0
    for s in stats:
        v = s["value"]
        if v == "8":
            # two entries with value 8: platforms first, method families second
            if not seen8:
                new = "proprietary platforms in production with clients"
                seen8 = True
            else:
                new = "patented method families from our research programme"
        elif v in STAT_LABELS:
            new = STAT_LABELS[v]
        else:
            continue
        if s["label"] != new:
            s["label"] = new
            changed += 1
    home["seo_title"] = SEO_TITLE
    home["meta_description"] = META_DESC
    home_p.write_text(json.dumps(home, indent=1, ensure_ascii=False) + "\n")
    print(f"home.json: {changed} stat labels updated, seo/meta rewritten")

    idx_p = SITE / "src/content/index.json"
    rows = json.loads(idx_p.read_text())
    n = 0
    for r in rows:
        if r.get("url") == "/":
            if r.get("seoTitle") != SEO_TITLE:
                r["seoTitle"] = SEO_TITLE
                n += 1
            if r.get("metaDescription") != META_DESC:
                r["metaDescription"] = META_DESC
                n += 1
    idx_p.write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    print(f"index.json: {n} home-row fields updated")

if __name__ == "__main__":
    main()
