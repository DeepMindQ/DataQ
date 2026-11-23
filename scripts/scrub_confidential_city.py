#!/usr/bin/env python3
"""Emergency confidentiality scrub for the achala repo (Wave 9).

Removes every occurrence of the confidential delivery-city/locality from the
site source, replacing with meaning-preserving country-level wording:
  - "Hyderabad"            -> "India" (or richer rewrites per context)
  - "Nanakramguda"/street  -> dropped; addresses become country-level
  - "US — Hyderabad Corner"/"US — Hyderabad" -> restored "US — Tysons Corner"
     (undo of an earlier faulty brand replace)

After scrubbing, prints a verification count that must be ZERO.
"""
import re
import sys
from pathlib import Path

SITE = Path("/home/z/achala-src/site")

# (file-relative, old, new) — applied in order, exact-string replaces.
REPLACES: list[tuple[str, str, str]] = [
    # ── brand.json ──
    ("src/content/brand.json",
     "founded in Hyderabad, with global delivery from India, Germany and Bulgaria",
     "founded in India, with global delivery across Germany and Bulgaria"),
    ("src/content/brand.json",
     '"city": "Financial District, Nanakramguda, Hyderabad"',
     '"city": "India"'),
    # ── home.json ──
    ("src/content/pages/home.json",
     "founded in Hyderabad, with global delivery from India, Germany and Bulgaria",
     "founded in India, with global delivery across Germany and Bulgaria"),
    # ── about-us.json ──
    ("src/content/pages/about-us.json",
     "Hyderabad HQ with delivery teams in Munich and Sofia",
     "India HQ with delivery teams in Munich and Sofia"),
    ("src/content/pages/about-us.json",
     "Headquartered in Hyderabad with delivery teams in Munich and Sofia",
     "Headquartered in India with delivery teams in Munich and Sofia"),
    ("src/content/pages/about-us.json",
     '"Founded",      "2009, Hyderabad, India"',
     '"Founded",      "2009, India"'),
    ("src/content/pages/about-us.json",
     "Flexible delivery across Hyderabad, Munich and Sofia",
     "Flexible delivery across India, Munich and Sofia"),
    # ── careers pages ──
    ("src/content/pages/careers_benefits-development.json",
     "across global delivery centers in Hyderabad, Munich and Sofia",
     "across global delivery centers in India, Munich and Sofia"),
    ("src/content/pages/careers_open-positions.json",
     "across global delivery centers in Hyderabad, Munich and Sofia",
     "across global delivery centers in India, Munich and Sofia"),
    ("src/content/pages/careers_working-here.json",
     "Delivery hubs in Hyderabad, Munich, Sofia and our India execution core, working as one pod across",
     "Delivery hubs in India, Munich and Sofia, working as one pod across"),
    ("src/content/pages/careers_working-here.json",
     "across global delivery centers in Hyderabad, Munich and Sofia",
     "across global delivery centers in India, Munich and Sofia"),
    # ── contact.json ──
    ("src/content/pages/contact.json",
     "Contact Achala IT Solutions | Hyderabad · Munich · Sofia",
     "Contact Achala IT Solutions | India · Munich · Sofia"),
    ("src/content/pages/contact.json",
     "Achala IT Solutions Private Limited, Floor 10, 285 FD by Phoenix, Financial District, Nanakramguda, Hyderabad, Telangana 500089",
     "Achala IT Solutions Private Limited, India — Global Delivery Headquarters"),
    ("src/content/pages/contact.json",
     "Achala IT Solutions Private Limited, 3rd Floor, Plot No 342 & 343, Road Number 7, Kakateeya Hills, Hyderabad, Telangana 500081",
     "Achala IT Solutions Private Limited, India (Registered office)"),
    # ── global-offices.json ──
    ("src/content/pages/global-offices.json",
     "delivers from Hyderabad (India), Munich (Germany) and Sofia (Bulgaria)",
     "delivers from India, Munich (Germany) and Sofia (Bulgaria)"),
    ("src/content/pages/global-offices.json",
     "Achala IT Solutions Private Limited, Floor 10, 285 FD by Phoenix, Financial District, Nanakramguda, Hyderabad, Telangana 500089",
     "Achala IT Solutions Private Limited, India — Global Delivery Headquarters"),
    ("src/content/pages/global-offices.json",
     "3rd Floor, Plot No 342 & 343, Road Number 7, Kakateeya Hills, Hyderabad, Telangana 500081",
     "Achala IT Solutions Private Limited, India (Registered office)"),
    ("src/content/pages/global-offices.json",
     '"US — Hyderabad Corner"',
     '"US — Tysons Corner"'),
    # ── our-approach global delivery model ──
    ("src/content/pages/our-approach_global-delivery-model.json",
     '"US — Hyderabad"',
     '"US — Tysons Corner"'),
    # ── leadership pages (identical string in 8 files) ──
    ("src/content/pages/leadership_chief-ai-data-officer.json",
     "global delivery centers in Hyderabad, Munich and Sofia",
     "global delivery centers in India, Munich and Sofia"),
    ("src/content/pages/leadership_chief-commercial-officer.json",
     "global delivery centers in Hyderabad, Munich and Sofia",
     "global delivery centers in India, Munich and Sofia"),
    ("src/content/pages/leadership_chief-delivery-officer.json",
     "global delivery centers in Hyderabad, Munich and Sofia",
     "global delivery centers in India, Munich and Sofia"),
    ("src/content/pages/leadership_chief-executive-officer.json",
     "global delivery centers in Hyderabad, Munich and Sofia",
     "global delivery centers in India, Munich and Sofia"),
    ("src/content/pages/leadership_chief-financial-officer.json",
     "global delivery centers in Hyderabad, Munich and Sofia",
     "global delivery centers in India, Munich and Sofia"),
    ("src/content/pages/leadership_chief-people-officer.json",
     "global delivery centers in Hyderabad, Munich and Sofia",
     "global delivery centers in India, Munich and Sofia"),
    ("src/content/pages/leadership_chief-security-officer.json",
     "global delivery centers in Hyderabad, Munich and Sofia",
     "global delivery centers in India, Munich and Sofia"),
    ("src/content/pages/leadership_chief-technology-officer.json",
     "global delivery centers in Hyderabad, Munich and Sofia",
     "global delivery centers in India, Munich and Sofia"),
    # ── HomeView.tsx ──
    ("src/components/site/HomeView.tsx",
     "Hyderabad headquarters with delivery teams in Munich and Sofia",
     "India headquarters with delivery teams in Munich and Sofia"),
    ("src/components/site/HomeView.tsx",
     "deliver from Hyderabad (HQ), Munich and Sofia",
     "deliver from India (HQ), Munich and Sofia"),
]

BANNED = re.compile(r"(?i)hyderabad|nanakramguda|kakateeya")


def main() -> int:
    changed = 0
    for rel, old, new in REPLACES:
        p = SITE / rel
        if not p.exists():
            print(f"MISSING FILE: {rel}")
            continue
        s = p.read_text(encoding="utf-8")
        if old not in s:
            print(f"NOT FOUND in {rel}: {old[:70]}...")
            continue
        p.write_text(s.replace(old, new), encoding="utf-8")
        changed += 1
    print(f"replacements applied: {changed}/{len(REPLACES)}")

    # verification sweep
    leftover = []
    for root, dirs, files in SITE.walk():
        dirs[:] = [d for d in dirs if not d.startswith("_backup")]
        for f in files:
            if not f.endswith((".ts", ".tsx", ".json", ".css", ".md")):
                continue
            p = root / f
            s = p.read_text(encoding="utf-8", errors="ignore")
            n = len(BANNED.findall(s))
            if n:
                leftover.append((str(p.relative_to(SITE)), n))
    if leftover:
        print("LEFTOVER BANNED WORDS:")
        for rel, n in leftover:
            print(f"  {rel}: x{n}")
        return 1
    print("VERIFIED: zero confidential city/locality strings in site source.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
