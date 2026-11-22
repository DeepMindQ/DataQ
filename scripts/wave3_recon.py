#!/usr/bin/env python3
"""Wave 3 recon: schema of expertise_hub blocks, skeleton comparison across the 8 hubs."""
import json, collections, os

PAGES = 'site/src/content/pages'
DOM = ["agentic-ai-hyperautomation","applied-ai-generative-ai","blockchain-digital-trust",
       "cloud-edge-platform-engineering","cybersecurity-zero-trust","data-analytics-lakehouse",
       "iot-digital-twin-robotics","quantum-advanced-compute"]

# 1. schema: which fields each block type uses across the 8 hubs
field_use = collections.defaultdict(collections.Counter)
for d in DOM:
    j = json.load(open(f'{PAGES}/services_{d}.json'))
    for b in j['blocks']:
        for k in b.keys():
            field_use[b['t']][k] += 1
print('== SCHEMA (field usage per block type, max 8) ==')
for t in ['hero','p','h2','table','arch','idash','chart','explorer','bullets','cta','cards','quote']:
    if t in field_use:
        print(f"{t:9s}", dict(field_use[t]))

# 2. skeleton comparison: h2 sequence per hub
print('\n== H2 SKELETON PER HUB ==')
for d in DOM:
    j = json.load(open(f'{PAGES}/services_{d}.json'))
    h2s = [b['x'][:70] for b in j['blocks'] if b['t']=='h2']
    print(f"\n{d} ({len(j['blocks'])} blocks, {len(h2s)} h2)")
    for i,h in enumerate(h2s): print(f"  {i+1}. {h}")

# 3. arch/idash/chart payload shapes (first hub, abbreviated)
print('\n== ARCH PAYLOAD KEYS (agentic) ==')
j = json.load(open(f'{PAGES}/services_agentic-ai-hyperautomation.json'))
for b in j['blocks']:
    if b['t']=='arch':
        x=b.get('x',{})
        print('arch keys:', list(x.keys()))
        for lane in x.get('lanes',[])[:1]:
            print('lane:', {k:(v if not isinstance(v,list) else f"[{len(v)} items]") for k,v in lane.items()})
        for n in x.get('nodes',[])[:2]: print('node:', n)
        for e in x.get('edges',[])[:2]: print('edge:', e)
        print('badges:', x.get('badges'))
    if b['t']=='idash':
        x=b.get('x',{})
        print('\nidash keys:', list(x.keys()))
        tiles=x.get('tiles',[])
        if tiles: print('tile0:', tiles[0])
        for k,v in x.items():
            if k!='tiles' and isinstance(v,list) and v:
                print(f"{k}[0]:", v[0] if not isinstance(v[0],dict) else {kk:str(vv)[:60] for kk,vv in v[0].items()})
    if b['t']=='chart':
        x=b.get('x',{})
        print('\nchart keys:', list(x.keys()))
        print(json.dumps(x, ensure_ascii=False)[:500])
    if b['t']=='explorer':
        x=b.get('x',{})
        print('\nexplorer keys:', list(x.keys()), {k:(f"[{len(v)} items]" if isinstance(v,list) else str(v)[:60]) for k,v in x.items()})
