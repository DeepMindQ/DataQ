#!/usr/bin/env python3
"""Dump each service inner page JSON fully: template, blocks (t+x), cards, l1/l2/l3, seo."""
import json, os

PAGES = "/home/z/my-project/site/src/content/pages"
files = sorted(f for f in os.listdir(PAGES) if f.endswith(".json"))
for f in files:
    with open(os.path.join(PAGES, f)) as fh:
        d = json.load(fh)
    tpl = d.get("template", "?")
    # Only dump service-ish templates in detail
    print("=" * 78)
    print(f"FILE: {f}   template={tpl}")
    print(f"  seo_title: {d.get('seo_title', '')}")
    cards = d.get("cards")
    if cards:
        print(f"  cards: {len(cards)}")
        for c in cards[:3]:
            print(f"    - {json.dumps(c)[:200]}")
    for key in ("l1", "l2", "l3"):
        v = d.get(key)
        if v:
            print(f"  {key}: {json.dumps(v)[:300]}")
    blocks = d.get("blocks", [])
    print(f"  blocks ({len(blocks)}):")
    for i, b in enumerate(blocks):
        t = b.get("t", "?")
        x = str(b.get("x", ""))[:180].replace("\n", " | ")
        extra = {k: v for k, v in b.items() if k not in ("t", "x")}
        exs = json.dumps(extra)[:150] if extra else ""
        print(f"    [{i:2d}] {t:12s} {x}")
        if exs:
            print(f"         extra: {exs}")
