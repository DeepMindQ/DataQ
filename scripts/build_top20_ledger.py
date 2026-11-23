#!/usr/bin/env python3
"""Top-20 execution ledger (gate deliverable, replaces the stale 500+ list).
Waves 0-7 recorded as delivered; Top-20 (2026-11-23) is the active queue."""
import sys, os, json
XLSX_SKILL_DIR = "/home/z/my-project/skills/xlsx"
for sub in [XLSX_SKILL_DIR, os.path.join(XLSX_SKILL_DIR, "templates")]:
    if sub not in sys.path: sys.path.insert(0, sub)
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

REG = json.load(open("/home/z/my-project/scripts/top20_register.json"))

wb = Workbook()

HDR_FILL = PatternFill("solid", fgColor="18142D")
ORANGE = PatternFill("solid", fgColor="FE5722")
OK_FILL = PatternFill("solid", fgColor="E8F5E9")
WIP_FILL = PatternFill("solid", fgColor="FFF3E0")
HDR_FONT = Font(color="FFFFFF", bold=True, size=10)
THIN = Border(bottom=Side(style="thin", color="DDDDDD"))

# ── Sheet 1: Top-20 active queue ────────────────────────────────────────────
ws = wb.active
ws.title = "Top-20 queue (active)"
headers = ["#", "Priority", "Area", "Change", "Why (evidence)", "Effort", "Status"]
widths = [5, 9, 14, 52, 52, 7, 16]
for c, (h, w) in enumerate(zip(headers, widths), 1):
    cell = ws.cell(row=1, column=c, value=h)
    cell.font = HDR_FONT; cell.fill = HDR_FILL
    cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.column_dimensions[get_column_letter(c)].width = w
r = 2
for item in REG["items"]:
    vals = [item["id"], item["priority"], item["area"], item["change"], item["why"], item["effort"], item["status"]]
    for c, v in enumerate(vals, 1):
        cell = ws.cell(row=r, column=c, value=v)
        cell.alignment = Alignment(vertical="top", wrap_text=True)
        cell.border = THIN
        if item["priority"] == "P0":
            cell.fill = WIP_FILL
    ws.cell(row=r, column=2).font = Font(bold=True, color="C2410C" if item["priority"] == "P0" else "374151")
    r += 1
ws.freeze_panes = "A2"

# ── Sheet 2: delivered waves ────────────────────────────────────────────────
ws2 = wb.create_sheet("Delivered (Waves 0-7)")
waves = [
    ("Wave 0+1", "Trust guards (E-20 lint) + homepage rebuild per change register", "Delivered"),
    ("Wave 2", "Services hub rebuild + baseline", "Delivered"),
    ("Wave 3", "Eight expertise hub rebuilds — unique architectures, consoles, FAQs, interlinking", "Delivered"),
    ("Wave 4", "All 54 service subpages rewritten — de-templated titles, 162 table captions, 270 FAQ JSON-LD, metas", "Delivered"),
    ("Wave 5-5d", "Homepage repositioned: IT-services & consulting brand voice (TCS/Infosys pattern), IP-differential section, de-numbered", "Delivered"),
    ("Wave 6", "Auto-load fix, hero 3-graph console, interactive charts, 100X motion, de-templated cases/insights, patent-deep platform pages", "Delivered"),
    ("Wave 7", "Who-we-are identity band, enterprise-systems strip (SAP/BI/HANA), Global Delivery band, RPA lifecycle", "Delivered"),
    ("Top-20 wave", "Search basePath fix, form fallbacks, domain repoint, per-section OG images, seeded visuals, CI pipeline, consent+analytics, a11y/motion parity, ledger", "This deploy"),
]
for c, (h, w) in enumerate(zip(["Wave", "Scope", "Status"], [12, 90, 12]), 1):
    cell = ws2.cell(row=1, column=c, value=h)
    cell.font = HDR_FONT; cell.fill = HDR_FILL
    ws2.column_dimensions[get_column_letter(c)].width = w
r = 2
for w_, scope, st in waves:
    ws2.cell(row=r, column=1, value=w_).font = Font(bold=True)
    ws2.cell(row=r, column=2, value=scope)
    c3 = ws2.cell(row=r, column=3, value=st); c3.fill = OK_FILL
    for c in range(1, 4):
        ws2.cell(row=r, column=c).alignment = Alignment(vertical="top", wrap_text=True)
    r += 1
ws2.freeze_panes = "A2"

# ── Sheet 3: verification evidence ──────────────────────────────────────────
ws3 = wb.create_sheet("Evidence (2026-11-23)")
ev = [
    ("Search broken live", "pagefind loader /pagefind/pagefind.js -> 404 on Pages; live query returned 0 results", "Fixed: basePath-aware import"),
    ("Forms dead", "NEXT_PUBLIC_FORM_ACCESS_KEY unset at export; ContactForm faked success", "Fixed: honest mailto fallback + env wiring"),
    ("Domain split-brain", "canonical/OG/sitemap/robots -> www.dataqsoft.com which serves a challenge interstitial; no CNAME on gh-pages", "Repointed identity to Pages URL; one-env flip back when domain attached"),
    ("OG images", "one default PNG for 727 pages on broken host", "38 branded per-section OG images + absolute-URL wiring"),
    ("Analytics", "consent UI offered but nothing loaded", "ConsentAnalytics: Plausible loads only after consent; search event instrumented"),
    ("Dead links", "footer LinkedIn/X/YouTube href='#'", "Removed until real profiles; Cookie settings control added"),
    ("Sitemap", "lastmod = build timestamp on all URLs", "git-derived lastmod.json (739 paths); 404 title fixed"),
    ("Images", "29 images for 727 pages; all cases/insights shared 2 images", "4 AI industry heroes + 148 seeded per-slug visuals + wiring"),
    ("CI", "manual token deploy, no validation", "GitHub Actions workflow + linkcheck + naming gate + consolidated export"),
    ("Homepage weight", "613 KB raw", "82 KB gzipped measured — acceptable; flight payload is SSR-inherent"),
    ("Motion", "duplicated CSS block; width animations; patchy reduced-motion", "Deduped; scaleX conversions; global parity blanket"),
    ("A11y", "charts announced bare titles", "Data-aware aria summaries on all 10 chart types"),
    ("Naming gate", "URL path /DataQ false-positives", "Deploy-path exception + out-gh HTML scan (--scan-out) in pipeline"),
]
for c, (h, w) in enumerate(zip(["Issue", "Evidence", "Resolution"], [24, 62, 56]), 1):
    cell = ws3.cell(row=1, column=c, value=h)
    cell.font = HDR_FONT; cell.fill = HDR_FILL
    ws3.column_dimensions[get_column_letter(c)].width = w
r = 2
for a, b, cc in ev:
    ws3.cell(row=r, column=1, value=a).font = Font(bold=True)
    ws3.cell(row=r, column=2, value=b)
    ws3.cell(row=r, column=3, value=cc).fill = OK_FILL
    for c in range(1, 4):
        ws3.cell(row=r, column=c).alignment = Alignment(vertical="top", wrap_text=True)
    r += 1
ws3.freeze_panes = "A2"

out = "/home/z/my-project/download/DataQ_Top20_ledger.xlsx"
os.makedirs(os.path.dirname(out), exist_ok=True)
wb.save(out)
print("saved", out)
