#!/usr/bin/env python3
"""Dump the remaining formulaic fields: sector-bar captions, idash notes, arch titles/notes, explorer practiceNote."""
import json

PAGES='site/src/content/pages'
DOM=["agentic-ai-hyperautomation","applied-ai-generative-ai","blockchain-digital-trust",
     "cloud-edge-platform-engineering","cybersecurity-zero-trust","data-analytics-lakehouse",
     "iot-digital-twin-robotics","quantum-advanced-compute"]
for d in DOM:
    j=json.load(open(f'{PAGES}/services_{d}.json'))
    print('='*90); print(d)
    for i,b in enumerate(j['blocks']):
        if b['t']=='chart' and b['variant']=='bar' and 'briefs by sector' in b['title']:
            print(f" [{i}] bar caption: {b.get('caption')}")
            print(f"     bar note: {b.get('note')}")
        if b['t']=='idash':
            print(f" [{i}] idash note: {b.get('note')} | badge: {b.get('badge')}")
        if b['t']=='arch':
            print(f" [{i}] arch title: {b['title']}")
            print(f"     arch note: {b.get('note')}")
            print(f"     badges: {[(bd['label'],bd['value']) for bd in b.get('badges',[])]}")
        if b['t']=='explorer':
            print(f" [{i}] explorer practiceNote: {b.get('practiceNote','')[:160]}")
            print(f"     industries: {[(x['name'],x['capUrl'][:70]) for x in b['industries'][:4]]}... ({len(b['industries'])})")
