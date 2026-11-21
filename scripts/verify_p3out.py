import json, os, re

d = '/tmp/p3test/src/content/pages'
files = [f for f in os.listdir(d) if f == 'services.json' or f.startswith('services_')]
print('pages:', len(files))

# 1. arch topology uniqueness
arch_sigs = {}
for f in files:
    j = json.load(open(os.path.join(d, f), encoding='utf-8'))
    for b in j['blocks']:
        if b['t'] == 'arch':
            sig = (tuple(b['lanes']), tuple(n['label'] for n in b['nodes']))
            arch_sigs.setdefault(sig, []).append(f)
dups = {k: v for k, v in arch_sigs.items() if len(v) > 1}
print('arch blocks:', len(arch_sigs), 'duplicate topologies:', len(dups))
for k, v in list(dups.items())[:5]:
    print('  DUP:', v)

# 2. idash preserved everywhere?
no_idash = []
for f in files:
    j = json.load(open(os.path.join(d, f), encoding='utf-8'))
    if not any(b['t'] == 'idash' for b in j['blocks']):
        no_idash.append(f)
print('pages without idash:', no_idash)

# 3. explorer presence + capUrl validity (against index)
idx = json.load(open('/tmp/p3test/src/content/index.json', encoding='utf-8'))
urls = set(r['url'] for r in idx if isinstance(r, dict) and r.get('url'))
bad = []
exp_count = 0
for f in files:
    j = json.load(open(os.path.join(d, f), encoding='utf-8'))
    for b in j['blocks']:
        if b['t'] == 'explorer':
            exp_count += 1
            for ind in b['industries']:
                if ind['capUrl'] not in urls:
                    bad.append((f, ind['capUrl']))
print('explorer blocks:', exp_count, 'bad capUrls:', len(bad), bad[:5])

# 4. card url validity
badc = []
for f in files:
    j = json.load(open(os.path.join(d, f), encoding='utf-8'))
    for c in j.get('cards', []):
        if c['url'] not in urls:
            badc.append((f, c['url']))
print('bad card urls:', len(badc), badc[:8])

# 5. related rail url validity
badr = []
for f in files:
    j = json.load(open(os.path.join(d, f), encoding='utf-8'))
    for c in j.get('related', []):
        if c['url'] not in urls:
            badr.append((f, c['url']))
print('bad related urls:', len(badr), badr[:8])

# 6. h2 uniqueness across section
seen = {}
dups = []
for f in files:
    j = json.load(open(os.path.join(d, f), encoding='utf-8'))
    for b in j['blocks']:
        if b['t'] == 'h2':
            k = b['x'].strip().lower()
            if k in seen and seen[k] != f:
                dups.append((k, seen[k], f))
            seen.setdefault(k, f)
print('h2 duplicates:', len(dups), dups[:6])

# 7. block type census + word range
census = {}
words = []
for f in files:
    j = json.load(open(os.path.join(d, f), encoding='utf-8'))
    words.append(j['words'])
    for b in j['blocks']:
        census[b['t']] = census.get(b['t'], 0) + 1
print('block census:', census)
print('words min/max/avg:', min(words), max(words), sum(words)//len(words))
