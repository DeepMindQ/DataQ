#!/usr/bin/env python3
"""Wave 4 inventory — per-subpage dump of every block the wave will edit.
Output: scripts/wave4_inventory.json  {page_id: {hero, chip_ctx, blocks:[...], tables, charts, idash, arch, cta}}"""
import json
from pathlib import Path

PAGES = Path('/home/z/my-project/site/src/content/pages')
HUBS = {'agentic-ai-hyperautomation','applied-ai-generative-ai','blockchain-digital-trust',
        'cloud-edge-platform-engineering','cybersecurity-zero-trust','data-analytics-lakehouse',
        'iot-digital-twin-robotics','quantum-advanced-compute'}
files = sorted(PAGES.glob('services_*_*.json'))
subs = [f for f in files if len(f.stem.split('_')) >= 3]

inv = {}
for f in subs:
    d = json.loads(f.read_text())
    blocks = d['blocks']
    page = {
        'title': d['title'],
        'domain': f.stem.split('_')[1],
        'hero': d.get('l1', '')[:200],
        'hero_l2': d.get('l2', '')[:160],
        'l3': d.get('l3', '')[:120],
        'blocks': [],
    }
    for i, b in enumerate(blocks):
        t = b['t']
        e = {'i': i, 't': t, 'x': b.get('x', '')[:170]}
        if t == 'h2':
            e['sub'] = (b.get('sub') or '')[:130]
            # peek at next paragraph for context
            for j in range(i + 1, min(i + 3, len(blocks))):
                if blocks[j]['t'] == 'p':
                    e['next_p'] = blocks[j]['x'][:220]
                    break
        elif t == 'table':
            e['caption'] = (b.get('caption') or '')[:110]
            e['rows'] = len(b.get('rows', []))
            hdr = b.get('header') or (b.get('rows') or [[]])[0]
            e['header'] = [str(c)[:30] for c in (hdr or [])][:5]
            # first data row for flavor
            rr = b.get('rows', [])
            if rr: e['row0'] = [str(c)[:45] for c in rr[0]][:4]
        elif t == 'chart':
            e['variant'] = b.get('variant')
            e['caption'] = (b.get('caption') or '')[:110]
            e['series_keys'] = [s.get('label', '?') if isinstance(s, dict) else str(s)[:20] for s in (b.get('series', []) if isinstance(b.get('series'), list) else [])][:4]
        elif t == 'idash':
            e['badge'] = (b.get('badge') or '')[:60]
            e['note'] = (b.get('note') or '')[:120]
        elif t == 'arch':
            e['title'] = (b.get('title') or '')[:110]
            e['badge_list'] = [f"{bd.get('label','?')}={bd.get('value','?')}" for bd in (b.get('badges') or [])][:6]
            e['lanes'] = [ln.get('name', '?') if isinstance(ln, dict) else str(ln)[:25] for ln in (b.get('lanes') or [])][:8]
        elif t == 'cta':
            e['x'] = b.get('x', '')[:140]
        page['blocks'].append(e)
    inv[f.stem] = page

out = Path('/home/z/my-project/scripts/wave4_inventory.json')
out.write_text(json.dumps(inv, ensure_ascii=False, indent=1))
print('pages:', len(inv), '-> written', out, out.stat().st_size, 'bytes')

# per-domain file sizes for reading slices
from collections import Counter
c = Counter(v['domain'] for v in inv.values())
for k, n in sorted(c.items()):
    print(f'  {k}: {n} pages')
