#!/usr/bin/env python3
"""Compact per-page reference for pack authoring: explorer fields, hot nodes, h2s."""
import json, os

PAGES = "/home/z/my-project/site/src/content/pages"
files = sorted(f for f in os.listdir(PAGES) if f.endswith(".json") and f.startswith("services_"))
out = []
for f in files:
    with open(os.path.join(PAGES, f)) as fh:
        d = json.load(fh)
    print("=" * 100)
    print(f"FILE {f}")
    print(f"  title: {d.get('title')}  url: {d.get('url')}")
    for b in d.get("blocks", []):
        if b.get("t") == "hero":
            print(f"  HERO: {b.get('x', '')[:170]}")
        elif b.get("t") == "h2":
            print(f"  H2: {b.get('x', '')}")
        elif b.get("t") == "explorer":
            print(f"  EXPLORER intro: {b.get('intro', '')[:180]}")
            print(f"  EXPLORER service: {b.get('service', '')}")
            print(f"  EXPLORER practiceNote: {b.get('practiceNote', '')[:200]}")
            inds = b.get("industries", [])
            for ind in inds:
                print(f"    IND {ind['slug']:<32} flag={ind.get('flagship')} hook={ind.get('hook', '')[:110]}")
                print(f"      plays: {ind.get('plays')}")
                print(f"      kpis: {ind.get('kpis')}")
        elif b.get("t") == "arch":
            hot = [n["label"] for n in b.get("nodes", []) if n.get("hot")]
            allnodes = [n["label"] for n in b.get("nodes", [])]
            print(f"  ARCH title: {b.get('title', '')[:120]}")
            print(f"  ARCH lanes: {b.get('lanes')}")
            print(f"  ARCH hot: {hot}")
            print(f"  ARCH nodes: {allnodes}")
            print(f"  ARCH note: {str(b.get('note', ''))[:150]}")
