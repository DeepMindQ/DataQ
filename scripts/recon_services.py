import json, os, re, sys

base = '/home/z/my-project/site/src/content/pages'

def block_titles(b):
    out = []
    if isinstance(b, dict):
        for k in ('t', 'title', 'h', 'heading'):
            v = b.get(k)
            if isinstance(v, str) and v.strip():
                out.append((k, v.strip()[:110]))
    return out

print('=== ALL PAGE JSONs ===')
for f in sorted(os.listdir(base)):
    if not f.endswith('.json'):
        continue
    p = os.path.join(base, f)
    try:
        d = json.load(open(p, encoding='utf-8'))
    except Exception as e:
        print(f'ERR {f}: {e}')
        continue
    slug = d.get('slug') or '(none)'
    template = d.get('template') or '(none)'
    blocks = d.get('blocks') or []
    cards = d.get('cards') or []
    print(f'--- {f} | slug={slug} | template={template} | blocks={len(blocks)} cards={len(cards)}')
    seen = []
    for b in blocks:
        for k, v in block_titles(b):
            seen.append(f'[{b.get("type", b.get("kind", "?"))}] {k}: {v}')
    for s in seen[:40]:
        print('    ' + s)
    if len(seen) > 40:
        print(f'    ... {len(seen)-40} more block titles')

print()
print('=== TOWER OCCURRENCES (unfiltered walk) ===')
pat = re.compile(r'tower', re.I)
roots = ['/home/z/my-project/site/src', '/home/z/my-project/scripts']
for root in roots:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ('node_modules', '.next', 'out', 'out-gh', '.gh-deploy')]
        for fn in filenames:
            if not fn.endswith(('.json', '.tsx', '.ts', '.js', '.py', '.md', '.mdx', '.html', '.css')):
                continue
            p = os.path.join(dirpath, fn)
            try:
                s = open(p, encoding='utf-8', errors='replace').read()
            except Exception:
                continue
            for i, line in enumerate(s.splitlines(), 1):
                if pat.search(line):
                    print(f'{p}:{i}: {line.strip()[:170]}')
