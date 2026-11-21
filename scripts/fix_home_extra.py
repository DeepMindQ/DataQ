"""Fix home.json extras (towers descs) + HomeView residual copy."""
import json, re

P = '/home/z/my-project/site/src/content/pages/home.json'
d = json.load(open(P))
ex = d['extras']

TOWER_DESC = {
    "Applied AI & Generative AI": "Strategy, model selection, retrieval, evaluation and production operations. AI measured on the P&L.",
    "Agentic AI & Hyperautomation": "Digital workers with defined roles, budgets and human checkpoints. Every action logged and reversible.",
    "Data, Analytics & Lakehouse": "Pipelines, lakehouse and governance: reports that reconcile, lineage you can trace, access under control.",
    "Cybersecurity & Zero-Trust": "Identity-first architecture for people, machines and models, with detection and response in one program.",
    "Cloud, Edge & Platform Engineering": "Hybrid and edge estates engineered for reliability and cost per workload, with platforms teams adopt.",
    "Quantum & Advanced Compute": "Optimization, simulation and PQC migration where the mathematics pays back, benchmarked against classical methods.",
    "Blockchain & Digital Trust": "Permissioned networks, tokenization and verifiable credentials with the reporting supervisors expect.",
    "IoT, Digital Twin & Robotics": "Sensor integration, digital twins and robotics: see, simulate and act on physical assets in one loop.",
}
for t in ex['towers']:
    if t['name'] in TOWER_DESC:
        t['desc'] = TOWER_DESC[t['name']]

# industries descriptions cleanup
for i in ex.get('industries', []):
    if isinstance(i, dict) and i.get('desc'):
        i['desc'] = re.sub(r'—\s*(that cannot fail quietly|with governance attached|on the shop floor|for the energy transition|and shelf truth)', '', i['desc'])
        i['desc'] = i['desc'].replace('Real-time risk, resilient operations and auditable AI for institutions ', 'Real-time risk decisions, resilient operations and AI controls that pass supervisory review ')
json.dump(d, open(P, 'w'), indent=1, ensure_ascii=False)
print('home extras fixed')

# HomeView residual copy
hv = '/home/z/my-project/site/src/components/site/HomeView.tsx'
s = open(hv).read()
s = s.replace('See the output, not the pitch', 'What a delivery produces')
s = s.replace('''We do not sell generic application development. We sell the capability layers that
                  decide whether an enterprise competes in the intelligence era — each tower aligned to
                  your industry from day one.''',
'''These are the capability layers enterprise programs are built on. Every tower
                  carries named services, committed outcomes and the platform rails it deploys on.''')
s = s.replace('filed by our IP foundation and\n                hardened in production.', 'developed by our research programme and\n                in production use inside named platforms.')
s = s.replace('The patent map', 'The method map')
s = s.replace('Every engagement reports the same three curves — baseline locked, delta measured, gates audited.',
              'Baseline locked in weeks 1–2. Delta measured at every gate. The same three panels go to your steering committee.')
s = s.replace('''Illustrative telemetry from comparable programs. Your baseline is set in the value assessment;
            the same panels go to your steering committee every fortnight.''',
'''Composite planning views from our pattern library — not client data. Your own
            baseline replaces these figures at the value assessment.''')
open(hv,'w').write(s)
print('HomeView copy cleaned')
