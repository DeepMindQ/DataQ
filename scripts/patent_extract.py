import re, os, glob, json

out = {}
for f in sorted(glob.glob('/tmp/patents/*.txt')):
    name = os.path.basename(f)
    txt = open(f, encoding='utf-8', errors='ignore').read()
    txt = re.sub(r'\s+', ' ', txt)
    rec = {'file': name}
    # title
    m = re.search(r'TITLE OF THE INVENTION:\s*(.{0,300}?)2\.\s*APPLICANT', txt)
    rec['title'] = m.group(1).strip() if m else ''
    # abstract
    m = re.search(r'ABSTRACT\s*(?:OF THE INVENTION)?[:\.]?\s*(.{0,2200}?)(?:Page \d+|\Z)', txt)
    rec['abstract'] = m.group(1).strip() if m else ''
    # summary of invention fallback
    if not rec['abstract']:
        m = re.search(r'SUMMARY OF (?:THE )?INVENTION[:\.]?\s*(.{0,2200}?)(?:BRIEF DESCRIPTION|Page \d+|\Z)', txt)
        rec['abstract'] = m.group(1).strip() if m else ''
    # technical advantages / effects
    adv = re.findall(r'(?:technical effect|advantage|benefit)[s]?\s*(?:of[^.:]{0,80})?[:\.]\s*([^.]{30,300}\.)', txt, re.I)
    rec['advantages'] = adv[:8]
    # example figures
    figs = re.findall(r'FIG(?:URE)?\.?\s*\d+[A-Z]?\s*[:\-–]?\s*([^.;]{15,150})[.;]', txt, re.I)
    rec['figures'] = figs[:10]
    out[name] = rec

print(json.dumps(out, indent=1)[:12000])
