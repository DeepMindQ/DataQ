#!/usr/bin/env python3
"""Measure arch/idash/explorer richness across services pages."""
import json, os
from collections import Counter

PAGES = "/home/z/my-project/site/src/content/pages"
files = sorted(f for f in os.listdir(PAGES) if f.endswith(".json") and (f == "services.json" or f.startswith("services_")))

arch_stats = Counter()
arch_missing = []
explorer_issues = []
edge_label_count = 0
node_count = 0
sub_count = 0
edge_count = 0

for f in files:
    with open(os.path.join(PAGES, f)) as fh:
        d = json.load(fh)
    for b in d.get("blocks", []):
        if b.get("t") == "arch":
            nodes = b.get("nodes", [])
            edges = b.get("edges", [])
            node_count += len(nodes)
            sub_count += sum(1 for n in nodes if n.get("sub"))
            edge_count += len(edges)
            edge_label_count += sum(1 for e in edges if e.get("label"))
            arch_stats["arch"] += 1
            if not edges:
                arch_missing.append((f, "NO EDGES"))
            elif len(edges) < 6:
                arch_missing.append((f, f"only {len(edges)} edges"))
        if b.get("t") == "explorer":
            inds = b.get("industries", [])
            hooks = [i.get("hook", "") for i in inds]
            plays = [tuple(i.get("plays", [])) for i in inds]
            kpis = [tuple((k.get("label"), k.get("value")) for k in i.get("kpis", [])) for i in inds]
            frag = sum(1 for h in hooks if len(h) < 60 or h.strip().startswith(":") or h.strip().startswith(","))
            dup_plays = len(set(plays)) == 1 if plays else False
            dup_kpis = len(set(kpis)) == 1 if kpis else False
            explorer_issues.append({
                "file": f,
                "n_ind": len(inds),
                "frag_hooks": frag,
                "dup_plays": dup_plays,
                "dup_kpis": dup_kpis,
            })

print(f"ARCH blocks: {arch_stats['arch']}")
print(f"  nodes total: {node_count}, with sub: {sub_count}")
print(f"  edges total: {edge_count}, with labels: {edge_label_count}")
print(f"  pages with weak edges: {len(arch_missing)}")
for f, msg in arch_missing[:20]:
    print(f"    {f}: {msg}")

print()
print(f"EXPLORER blocks: {len(explorer_issues)}")
flagged = [e for e in explorer_issues if e["frag_hooks"] or e["dup_plays"] or e["dup_kpis"]]
print(f"  flagged (frag hooks / dup plays / dup kpis): {len(flagged)}")
for e in explorer_issues:
    if e["frag_hooks"] or e["dup_plays"] or e["dup_kpis"]:
        print(f"    {e['file']}: inds={e['n_ind']} fragHooks={e['frag_hooks']} dupPlays={e['dup_plays']} dupKpis={e['dup_kpis']}")

# Check the page-level 'related' key usage
print()
rel_missing = []
for f in files:
    with open(os.path.join(PAGES, f)) as fh:
        d = json.load(fh)
    rel = d.get("related")
    n = len(rel) if rel else 0
    if f != "services.json" and n < 3:
        rel_missing.append((f, n))
print(f"Pages with <3 related links: {len(rel_missing)}")
for f, n in rel_missing[:20]:
    print(f"    {f}: {n}")

# l1/l2/l3 chips sample
print()
for f in files[:3]:
    with open(os.path.join(PAGES, f)) as fh:
        d = json.load(fh)
    print(f, "l1:", d.get("l1"), "| l2:", d.get("l2"), "| l3:", d.get("l3"), "| l4:", d.get("l4"))
