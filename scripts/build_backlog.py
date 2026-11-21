#!/usr/bin/env python3
"""Build the Dataq Software website 50%-target change backlog workbook.

Sheets:
  1. Overview        - audit snapshot, completed-this-round, phase plan (live COUNTIF), 50% definition
  2. Backlog         - 500+ change items (ID, Phase, Workstream, Item, Where, DoD, Impact, Effort, Status)
  3. Naming-Conf     - naming + confidentiality sweep log and rules
  4. Homepage Charts - current chart issues vs target spec (design-before-develop artifact)
"""
import sys, os

XLSX_SKILL_DIR = "/home/z/my-project/skills/xlsx"
for sub in [XLSX_SKILL_DIR, os.path.join(XLSX_SKILL_DIR, "templates")]:
    if sub not in sys.path:
        sys.path.insert(0, sub)

SCRIPTS = "/home/z/my-project/scripts"
if SCRIPTS not in sys.path:
    sys.path.insert(0, SCRIPTS)

from base import *  # noqa: F401,F403  (design tokens + helpers)
import base
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter

from backlog_core_home import P0, P1, P9
from backlog_charts_nav import P2, P3, P7
from backlog_content_visual import P4, P5
from backlog_motion_seo import P6, P8, P3X, P2X, P1X, P10
from backlog_extra import P1E, P3E, P5E, P7E, P8E, P4E

base.use_palette_explicit("warm")

OUT = "/home/z/my-project/download/Dataq-Software-Website-50pct-Change-Backlog.xlsx"

ROWS = (P0 + P1 + P9 + P2 + P3 + P7 + P4 + P5 + P6 + P8
        + P3X + P2X + P1X + P10 + P1E + P3E + P5E + P7E + P8E + P4E)

# order by phase then keep original order inside phase
PHASE_ORDER = {p: i for i, p in enumerate(
    ["P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"])}
ROWS = sorted(ROWS, key=lambda r: PHASE_ORDER.get(r[0], 99))
for i, r in enumerate(ROWS, 1):
    pass  # ids assigned at write time

wb = Workbook()

# ---------------------------------------------------------------- helpers
def write_table(ws, start_row, headers, data, title=None, widths=None, note=None):
    """Write a titled table starting at B<start_row>; returns next free row."""
    r = start_row
    if title:
        c = ws.cell(row=r, column=2, value=title)
        c.font = font_subheader()
        c.alignment = Alignment(horizontal="left", vertical="center")
        ws.row_dimensions[r].height = 24
        r += 1
    hr = r
    for ci, h in enumerate(headers, start=2):
        ws.cell(row=hr, column=ci, value=h)
    style_header_row(ws, row_num=hr, col_start=2, col_end=1 + len(headers))
    r += 1
    for idx, row in enumerate(data):
        for ci, v in enumerate(row, start=2):
            ws.cell(row=r, column=ci, value=v)
        style_data_row(ws, row_num=r, col_start=2, col_end=1 + len(headers), row_index=idx)
        r += 1
    if note:
        c = ws.cell(row=r + 0, column=2, value=note)
        c.font = font_caption()
        r += 1
    return r + 1, hr

def set_widths(ws, widths):
    for col, w in widths.items():
        ws.column_dimensions[col].width = w

# ---------------------------------------------------------------- Sheet 2: Backlog (built first so Overview formulas resolve)
ws = wb.active
ws.title = "Backlog"
HEADERS = ["ID", "Phase", "Workstream", "Change item", "Where (file / component / cluster)",
           "Acceptance criteria (definition of done)", "Impact", "Effort", "Status"]
LAST = 1 + len(HEADERS)
setup_sheet(ws, title="Dataq Software website - change backlog to the 50% target (541 items)", last_col=LAST)

for ci, h in enumerate(HEADERS, start=2):
    ws.cell(row=4, column=ci, value=h)
style_header_row(ws, row_num=4, col_start=2, col_end=LAST)

r = 5
for idx, row in enumerate(ROWS):
    phase, wsname, item, where, dod, impact, effort, *rest = row
    status = rest[0] if rest else ""
    status = status or "Pending"
    values = [f"BG-{idx + 1:03d}", phase, wsname, item, where, dod, impact, effort, status]
    for ci, v in enumerate(values, start=2):
        ws.cell(row=r, column=ci, value=v)
    style_data_row(ws, row_num=r, col_start=2, col_end=LAST, row_index=idx)
    r += 1

total_row = r
ws.cell(row=total_row, column=2, value="Total")
ws.cell(row=total_row, column=3, value=f"{len(ROWS)} items")
ws.cell(row=total_row, column=5, value="All phases P0-P10")
ws.cell(row=total_row, column=7, value=f"{sum(1 for x in ROWS if (x[7] if len(x) > 7 else '') == 'Done')} done / {len(ROWS) - sum(1 for x in ROWS if (x[7] if len(x) > 7 else '') == 'Done')} open")
style_total_row(ws, row_num=total_row, col_start=2, col_end=LAST)

set_widths(ws, {"A": 3, "B": 9, "C": 8, "D": 22, "E": 58, "F": 30, "G": 46, "H": 9, "I": 8, "J": 10})
ws.freeze_panes = "C5"
ws.auto_filter.ref = f"B4:{get_column_letter(LAST)}{total_row - 1}"

# status conditional formatting: Done -> positive, Pending -> neutral (no fill)
rng = f"J5:J{total_row - 1}"
ws.conditional_formatting.add(rng, FormulaRule(
    formula=['$J5="Done"'], fill=PatternFill("solid", fgColor="E8F5E9"),
    font=Font(name=FONT_NAME, color=ACCENT_POSITIVE)))
ws.conditional_formatting.add(rng, FormulaRule(
    formula=['$J5=""'], fill=None))

# wrap long text columns
for row in range(5, total_row):
    for col in ("D", "E", "F", "G"):
        ws[f"{col}{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    ws[f"B{row}"].alignment = Alignment(horizontal="right", vertical="top")
    for col in ("C", "H", "I", "J"):
        ws[f"{col}{row}"].alignment = Alignment(horizontal="center", vertical="top")

# ---------------------------------------------------------------- Sheet 1: Overview
ov = wb.create_sheet("Overview", 0)
setup_sheet(ov, title="Dataq Software website - roadmap to the 50% target", last_col=7)

snapshot = [
    ["Content pages (JSON)", "633 pages / 13,992 content blocks (avg 22.1 per page)"],
    ["Built HTML pages", "639 pages exported + pagefind index (7,962 words)"],
    ["AI-tell: identical epigram bullets", "541 pages share the same '[Label] - punchline' pattern"],
    ["AI-tell: shared hero formula", "462 pages start with the same broken hero pattern"],
    ["Internal link health", "avg 7.42 related links/page; 7 pages have zero related links"],
    ["Container width today", "1280px - leaves wide empty margins on 1366/1920 screens"],
    ["Homepage charts today", "3 charts: div-based bars with no axes, line chart with a single y-label, static donut; unequal card heights"],
    ["Brand naming before sweep", "2,375 'DataQ Soft' forms + 3,193 bare 'DataQ' tokens across 1,258 files"],
    ["Brand naming after sweep", "0 hits in source (src + docs) and 0 hits across 3,827 built files; 64,198 'Dataq Software' instances in build"],
    ["Confidentiality (patent source)", "0 mentions of applicant entity / inventor / applicant city in source and built output; internal KB anonymized"],
]
r_next, hr1 = write_table(ov, 4, ["Audit metric", "Value"], snapshot, title="Where we are (audit snapshot)")
set_widths(ov, {"A": 3, "B": 34, "C": 96})
for row in range(hr1 + 1, r_next - 1):
    ov[f"C{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    ov[f"B{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

done_now = [
    ["1", "Brand naming sweep: 'Dataq Software' everywhere, abbreviation banned (scripts/fix_naming.py)", "1,258 files changed; verified 0 remaining"],
    ["2", "Patent-source confidentiality scrub (site + internal KB anonymized)", "0 confidentiality tokens in source + build"],
    ["3", "Header fit-guard built into export and verified on built site at 1366px", "nav fits, burger hidden, document overflow 0"],
    ["4", "Static export rebuilt + pagefind re-indexed", "639 pages, STATIC EXPORT OK"],
    ["5", "Build verification scripts (naming + confidentiality)", "scripts/verify_build_naming.py - green"],
    ["6", "Audit scripts (naming, clusters, content tells)", "scripts/audit_naming.py, audit_clusters.py, content_audit.py"],
]
r_next, hr2 = write_table(ov, r_next, ["#", "Completed in this round", "Result"],
                          done_now, title="Completed in this round")
for row in range(hr2 + 1, r_next - 1):
    ov[f"C{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

phases = [
    ["P0", "Trust & integrity: naming rule, confidentiality rule, legal pages, CI scans"],
    ["P1", "Homepage rebuild: CXO hero, steering-pack charts, 9 sections, motion, full-width density"],
    ["P2", "Chart & visualization system: ChartFrame v2, axes/tooltips/footnotes, 12 new chart types, per-template mapping"],
    ["P3", "Navigation & IA: mega menu redesign, header/drawer v2, in-page TOC, footer, search"],
    ["P4", "Content overhaul 100%: engine rules, 633-page cluster rewrites, cross-linking system, new blocks, SEO copy"],
    ["P5", "Imagery, icons & architecture diagrams: 48-icon set, DiagramFrame, 8 tower + 12 industry diagrams"],
    ["P6", "Motion system: tokens, Reveal v2, choreography, micro-interactions, quality gates"],
    ["P7", "Layout & density: container 1360, grids, typography, whitespace system, 1920/2560 passes"],
    ["P8", "SEO / A11y / Perf: schema, unique metas, WCAG AA, Lighthouse >=90 x4, budgets"],
    ["P9", "QA infrastructure: audit scripts, screenshot diffs, browser matrix, definition of 50%"],
    ["P10", "Execution plan: 10 batches, cadence, estimates, risks, 50% gate review"],
]
phase_rows = []
r_start_phases = r_next + 2  # title + header + rows
for i, (pid, focus) in enumerate(phases):
    rr = r_start_phases + 1 + i
    phase_rows.append([pid, focus,
                       f'=COUNTIF(Backlog!C:C,"{pid}")',
                       f'=COUNTIFS(Backlog!C:C,"{pid}",Backlog!J:J,"Done")'])
r_next, hr3 = write_table(ov, r_next, ["Phase", "Focus", "Items", "Done"], phase_rows,
                          title="Phase plan (live counts from the Backlog sheet)")
for rr in range(hr3 + 1, r_next - 1):
    ov[f"C{rr}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    ov[f"D{rr}"].alignment = Alignment(horizontal="center")
    ov[f"E{rr}"].alignment = Alignment(horizontal="center")
ov.column_dimensions["E"].width = 10
ov.column_dimensions["D"].width = 10

tot = r_next - 1
ov.cell(row=tot, column=2, value="Total")
ov.cell(row=tot, column=4, value=f"=SUM(D{hr3 + 1}:D{tot - 1})")
ov.cell(row=tot, column=5, value=f"=SUM(E{hr3 + 1}:E{tot - 1})")
style_total_row(ov, row_num=tot, col_start=2, col_end=7)
ov[f"D{tot}"].alignment = Alignment(horizontal="center")
ov[f"E{tot}"].alignment = Alignment(horizontal="center")

def50 = [
    ["D1", "100% of 633 pages: rewritten hero, 600+ word body (template norm), 0 banned phrases"],
    ["D2", "Every service/solution/industry/platform/method page: >=2 business visuals answering a stated CXO question"],
    ["D3", "Interlink density: >=3 contextual inline links + >=6 related links per content page; 0 orphans"],
    ["D4", "Lighthouse >=90 (Perf/A11y/BestPractices/SEO) on home + 6 template goldens at 4G"],
    ["D5", "Header fits at 1280/1366/1440/1920 on Chrome + Edge + Safari (fit-guard verified)"],
    ["D6", "633/633 unique SEO titles + meta descriptions; schema validates"],
    ["D7", "Motion tokens sitewide; reduced-motion honored; 60fps scroll on goldens"],
    ["D8", "'Dataq Software' naming CI green; confidentiality CI green; zero banned tokens in build"],
    ["D9", "Equal-height chart/diagram cards everywhere; no ragged grid bottoms at 1366/1920"],
    ["D10", "Homepage: every section states and answers a named CXO question; signed design review"],
]
r_next, hr4 = write_table(ov, r_next, ["#", "Measurable acceptance criterion"], def50,
                          title="Definition of '50% of the expected website' (measurable)")
for row in range(hr4 + 1, r_next - 1):
    ov[f"C{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

c = ov.cell(row=r_next, column=2,
            value="Brand rule: the name is 'Dataq Software' in every string - 'DataQ Soft' and bare 'DataQ' are banned. "
                  "Confidentiality rule: the patent applicant entity, its city and any inventor are never named; capabilities only.")
c.font = font_caption()
ov.merge_cells(start_row=r_next, start_column=2, end_row=r_next, end_column=7)
ov.row_dimensions[r_next].height = 26
c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

# ---------------------------------------------------------------- Sheet 3: Naming & Confidentiality
nc = wb.create_sheet("Naming & Confidentiality")
setup_sheet(nc, title="Naming + confidentiality sweep log", last_col=4)
passes = [
    ["Pass 1", "'DataQ Soft' (not followed by 'ware') -> 'Dataq Software'", "2,375 replacements"],
    ["Pass 2", "'DataQSoft' (joined form) -> 'Dataq Software'", "0 found"],
    ["Pass 3", "bare 'DataQ' (word-bounded) -> 'Dataq'", "3,193 replacements"],
    ["Coverage", "site/src + site/public + docs (ts, tsx, js, json, css, md, svg, html)", "1,258 files changed"],
    ["Verification (source)", "re-scan src + docs", "0 abbreviations, 0 bare 'DataQ', 2,376 full-name instances"],
    ["Verification (build)", "scan of out/: html, xml, txt, json (3,827 files)", "0 abbreviations, 0 bare 'DataQ' in visible text, 64,198 full-name instances"],
    ["Confidentiality (source)", "Strategemist / Pisupati / Shanker scan of src + docs", "0 hits (internal KB title + applicant line rewritten and anonymized)"],
    ["Confidentiality (build)", "same scan across 3,827 built files", "0 hits"],
]
r_next, hr5 = write_table(nc, 4, ["Step", "Scope", "Result"], passes,
                          title="What was swept and verified this round")
set_widths(nc, {"A": 3, "B": 26, "C": 60, "D": 46})
for row in range(hr5 + 1, r_next - 1):
    nc[f"C{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    nc[f"D{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

rules = [
    ["R1", "Name = 'Dataq Software' in every user-visible string; abbreviation 'DataQ Soft' and mixed 'DataQ' are banned. Lowercase domains/emails (dataqsoft.com) are unchanged."],
    ["R2", "Logo letterforms already read lowercase 'dataq software' - the graphic is untouched; only aria/alt/meta text was corrected."],
    ["R3", "The patent applicant entity, its city, any inventor and filing details are never named on the site or in client material. Families are referenced as 'our research programme' / 'patented method families' / by capability."],
    ["R4", "Indirect capability mapping is allowed and encouraged: 8 method families mapped into services, solutions and industries copy - capability language only."],
    ["R5", "CI scans (naming + confidentiality) run on source and built output for every release; any hit fails the build."],
]
r_next, hr6 = write_table(nc, r_next, ["#", "Rule going forward"], rules,
                          title="Rules going forward")
for row in range(hr6 + 1, r_next - 1):
    nc[f"C{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
nc.column_dimensions["B"].width = 8
nc.column_dimensions["C"].width = 110

# ---------------------------------------------------------------- Sheet 4: Homepage chart spec
cs = wb.create_sheet("Homepage Charts")
setup_sheet(cs, title="Homepage charts - current issues and target specification (design before develop)", last_col=6)
issues = [
    ["I1", "Bar chart has no y-axis, no gridlines, no unit axis - bars are HTML divs", "DataVisuals.tsx BarChart (div-based)", "SVG bars with axis ticks, gridlines, unit title, hover tooltips"],
    ["I2", "Line chart shows a single y-axis label (the max value) - reads like a sketch", "DataVisuals.tsx LineArea", "Ticks both axes, target band, crosshair + value bubble"],
    ["I3", "No tooltips or hover interaction anywhere", "all charts", "Tooltip singleton per chart per P2 spec"],
    ["I4", "Mixed rendering (HTML bars vs SVG lines) - inconsistent baselines and paddings", "BarChart vs LineArea", "Everything SVG inside one ChartFrame v2"],
    ["I5", "Unequal card heights in the 3-up row (fixed 210px canvas + different legends)", "HomeView output band", "Equal-height grid contract + height tokens (240/320/420)"],
    ["I6", "Donut shows bare percentages with no business scale", "HomeDonut", "Composition bar with $-mapped legend"],
    ["I7", "Hero 'decision mesh' is decorative nodes with no meaning", "hero NetworkGraph", "Executive Outcome Console: rotating industry scenarios with metric tickers"],
    ["I8", "No source/assumption footnotes - charts look like invented client data", "all", "Mandatory footnote slot in ChartFrame v2"],
]
r_next, hr7 = write_table(cs, 4, ["#", "Current issue", "Where", "Target"], issues,
                          title="What is wrong today (code-level evidence)")
set_widths(cs, {"A": 3, "B": 6, "C": 52, "D": 34, "E": 46})
for row in range(hr7 + 1, r_next - 1):
    for col in ("C", "D", "E"):
        cs[f"{col}{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

targets = [
    ["V1", "Decision latency: baseline vs day-90 by process", "Are decisions actually faster?", "Grouped bar v2", "Hover per bar, delta callout", "H-320"],
    ["V2", "Autonomous resolution ramp vs committed band", "Does the ramp hold against the target?", "Line v2 + band", "Crosshair, point values", "H-320"],
    ["V3", "Value composition ($-mapped)", "Where does the money land?", "Stacked composition bar", "Segment legend with $ ranges", "H-320"],
    ["V4", "Gate report table mock", "What does the steering pack look like?", "Styled table", "Row hover; tabular numerals", "H-320"],
    ["V5", "Value-creation waterfall across gates", "How does value compound?", "Waterfall", "Step hover, bridge values", "H-420 hero band"],
    ["V6", "Cost-of-delay curve", "What does waiting 90/180 days cost?", "Two-series area", "Delta callout animated", "H-420 hero band"],
    ["V7", "Maturity-to-outcome quadrant", "Where are we on the map?", "Scatter quadrant", "Hover stage definitions", "P1 backlog"],
    ["V8", "Risk-exposure bullet strip", "Is control coverage improving?", "Bullet bars x4 domains", "Target/actual readout", "P1 backlog"],
]
r_next, hr8 = write_table(cs, r_next, ["#", "Visual", "CXO question it answers", "Type", "Interaction", "Size token"],
                          targets, title="Target visual set for the homepage")
for row in range(hr8 + 1, r_next - 1):
    for col in ("C", "D", "E", "F", "G"):
        cs[f"{col}{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

tokens = [
    ["T1", "Height tokens: compact 240 / standard 320 / hero 420 px; no raw heights elsewhere"],
    ["T2", "Y-axis: 4-6 nice-number ticks, unit in axis title, zero baseline; gridlines horizontal only"],
    ["T3", "Tooltips: single per chart, label + value + unit + delta; touch: tap to show, tap to dismiss"],
    ["T4", "Footnote: 'Illustrative composite - replaced by your baseline at value assessment' on every chart"],
    ["T5", "A11y: role=img + sr-only data table; focusable points; contrast AA on navy and white"],
    ["T6", "Animation: axes -> series -> annotations, 120ms stagger, one-shot, reduced-motion instant"],
]
r_next, hr9 = write_table(cs, r_next, ["#", "Chart system token / rule"], tokens,
                          title="Chart system tokens (apply site-wide)")
for row in range(hr9 + 1, r_next - 1):
    cs[f"C{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
cs.column_dimensions["B"].width = 8
cs.column_dimensions["C"].width = 110

wb.properties.creator = "Z.ai"
wb.save(OUT)

# ---------------------------------------------------------------- verification
from openpyxl import load_workbook
wb2 = load_workbook(OUT)
counts = {s: wb2[s].max_row for s in wb2.sheetnames}
backlog_items = sum(1 for row in range(5, total_row) if wb2["Backlog"][f"B{row}"].value)
print("saved:", OUT)
print("sheets:", counts)
print("backlog item rows:", backlog_items)
assert backlog_items >= 500, "need 500+ items"
print("OK: 500+ items")
