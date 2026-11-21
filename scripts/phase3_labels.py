#!/usr/bin/env python3
"""Measure distinct node labels per domain; inspect index.json case rows + patents lib."""
import json, os
from collections import defaultdict

PAGES = "/home/z/my-project/site/src/content/pages"
files = sorted(f for f in os.listdir(PAGES) if f.endswith(".json") and f.startswith("services_"))
bydom = defaultdict(lambda: defaultdict(int))  # dom -> label -> count
doms = defaultdict(list)
for f in files:
    dom = f[:-5].split("_")[1]
    doms[dom].append(f)
    with open(os.path.join(PAGES, f)) as fh:
        d = json.load(fh)
    for b in d.get("blocks", []):
        if b.get("t") == "arch":
            for n in b.get("nodes", []):
                bydom[dom][n["label"].strip()] += 1

for dom in sorted(doms):
    labels = bydom[dom]
    uniq = sorted(labels)
    print(f"=== {dom}: {len(doms[dom])} files, {len(uniq)} distinct node labels ===")
    for l in uniq:
        print(f"   [{labels[l]:2d}] {l}")

# index.json case row structure
idx = json.load(open("/home/z/my-project/site/src/content/index.json"))
rows = idx if isinstance(idx, list) else idx.get("rows", idx.get("pages", []))
print("\nindex.json type:", type(idx).__name__, "len:", len(rows) if isinstance(rows, list) else "?")
if isinstance(rows, list):
    cases = [r for r in rows if r.get("template") == "case_study"][:3]
    svcrows = [r for r in rows if r.get("template") == "service_page"][:2]
    print("sample case rows:", json.dumps(cases, indent=1)[:1200])
    print("sample service rows:", json.dumps(svcrows, indent=1)[:800])
    # check fields available
    keys = set()
    for r in rows:
        keys |= set(r.keys())
    print("all row keys:", sorted(keys))
