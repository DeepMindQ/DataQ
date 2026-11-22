#!/usr/bin/env python3
"""Per-page JSON digest: hero, heading flow, first paragraph, idash KPIs,
arch nodes, tabs, related, evidence — for the content audit."""
import json
import os
from collections import Counter

SRC = "/home/z/my-project/site/src/content/pages"
OUT = "/home/z/my-project/audit"

DOMAIN_ORDER = [
    "agentic-ai-hyperautomation",
    "applied-ai-generative-ai",
    "blockchain-digital-trust",
    "cloud-edge-platform-engineering",
    "cybersecurity-zero-trust",
    "data-analytics-lakehouse",
    "iot-digital-twin-robotics",
    "quantum-advanced-compute",
]


def clip(s, n=200):
    s = " ".join(str(s).split())
    return s[:n] + ("…" if len(s) > n else "")


def digest_page(path, lines):
    d = json.load(open(path, encoding="utf-8"))
    slug = d.get("id", os.path.basename(path))
    lines.append(f"\n{'='*88}\n== {slug}")
    for b in d["blocks"]:
        bt = b.get("t")
        if bt == "hero":
            lines.append(f"HERO.T: {clip(b.get('t2') or b.get('title') or '', 120)}")
            lines.append(f"HERO.X: {clip(b.get('x'), 320)}")
        elif bt == "h2":
            lines.append(f"H2: {clip(b.get('x'), 110)}   [sub: {clip(b.get('sub'), 90)}]")
        elif bt == "p":
            lines.append(f"   ¶ {clip(b.get('x'), 150)}")
        elif bt == "idash":
            kpis = b.get("kpis", [])
            ks = "; ".join(f"{k.get('label')}={k.get('value')}" for k in kpis[:6])
            lines.append(f"IDASH: title={clip(b.get('title'),70)} | tabs={b.get('tabs')}")
            lines.append(f"   KPI: {ks}")
        elif bt == "arch":
            nodes = b.get("nodes", [])
            edges = b.get("edges", [])
            ns = "; ".join(f"{n.get('label')}({clip(n.get('sub',''),36)})" for n in nodes[:9])
            es = "; ".join(f"{e.get('label','')}" for e in edges[:8] if e.get("label"))
            lines.append(f"ARCH: {clip(b.get('title'),70)} | nodes={len(nodes)} edges={len(edges)}")
            lines.append(f"   N: {ns}")
            if es:
                lines.append(f"   E: {es}")
            lines.append(f"   badges: {b.get('badges')}")
        elif bt == "cards":
            cs = b.get("items") or b.get("cards") or []
            lines.append(f"CARDS[{len(cs)}]: " + " | ".join(clip(c.get("t") or c.get("title"), 42) for c in cs[:6]))
        elif bt == "table":
            rows = b.get("rows", [])
            lines.append(f"TABLE: {clip(b.get('caption'),80)} rows={len(rows)} first={clip(rows[0][0] if rows and rows[0] else '',60)}")
    rel = d.get("related", [])
    lines.append(f"RELATED[{len(rel)}]: " + " | ".join(r.get("label") or r.get("title") or "?" for r in rel[:11]))
    ev = d.get("evidence")
    if isinstance(ev, list):
        lines.append(f"EVIDENCE[{len(ev)}]: " + " | ".join(clip(e.get("title") or e.get("t"), 60) for e in ev[:3]))
    else:
        lines.append(f"EVIDENCE: {clip(ev, 100)}")


def main():
    files = sorted(f for f in os.listdir(SRC) if f.startswith("services"))
    # group by domain
    hub = [f for f in files if f == "services.json"]
    hubs = {dom: f"services_{dom}.json" for dom in DOMAIN_ORDER}
    subs = {}
    for dom in DOMAIN_ORDER:
        subs[dom] = sorted(f for f in files if f.startswith(f"services_{dom}_"))
    # one big file per domain (hub file includes services.json digest first)
    for dom in DOMAIN_ORDER:
        lines = []
        digest_page(os.path.join(SRC, "services.json"), lines)
        digest_page(os.path.join(SRC, hubs[dom]), lines)
        for s in subs[dom]:
            digest_page(os.path.join(SRC, s), lines)
        out = os.path.join(OUT, f"j__{dom}.txt")
        open(out, "w", encoding="utf-8").write("\n".join(lines))
        print(dom, os.path.getsize(out))
    # homepage
    hp = os.path.join(SRC, "home.json")
    if os.path.exists(hp):
        lines = []
        digest_page(hp, lines)
        open(os.path.join(OUT, "j__home.txt"), "w", encoding="utf-8").write("\n".join(lines))
        print("home", os.path.getsize(os.path.join(OUT, "j__home.txt")))
    # heading-frequency metric across inner pages
    h2c = Counter()
    subpages = [f for f in files if f.count("_") >= 2]
    for f in subpages:
        d = json.load(open(os.path.join(SRC, f), encoding="utf-8"))
        for b in d["blocks"]:
            if b.get("t") == "h2":
                h2c[" ".join(str(b.get("x")).split())] += 1
    lines = [f"== H2 headings shared across the {len(subpages)} inner pages =="]
    for h, c in h2c.most_common(30):
        lines.append(f"  {c}/{len(subpages)}  {h}")
    open(os.path.join(OUT, "h2freq.txt"), "w", encoding="utf-8").write("\n".join(lines))
    print("h2freq.txt written")


if __name__ == "__main__":
    main()
