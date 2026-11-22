#!/usr/bin/env python3
"""Fix p3 references -> correct param index in the 4 affected pages (JSON + generator sources)."""
import json

fixes = {
    'site/src/content/pages/services_cloud-edge-platform-engineering_finops-sustainable-computing.json': [
        ('max(0, (p3-25)*0.7+p0*0.18-p1*4)', 'max(0, (p2-25)*0.7+p0*0.18-p1*4)'),
        ('(100-p0)*0.32*(1+p3/60)', '(100-p0)*0.32*(1+p2/60)'),
    ],
    'site/src/content/pages/services_cybersecurity-zero-trust_ai-security-model-protection.json': [
        ('p0*0.08*p1*0.06*p3/1000', 'p0*0.08*p1*0.06*p2/1000'),
    ],
    'site/src/content/pages/services_quantum-advanced-compute_post-quantum-cryptography.json': [
        ('max(0, p0*0.15*(1-p3*0.06))', 'max(0, p0*0.18*(1-p2*0.06))'),
    ],
    'site/src/content/pages/services_quantum-advanced-compute_quantum-readiness-strategy.json': [
        ('min(90, (100-p1)*0.5+p3*8)', 'min(90, (100-p1)*0.5+p2*8)'),
        ('max(5, p3*14-(100-p1)*0.3)', 'max(5, p2*14-(100-p1)*0.3)'),
    ],
}
gen_fixes = {
    'scripts/gen_svc/t4_cloud.py': [
        ('max(0, (p3-25)*0.7+p0*0.18-p1*4)', 'max(0, (p2-25)*0.7+p0*0.18-p1*4)'),
        ('(100-p0)*0.32*(1+p3/60)', '(100-p0)*0.32*(1+p2/60)'),
    ],
    'scripts/gen_svc/t5_security.py': [
        ('p0*0.08*p1*0.06*p3/1000', 'p0*0.08*p1*0.06*p2/1000'),
    ],
    'scripts/gen_svc/t8_quantum.py': [
        ('max(0, p0*0.15*(1-p3*0.06))', 'max(0, p0*0.18*(1-p2*0.06))'),
        ('min(90, (100-p1)*0.5+p3*8)', 'min(90, (100-p1)*0.5+p2*8)'),
        ('max(5, p3*14-(100-p1)*0.3)', 'max(5, p2*14-(100-p1)*0.3)'),
    ],
}

n = 0
for f, subs in fixes.items():
    raw = open(f).read()
    for old, new in subs:
        if old in raw:
            raw = raw.replace(old, new)
            n += 1
        else:
            print('MISS in', f, old[:40])
    json.dump(json.loads(raw), open(f, 'w'), indent=1, ensure_ascii=False)

for f, subs in gen_fixes.items():
    raw = open(f).read()
    for old, new in subs:
        if old in raw:
            raw = raw.replace(old, new)
        else:
            print('GEN MISS in', f, old[:40])
    open(f, 'w').write(raw)

print('json fixes applied:', n)
