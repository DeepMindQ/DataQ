import json

idx = json.load(open('/home/z/my-project/site/src/content/index.json', encoding='utf-8'))
urls = set()
pages = idx if isinstance(idx, list) else idx.get('pages', [])
for p in pages:
    if isinstance(p, dict) and p.get('url'):
        urls.add(p['url'])

inds = ['banking-financial-services', 'insurance', 'healthcare-life-sciences', 'manufacturing',
        'retail-consumer-goods', 'energy-utilities', 'telecom-media', 'logistics-supply-chain',
        'public-sector', 'education-research', 'technology-saas', 'agriculture-food']
svcs = ['agentic-ai-hyperautomation', 'applied-ai-generative-ai', 'blockchain-digital-trust',
        'cloud-edge-platform-engineering', 'cybersecurity-zero-trust', 'data-analytics-lakehouse',
        'iot-digital-twin-robotics', 'quantum-advanced-compute']

missing = []
for i in inds:
    for s in svcs:
        u = f'/industries/{i}/capabilities/{s}/'
        if u not in urls:
            missing.append(u)
print('capability URLs missing:', len(missing))
for m in missing[:20]:
    print('  ', m)

# sample industry hub urls to confirm slugs
for i in inds:
    u = f'/industries/{i}/'
    print(('OK ' if u in urls else 'MISS ') + u)
