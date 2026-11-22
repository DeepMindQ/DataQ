#!/usr/bin/env python3
"""Inspect routing, components, and sample service page structures."""
import os, re, json

ROOT = "/home/z/my-project"

def show(path, maxlines=None):
    p = os.path.join(ROOT, path)
    print("=" * 70)
    print("FILE:", path, f"({os.path.getsize(p)}B)" if os.path.exists(p) else "MISSING")
    print("=" * 70)
    if not os.path.exists(p):
        return
    with open(p, encoding="utf-8", errors="ignore") as fh:
        txt = fh.read()
    lines = txt.splitlines()
    if maxlines:
        lines = lines[:maxlines]
    for i, ln in enumerate(lines, 1):
        print(f"{i:5d}  {ln[:200]}")

# 1) Is dqs_proposal.js referenced by the build?
print("\n### dqs_proposal.js references:")
for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, "site/src")):
    for fn in filenames:
        p = os.path.join(dirpath, fn)
        with open(p, encoding="utf-8", errors="ignore") as fh:
            if "dqs_proposal" in fh.read():
                print("  referenced by:", p)

# 2) services.json hub structure (keys, first blocks)
p = os.path.join(ROOT, "site/src/content/pages/services.json")
with open(p) as fh:
    d = json.load(fh)
print("\n### services.json top-level keys:", list(d.keys()))
print("    template:", d.get("template"))
blocks = d.get("blocks", [])
print("    blocks count:", len(blocks))
for i, b in enumerate(blocks[:6]):
    if isinstance(b, dict):
        print(f"    block[{i}] t={b.get('t')} keys={sorted(b.keys())}")
        x = str(b.get("x", ""))[:120]
        print(f"            x: {x}")

# 3) One service page JSON: keys and block types
p = os.path.join(ROOT, "site/src/content/pages/services_data-analytics-lakehouse_realtime-streaming-decisioning.json")
with open(p) as fh:
    d = json.load(fh)
print("\n### service_page JSON top-level keys:", list(d.keys()))
blocks = d.get("blocks", [])
print("    blocks count:", len(blocks))
typecount = {}
for b in blocks:
    t = b.get("t") if isinstance(b, dict) else "?"
    typecount[t] = typecount.get(t, 0) + 1
print("    block types:", typecount)
for i, b in enumerate(blocks):
    if isinstance(b, dict):
        keys = sorted(b.keys())
        x = str(b.get("x", ""))[:100]
        print(f"    [{i}] t={b.get('t'):22s} keys={keys}")
        if x:
            print(f"         x: {x}")

# 4) Sample the "arch"-ish blocks in a few service pages to see diagram data shape
print("\n### Looking for diagram-shaped blocks in service pages:")
for fn in ["services_data-analytics-lakehouse_realtime-streaming-decisioning.json",
           "services_cybersecurity-zero-trust_zero-trust-architecture.json",
           "services_agentic-ai-hyperautomation_agentic-process-automation.json"]:
    p = os.path.join(ROOT, "site/src/content/pages", fn)
    with open(p) as fh:
        d = json.load(fh)
    for key in d.keys():
        if key in ("blocks", "cards", "l1", "l2", "l3", "seo_title", "template", "title", "meta_description", "slug"):
            continue
        print(f"    {fn}: extra key '{key}' = {str(d[key])[:200]}")
    for i, b in enumerate(d.get("blocks", [])):
        t = b.get("t", "")
        if any(k in t for k in ("arch", "flow", "diagram", "stack", "layer", "visual", "chart", "dash")):
            print(f"    {fn} block[{i}] t={t} keys={sorted(b.keys())}")
            print(f"         content: {json.dumps(b)[:400]}")
