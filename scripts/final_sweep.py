#!/usr/bin/env python3
"""Final sweep over out/: banned strings, confidential names, case count, link integrity on key pages."""
import os, re, json, sys
from urllib.parse import urlparse, unquote

OUT = "/home/z/my-project/site/out"

banned = [
    "Thirty-six anonymized", "Case Studies Overview", "How this section is organized",
    "Choosing an entry point", "Outcomes surfaced as ranked decisionsEvidence",
    "Platform Status", "System Status", "Search 639 pages",
    "Strategemist", "Pisupati", "Hyderabad",
]
conf_rx = re.compile(r"Strategemist|Pisupati|Ravi\s+Shanker", re.I)

hits = []
pages = 0
for dirpath, dirnames, filenames in os.walk(OUT):
    for fn in filenames:
        if fn.endswith((".html", ".txt", ".xml", ".json")) and not fn.startswith("pagefind"):
            p = os.path.join(dirpath, fn)
            try:
                txt = open(p, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            pages += 1 if fn == "index.html" else 0
            for s in banned:
                if s in txt:
                    hits.append(f"BANNED {s!r} in {p.replace(OUT, '')}")
            m = conf_rx.search(txt)
            if m:
                hits.append(f"CONFIDENTIAL {m.group(0)!r} in {p.replace(OUT, '')}")

print(f"html pages scanned: {pages}")
print(f"banned/confidential hits: {len(hits)}")
for h in hits[:20]:
    print(" ", h)

# case count + dual index on hub
hub = open(os.path.join(OUT, "case-studies/index.html"), encoding="utf-8", errors="replace").read()
n_case_links = len(re.findall(r'href="/case-studies/[a-z]{2,4}-\d{2}/"', hub))
print(f"case detail links on hub (static HTML): {n_case_links}")
print("by-industry anchor:", 'id="by-industry"' in hub, "| by-service anchor:", 'id="by-service"' in hub)

# internal link integrity on the hub + home: every href exists as dir/index.html
def check_links(page_path):
    txt = open(page_path, encoding="utf-8", errors="replace").read()
    hrefs = set(re.findall(r'href="(/[^"#]*)"', txt))
    bad = []
    for h in hrefs:
        if h.startswith("//") or "mailto:" in h:
            continue
        target = os.path.join(OUT, unquote(h).lstrip("/"))
        if h in ("/robots.txt", "/sitemap.xml", "/search"):
            ok = os.path.exists(os.path.join(OUT, h.strip("/"))) or os.path.exists(target)
        else:
            ok = os.path.exists(target)  # dir (with index.html) or file both fine
        if not ok:
            bad.append(h)
    return sorted(bad)

for page in ["case-studies/index.html", "index.html", "about-us/index.html", "services/index.html"]:
    bad = check_links(os.path.join(OUT, page))
    print(f"link check {page}: {len(bad)} broken", bad[:8] if bad else "")
sys.exit(1 if hits else 0)
