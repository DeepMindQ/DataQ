#!/usr/bin/env python3
"""Shared builders for the Services deep-content generator.

Block dicts produced here match the Block union in
site/src/lib/content.ts, including the interactive `idash`
block rendered by DashSuite/DashWidgets (client components).

Page writer: loads the existing JSON (preserving all metadata fields
and the industry explorer block), replaces blocks wholesale, recounts
the word estimate, writes back.
"""
import json, os, re

PAGES_DIR = "site/src/content/pages"

# ── static text blocks ────────────────────────────────────────────────────
def hero(x): return {"t": "hero", "x": x}
def p(x): return {"t": "p", "x": x}
def h2(x): return {"t": "h2", "x": x}
def note(x): return {"t": "note", "x": x}
def cta(x): return {"t": "cta", "x": x}
def bullets(items): return {"t": "bullets", "items": items}
def table(caption, headers, rows): return {"t": "table", "caption": caption, "headers": headers, "rows": rows}

# ── interactive dashboard block ───────────────────────────────────────────
def kpi(label, value, delta=None, dir_=None, spark=None):
    d = {"label": label, "value": value}
    if delta: d["delta"] = delta
    if dir_: d["dir"] = dir_
    if spark: d["spark"] = spark
    return d

def idash(title, kpis_, tabs, badge=None, note_=None):
    b = {"t": "idash", "title": title, "kpis": kpis_, "tabs": tabs}
    if badge: b["badge"] = badge
    if note_: b["note"] = note_
    return b

def tab(name, widgets): return {"name": name, "widgets": widgets}

# ── widget builders (must match DashWidget union) ─────────────────────────
def w_line(title, cats, series, unit=None, yMax=None, note_=None):
    d = {"kind": "line", "title": title, "cats": cats, "series": series}
    if unit: d["unit"] = unit
    if yMax: d["yMax"] = yMax
    if note_: d["note"] = note_
    return d

def w_bar(title, cats, series, unit=None, yMax=None, note_=None):
    d = {"kind": "bar", "title": title, "cats": cats, "series": series}
    if unit: d["unit"] = unit
    if yMax: d["yMax"] = yMax
    if note_: d["note"] = note_
    return d

def w_radar(title, cats, series, yMax=100, note_=None):
    d = {"kind": "radar", "title": title, "cats": cats, "series": series, "yMax": yMax}
    if note_: d["note"] = note_
    return d

def w_heat(title, rows, cats, matrix, unit=None, note_=None):
    d = {"kind": "heat", "title": title, "rows": rows, "cats": cats, "matrix": matrix}
    if unit: d["unit"] = unit
    if note_: d["note"] = note_
    return d

def w_donut(title, cats, points, unit=None, note_=None):
    d = {"kind": "donut", "title": title, "cats": cats, "points": points}
    if unit: d["unit"] = unit
    if note_: d["note"] = note_
    return d

def w_gauge(title, items, note_=None):
    d = {"kind": "gauge", "title": title, "items": items}
    if note_: d["note"] = note_
    return d

def gauge_item(name, value, max_, unit, warn=None, crit=None):
    d = {"name": name, "value": value, "max": max_, "unit": unit}
    if warn is not None: d["warn"] = warn
    if crit is not None: d["crit"] = crit
    return d

def w_slo(title, target, windowDays, traffic, errPct, note_=None):
    d = {"kind": "slo", "title": title, "target": target, "windowDays": windowDays,
         "traffic": traffic, "errPct": errPct}
    if note_: d["note"] = note_
    return d

def w_sim(title, params, outputs, curve=None, note_=None):
    d = {"kind": "sim", "title": title, "params": params, "outputs": outputs}
    if curve: d["curve"] = curve
    if note_: d["note"] = note_
    return d

def sim_param(name, min_, max_, step, value, unit):
    return {"name": name, "min": min_, "max": max_, "step": step, "value": value, "unit": unit}

def sim_out(name, unit, formula, good=None, bad=None):
    d = {"name": name, "unit": unit, "formula": formula}
    if good is not None: d["good"] = good
    if bad is not None: d["bad"] = bad
    return d

def sim_curve(param, output, label):
    return {"param": param, "output": output, "label": label}

def w_flow(title, stages, note_=None):
    d = {"kind": "flow", "title": title, "stages": stages}
    if note_: d["note"] = note_
    return d

def flow_stage(name, role, detail, metrics):
    return {"name": name, "role": role, "detail": detail, "metrics": metrics}

def fm(label, value): return {"label": label, "value": value}

def w_arch(title, lanes, nodes, edges, note_=None):
    d = {"kind": "arch", "title": title, "lanes": lanes, "nodes": nodes, "edges": edges}
    if note_: d["note"] = note_
    return d

def arch_node(id_, lane, label, detail, hot=False):
    d = {"id": id_, "lane": lane, "label": label, "detail": detail}
    if hot: d["hot"] = True
    return d

def edge(a, b, label=None):
    d = {"a": a, "b": b}
    if label: d["label"] = label
    return d

def w_table(title, headers, rows, note_=None):
    d = {"kind": "table", "title": title, "headers": headers, "rows": rows}
    if note_: d["note"] = note_
    return d

def w_scatter(title, points, groups, xLabel, yLabel, xMax=None, yMax=None, note_=None):
    d = {"kind": "scatter", "title": title, "points": points, "groups": groups,
         "xLabel": xLabel, "yLabel": yLabel}
    if xMax: d["xMax"] = xMax
    if yMax: d["yMax"] = yMax
    if note_: d["note"] = note_
    return d

def sc_pt(x, y, label, group): return {"x": x, "y": y, "label": label, "group": group}

# ── page writer ───────────────────────────────────────────────────────────
def write_page(fname, blocks, wordfloor=0):
    """Preserve page metadata + explorer block; replace everything else."""
    path = os.path.join(PAGES_DIR, fname)
    old = json.load(open(path))
    keep_explorer = None
    for b in old.get("blocks", []):
        if isinstance(b, dict) and b.get("t") == "explorer":
            keep_explorer = b
            break
    new_blocks = []
    for b in blocks:
        if b is None:
            continue
        if b.get("t") == "explorer":
            if keep_explorer is not None:
                new_blocks.append(keep_explorer)
            continue
        new_blocks.append(b)
    old["blocks"] = new_blocks
    words = sum(len(str(b.get("x", "")).split()) for b in new_blocks if isinstance(b.get("x"), str))
    for b in new_blocks:
        if b.get("t") == "bullets":
            words += sum(len(str(a).split()) + len(str(c).split()) for a, c in b.get("items", []))
        if b.get("t") == "table":
            words += sum(len(str(c).split()) for r in b.get("rows", []) for c in r)
        if b.get("t") == "idash":
            for k in b.get("kpis", []):
                words += len(str(k.get("label", "")).split()) + len(str(k.get("delta", "")).split())
            for t in b.get("tabs", []):
                for w in t.get("widgets", []):
                    words += len(str(w.get("title", "")).split()) + len(str(w.get("note", "") or "").split())
    old["words"] = max(words, wordfloor)
    json.dump(old, open(path, "w"), indent=1, ensure_ascii=False)
    return old["words"]
