#!/usr/bin/env python3
"""Count content pages per cluster (l1/l2) to ground the backlog rows."""
import os, json, collections

PAGES = "/home/z/my-project/site/src/content/pages"
counts = collections.Counter()
templates = collections.Counter()
totals = {"pages": 0, "blocks": 0}
link_density = []

for dirpath, dirnames, filenames in os.walk(PAGES):
    for fn in filenames:
        if not fn.endswith(".json"):
            continue
        totals["pages"] += 1
        path = os.path.join(dirpath, fn)
        d = json.load(open(path, encoding="utf-8"))
        templates[d.get("template", "?")] += 1
        l1 = d.get("l1", "")
        counts[l1] += 1
        totals["blocks"] += len(d.get("blocks", []))
        rel = d.get("related", [])
        link_density.append(len(rel) if isinstance(rel, list) else 0)

print("total pages:", totals["pages"])
print("total blocks:", totals["blocks"], " avg/page:", round(totals["blocks"] / totals["pages"], 1))
print("\nby l1:")
for k, v in counts.most_common(30):
    print(f"  {k or '(none)'}: {v}")
print("\nby template:")
for k, v in templates.most_common(20):
    print(f"  {k}: {v}")
rel = [x for x in link_density if x]
if rel:
    print("\nrelated links: avg", round(sum(rel) / len(rel), 2), " zero-related pages:", link_density.count(0))
