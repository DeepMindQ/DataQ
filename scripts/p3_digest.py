#!/usr/bin/env python3
"""Compact per-page digest of every services page for the content audit.
Captures the user skim-path: hero, section headings, first paragraph after each
heading, KPI tiles, arch node labels+subs, tab names, CTA lines."""
import html as htmlmod
import os
import re

ROOT = "/home/z/my-project/site/out-gh"
OUT = "/home/z/my-project/audit"
CAP = 300  # chars per paragraph


def read(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


def blockify(s):
    s = re.sub(r"<script[\s\S]*?</script>", " ", s, flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s, flags=re.I)
    s = re.sub(r"<svg[\s\S]*?</svg>", " ", s, flags=re.I)
    return s


def digest(path, label, lines):
    if not os.path.exists(path):
        lines.append(f"!! MISSING {path}")
        return
    s = blockify(read(path))
    # hero
    m = re.search(r"<h1[^>]*>([\s\S]*?)</h1>", s)
    h1 = re.sub(r"<[^>]+>", " ", m.group(1)) if m else "(no h1)"
    lines.append(f"\n{'#'*84}\n# {label}\n{'#'*84}")
    lines.append("H1: " + " ".join(htmlmod.unescape(h1).split()))
    # subtitle: first <p> after h1
    tail = s[m.end():] if m else s
    mp = re.search(r"<p[^>]*>([\s\S]*?)</p>", tail)
    if mp:
        sub = re.sub(r"<[^>]+>", " ", mp.group(1))
        lines.append("SUB: " + " ".join(htmlmod.unescape(sub).split())[:CAP * 2])
    # kpi tiles (label/value pairs in dash tiles)
    kpis = re.findall(r'class="[^"]*kpiLabel[^"]*"[^>]*>([\s\S]*?)<', s)
    kvals = re.findall(r'class="[^"]*kpiValue[^"]*"[^>]*>([\s\S]*?)<', s)
    if kpis:
        pairs = [f"{a.strip()}={b.strip()}" for a, b in zip(kpis, kvals)][:8]
        lines.append("KPI: " + "; ".join(pairs))
    # tabs
    tabs = re.findall(r'class="[^"]*tabBtn[^"]*"[^>]*>\s*([^<]{2,40})', s)
    if tabs:
        lines.append("TABS: " + " | ".join(t.strip() for t in tabs[:10]))
    # section headings + first paragraph after each
    for hm in re.finditer(r"<h2[^>]*>([\s\S]*?)</h2>([\s\S]{0,2600}?)((?=<h2)|$)", s):
        h2 = " ".join(htmlmod.unescape(re.sub(r"<[^>]+>", " ", hm.group(1))).split())
        body = hm.group(2)
        pm = re.search(r"<p[^>]*>([\s\S]*?)</p>", body)
        para = ""
        if pm:
            para = " ".join(htmlmod.unescape(re.sub(r"<[^>]+>", " ", pm.group(1))).split())[:CAP]
        lines.append(f"H2: {h2}")
        if para:
            lines.append(f"   ¶ {para}")
    # arch node labels with subs
    nodes = re.findall(r'data-node[^>]*>|class="archNode[^"]*"[\s\S]{0,400}?</div>', s)
    nl = re.findall(r'archNLab[^>]*>([^<]{2,60})<[\s\S]{0,200}?archNSub[^>]*>([^<]{2,80})<', s)
    if nl:
        lines.append("ARCH nodes: " + " ; ".join(f"{a} [{b}]" for a, b in nl[:10]))
    # cta-ish lines
    ctas = re.findall(r"<a[^>]*>([^<]{3,60})</a>", s)
    interesting = [c.strip() for c in ctas if re.search(r"book|brief|assess|contact|talk|start", c, re.I)][:4]
    if interesting:
        lines.append("CTA: " + " | ".join(interesting))
    # word count of visible text
    txt = " ".join(htmlmod.unescape(re.sub(r"<[^>]+>", " ", s)).split())
    lines.append(f"(words≈{len(txt.split())})")


def main():
    svc = os.path.join(ROOT, "services")
    domains = sorted(d for d in os.listdir(svc) if os.path.isdir(os.path.join(svc, d)))
    for d in domains:
        dpath = os.path.join(svc, d)
        lines = []
        digest(os.path.join(svc, "index.html"), "/services/ (hub)", lines)
        digest(os.path.join(dpath, "index.html"), f"/services/{d}/ (hub)", lines)
        for s2 in sorted(x for x in os.listdir(dpath) if os.path.isdir(os.path.join(dpath, x))):
            digest(os.path.join(dpath, s2, "index.html"), f"/services/{d}/{s2}/", lines)
        out = os.path.join(OUT, f"d__{d}.txt")
        with open(out, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(d, os.path.getsize(out))


if __name__ == "__main__":
    main()
