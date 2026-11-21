#!/usr/bin/env python3
"""检索 Phase 1 遗留：Platform Status、菜单页数计数、菜单截断 CSS。"""
import os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else 'site/src'
patterns = {
    'PLATFORM_STATUS': re.compile(r'Platform\s*Status', re.I),
    'PAGES_COUNT': re.compile(r'\bpages?\b\s*<|>\s*\d+\s*pages|"pages"|\{\w+\}\s*pages|pageCount|pagesCount|n_pages', re.I),
    'TRUNCATE_CSS': re.compile(r'truncate|text-ellipsis|ellipsis|line-clamp'),
}
hits = {k: [] for k in patterns}
for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in ('node_modules', '.next', '.next-export')]
    for f in filenames:
        if not f.endswith(('.tsx', '.ts', '.css', '.json')):
            continue
        p = os.path.join(dirpath, f)
        try:
            t = open(p, encoding='utf-8', errors='ignore').read()
        except Exception:
            continue
        for k, rx in patterns.items():
            if rx.search(t):
                hits[k].append(p)

for k, files in hits.items():
    print(f'=== {k} ({len(files)}) ===')
    for p in sorted(set(files)):
        print('  ', p)

# nav.json 结构
nav_path = os.path.join(root, 'content', 'nav.json')
if os.path.exists(nav_path):
    import json
    nav = json.load(open(nav_path, encoding='utf-8'))
    print('\n=== nav.json top-level keys ===')
    if isinstance(nav, dict):
        for k, v in nav.items():
            print(' ', k, type(v).__name__, (len(v) if hasattr(v, '__len__') else v))
        # 打印前两组菜单结构样例
        for k, v in list(nav.items())[:2]:
            print('\n--- sample:', k, '---')
            print(json.dumps(v, indent=1, ensure_ascii=False)[:1500])
