#!/usr/bin/env python3
"""Unfiltered scan of site/ for key strings: Platform Status, page counts, case study block, nav components, breakpoints."""
import os, re, json, sys

ROOT = "/home/z/my-project/site"
SKIP_DIRS = {"node_modules", ".next", ".next-export", "out", "out-gh", ".git"}

targets = {
    "platform_status": re.compile(r"Platform\s*Status", re.I),
    "page_count_menu": re.compile(r"\d+\s*pages?", re.I),
    "thirty_six": re.compile(r"Thirty-six\s+anonymized", re.I),
    "ranked_decisions": re.compile(r"Outcomes\s+surfaced\s+as\s+ranked", re.I),
    "diagnostic_baseline": re.compile(r"diagnostic\s+that\s+locked\s+each\s+baseline", re.I),
    "how_section_organized": re.compile(r"How\s+this\s+section\s+is\s+organized", re.I),
    "choosing_entry": re.compile(r"Choosing\s+an\s+entry\s+point", re.I),
    "exec_briefing": re.compile(r"Book\s+an\s+Executive\s+Briefing", re.I),
    "value_assessment": re.compile(r"Request\s+a\s+Value\s+Assessment", re.I),
    "case_studies_overview": re.compile(r"Case\s+Studies\s+Overview", re.I),
    "md_break": re.compile(r"md:|lg:|sm:"),
    "hamburger": re.compile(r"hamburger|menuOpen|mobileMenu|isMobile|useMediaQuery", re.I),
}

hits = {k: [] for k in targets}
exts = {".ts", ".tsx", ".js", ".jsx", ".json", ".css", ".md", ".mdx", ".html"}

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        ext = os.path.splitext(fn)[1].lower()
        if ext not in exts:
            continue
        p = os.path.join(dirpath, fn)
        try:
            with open(p, "r", encoding="utf-8", errors="replace") as f:
                for i, line in enumerate(f, 1):
                    for name, rx in targets.items():
                        if rx.search(line):
                            hits[name].append((p.replace(ROOT + "/", ""), i, line.strip()[:220]))
        except Exception:
            pass

for name in ["platform_status", "thirty_six", "ranked_decisions", "diagnostic_baseline",
             "how_section_organized", "choosing_entry", "exec_briefing", "value_assessment",
             "case_studies_overview"]:
    print(f"\n=== {name} ({len(hits[name])}) ===")
    for p, i, l in hits[name][:15]:
        print(f"  {p}:{i}: {l}")

print("\n=== hamburger/menu-related files (unique) ===")
files = sorted({p for p, i, l in hits["hamburger"]})
for f in files:
    print(" ", f)

print("\n=== page_count_menu sample (top-level src only) ===")
for p, i, l in hits["page_count_menu"]:
    if p.startswith("src/"):
        print(f"  {p}:{i}: {l}")
