#!/usr/bin/env python3
"""Wave 3 engine — applies per-hub content ops to the 8 expertise hub JSONs.

Usage: python3 scripts/wave3_apply.py wave3_data1|wave3_data2|wave3_data3
Each data module defines HUB_OPS = {domain: ops}. Ops are applied with hard
assertions on the current text (old_prefix) so nothing is silently mis-edited.
"""
import json, sys, importlib
from pathlib import Path

PAGES = Path('/home/z/my-project/site/src/content/pages')

def apply(mod_name: str) -> None:
    mod = importlib.import_module(mod_name)
    for domain, ops in mod.HUB_OPS.items():
        f = PAGES / f'services_{domain}.json'
        j = json.loads(f.read_text())
        blocks = j['blocks']
        tag = f"{mod_name}:{domain}"

        for idx, old_prefix, title, sub in ops.get('h2', []):
            b = blocks[idx]
            assert b['t'] == 'h2' and b['x'].startswith(old_prefix), \
                f"{tag} h2[{idx}] expected {old_prefix!r}, got {b['x'][:60]!r}"
            b['x'] = title
            b['sub'] = sub

        for idx, old_prefix, text in ops.get('p', []):
            b = blocks[idx]
            assert b['t'] == 'p' and b['x'].startswith(old_prefix), \
                f"{tag} p[{idx}] expected {old_prefix!r}, got {b['x'][:60]!r}"
            b['x'] = text

        for idx, cap in ops.get('table_cap', []):
            assert blocks[idx]['t'] == 'table', f"{tag} table[{idx}] not a table"
            blocks[idx]['caption'] = cap

        for idx, title, badges in ops.get('arch', []):
            assert blocks[idx]['t'] == 'arch', f"{tag} arch[{idx}] not arch"
            blocks[idx]['title'] = title
            blocks[idx]['badges'] = [{'label': l, 'value': v} for l, v in badges]

        for idx, cap in ops.get('bar_cap', []):
            b = blocks[idx]
            assert b['t'] == 'chart' and b['variant'] == 'bar', f"{tag} bar[{idx}] not a bar chart"
            b['caption'] = cap

        for idx, note, badge in ops.get('idash', []):
            assert blocks[idx]['t'] == 'idash', f"{tag} idash[{idx}] not idash"
            blocks[idx]['note'] = note
            blocks[idx]['badge'] = badge

        for idx, note in ops.get('explorer', []):
            assert blocks[idx]['t'] == 'explorer', f"{tag} explorer[{idx}] not explorer"
            blocks[idx]['practiceNote'] = note

        for anchor_prefix, items in ops.get('faq', []):
            ci = next(i for i, b in enumerate(blocks) if b['t'] == 'cta')
            assert blocks[ci]['x'].startswith(anchor_prefix), \
                f"{tag} cta expected {anchor_prefix!r}, got {blocks[ci]['x'][:50]!r}"
            blocks.insert(ci, {'t': 'bullets', 'items': [[q, a] for q, a in items]})

        if 'meta' in ops:
            j['meta_description'] = ops['meta']
        if 'chip' in ops:
            j['hero_chip'] = {'head': ops['chip'][0], 'sub': ops['chip'][1]}

        f.write_text(json.dumps(j, ensure_ascii=False, indent=1) + '\n')
        nfaq = sum(len(x[1]) for x in ops.get('faq', []))
        print(f"OK {tag}: {len(blocks)} blocks, +{nfaq} FAQ items, chip+meta set")

if __name__ == '__main__':
    sys.path.insert(0, '/home/z/my-project/scripts')
    apply(sys.argv[1])
    print("Wave 3 batch applied.")
