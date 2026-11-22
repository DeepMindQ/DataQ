#!/usr/bin/env python3
"""Wave 4 engine — applies per-page content ops to the 54 service subpage JSONs.

Usage: python3 scripts/wave4_apply.py wave4_d1_agentic [... module names ...]
Each data module defines OPS = {page_stem: ops}. Every edit is guarded by a hard
assertion on the current text (old_prefix) so nothing is silently mis-applied.
"""
import json, sys, importlib
from pathlib import Path

PAGES = Path('/home/z/my-project/site/src/content/pages')


def _matches(blocks, t, prefix, tag, field='x'):
    hits = [i for i, b in enumerate(blocks) if b.get('t') == t and str(b.get(field, '')).startswith(prefix)]
    assert len(hits) == 1, f"{tag}: {len(hits)} {t} blocks match prefix {prefix[:60]!r}"
    return hits[0]


def _h2_index(blocks, old_prefix, new_title, tag):
    """Locate the h2 to edit; tolerate an already-applied op (idempotent re-runs)."""
    hits = [i for i, b in enumerate(blocks) if b.get('t') == 'h2' and str(b.get('x', '')).startswith(old_prefix)]
    if not hits:
        done = [i for i, b in enumerate(blocks) if b.get('t') == 'h2' and b.get('x') == new_title]
        assert len(done) == 1, f'{tag}: h2 {old_prefix[:50]!r} not found and new title not present either'
        return None
    assert len(hits) == 1, f'{tag}: {len(hits)} h2 blocks match {old_prefix[:50]!r}'
    return hits[0]


# The 3 templated table captions that exist on every subpage (1 table each).
TCAP_TEMPLATES = {
    'failure': 'failure modes we design against',
    'defaults': 'default stack and the conditions under which we deviate',
    'gates': 'Release gates for',
}


def apply_page(stem: str, ops: dict) -> None:
    f = PAGES / f'{stem}.json'
    j = json.loads(f.read_text())
    blocks = j['blocks']
    tag = stem

    if 'chip' in ops:
        head, sub = ops['chip']
        j['hero_chip'] = {'head': head, 'sub': sub}

    for old_prefix, new_title, new_sub in ops.get('h2', []):
        i = _h2_index(blocks, old_prefix, new_title, f'{tag} h2')
        if i is None:
            continue  # already applied on a previous run
        blocks[i]['x'] = new_title
        if new_sub is not None:
            blocks[i]['sub'] = new_sub

    for old_prefix, new_title in ops.get('arch', []):
        hits = [i for i, b in enumerate(blocks) if b.get('t') == 'arch' and str(b.get('title', '')).startswith(old_prefix)]
        if not hits:
            assert any(b.get('t') == 'arch' and b.get('title') == new_title for b in blocks), \
                f'{tag}: arch {old_prefix[:50]!r} not found and new title absent'
            continue  # already applied
        assert len(hits) == 1, f'{tag}: {len(hits)} arch blocks match {old_prefix[:50]!r}'
        blocks[hits[0]]['title'] = new_title

    for tpl_key, new_cap in ops.get('tcap', []):
        if tpl_key in TCAP_TEMPLATES:
            tpl = TCAP_TEMPLATES[tpl_key]
            field_ok = lambda cap: tpl in str(cap)
        else:
            tpl = tpl_key
            field_ok = lambda cap: str(cap).startswith(tpl)
        hits = [i for i, b in enumerate(blocks) if b.get('t') == 'table' and field_ok(b.get('caption', ''))]
        if not hits:
            assert any(b.get('t') == 'table' and b.get('caption') == new_cap for b in blocks), \
                f'{tag}: tcap template {tpl!r} not found and new caption absent'
            continue  # already applied
        assert len(hits) == 1, f"{tag}: {len(hits)} tables match template {tpl!r}"
        blocks[hits[0]]['caption'] = new_cap

    if 'ccap' in ops:
        charts = [i for i, b in enumerate(blocks) if b.get('t') == 'chart']
        assert len(charts) == 1, f'{tag}: expected exactly 1 chart, found {len(charts)}'
        blocks[charts[0]]['caption'] = ops['ccap']

    if 'idash' in ops:
        new_note, new_badge = ops['idash']
        idash = [i for i, b in enumerate(blocks) if b.get('t') == 'idash']
        assert len(idash) == 1, f'{tag}: expected exactly 1 idash'
        blocks[idash[0]]['note'] = new_note
        blocks[idash[0]]['badge'] = new_badge

    faq = ops.get('faq', [])
    if faq:
        already = any(b['t'] == 'bullets' and b.get('items') and isinstance(b['items'][0], (list, tuple))
                      and str(b['items'][0][0]).rstrip().endswith('?') for b in blocks)
        if not already:
            ci = next(i for i, b in enumerate(blocks) if b['t'] == 'cta')
            blocks.insert(ci, {'t': 'bullets', 'items': [[q, a] for q, a in faq]})

    if 'meta' in ops:
        j['meta_description'] = ops['meta']

    f.write_text(json.dumps(j, ensure_ascii=False, indent=1) + '\n')
    print(f"OK {tag}: chip={'Y' if 'chip' in ops else '-'} "
          f"h2={len(ops.get('h2', []))} arch={len(ops.get('arch', []))} "
          f"tcap={len(ops.get('tcap', []))} ccap={'Y' if 'ccap' in ops else '-'} "
          f"faq={len(faq)} meta={'Y' if 'meta' in ops else '-'}")


def apply(mod_name: str) -> None:
    mod = importlib.import_module(mod_name)
    for stem, ops in mod.OPS.items():
        apply_page(stem, ops)


if __name__ == '__main__':
    sys.path.insert(0, '/home/z/my-project/scripts')
    for name in sys.argv[1:]:
        apply(name)
    print('Wave 4 batches applied.')
