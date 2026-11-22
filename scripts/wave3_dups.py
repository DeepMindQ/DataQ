#!/usr/bin/env python3
"""Quantify cross-hub duplication: sentences shared verbatim between the 8 expertise hubs,
and formulaic title patterns."""
import json, re, collections

PAGES='site/src/content/pages'
DOM=["agentic-ai-hyperautomation","applied-ai-generative-ai","blockchain-digital-trust",
     "cloud-edge-platform-engineering","cybersecurity-zero-trust","data-analytics-lakehouse",
     "iot-digital-twin-robotics","quantum-advanced-compute"]

sent=collections.defaultdict(list)
h2first=collections.Counter()
for d in DOM:
    j=json.load(open(f'{PAGES}/services_{d}.json'))
    for b in j['blocks']:
        xs=[]
        if isinstance(b.get('x'),str): xs=[b['x']]
        if b['t']=='bullets':
            xs=[it[0]+' '+it[1] for it in b['items']]
        if b['t']=='table':
            xs=[c for r in b['rows'] for c in r]
        for x in xs:
            for s in re.split(r'(?<=[.!?]) ', x):
                s=s.strip()
                if len(s)>60: sent[s].append(d)
        if b['t']=='h2':
            h2first[b['x'].split(' — ')[0][:45]]+=1

print('== VERBATIM SENTENCES SHARED BY >=3 HUBS ==')
n=0
for s,ds in sorted(sent.items(), key=lambda kv:-len(kv[1])):
    if len(ds)>=3:
        n+=1
        if n<=25: print(f"[{len(ds)} hubs] {s[:110]}")
print('total shared>=3:', n, '| shared>=2:', sum(1 for s,ds in sent.items() if len(ds)>=2))

print('\n== H2 LEADING PATTERN FREQUENCY (8 hubs) ==')
for p,c in h2first.most_common(14): print(f"[{c}x] {p}")
