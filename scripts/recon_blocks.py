import json, os

base = '/home/z/my-project/site/src/content/pages'
kinds = {}
rows = []
for f in sorted(os.listdir(base)):
    if not (f == 'services.json' or f.startswith('services_')):
        continue
    d = json.load(open(os.path.join(base, f), encoding='utf-8'))
    types = {}
    words = 0
    for b in d.get('blocks', []):
        t = b.get('t', '?')
        types[t] = types.get(t, 0) + 1
        if t == 'p':
            words += len(str(b.get('x', '')).split())
    key = json.dumps(types, sort_keys=True)
    kinds.setdefault(key, []).append(f)
    rows.append((f, d.get('template'), words, types))

print('=== BLOCK-SIGNATURE GROUPS (services pages) ===')
for k, fs in sorted(kinds.items(), key=lambda kv: -len(kv[1])):
    print(f'{len(fs)} pages: {k}')
    for f in fs[:60]:
        print('   ', f)

print()
print('=== WORD COUNTS (prose only, p blocks) ===')
for f, tpl, w, types in sorted(rows, key=lambda r: r[2]):
    print(f'{w:5d}  {f}')
