#!/usr/bin/env python3
"""Audit all Services pages: richness of arch/diagram/idash/chart/explorer blocks + interlinking."""
import os, json

PAGES = "/home/z/my-project/site/src/content/pages"
svc_files = sorted(f for f in os.listdir(PAGES) if f.startswith("services"))

HUBS = [
    "agentic-ai-hyperautomation", "applied-ai-generative-ai", "blockchain-digital-trust",
    "cloud-edge-platform-engineering", "cybersecurity-zero-trust", "data-analytics-lakehouse",
    "iot-digital-twin-robotics", "quantum-advanced-compute",
]

def arch_stats(b):
    nodes = b.get("nodes", [])
    edges = b.get("edges", []) or []
    with_sub = sum(1 for n in nodes if n.get("sub"))
    hot = sum(1 for n in nodes if n.get("hot"))
    edge_lbl = sum(1 for e in edges if e.get("label"))
    badges = b.get("badges") or []
    return len(nodes), with_sub, len(edges), edge_lbl, len(badges), hot

print(f"{'file':64s} {'archN':>5} {'sub':>4} {'edg':>4} {'elbl':>4} {'bdg':>4} {'hot':>4} {'idash':>5} {'tabs':>4} {'kpi':>4} {'chart':>5} {'expl':>4} {'inds':>4} {'rel':>4} {'ev':>3} words")
tot = dict(n=0, sub=0, edg=0, elbl=0, bdg=0, no_expl=0, no_idash=0)
for fn in svc_files:
    with open(os.path.join(PAGES, fn)) as fh:
        d = json.load(fh)
    archN = sub = edg = elbl = bdg = hot = 0
    idash = tabs = kpi = chart = expl = inds = 0
    for b in d.get("blocks", []):
        t = b.get("t")
        if t == "arch":
            archN, sub, edg, elbl, bdg, hot = arch_stats(b)
        elif t == "idash":
            idash = 1
            tabs = len(b.get("tabs") or [])
            kpi = len(b.get("kpis") or [])
        elif t == "chart":
            chart = 1
        elif t == "explorer":
            expl = 1
            inds = len(b.get("industries") or [])
    rel = len(d.get("related") or [])
    ev = len(d.get("evidence") or [])
    words = d.get("words", 0)
    is_hub = fn == "services.json" or (fn.endswith(".json") and fn.split("_")[1] in HUBS and fn.count("_") == 1)
    tag = "HUB " if is_hub else "    "
    tot["n"] += archN; tot["sub"] += sub; tot["edg"] += edg; tot["elbl"] += elbl; tot["bdg"] += bdg
    if not expl and not is_hub: tot["no_expl"] += 1
    if not idash and not is_hub: tot["no_idash"] += 1
    flag = ""
    if not is_hub:
        if archN and sub == 0: flag += " NOSUB"
        if archN and elbl == 0: flag += " NOELBL"
        if archN and bdg == 0: flag += " NOBDG"
        if not expl: flag += " NOEXPL"
        if not idash: flag += " NOIDASH"
    print(f"{tag}{fn:60s} {archN:>5} {sub:>4} {edg:>4} {elbl:>4} {bdg:>4} {hot:>4} {idash:>5} {tabs:>4} {kpi:>4} {chart:>5} {expl:>4} {inds:>4} {rel:>4} {ev:>3} {words:>5}{flag}")

print("\nTOTALS:", tot)
