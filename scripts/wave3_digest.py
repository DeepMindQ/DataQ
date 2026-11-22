#!/usr/bin/env python3
"""Wave 3 digests: dump full narrative text of the 8 expertise hubs for rewriting."""
import json

PAGES='site/src/content/pages'
DOM=["agentic-ai-hyperautomation","applied-ai-generative-ai","blockchain-digital-trust",
     "cloud-edge-platform-engineering","cybersecurity-zero-trust","data-analytics-lakehouse",
     "iot-digital-twin-robotics","quantum-advanced-compute"]

out=[]
for d in DOM:
    j=json.load(open(f'{PAGES}/services_{d}.json'))
    out.append('='*100)
    out.append(f"HUB: {d}  title={j['title']!r}")
    out.append(f"meta_description: {j['meta_description']}")
    out.append(f"seo_title: {j['seo_title']}")
    for i,b in enumerate(j['blocks']):
        t=b['t']
        if t in ('hero','p','h2','cta','note'):
            sub=f"\n   sub: {b['sub']}" if b.get('sub') else ''
            out.append(f"[{i:02d}] {t}: {b.get('x','')}{sub}")
        elif t=='bullets':
            out.append(f"[{i:02d}] bullets ({len(b['items'])}):")
            for q,a in b['items']: out.append(f"     - {q} :: {a[:200]}")
        elif t=='table':
            out.append(f"[{i:02d}] table: {b.get('caption','')} | headers={b['headers']}")
            for r in b['rows']: out.append(f"     row: {' | '.join(str(c)[:90] for c in r)}")
        elif t=='arch':
            n_lab=[n['label'] for n in b['nodes']]
            out.append(f"[{i:02d}] arch: {b['title']} | lanes={b['lanes']} | nodes({len(n_lab)})={n_lab[:9]}... | edges={len(b['edges'])} | note={b.get('note','')[:120]}")
        elif t=='idash':
            out.append(f"[{i:02d}] idash: {b['title']} | kpis={[k['label'] for k in b['kpis']]} | tabs={[tb['name'] for tb in b['tabs']]} | note={b.get('note','')[:120]}")
        elif t=='chart':
            out.append(f"[{i:02d}] chart({b['variant']}): {b['title']} | caption={b.get('caption','')[:130]}")
        elif t=='explorer':
            out.append(f"[{i:02d}] explorer: {b['title']} | intro={b['intro'][:150]}")
    out.append(f"cards ({len(j.get('cards',[]))}):")
    for c in j.get('cards',[]): out.append(f"  - {c['title']} [{c['tag']}] :: {c['desc'][:130]}")
    out.append(f"related: {[(r['title'],r['url']) for r in j.get('related',[])]}")
    out.append(f"evidence: {[(e['title'][:44],e['url']) for e in j.get('evidence',[])]}")
    out.append('')

open('scripts/wave3_digest_out.txt','w').write('\n'.join(out))
print('written', len('\n'.join(out)), 'chars')
