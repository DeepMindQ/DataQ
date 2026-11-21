#!/usr/bin/env python3
"""修复 nav.json：去重主菜单与 mega 分组、校验全部 URL 是否真实存在。"""
import json, re, sys

NAV = 'site/src/content/nav.json'
IDX = 'site/src/content/index.json'

idx = json.load(open(IDX, encoding='utf-8'))
known = {r['url'] for r in idx}
nav = json.load(open(NAV, encoding='utf-8'))

def dedupe_items(items, what):
    seen, out, removed = set(), [], []
    for it in items:
        key = it['label']
        if key in seen:
            removed.append(f'{what}: {key!r}')
            continue
        seen.add(key)
        out.append(it)
    return out, removed

removed = []
prim, rm = dedupe_items(nav['nav']['primary'], 'primary')
nav['nav']['primary'] = prim
removed += rm

for item in nav['nav']['primary']:
    if item.get('mega'):
        mega, rm = dedupe_items(item['mega'], f"{item['label']}/mega")
        item['mega'] = mega
        removed += rm
        for g in item['mega']:
            kids, rm = dedupe_items(g.get('children') or [], f"{g['label']}/children")
            g['children'] = kids
            removed += rm

for col in nav['footer']:
    links, rm = dedupe_items(col['links'], f"footer/{col['title']}")
    col['links'] = links
    removed += rm

# ── 校验链接 ──────────────────────────────────────────────
dead = []
def check(url, where):
    if url.startswith(('http', 'mailto', '#')):
        return
    if url not in known:
        dead.append(f'{where} -> {url}')

check(nav['nav']['cta']['url'], 'cta')
for item in nav['nav']['primary']:
    check(item['url'], f"primary/{item['label']}")
    for g in item.get('mega') or []:
        check(g['url'], f"primary/{item['label']}/{g['label']}")
        for ch in g.get('children') or []:
            check(ch['url'], f"primary/{item['label']}/{g['label']}/{ch['label']}")
for col in nav['footer']:
    for l in col['links']:
        check(l['url'], f"footer/{col['title']}/{l['label']}")
        for ch in l.get('children') or []:
            check(ch['url'], f"footer/{col['title']}/{l['label']}/{ch['label']}")

json.dump(nav, open(NAV, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

print('removed duplicates:', len(removed))
for r in removed: print('  -', r)
print('dead links:', len(dead))
for d in dead: print('  !', d)
print('primary now:', [i['label'] for i in nav['nav']['primary']])
