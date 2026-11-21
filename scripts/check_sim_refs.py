#!/usr/bin/env python3
"""Scan all idash sim widgets: formulas must only reference params that exist."""
import json, glob, re, sys

bad = 0
for f in sorted(glob.glob('site/src/content/pages/services_*.json')):
    j = json.load(open(f))
    for b in j.get('blocks', []):
        if not isinstance(b, dict) or b.get('t') != 'idash':
            continue
        for t in b.get('tabs', []):
            for w in t.get('widgets', []):
                if w.get('kind') == 'sim':
                    n = len(w.get('params', []))
                    ok_refs = {f'p{i}' for i in range(n)}
                    for o in w.get('outputs', []):
                        refs = set(re.findall(r'p(\d+)', o['formula']))
                        for r in refs:
                            if int(r) >= n:
                                print(f"{f}: output '{o['name']}' refs p{r} but only {n} params")
                                bad += 1
                    c = w.get('curve')
                    if c:
                        if c['param'] >= n:
                            print(f"{f}: curve param idx {c['param']} >= {n} params")
                            bad += 1
                        if c['output'] >= len(w.get('outputs', [])):
                            print(f"{f}: curve output idx {c['output']} >= {len(w.get('outputs', []))} outputs")
                            bad += 1
print("bad refs:", bad)
sys.exit(1 if bad else 0)
