#!/usr/bin/env python3
"""Compressed per-page digest (6-8 lines) + block-sequence skeleton fingerprint."""
import json
import os
from collections import Counter

SRC = "/home/z/my-project/site/src/content/pages"
OUT = "/home/z/my-project/audit"
DOMAINS = [
    "agentic-ai-hyperautomation", "applied-ai-generative-ai", "blockchain-digital-trust",
    "cloud-edge-platform-engineering", "cybersecurity-zero-trust", "data-analytics-lakehouse",
    "iot-digital-twin-robotics", "quantum-advanced-compute",
]


def clip(s, n=170):
    s = " ".join(str(s).split())
    return s[:n] + ("…" if len(s) > n else "")


def main():
    files = sorted(f for f in os.listdir(SRC) if f.startswith("services"))
    seqs = Counter()
    lines = []
    # hub + domain hubs
    d = json.load(open(os.path.join(SRC, "services.json"), encoding="utf-8"))
    lines.append("### /services/ hub")
    for b in d["blocks"]:
        bt = b.get("t")
        if bt == "h2":
            lines.append(f"H2: {clip(b.get('x'),90)} [sub: {clip(b.get('sub'),70)}]")
    lines.append("")

    for dom in DOMAINS:
        lines.append(f"### DOMAIN HUB: {dom}")
        dh = json.load(open(os.path.join(SRC, f"services_{dom}.json"), encoding="utf-8"))
        for b in dh["blocks"]:
            bt = b.get("t")
            if bt == "hero":
                lines.append(f"HERO.X: {clip(b.get('x'),230)}")
            elif bt == "h2":
                lines.append(f"H2: {clip(b.get('x'),90)} [sub: {clip(b.get('sub'),70)}]")
        lines.append("")
        for f in sorted(x for x in files if x.startswith(f"services_{dom}_")):
            pd = json.load(open(os.path.join(SRC, f), encoding="utf-8"))
            blocks = pd["blocks"]
            seq = "-".join(b.get("t", "?")[:4] for b in blocks)
            seqs[seq] += 1
            lines.append(f"--- {dom}/")
            lines.append("SLUG: " + f.replace(f"services_{dom}_", "").replace(".json", ""))
            for b in blocks[:3]:
                if b.get("t") == "hero":
                    lines.append("HERO.X: " + clip(b.get("x"), 230))
            h2s = [b for b in blocks if b.get("t") == "h2"]
            lines.append("H2s(" + str(len(h2s)) + "): " + " | ".join(clip(b.get("x"), 44) for b in h2s[:8]))
            for b in blocks:
                if b.get("t") == "idash":
                    kpis = b.get("kpis", [])
                    lines.append("KPI: " + "; ".join(f"{k.get('label')}={k.get('value')}" for k in kpis[:6]))
                    break
            arch = next((b for b in blocks if b.get("t") == "arch"), None)
            if arch:
                nodes = arch.get("nodes", [])
                lines.append("ARCH(" + str(len(nodes)) + "): " + "; ".join(
                    f"{n.get('label')}~{clip(n.get('sub',''),26)}" for n in nodes[:6]))
    open(os.path.join(OUT, "compact.txt"), "w", encoding="utf-8").write("\n".join(lines))
    print("compact.txt", os.path.getsize(os.path.join(OUT, "compact.txt")))

    lines2 = [f"== block-sequence fingerprints across {sum(seqs.values())} inner pages =="]
    for s, c in seqs.most_common(10):
        lines2.append(f"  {c}x  {s[:120]}")
    # deeper: positions of interactive blocks
    pos = Counter()
    for f in [x for x in files if x.count("_") >= 2]:
        pd = json.load(open(os.path.join(SRC, f), encoding="utf-8"))
        for i, b in enumerate(pd["blocks"]):
            if b.get("t") in ("arch", "idash", "chart", "explorer", "table", "cards"):
                pos[f"{i}:{b.get('t')}"] += 1
    lines2.append("\n== block position histogram (position:type -> count of 54) ==")
    for k, c in sorted(pos.items(), key=lambda kv: -kv[1])[:30]:
        lines2.append(f"  {c}/54  {k}")
    open(os.path.join(OUT, "skeleton.txt"), "w", encoding="utf-8").write("\n".join(lines2))
    print("skeleton.txt written")


if __name__ == "__main__":
    main()
