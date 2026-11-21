import json, glob, re, collections

files = glob.glob('/home/z/my-project/site/src/content/pages/*.json')
print('files:', len(files))

pat_counts = collections.Counter()
samples = collections.defaultdict(list)

TELLS = [
    r'not by slide', r'not slideware', r'regulatory teeth', r"sector'?s? physics",
    r'governed autonomy', r'intelligence layer', r'cannot fail quietly', r'fail quietly',
    r'investor discipline', r'silently depend', r'falsifiable', r'evidence generation',
    r'evidence to defend', r'wearing a compliance uniform', r'margin recovered in milliseconds',
    r'stand up to audit', r'answers to the P&L', r'compete in the intelligence era',
    r'hoarders', r'self-healing workflows', r'decision velocity', r'pattern 80',
    r'outcome-linked', r'auditable', r'replayable', r'evidence trail', r'named gates',
    r'zero-exposure', r'quietly', r'with the evidence', r'at decision speed',
    r'one governed', r'measured, auditable', r'the machinery', r'accumulating AI pilots',
    r'operating machinery', r'that compounds', r'shared truth', r'verified \u2014',
    r'X, not Y', r'not just', r'rather than', r'in one program', r'one program',
    r'engineered for outcomes', r'Intelligence, Engineered',
]

def walk(o):
    if isinstance(o, dict):
        for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
    elif isinstance(o, str):
        for p in TELLS:
            for m in re.finditer(p, o, re.I):
                pat_counts[p] += 1
                if len(samples[p]) < 2:
                    samples[p].append(o[:160])

for f in files:
    try: d = json.load(open(f))
    except Exception: continue
    walk(d)

for p, c in pat_counts.most_common():
    print(f'{c:5d}  {p}')
    for s in samples[p][:1]:
        print('        e.g.', s.replace(chr(10),' ')[:150])
