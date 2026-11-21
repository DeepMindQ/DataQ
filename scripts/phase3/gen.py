#!/usr/bin/env python3
"""Phase 3 generator: applies domain packs to services JSON pages.

Transforms per page:
  1. explorer rebuild — industry hooks, KPI names/values, systems-in-scope, evidence links
  2. arch upgrades — node `sub` annotations (hot nodes + common labels), KPI badges
  3. deep section — new engineering-depth block group inserted before the CTA
  4. heading polish — old->new h2 replacements with deck sublines
QC report printed at end; idempotent (deep sections carry a marker id and are
replaced, not duplicated, on re-run).
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shared import INDUSTRIES, DOMAINS, domain_of, pick_value, stable_int, pick_word  # noqa: E402

PAGES = "/home/z/my-project/site/src/content/pages"
IND_NAME = dict(INDUSTRIES)
IND_SLUG = {v: k for k, v in IND_NAME.items()}
DEEP_MARK = "__deep__"

PACK_NAMES = [
    "pack_agentic",
    "pack_applied",
    "pack_blockchain",
    "pack_cloud",
    "pack_cyber",
    "pack_data",
    "pack_iot",
    "pack_quantum",
]


def load_packs():
    packs = {}
    for name in PACK_NAMES:
        try:
            mod = __import__(name)
            packs[mod.DOM] = mod
        except ModuleNotFoundError:
            print(f"[gen] pack {name} not present yet — skipped")
    return packs


def build_case_map():
    """cases[(dom_slug, ind_slug)] -> [(title, url), ...] ; cases_by_dom[dom] -> [(ind, title, url)]"""
    import re

    dom_by_name = {v: k for k, v in DOMAINS.items()}
    cases = {}
    by_dom = {}
    files = sorted(f for f in os.listdir(PAGES) if f.startswith("case-studies_") and f.endswith(".json"))
    for f in files:
        with open(os.path.join(PAGES, f)) as fh:
            d = json.load(fh)
        row_title = d.get("title", "")
        url = d.get("url")
        ind_slug = IND_SLUG.get(d.get("l2", ""))
        s = json.dumps(d)
        doms = set()
        for disp, slug in DOMAINS.items():
            if disp in s:
                doms.add(slug)
        for m in re.findall(r"/services/([a-z-]+)/", s):
            if m in DOMAINS:
                doms.add(m)
        for slug in doms:
            cases.setdefault((slug, ind_slug), []).append((row_title, url))
            by_dom.setdefault(slug, []).append((ind_slug, row_title, url))
    return cases, by_dom


def fmt_cents(v):
    return f"${v / 100:.2f}"


def rebuild_explorer(page_stem, dom, pack, b, cases):
    hooks = pack.HOOKS
    kpis = pack.KPIS
    sysm = getattr(pack, "SYSTEMS", {})
    changes = 0
    for ind in b.get("industries", []):
        slug = ind.get("slug")
        if slug in hooks:
            ind["hook"] = hooks[slug]
            changes += 1
        # KPIs: rebuild from pack spec with deterministic per-page values
        spec = kpis.get(slug)
        if spec:
            newk = []
            for (label, lo, hi, fmt) in spec:
                val = pick_value(page_stem, slug, label, lo, hi, fmt)
                newk.append({"label": label, "value": val})
            ind["kpis"] = newk
            changes += 1
        # systems-in-scope chips
        if slug in sysm:
            ind["systems"] = sysm[slug]
            changes += 1
        # evidence: 2 anonymized cases for (dom, industry)
        ev = cases.get((dom, slug), [])[:2]
        if ev:
            ind["evidence"] = [{"title": t, "url": u} for (t, u) in ev]
            changes += 1
    return changes


def apply_arch(page_stem, dom, pack, b):
    subs = pack.PAGES.get(page_stem, {}).get("archsubs", {})
    common = getattr(pack, "COMMON_SUBS", {})
    badges = pack.PAGES.get(page_stem, {}).get("badges", [])
    n_sub = 0
    for n in b.get("nodes", []):
        label = n.get("label", "")
        s = subs.get(label) or common.get(label)
        if s and not n.get("sub"):
            n["sub"] = s
            n_sub += 1
    if badges and not b.get("badges"):
        b["badges"] = [{"label": l, "value": v} for (l, v) in badges]
    return n_sub


def apply_deep(page_stem, pack, blocks):
    spec = pack.PAGES.get(page_stem, {}).get("deep")
    if not spec:
        return 0
    # remove previous deep group if re-run (every group block carries phase3_deep)
    kept = [b for b in blocks if b.get("t") != "__deep__" and not b.get("phase3_deep")]
    # legacy text-based removal (groups inserted before the marker scheme existed)
    para_set = set(spec.get("paras", []))
    note_x = spec.get("note", "")
    bullet_titles = {t for (t, _d) in spec.get("bullets", [])}
    out, skipping = [], False
    for b in kept:
        if b.get("t") == "h2" and b.get("x") == spec["h2"] and not b.get("phase3_deep"):
            skipping = True
            continue
        if skipping:
            if b.get("t") == "p" and b.get("x") in para_set:
                continue
            if b.get("t") == "note" and note_x and b.get("x") == note_x:
                continue
            if b.get("t") == "bullets" and any(it[0] in bullet_titles for it in b.get("items", [])):
                continue
            skipping = False
        out.append(b)
    blocks2 = out
    # find insert index: before last cta block
    idx = len(blocks2)
    for i in range(len(blocks2) - 1, -1, -1):
        if blocks2[i].get("t") == "cta":
            idx = i
            break
    group = [{"t": "h2", "x": spec["h2"], "sub": spec.get("sub", ""), "phase3_deep": True}]
    for p in spec.get("paras", []):
        group.append({"t": "p", "x": p, "phase3_deep": True})
    bl = spec.get("bullets")
    if bl:
        group.append({"t": "bullets", "items": bl, "phase3_deep": True})
    if spec.get("note"):
        group.append({"t": "note", "x": spec["note"], "phase3_deep": True})
    blocks2[idx:idx] = group
    blocks[:] = blocks2
    return 1


def apply_heads(page_stem, pack, blocks, report):
    heads = pack.PAGES.get(page_stem, {}).get("heads", {})
    found = set()
    hit = 0
    for b in blocks:
        if b.get("t") in ("h2", "h3"):
            x = b.get("x", "")
            if x in heads:
                new, deck = heads[x]
                b["x"] = new
                if deck:
                    b["sub"] = deck
                found.add(x)
                hit += 1
    miss = [old for old in heads if old not in found]
    return hit, miss


def bake_evidence(page_stem, dom, by_dom, page):
    """3 flagship-first cases for the ServiceNetwork section."""
    rows = by_dom.get(dom, [])
    if not rows:
        return []
    # prefer flagship industries, then stable order, distinct industries
    flagship = {"banking-financial-services", "insurance", "telecom-media", "logistics-supply-chain"}
    picked, seen = [], set()
    for weight in (1, 0):
        for ind, title, url in rows:
            if (ind in flagship) == bool(weight) and ind not in seen:
                picked.append({"title": title, "url": url, "ind": IND_NAME.get(ind, ind)})
                seen.add(ind)
            if len(picked) >= 3:
                break
        if len(picked) >= 3:
            break
    return picked


def main():
    packs = load_packs()
    cases, by_dom = build_case_map()
    files = sorted(f for f in os.listdir(PAGES) if f.endswith(".json") and f.startswith("services_"))
    qc = {"explorer_cells": 0, "arch_subs": 0, "arch_badges": 0, "deep": 0, "heads_hit": 0, "heads_miss": [], "evidence": 0}
    for f in files:
        stem = f[:-5]
        dom = domain_of(stem)
        pack = packs.get(dom)
        path = os.path.join(PAGES, f)
        with open(path) as fh:
            d = json.load(fh)
        if pack is None:
            continue
        for b in d.get("blocks", []):
            if b.get("t") == "explorer":
                qc["explorer_cells"] += rebuild_explorer(stem, dom, pack, b, cases)
            elif b.get("t") == "arch":
                qc["arch_subs"] += apply_arch(stem, dom, pack, b)
                qc["arch_badges"] += 1 if b.get("badges") else 0
        qc["deep"] += apply_deep(stem, pack, d.get("blocks", []))
        hit, miss = apply_heads(stem, pack, d.get("blocks", []), qc)
        qc["heads_hit"] += hit
        qc["heads_miss"].extend((f, m) for m in miss)
        ev = bake_evidence(stem, dom, by_dom, d)
        if ev and not d.get("evidence"):
            d["evidence"] = ev
            qc["evidence"] += 1
        with open(path, "w") as fh:
            json.dump(d, fh, indent=1, ensure_ascii=False)
            fh.write("\n")
    print("[gen] QC:", {k: v for k, v in qc.items() if k != "heads_miss"})
    for f, m in qc["heads_miss"]:
        print(f"[gen] HEAD MISS {f}: {m[:90]}")
    print("[gen] done")


if __name__ == "__main__":
    main()
