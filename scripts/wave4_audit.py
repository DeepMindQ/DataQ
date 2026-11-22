#!/usr/bin/env python3
"""Wave 4 audit — inventory every formulaic family / gap across the 54 service subpages.
Mirrors the Wave 3 register method: find what repeats, what is missing, what is wrong."""
import json, collections, re
from pathlib import Path

PAGES = Path('/home/z/my-project/site/src/content/pages')
HUBS = {'agentic-ai-hyperautomation','applied-ai-generative-ai','blockchain-digital-trust',
        'cloud-edge-platform-engineering','cybersecurity-zero-trust','data-analytics-lakehouse',
        'iot-digital-twin-robotics','quantum-advanced-compute'}
files = sorted(PAGES.glob('services_*_*.json'))
subs = [f for f in files if f.stem.split('_', 1)[1].split('_', 1)[0] in HUBS and f.stem.count('_') >= 2]
# hub files are services_<domain>.json (single _), subpages services_<domain>_<sub>.json
subs = [f for f in files if len(f.stem.split('_')) >= 3]
print('SUBPAGES:', len(subs))

data = {}
for f in subs:
    data[f.stem] = json.loads(f.read_text())

def fam(title):
    """Reduce an h2 to its formulaic family signature."""
    t = re.sub(r'^(the |a |an )', '', title.lower())
    t = re.sub(r'[^a-z ]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

# 1. hero_chip presence
nochip = [k for k, d in data.items() if not d.get('hero_chip')]
print('\n[1] hero_chip MISSING on', len(nochip), '/', len(subs), 'subpages')

# 2. h2 families repeated across pages (exact normalized match on 3+ pages)
famc = collections.defaultdict(list)
for k, d in data.items():
    for b in d['blocks']:
        if b['t'] == 'h2':
            famc[fam(b['x'])].append((k, b['x']))
print('\n[2] h2 titles shared verbatim-across-pages (normalized, >=3 pages):')
for fam_, occ in sorted(famc.items(), key=lambda kv: -len(kv[1])):
    if len(occ) >= 3:
        pages = set(k.split('_')[1] for k, _ in occ)
        print(f'  {len(occ):2d}x across {len(pages)} domains: "{occ[0][1][:80]}"')

# 3. h2 families with formulaic STEMS (prefix match >=6 pages)
stems = ['reference architecture', 'release gates', 'how ', 'engagement', 'console',
         'what the engineering teams inherit', 'the deliverable', 'failure modes',
         'defaults', 'week by week', 'integration surface']
print('\n[3] h2 formulaic STEMS (>=6 occurrences):')
for stem in stems:
    hits = []
    for k, d in data.items():
        for b in d['blocks']:
            if b['t'] == 'h2' and stem in b['x'].lower():
                hits.append((k, b['x']))
    if len(hits) >= 6:
        print(f'  {len(hits):2d}x "{stem}": e.g. "{hits[0][1][:70]}" | "{hits[1][1][:70]}"')

# 4. chart captions
cc = collections.Counter()
empty_cap = 0
variants = collections.Counter()
for k, d in data.items():
    for b in d['blocks']:
        if b['t'] == 'chart':
            variants[b.get('variant', '?')] += 1
            cap = (b.get('caption') or '').strip()
            if not cap: empty_cap += 1
            else: cc[cap] += 1
print('\n[4] charts: variants', dict(variants), '| EMPTY captions:', empty_cap)
for cap, n in cc.most_common(6):
    print(f'   cap {n:2d}x: "{cap[:80]}"')

# 5. idash badges + notes
ib = collections.Counter(); inn = collections.Counter()
for k, d in data.items():
    for b in d['blocks']:
        if b['t'] == 'idash':
            ib[(b.get('badge') or '').strip()] += 1
            inn[(b.get('note') or '').strip()[:60]] += 1
print('\n[5] idash badges:')
for b, n in ib.most_common(12):
    print(f'   {n:2d}x "{b[:70]}"')

# 6. table captions
tc = collections.Counter()
for k, d in data.items():
    for b in d['blocks']:
        if b['t'] == 'table':
            cap = (b.get('caption') or '').strip()
            tc[re.sub(re.escape(d['title']), 'TITLE', cap)] += 1
print('\n[6] table caption TEMPLATES (title-normalized):')
for cap, n in tc.most_common(10):
    if n >= 2:
        print(f'   {n:2d}x "{cap[:85]}"')

# 7. meta_description duplicates
mc = collections.Counter()
for k, d in data.items():
    m = (d.get('meta_description') or '').strip()
    m = re.sub(re.escape(d['title']), 'TITLE', m)
    mc[m] += 1
print('\n[7] meta_description templates:')
for m, n in mc.most_common(8):
    print(f'   {n:2d}x "{m[:85]}"')

# 8. explorer practiceNote
en = collections.Counter()
for k, d in data.items():
    for b in d['blocks']:
        if b['t'] == 'explorer':
            en[(b.get('practiceNote') or 'NONE')[:70]] += 1
print('\n[8] explorer practiceNotes:')
for n_, c in en.most_common(10):
    print(f'   {c:2d}x "{n_}"')

# 9. FAQ presence (question-shaped bullets before cta)
nofaq = []
for k, d in data.items():
    blocks = d['blocks']
    ci = next((i for i, b in enumerate(blocks) if b['t'] == 'cta'), None)
    qbullets = 0
    for b in blocks[:ci if ci is not None else len(blocks)]:
        if b['t'] == 'bullets':
            for it in b.get('items', []):
                q = it[0] if isinstance(it, list) else it
                if isinstance(q, str) and q.rstrip().endswith('?'):
                    qbullets += 1
    if qbullets == 0:
        nofaq.append(k)
print('\n[9] subpages with NO question-shaped FAQ bullets:', len(nofaq), '/', len(subs))

# 10. arch titles/badges
at = collections.Counter()
for k, d in data.items():
    for b in d['blocks']:
        if b['t'] == 'arch':
            at[(b.get('title') or 'NONE')[:80]] += 1
print('\n[10] arch titles:')
for t, n in at.most_common(8):
    print(f'   {n:2d}x "{t}"')

# 11. diagram blocks (flow schematic)
diag = collections.Counter()
for k, d in data.items():
    for b in d['blocks']:
        if b['t'] == 'diagram':
            diag[(b.get('caption') or b.get('title') or 'UNTITLED')[:60]] += 1
print('\n[11] diagram block captions:')
for t, n in diag.most_common(8):
    print(f'   {n:2d}x "{t}"')

# 12. related links health
weak = []
for k, d in data.items():
    rel = d.get('related', [])
    urls = [r if isinstance(r, str) else r.get('url', '') for r in rel]
    hub_link = any(u.rstrip('/').endswith(k.split('_')[1]) and u.count('/') <= 5 for u in urls)
    sib = sum(1 for u in urls if '/services/' in u and not u.rstrip('/').endswith(k.split('_')[1]))
    cases = sum(1 for u in urls if '/case-studies/' in u)
    inds = sum(1 for u in urls if '/industries/' in u)
    if not hub_link or sib < 1 or cases < 1 or inds < 2:
        weak.append((k, hub_link, sib, cases, inds))
print('\n[12] related-link health: weak pages =', len(weak))
for w in weak[:6]:
    print('   ', w)

# 13. word counts
wc = sorted((d.get('words', 0), k) for k, d in data.items())
print('\n[13] words: min', wc[0], '| median', wc[len(wc)//2], '| max', wc[-1])
low = [x for x in wc if x[0] < 900]
print('    pages under 900 words:', len(low), [k for _, k in low[:8]])

# 14. l1 breadcrumb check
l1 = collections.Counter(str(d.get('l1')) for d in data.values())
print('\n[14] l1 values:', dict(l1))
