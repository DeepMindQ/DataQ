import json, os, re

base = '/home/z/my-project/site/src/content/pages'
out = []

# 1) services pages inventory
for f in sorted(os.listdir(base)):
    if not (f == 'services.json' or f.startswith('services_')):
        continue
    p = os.path.join(base, f)
    try:
        d = json.load(open(p, encoding='utf-8'))
    except Exception as e:
        out.append(f'ERR {f}: {e}')
        continue
    template = d.get('template') or '(none)'
    blocks = d.get('blocks') or []
    out.append(f'--- {f} | template={template} | blocks={len(blocks)}')
    for i, b in enumerate(blocks):
        if isinstance(b, dict):
            t = str(b.get('t', ''))[:130]
            x = str(b.get('x', ''))[:90]
            keys = ','.join(sorted(b.keys()))
            out.append(f'    [{i}] {t} || x:{x} || keys:{keys}')

# 2) tower occurrences in src (skip content pages, they are covered above by inventory)
pat = re.compile(r'tower', re.I)
root = '/home/z/my-project/site/src'
out.append('')
out.append('=== TOWER OCCURRENCES in src (tsx/ts/json) ===')
for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in ('node_modules', '.next', 'out', 'out-gh')]
    for fn in filenames:
        if not fn.endswith(('.json', '.tsx', '.ts', '.css')):
            continue
        p = os.path.join(dirpath, fn)
        try:
            s = open(p, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        for i, line in enumerate(s.splitlines(), 1):
            if pat.search(line):
                out.append(f'{p.replace(root, "")}:{i}: {line.strip()[:170]}')

open('/home/z/my-project/scripts/recon_out.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('done, lines:', len(out))
