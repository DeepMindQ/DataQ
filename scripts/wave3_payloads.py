#!/usr/bin/env python3
"""Dump real payloads of arch/idash/chart/explorer/table from two hubs."""
import json

PAGES='site/src/content/pages'
for f in ['services_agentic-ai-hyperautomation','services_data-analytics-lakehouse']:
    j=json.load(open(f'{PAGES}/{f}.json'))
    print('='*110); print(f)
    for i,b in enumerate(j['blocks']):
        t=b['t']
        if t in ('arch','idash','chart','explorer'):
            print(f"--- block {i} {t} ---")
            print(json.dumps({k:v for k,v in b.items() if k!='t'}, ensure_ascii=False, indent=1)[:3300])
        elif t=='table':
            print(f"--- block {i} table ---")
            print('caption:', b.get('caption')); print('headers:', b.get('headers'))
            for r in b.get('rows',[])[:3]: print(' row:', r[:3] if isinstance(r,list) else r)
        elif t=='cards':
            print(f"--- block {i} cards ---")
            for c in b.get('cards',[])[:3]: print(' card:', {k:str(v)[:70] for k,v in c.items()})
    # also cards at top level and related
    print('TOP-LEVEL cards:', len(j.get('cards',[])))
    for c in j.get('cards',[])[:8]: print('  ', {k:str(v)[:60] for k,v in c.items()})
    print('related:', [r['url'] for r in j.get('related',[])])
    print('evidence:', [(e['title'][:40],e['url']) for e in j.get('evidence',[])])
