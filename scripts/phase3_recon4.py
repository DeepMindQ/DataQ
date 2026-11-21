#!/usr/bin/env python3
"""Survey block types used across services pages; count pages per domain; dump a full sample page."""
import json, os
from collections import Counter, defaultdict

PAGES = "/home/z/my-project/site/src/content/pages"
files = sorted(f for f in os.listdir(PAGES) if f.endswith(".json") and (f == "services.json" or f.startswith("services_")))

hubs = [f for f in files if not f.count("_") > 0 or f.count("_") == 0]
domain_files = defaultdict(list)
hubfiles = []
innerfiles = []
for f in files:
    if f == "services.json":
        hubfiles.append(f)
        continue
    base = f[:-5]
    parts = base.split("_")
    if len(parts) == 2:
        hubfiles.append(f)
        domain_files[parts[1]].append(f)
    else:
        innerfiles.append(f)
        domain_files[parts[1]].append(f)

print("Hub pages:", hubfiles)
print()
for dom, fl in sorted(domain_files.items()):
    print(f"{dom}: {len(fl)} pages")

tcount = Counter()
for f in files:
    with open(os.path.join(PAGES, f)) as fh:
        d = json.load(fh)
    for b in d.get("blocks", []):
        tcount[b.get("t", "?")] += 1
print()
print("Block types across all services files:")
for t, c in tcount.most_common():
    print(f"  {t}: {c}")

# Full dump of one service page JSON (first inner page) to inspect schema
target = "services_agentic-ai-hyperautomation_agentic-process-automation.json"
with open(os.path.join(PAGES, target)) as fh:
    d = json.load(fh)
print("\n" + "=" * 78)
print(f"FULL DUMP of {target} (length {os.path.getsize(os.path.join(PAGES, target))} bytes)")
print(json.dumps(d, indent=1)[:12000])
