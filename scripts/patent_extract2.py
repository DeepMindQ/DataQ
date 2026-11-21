import re, os, glob, json

out = {}
for f in sorted(glob.glob('/tmp/patents/*.txt')):
    name = os.path.basename(f)
    txt = open(f, encoding='utf-8', errors='ignore').read()
    txt = re.sub(r'\s+', ' ', txt)
    rec = {'file': name}
    # objects of invention
    m = re.search(r'OBJECTS? OF (?:THE )?INVENTION[:\.]?\s*(.{0,3000}?)(?:SUMMARY|BRIEF DESCRIPTION|DESCRIPTION OF|Page \d+ of \d+|\Z)', txt)
    rec['objects'] = m.group(1).strip() if m else ''
    # numeric performance claims
    nums = re.findall(r'[^.]{0,160}\b(?:accuracy|efficiency|latency|reduction|improvement|faster|percent|throughput)\b[^.]{0,120}\.', txt, re.I)
    rec['claims_num'] = [n.strip() for n in nums if re.search(r'\d', n)][:12]
    # applications / industries mentioned
    m = re.search(r'(?:applicable across|applied in|industries,? including|domains? including|use cases? include)\s*([^.] {0,200})', txt, re.I)
    rec['applications'] = m.group(1).strip() if m else ''
    out[name] = rec

# Print compactly
for k, v in out.items():
    print('='*20, k)
    print('OBJECTS:', (v['objects'][:1200] if v['objects'] else '(none found)'))
    print()
    print('NUM CLAIMS:')
    for c in v['claims_num'][:8]:
        print('  -', c[:220])
    print('APPLICATIONS:', v['applications'][:300])
    print()
