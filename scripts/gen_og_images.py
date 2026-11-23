#!/usr/bin/env python3
"""Generate branded per-section OpenGraph images (1200x630) for Dataq Software.

Brand system: deep navy #18142D field, orange #FE5722 accent, dot-grid texture,
geometric arc motif. Wordmark drawn as text (no SVG rasterization dependency).
Output: site/public/og/<name>.png  (~40-90 KB each, palette-optimized PNG).
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = "/home/z/my-project/site/public/og"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
BOOK = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY_TOP = (24, 20, 45)      # 18142D
NAVY_BOT = (42, 31, 77)      # deep violet-navy
ORANGE = (254, 87, 34)       # FE5722
WHITE = (255, 255, 255)

W, H = 1200, 630

SECTIONS = [
    # (file, eyebrow, title lines)
    ("home", "DATAQ SOFTWARE", ["Enterprise AI, data and", "automation — delivered", "against a signed baseline."]),
    ("services", "SERVICES & CONSULTING", ["The expertise your next", "move needs — under one", "accountable delivery system."]),
    ("services-applied-ai-generative-ai", "SERVICES", ["Applied AI &", "Generative AI"]),
    ("services-agentic-ai-hyperautomation", "SERVICES", ["Agentic AI &", "Hyperautomation"]),
    ("services-data-analytics-lakehouse", "SERVICES", ["Data, Analytics", "& Lakehouse"]),
    ("services-cybersecurity-zero-trust", "SERVICES", ["Cybersecurity", "& Zero-Trust"]),
    ("services-cloud-edge-platform-engineering", "SERVICES", ["Cloud, Edge &", "Platform Engineering"]),
    ("services-quantum-advanced-compute", "SERVICES", ["Quantum &", "Advanced Compute"]),
    ("services-blockchain-digital-trust", "SERVICES", ["Blockchain", "& Digital Trust"]),
    ("services-iot-digital-twin-robotics", "SERVICES", ["IoT, Digital Twin", "& Robotics"]),
    ("consulting", "CONSULTING", ["Consulting that ends", "in delivery"]),
    ("industries", "INDUSTRIES", ["Built where you operate —", "under the rules you", "are held to."]),
    ("industries-banking-financial-services", "INDUSTRIES", ["Banking &", "Financial Services"]),
    ("industries-insurance", "INDUSTRIES", ["Insurance & Risk"]),
    ("industries-healthcare-life-sciences", "INDUSTRIES", ["Healthcare &", "Life Sciences"]),
    ("industries-manufacturing", "INDUSTRIES", ["Manufacturing", "& Industrial"]),
    ("industries-retail-consumer-goods", "INDUSTRIES", ["Retail &", "Consumer Goods"]),
    ("industries-telecom-media", "INDUSTRIES", ["Telecom, Media &", "Entertainment"]),
    ("industries-energy-utilities", "INDUSTRIES", ["Energy & Utilities"]),
    ("industries-logistics-supply-chain", "INDUSTRIES", ["Logistics &", "Supply Chain"]),
    ("industries-public-sector", "INDUSTRIES", ["Public Sector", "& Government"]),
    ("industries-education-research", "INDUSTRIES", ["Education & Research"]),
    ("industries-technology-saas", "INDUSTRIES", ["Technology & SaaS"]),
    ("industries-agriculture-food", "INDUSTRIES", ["Agriculture &", "Food Systems"]),
    ("solutions", "SOLUTIONS", ["Programs built around", "one business metric"]),
    ("platforms", "PLATFORMS", ["Eight proprietary platforms —", "the productized form of", "patented delivery IP."]),
    ("platforms-nexus", "PLATFORMS", ["Dataq Nexus", "Decision Intelligence Hub"]),
    ("platforms-forge", "PLATFORMS", ["Dataq Forge", "Data & Lakehouse Engineering"]),
    ("platforms-swarm", "PLATFORMS", ["Dataq Swarm", "Agentic AI Orchestration"]),
    ("platforms-sentinel", "PLATFORMS", ["Dataq Sentinel", "Zero-Trust & AI Security"]),
    ("platforms-twinverse", "PLATFORMS", ["Dataq Twinverse", "Digital Twin & IoT Intelligence"]),
    ("platforms-quanta", "PLATFORMS", ["Dataq Quanta", "Quantum & Advanced Compute"]),
    ("platforms-ledger", "PLATFORMS", ["Dataq Ledger", "Distributed Trust & Tokenization"]),
    ("platforms-compass", "PLATFORMS", ["Dataq Compass", "Responsible AI & Governance"]),
    ("case-studies", "EVIDENCE", ["Engagement notes with the", "measured delta attached."]),
    ("insights", "INSIGHTS", ["From the delivery floor —", "practitioner theses, no noise."]),
    ("company", "THE COMPANY", ["Consulting, build and run —", "one accountable partner."]),
    ("patented-intelligence", "PATENTED INTELLIGENCE", ["Eight patented method families,", "in production inside the", "platforms."]),
]


def base_canvas():
    img = Image.new("RGB", (W, H), NAVY_TOP)
    dr = ImageDraw.Draw(img)
    # vertical gradient
    for y in range(H):
        t = y / H
        c = tuple(int(a + (b - a) * t) for a, b in zip(NAVY_TOP, NAVY_BOT))
        dr.line([(0, y), (W, y)], fill=c)
    # dot grid
    for gy in range(30, H, 44):
        for gx in range(30, W, 44):
            dr.ellipse([gx, gy, gx + 2, gy + 2], fill=(255, 255, 255, 8))
    # arc motif bottom-right (concentric quarter arcs, orange + white, faint)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    for i, (r, col) in enumerate([(340, ORANGE), (420, (255, 255, 255)), (500, ORANGE), (580, (255, 255, 255))]):
        a = 90 if i % 2 == 0 else 40
        ld.arc([W - r, H - r // 2 - 60, W + r, H + r - 60], start=200, end=340, fill=col + (a,), width=5)
    layer = layer.filter(ImageFilter.GaussianBlur(0.6))
    img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    return img


def fit_title(lines, max_w, max_size=76, min_size=46):
    size = max_size
    while size > min_size:
        f = ImageFont.truetype(BOLD, size)
        if all(f.getlength(l) <= max_w for l in lines):
            return f, size
        size -= 2
    return ImageFont.truetype(BOLD, min_size), min_size


def gen(name, eyebrow, lines):
    img = base_canvas()
    dr = ImageDraw.Draw(img)

    # wordmark: "dataq" + orange dot + "software"
    f_mark = ImageFont.truetype(BOLD, 34)
    x, y = 72, 64
    dr.text((x, y), "dataq", font=f_mark, fill=WHITE)
    wq = f_mark.getlength("dataq")
    dr.ellipse([x + wq + 8, y + 24, x + wq + 22, y + 38], fill=ORANGE)
    dr.text((x + wq + 34, y), "software", font=f_mark, fill=(255, 255, 255, 200))

    # eyebrow
    f_eye = ImageFont.truetype(BOLD, 20)
    ey = 250
    dr.rectangle([72, ey + 2, 78, ey + 22], fill=ORANGE)
    dr.text((92, ey), eyebrow, font=f_eye, fill=ORANGE)

    # title
    f_t, sz = fit_title(lines, max_w=1010, max_size=68 if len(lines) > 2 else 78)
    ty = 300 if len(lines) >= 3 else 320
    lh = int(sz * 1.24)
    for i, l in enumerate(lines):
        dr.text((72, ty + i * lh), l, font=f_t, fill=WHITE)

    # footer hairline + descriptor
    dr.line([(72, H - 88), (W - 72, H - 88)], fill=(255, 255, 255, 26), width=1)
    f_f = ImageFont.truetype(BOOK, 17)
    dr.text((72, H - 70), "IT services · consulting · business solutions", font=f_f, fill=(255, 255, 255, 130))
    msg = "Patented delivery IP · Every program measured on a signed baseline"
    dr.text((W - 72 - f_f.getlength(msg), H - 70), msg, font=f_f, fill=(255, 255, 255, 110))

    # palette-optimized PNG
    img.quantize(colors=200, method=Image.MEDIANCUT).save(
        os.path.join(OUT, name + ".png"), optimize=True
    )


def main():
    os.makedirs(OUT, exist_ok=True)
    for row in SECTIONS:
        gen(*row)
    print(f"generated {len(SECTIONS)} OG images -> {OUT}")


if __name__ == "__main__":
    main()
