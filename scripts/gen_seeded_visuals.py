#!/usr/bin/env python3
"""Seeded per-page visuals for case studies and insights (Top-20 #8).

Deterministic abstract brand compositions — navy field, brand-safe accents,
motif vocabulary (arcs, node mesh, orbit rings, bar field, flow ribbons) mixed
by slug seed so every one of the 116 case studies and 32 insights gets a
distinct-but-family visual. Palette-quantized PNG keeps each file ~20-40 KB.

Output: site/public/images/gen/case-<slug>.png, insight-<slug>.png
"""
import math
import os
import random
import re
import sys
from PIL import Image, ImageDraw, ImageFilter

GEN = "/home/z/my-project/site/public/images/gen"
W, H = 1344, 576  # matches 21:9 hero crop comfortably

NAVY_TOP = (24, 20, 45)
NAVY_BOT = (43, 32, 80)
ORANGE = (254, 87, 34)
ACCENTS = [
    (254, 87, 34),    # brand orange
    (245, 166, 35),   # amber
    (46, 196, 182),   # teal
    (124, 111, 240),  # violet
    (255, 255, 255),  # white
]

# case-slug industry prefix -> preferred accent index
PREF = {
    "bank": 3, "ins": 2, "hc": 1, "mfg": 0, "ret": 1, "tel": 2,
    "en": 0, "log": 2, "edu": 1, "pub": 3, "tech": 2, "agr": 1,
}


def slug_list(kind):
    """kind: 'case' or 'insight' — slugs from content filenames."""
    pages = "/home/z/my-project/site/src/content/pages"
    out = []
    for f in os.listdir(pages):
        if kind == "case" and f.startswith("case-studies_"):
            out.append(f[len("case-studies_"):-len(".json")])
        if kind == "insight" and f.startswith("insights_"):
            out.append(f[len("insights_"):-len(".json")])
    return sorted(out)


def base(seed_bg):
    img = Image.new("RGB", (W, H), NAVY_TOP)
    dr = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = tuple(int(a + (b - a) * t) for a, b in zip(NAVY_TOP, NAVY_BOT))
        dr.line([(0, y), (W, y)], fill=c)
    # dot grid with seeded phase
    rnd = random.Random(seed_bg)
    ox, oy = rnd.randint(0, 40), rnd.randint(0, 40)
    for gy in range(oy, H, 46):
        for gx in range(ox, W, 46):
            dr.ellipse([gx, gy, gx + 2, gy + 2], fill=(255, 255, 255))
    return img, dr


def motif_arcs(dr, rnd, accent, dims):
    cx, cy = rnd.randint(int(W * 0.55), int(W * 0.9)), rnd.randint(int(H * 0.25), int(H * 0.8))
    r0 = rnd.randint(90, 150)
    n = rnd.randint(4, 7)
    for i in range(n):
        r = r0 + i * rnd.randint(28, 46)
        a0 = rnd.randint(140, 220)
        a1 = a0 + rnd.randint(60, 140)
        col = accent if i % 2 == 0 else (255, 255, 255)
        alpha = rnd.randint(70, 150)
        dr.arc([cx - r, cy - r, cx + r, cy + r], start=a0, end=a1, fill=_mix(col, alpha), width=rnd.choice([3, 4, 6]))


def motif_mesh(dr, rnd, accent, dims):
    pts = [(rnd.randint(60, W - 60), rnd.randint(60, H - 60)) for _ in range(rnd.randint(9, 14))]
    for i, (x, y) in enumerate(pts):
        for x2, y2 in pts[i + 1:]:
            if abs(x - x2) < 300 and abs(y - y2) < 220 and random.Random(x * 7 + y * 13 + x2).random() < 0.6:
                dr.line([(x, y), (x2, y2)], fill=_mix(accent, 60), width=1)
    for x, y in pts:
        r = rnd.randint(3, 7)
        dr.ellipse([x - r, y - r, x + r, y + r], fill=_mix(accent, rnd.randint(120, 210)))


def motif_orbits(dr, rnd, accent, dims):
    cx, cy = W // 2 + rnd.randint(-180, 180), H // 2 + rnd.randint(-80, 80)
    for i in range(rnd.randint(3, 5)):
        rx = 120 + i * rnd.randint(55, 85)
        ry = int(rx * rnd.uniform(0.42, 0.62))
        ang = rnd.randint(0, 90)
        box = [cx - rx, cy - ry, cx + rx, cy + ry]
        dr.arc(box, ang, ang + 200, fill=_mix((255, 255, 255), 80), width=2)
        dr.arc(box, ang + 210, ang + 360, fill=_mix(accent, 110), width=3)
        # planet on the ring
        px = cx + int(rx * math.cos(math.radians(ang + rnd.randint(0, 360))))
        py = cy + int(ry * math.sin(math.radians(ang + rnd.randint(0, 360))))
        dr.ellipse([px - 7, py - 7, px + 7, py + 7], fill=_mix(accent, 220))


def motif_bars(dr, rnd, accent, dims):
    n = rnd.randint(14, 22)
    x0 = rnd.randint(40, 140)
    gap = rnd.randint(26, 44)
    base_h = rnd.randint(40, 90)
    for i in range(n):
        h = int(base_h * rnd.uniform(0.4, 2.6))
        x = x0 + i * gap
        col = accent if (i + dims) % 3 else (255, 255, 255)
        alpha = rnd.randint(90, 190)
        dr.rounded_rectangle([x, H - 60 - h, x + gap - 10, H - 60], radius=4, fill=_mix(col, alpha))


def motif_ribbon(dr, rnd, accent, dims):
    y0 = rnd.randint(int(H * 0.25), int(H * 0.6))
    pts = []
    x = -40
    while x < W + 40:
        pts.append((x, y0 + math.sin((x / W) * math.pi * rnd.uniform(2, 4) + dims) * rnd.randint(30, 70)))
        x += 14
    for off, alpha, wd in [(0, 150, 4), (26, 90, 2), (-26, 90, 2)]:
        dr.line([(px, py + off) for px, py in pts], fill=_mix(accent if off == 0 else (255, 255, 255), alpha), width=wd)


def motif_pillars(dr, rnd, accent, dims):
    n = rnd.randint(5, 8)
    x0 = rnd.randint(80, 220)
    for i in range(n):
        x = x0 + i * rnd.randint(90, 130)
        h = rnd.randint(int(H * 0.2), int(H * 0.55))
        col = accent if i % 2 == 0 else (255, 255, 255)
        dr.rectangle([x, H - 60 - h, x + rnd.randint(14, 26), H - 60], fill=_mix(col, rnd.randint(50, 110)))
        dr.ellipse([x - 8, H - 60 - h - 8, x + 8, H - 60 - h + 8], fill=_mix(ORANGE, 180))


MOTIFS = [motif_arcs, motif_mesh, motif_orbits, motif_bars, motif_ribbon, motif_pillars]


def _mix(col, alpha):
    """Blend a color toward the navy field for faux-transparency on RGB canvas."""
    t = alpha / 255.0
    return tuple(int(c * t + b * (1 - t)) for c, b in zip(col, (31, 26, 56)))


def compose(slug, kind):
    rnd = random.Random(f"{kind}:{slug}")
    prefix = slug.split("-")[0]
    accent = ACCENTS[PREF.get(prefix, 0)] if kind == "case" else ACCENTS[rnd.randint(0, 3)]
    img, dr = base(f"{kind}:{slug}")
    k = rnd.randint(2, 3)
    motifs = rnd.sample(MOTIFS, k)
    for i, m in enumerate(motifs):
        m(dr, rnd, accent if i % 2 == 0 or k == 1 else (255, 255, 255), dims=rnd.randint(0, 6))
    # bottom-left delta signature — three rising marks in brand orange
    for i in range(3):
        h = 18 + i * 14
        dr.rounded_rectangle([64 + i * 26, H - 70 - h, 64 + i * 26 + 14, H - 70], radius=3, fill=_mix(ORANGE, 170 - i * 30))
    img.quantize(colors=64, method=Image.MEDIANCUT).save(
        os.path.join(GEN, f"{kind}-{slug}.png"), optimize=True
    )


def main():
    os.makedirs(GEN, exist_ok=True)
    cases, insights = slug_list("case"), slug_list("insight")
    for s in cases:
        compose(s, "case")
    for s in insights:
        compose(s, "insight")
    print(f"seeded visuals: {len(cases)} cases + {len(insights)} insights -> {GEN}")


if __name__ == "__main__":
    sys.exit(main())
