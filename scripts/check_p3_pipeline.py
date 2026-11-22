import importlib, json, os, re, sys

HERE = '/home/z/my-project/scripts/p3'
sys.path.insert(0, HERE)
import svc_meta as M  # noqa

SPEC = ['spec_applied', 'spec_agentic', 'spec_data', 'spec_cyber',
        'spec_cloud', 'spec_quantum', 'spec_blockchain', 'spec_iot']
NARR = {s: s.replace('spec_', 'narr_') for s in SPEC}

# TechDiagram kinds supported
td = open('/home/z/my-project/site/src/components/site/TechDiagrams.tsx', encoding='utf-8').read()
m = re.search(r'export const DIAGRAM_KINDS\s*=\s*\[(.*?)\] as const', td, re.S)
kinds = set(re.findall(r'"([^"]+)"', m.group(1))) if m else set()
print('DIAGRAM_KINDS:', sorted(kinds))

# ChartPanel variants supported (from ArchDash.tsx ChartPanel)
ad = open('/home/z/my-project/site/src/components/site/ArchDash.tsx', encoding='utf-8').read()
print('chart variants referenced:', sorted(set(re.findall(r'"(line|bar|radar|area|donut|funnel|heatmap|gauge|network)"', ad))))

flow_kinds = {}
chart_variants = {}
missing_narr = []
narr_keys_missing = {}
for name in SPEC:
    sm = importlib.import_module(name)
    nm = importlib.import_module(NARR[name])
    npages = nm.PAGES
    for sp in sm.PAGES:
        N = npages.get(sp['slug'])
        if not N:
            missing_narr.append((name, sp['slug']))
            continue
        fk = sp['flow'].get('kind', '?')
        flow_kinds.setdefault(fk, []).append(f"{sm.TOWER['slug']}/{sp['slug']}")
        cv = sp['chart'].get('variant', 'line')
        chart_variants.setdefault(cv, []).append(f"{sm.TOWER['slug']}/{sp['slug']}")
        # keys compose_sub_page_v2 needs from N
        need = ['hero', 's1_h', 's1_close', 's2_h', 's2_lead', 'arch_h', 'arch_lead', 'flow_h',
                'flow_lead', 'dash_h', 'dash_lead', 'dash_note', 'chart_h', 'chart_lead',
                'plays', 'flagships', 'stack_h', 'stack_lead', 'gates_h', 'artifacts_h',
                'timeline_h', 'integ_h', 'integ_lead', 'controls_h', 'controls_lead',
                'controls_note', 'cta']
        miss = [k for k in need if k not in N]
        if miss:
            narr_keys_missing[f"{name}/{sp['slug']}"] = miss
        # chart2 optional
        if N.get('chart2'):
            c2v = N['chart2'].get('variant', 'line')
            chart_variants.setdefault(c2v, []).append(f"{sm.TOWER['slug']}/{sp['slug']} (chart2)")

print('\nFLOW kinds used:')
for k, v in sorted(flow_kinds.items()):
    ok = 'OK' if k in kinds else '*** MISSING KIND ***'
    print(f'  {k}: {len(v)} pages {ok}  e.g. {v[:3]}')
print('\nCHART variants used:')
for k, v in sorted(chart_variants.items()):
    print(f'  {k}: {len(v)} pages  e.g. {v[:2]}')
print('\nmissing narr entries:', missing_narr)
print('narr keys missing:', narr_keys_missing if narr_keys_missing else 'none')

# hub narr keys
hub_need = ['hero', 's_practices', 's_deep', 's_arch', 'arch_lead', 's_dash', 'dash_lead',
            'dash_note', 's_chart', 'chart_lead', 'chart_note', 's_evidence', 'evidence_lead',
            'evidence_chart_title', 'explorer_title', 'explorer_intro', 'plays', 'flagships',
            's_engage', 'engage', 's_gates', 'cta']
for name in SPEC:
    nm = importlib.import_module(NARR[name])
    miss = [k for k in hub_need if k not in nm.HUB]
    if miss:
        print(f'HUB narr {name}: missing {miss}')
print('\nhub narr check done')
