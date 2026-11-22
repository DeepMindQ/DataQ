#!/usr/bin/env python3
"""Phase 3 recon: enumerate services pages + all 'tower' occurrences, no gitignore filtering."""
import os, re, json, sys

ROOT = "/home/z/my-project"
PAGES = os.path.join(ROOT, "site/src/content/pages")

print("=" * 70)
print("1) ALL CONTENT JSONs IN site/src/content/pages/")
print("=" * 70)
files = sorted(os.listdir(PAGES))
for f in files:
    p = os.path.join(PAGES, f)
    size = os.path.getsize(p)
    try:
        with open(p) as fh:
            d = json.load(fh)
        template = d.get("template", "?")
        title = d.get("title") or d.get("seo_title") or "?"
        print(f"  {f:40s} {size:7d}B  template={template:20s} title={str(title)[:60]}")
    except Exception as e:
        print(f"  {f:40s} {size:7d}B  ERROR: {e}")

print()
print("=" * 70)
print("2) SERVICES-RELATED JSONs (filename contains service|expertise|platform)")
print("=" * 70)
svc_files = [f for f in files if re.search(r"service|expertise|platform", f, re.I)]
for f in svc_files:
    print("  ", f)

print()
print("=" * 70)
print("3) 'tower' OCCURRENCES ACROSS site/ (case-insensitive, no filters)")
print("=" * 70)
hits = 0
for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, "site")):
    # skip build dirs
    skip = {"node_modules", ".next", ".next-export", "out", "out-gh", ".gh-deploy"}
    dirnames[:] = [d for d in dirnames if d not in skip]
    for fn in filenames:
        if not fn.endswith((".json", ".tsx", ".ts", ".md", ".mdx", ".js", ".mjs", ".css", ".html")):
            continue
        p = os.path.join(dirpath, fn)
        try:
            with open(p, encoding="utf-8", errors="ignore") as fh:
                txt = fh.read()
        except Exception:
            continue
        for m in re.finditer(r"[Tt]owers?", txt):
            hits += 1
            line_no = txt[: m.start()].count("\n") + 1
            line = txt.splitlines()[line_no - 1].strip()
            print(f"  {p.replace(ROOT + '/', '')}:{line_no}: {line[:150]}")
print(f"  TOTAL tower-hits in site/: {hits}")

print()
print("=" * 70)
print("4) 'tower' OCCURRENCES ACROSS scripts/ and root-level html/md (no filters)")
print("=" * 70)
for dirpath, dirnames, filenames in os.walk(ROOT):
    skip = {"node_modules", ".next", ".next-export", "out", "out-gh", ".gh-deploy", ".git", "site", "upload", "db"}
    dirnames[:] = [d for d in dirnames if d not in skip]
    for fn in filenames:
        if not fn.endswith((".json", ".tsx", ".ts", ".md", ".py", ".sh", ".js", ".html", ".css")):
            continue
        p = os.path.join(dirpath, fn)
        try:
            with open(p, encoding="utf-8", errors="ignore") as fh:
                txt = fh.read()
        except Exception:
            continue
        for m in re.finditer(r"[Tt]owers?", txt):
            line_no = txt[: m.start()].count("\n") + 1
            line = txt.splitlines()[line_no - 1].strip()
            print(f"  {p.replace(ROOT + '/', '')}:{line_no}: {line[:150]}")

print()
print("=" * 70)
print("5) SLUG ROUTING: how pages/*.json map to URLs")
print("=" * 70)
# read the catch-all route to understand slug mapping
route = os.path.join(ROOT, "site/src/app/[[...slug]]/page.tsx")
if os.path.exists(route):
    with open(route) as fh:
        print(fh.read()[:3000])
else:
    print("  route file not found at", route)
