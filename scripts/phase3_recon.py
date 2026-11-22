#!/usr/bin/env python3
"""Phase 3 recon: enumerate services pages, slugs, tower references, component inventory."""
import json, os, re, sys

ROOT = "/home/z/my-project"
PAGES = os.path.join(ROOT, "site/src/content/pages")
COMP = os.path.join(ROOT, "site/src/components/site")
SRC = os.path.join(ROOT, "site/src")

# 1. List all content JSON files
print("=" * 70)
print("1. ALL CONTENT JSON FILES (name | template | #blocks)")
print("=" * 70)
files = sorted(f for f in os.listdir(PAGES) if f.endswith(".json"))
for f in files:
    try:
        with open(os.path.join(PAGES, f)) as fh:
            d = json.load(fh)
        tpl = d.get("template", "?")
        nb = len(d.get("blocks", []))
        title = ""
        for b in d.get("blocks", []):
            if b.get("t") == "h1" or b.get("t") == "title":
                title = str(b.get("x", ""))[:60]
                break
        print(f"{f:40s} tpl={tpl:18s} blocks={nb:3d}  {title}")
    except Exception as e:
        print(f"{f:40s} ERROR {e}")

# 2. Find the page registry / slug mapping
print()
print("=" * 70)
print("2. SLUG REGISTRY (search for slug mapping in src)")
print("=" * 70)
for dirpath, dirnames, filenames in os.walk(SRC):
    if "node_modules" in dirpath or ".next" in dirpath:
        continue
    for fn in filenames:
        if fn.endswith((".ts", ".tsx")):
            p = os.path.join(dirpath, fn)
            with open(p) as fh:
                txt = fh.read()
            if "content/pages" in txt or "slugTo" in txt or "pageSlug" in txt:
                print("---", p.replace(ROOT + "/", ""))
                for i, line in enumerate(txt.split("\n")[:40], 1):
                    print(f"   {i:3d}| {line}")

# 3. Tower references across the whole repo (no gitignore filtering)
print()
print("=" * 70)
print("3. ALL 'tower' OCCURRENCES (case-insensitive, whole site tree)")
print("=" * 70)
hits = 0
for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, "site")):
    dirnames[:] = [d for d in dirnames if d not in ("node_modules", ".next", ".next-export", "out", "out-gh", ".gh-deploy")]
    for fn in filenames:
        if fn.endswith((".json", ".ts", ".tsx", ".js", ".md", ".mdx", ".css")):
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding="utf-8", errors="replace") as fh:
                    txt = fh.read()
            except Exception:
                continue
            for i, line in enumerate(txt.split("\n"), 1):
                if re.search(r"tower", line, re.I):
                    hits += 1
                    print(f"{p.replace(ROOT + '/', '')}:{i}: {line.strip()[:140]}")
print(f"TOTAL tower hits: {hits}")

# 4. Components inventory with sizes
print()
print("=" * 70)
print("4. SITE COMPONENTS (lines)")
print("=" * 70)
for fn in sorted(os.listdir(COMP)):
    p = os.path.join(COMP, fn)
    with open(p) as fh:
        n = sum(1 for _ in fh)
    print(f"{fn:35s} {n:5d} lines")

# 5. services.json full block dump
print()
print("=" * 70)
print("5. services.json STRUCTURE")
print("=" * 70)
with open(os.path.join(PAGES, "services.json")) as fh:
    d = json.load(fh)
print(json.dumps(d, indent=1)[:3000])
