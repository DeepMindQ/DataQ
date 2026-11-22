#!/usr/bin/env python3
"""rename_towers — sweep remaining 'tower' wording out of content JSONs.

Services pages were rebuilt by p3/build.py with hand-written wording; this
script handles everything else (case studies, industries, home, nav, index,
platforms, solutions, insights...). Physical tower senses (cooling tower,
control tower, cell tower...) are protected — they are legitimate industry
terms and stay.
"""
import json
import os
import re

SITE = "/home/z/my-project/site"
PAGES = os.path.join(SITE, "src/content/pages")

_PROTECT = re.compile(
    r"(cooling[ -]towers?|cell[ -]towers?|control[ -]towers?|power[ -]towers?|transmission[ -]towers?|Control Tower|control tower)",
    re.I,
)

def detower(s):
    keep = []
    def _stash(m):
        keep.append(m.group(0))
        return f"\x00{len(keep)-1}\x00"
    s = _PROTECT.sub(_stash, s)
    s = s.replace("Deep Technology Towers", "Expertise Domains")
    s = s.replace("deep technology towers", "expertise domains")
    s = s.replace("deep-tech towers", "deep-tech expertise domains")
    s = s.replace("Tower — ", "Expertise — ")
    s = s.replace("tower overview", "domain overview")
    s = s.replace("Tower overview", "Domain overview")
    s = s.replace("towers", "domains")
    s = s.replace("Towers", "Domains")
    s = s.replace("tower", "domain")
    s = s.replace("Tower", "Domain")
    s = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], s)
    return s

def walk(obj, key=None):
    # never touch structural keys — template/file values are internal identifiers
    if key in ("template", "file") and isinstance(obj, str):
        return obj
    if isinstance(obj, str):
        return detower(obj)
    if isinstance(obj, list):
        return [walk(x) for x in obj]
    if isinstance(obj, dict):
        return {k: walk(v, k) for k, v in obj.items()}
    return obj

changed = 0
skipped_services = 0
for fn in os.listdir(PAGES):
    if not fn.endswith(".json"):
        continue
    p = os.path.join(PAGES, fn)
    raw = open(p, encoding="utf-8").read()
    # skip files whose only tower hits are protected phrases
    stripped = _PROTECT.sub("", raw)
    if "tower" not in stripped.lower() and "Tower" not in stripped:
        continue
    j = json.loads(raw)
    out = walk(j)
    new_raw = json.dumps(out, indent=1, ensure_ascii=False)
    if new_raw != raw:
        json.dump(out, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        changed += 1
print(f"pages changed: {changed}")

# nav.json + index.json (content root)
for extra in ["src/content/nav.json", "src/content/index.json"]:
    p = os.path.join(SITE, extra)
    raw = open(p, encoding="utf-8").read()
    stripped = _PROTECT.sub("", raw)
    if "tower" in stripped.lower() or "Tower" in stripped:
        j = json.loads(raw)
        json.dump(walk(j), open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print(f"cleaned: {extra}")

# final residual audit across live content + components
residual = []
for dirpath, dirnames, filenames in os.walk(os.path.join(SITE, "src")):
    dirnames[:] = [d for d in dirnames if not d.startswith("_backup")]
    for fn in filenames:
        if not fn.endswith((".json", ".tsx", ".ts")):
            continue
        p = os.path.join(dirpath, fn)
        txt = open(p, encoding="utf-8").read()
        stripped = _PROTECT.sub("", txt)
        n = len(re.findall(r"[Tt]ower", stripped))
        if n:
            residual.append((n, os.path.relpath(p, SITE)))
residual.sort(reverse=True)
print("\nresidual tower refs (excluding template key tower_hub and protected phrases):")
total = 0
for n, p in residual:
    txt = open(os.path.join(SITE, p), encoding="utf-8").read()
    allowed = "tower_hub" in txt  # internal template keys are fine
    total += n
    print(f"  {n:3d}  {p}{'  (template key only?)' if allowed else ''}")
print("TOTAL residual:", total)
