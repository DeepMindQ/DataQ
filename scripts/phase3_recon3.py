#!/usr/bin/env python3
"""Enumerate services-related pages: hub + inner pages, template, url, block count, headings."""
import json, os

PAGES = "/home/z/my-project/site/src/content/pages"
files = sorted(f for f in os.listdir(PAGES) if f.endswith(".json"))
svc = [f for f in files if f == "services.json" or f.startswith("services_")]
print(f"Total services-related files: {len(svc)}")
for f in svc:
    with open(os.path.join(PAGES, f)) as fh:
        d = json.load(fh)
    blocks = d.get("blocks", [])
    heads = [b.get("x", "") for b in blocks if b.get("t") in ("h2", "h3")]
    print(f"\n### {f}")
    print(f"  url={d.get('url')} template={d.get('template')} blocks={len(blocks)} cards={len(d.get('cards', []))}")
    print(f"  h2/h3: ")
    for h in heads:
        print(f"    - {h}")
    extras = [k for k in d.keys() if k not in ("id", "title", "url", "template", "breadcrumb", "seo_title", "meta_description", "blocks", "cards")]
    if extras:
        print(f"  extra keys: {extras}")
