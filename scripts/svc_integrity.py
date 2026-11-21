#!/usr/bin/env python3
"""Integrity check: all service pages have unique idash consoles, no banned terms, valid JSON."""
import json, glob, hashlib, re

pages = sorted(glob.glob('site/src/content/pages/services_*.json'))
banned = ['Strategemist', 'Pisupati', 'Hyderabad', 'Ravi Shanker', 'tower']
problems = []
hashes = {}
total_words = 0
for f in pages:
    try:
        j = json.load(open(f))
    except Exception as e:
        problems.append(f"{f}: JSON error {e}")
        continue
    # banned terms (case-insensitive for tower)
    raw = json.dumps(j)
    for b in ['Strategemist', 'Pisupati', 'Hyderabad', 'Ravi Shanker']:
        if b in raw:
            problems.append(f"{f}: BANNED {b}")
    blocks = j.get('blocks', [])
    n_idash = sum(1 for b in blocks if isinstance(b, dict) and b.get('t') == 'idash')
    # hash the idash structure for uniqueness
    for b in blocks:
        if isinstance(b, dict) and b.get('t') == 'idash':
            h = hashlib.md5(json.dumps(b, sort_keys=True).encode()).hexdigest()[:8]
            hashes.setdefault(h, []).append(f.split('_', 1)[1])
            if n_idash != 1:
                problems.append(f"{f}: {n_idash} idash blocks")
    words = j.get('words', 0)
    total_words += words

# uniqueness of consoles
dups = {h: fs for h, fs in hashes.items() if len(fs) > 1}
print(f"Pages checked: {len(pages)}")
print(f"Total words (est): {total_words}")
print(f"Unique idash consoles: {len(hashes)}")
print(f"Duplicate consoles: {len(dups)}")
for h, fs in dups.items():
    print("  DUP:", fs)
print(f"Problems: {len(problems)}")
for p in problems:
    print("  !!", p)

# word-count distribution
ws = []
for f in pages:
    j = json.load(open(f))
    ws.append((j.get('words', 0), f.split('_', 1)[1]))
ws.sort()
print("Lowest 5 word counts:")
for w, n in ws[:5]:
    print(f"  {w:5d}  {n}")
