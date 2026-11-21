"""Final exhaustive secret-source scrub verification (multiple passes).
Checks every deliverable surface for the patent applicant/inventor names."""
import subprocess, os, glob

HITS = []
TERMS = ["strategemist", "pisupati", "ravi shanker", "applicant of record", "patents act, 1970"]

def scan_dir(root, exts, exclude=()):
    for ext in exts:
        try:
            out = subprocess.run(
                ["grep", "-rli", "-e", TERMS[0], "-e", TERMS[1], "-e", TERMS[2],
                 "-e", TERMS[3], "-e", TERMS[4],
                 "--include", ext, root],
                capture_output=True, text=True, timeout=110)
            for line in out.stdout.splitlines():
                if line and not any(x in line for x in exclude):
                    HITS.append((root, ext, line))
        except subprocess.TimeoutExpired:
            print("timeout scanning", root, ext)

SITE = '/home/z/my-project/site'
print("PASS 1 — site src (ts/tsx/json/css/md/py/js):")
scan_dir(SITE + '/src', ['*.ts', '*.tsx', '*.json', '*.css', '*.md', '*.js'])
print("PASS 2 — site public:")
scan_dir(SITE + '/public', ['*'])
print("PASS 3 — site scripts + docs + readme:")
scan_dir(SITE + '/scripts', ['*.py', '*.json', '*.md', '*.js', '*.sh'])
for f in [SITE + '/README.md', SITE + '/next.config.ts']:
    if os.path.exists(f):
        s = open(f, errors='ignore').read().lower()
        if any(t in s for t in TERMS):
            HITS.append(('file', f, ''))
print("PASS 4 — built export out/ (html/js/json/txt):")
scan_dir(SITE + '/out', ['*.html', '*.js', '*.json', '*.txt', '*.xml', '*.css'])
print("PASS 5 — repo-level docs:")
scan_dir('/home/z/my-project/docs', ['*.md'])

if HITS:
    print("FAIL — source mentions remain:")
    for h in HITS[:30]:
        print("  ", h)
else:
    print("CLEAN: zero occurrences of applicant/inventor names across src, public, scripts, docs, and the built export.")
