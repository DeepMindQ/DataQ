#!/usr/bin/env python3
"""Audit: which pages are services + what template/blocks/visuals they use."""
import json, os, re, sys

D = 'site/src/content/pages'
files = sorted(os.listdir(D))

svc = []
for f in files:
    try:
        j = json.load(open(os.path.join(D, f)))
    except Exception:
        continue
    tmpl = j.get('template', '')
    slug = j.get('slug', '')
    if 'service' in tmpl or 'tower' in tmpl or f.startswith('services') or f.startswith('svc'):
        svc.append((f, j))

print(f"== {len(svc)} service-related content files ==")
for f, j in svc:
    tmpl = j.get('template', '')
    title = j.get('title', '')
    words = sum(len(str(b.get('x', '')).split()) for b in j.get('blocks', []) if isinstance(b, dict))
    nblocks = len(j.get('blocks', []))
    print(f"{f:44s} tmpl={tmpl:20s} blk={nblocks:3d} w={words:5d}  {title}")

# summarize which templates exist
print("\n== template counts ==")
tc = {}
for f in files:
    try:
        j = json.load(open(os.path.join(D, f)))
    except Exception:
        continue
    tc[j.get('template', '?')] = tc.get(j.get('template', '?'), 0) + 1
for k, v in sorted(tc.items(), key=lambda x: -x[1]):
    print(f"  {k:24s} {v}")
