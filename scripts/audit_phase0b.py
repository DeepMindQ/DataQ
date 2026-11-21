#!/usr/bin/env python3
"""Phase-0 audit part 2: clean numbers, nav structure, per-template depth."""
import glob, json, os, re, collections, statistics

ROOT = "/home/z/my-project/site"
jroot = f"{ROOT}/src/content"
page_jsons = []
for j in glob.glob(f"{jroot}/**/*.json", recursive=True):
    if "_backup" in j: continue
    try: d = json.load(open(j, encoding="utf-8"))
    except Exception: continue
    if isinstance(d, dict) and d.get("template") and "blocks" in d:
        page_jsons.append((j, d))
print("LIVE PAGE JSONS:", len(page_jsons))

def block_words(d):
    txt = []
    for b in d.get("blocks", []):
        if isinstance(b, dict):
            for v in b.values():
                if isinstance(v, str): txt.append(v)
                elif isinstance(v, list): txt.extend(x for x in v if isinstance(x, str))
    for c in d.get("cards", []) or []:
        if isinstance(c, dict): txt.append(str(c.get("h",""))+" "+str(c.get("x","")))
    return len(re.findall(r"\w+", " ".join(txt)))

# per-template word stats
bytpl = collections.defaultdict(list)
for j, d in page_jsons:
    bytpl[d["template"]].append(block_words(d))
print("\nWORDS BY TEMPLATE (median / p10 / min):")
for t, ws in sorted(bytpl.items(), key=lambda kv: statistics.median(kv[1])):
    ws.sort()
    print(f"   {t:22s} n={len(ws):4d}  median={statistics.median(ws):6.0f}  p10={ws[len(ws)//10]:5.0f}  min={ws[0]:4d}  max={ws[-1]}")

# block-type histogram
bt = collections.Counter()
for j, d in page_jsons:
    types = set(b.get("t") for b in d.get("blocks", []) if isinstance(b, dict))
    for t in types: bt[t] += 1
print("\nPAGES USING EACH BLOCK TYPE:", dict(bt.most_common()))

# cards inside blocks
cardh = collections.Counter()
cards_per = []
for j, d in page_jsons:
    n = 0
    titles = []
    for b in d.get("blocks", []):
        if isinstance(b, dict):
            for key in ("cards", "items", "list"):
                for c in (b.get(key) or []):
                    if isinstance(c, dict) and c.get("h"):
                        n += 1; titles.append(str(c["h"]).strip().lower())
    cards_per.append(n)
    for t in set(titles): cardh[t] += 1
print("\nCARDS PER PAGE  median:", statistics.median(cards_per), "max:", max(cards_per))
print("TOP REPEATED CARD TITLES:")
for h, c in cardh.most_common(15): print(f"   x{c}: {h[:60]}")

# nav.json structure
nav = json.load(open(f"{jroot}/nav.json", encoding="utf-8"))
def walk(o, pre=""):
    if isinstance(o, dict):
        return {k: walk(v, pre+"/"+k) for k, v in list(o.items())[:12]}
    if isinstance(o, list):
        return [f"list[{len(o)}]"] + ([walk(o[0])] if o else [])
    return o
prim = nav.get("primary", [])
print("\nNAV PRIMARY:", len(prim))
for it in prim:
    mega = it.get("mega") or []
    kids = 0
    for c in mega:
        ch = c.get("children") or c.get("items") or []
        kids += len(ch)
    print(f"   {it.get('label','?'):16s} mega_cols={len(mega)} children={kids}")
    for c in mega[:2]:
        ch = c.get("children") or c.get("items") or []
        print(f"      col '{c.get('label','?')[:44]}' -> {len(ch)} children")

# JSON byte sizes of built pages = weight proxy
sizes = [os.path.getsize(p) for p in glob.glob(f"{ROOT}/out-gh/**/index.html", recursive=True)]
sizes.sort()
print("\nHTML KB  median:", int(statistics.median(sizes)/1024), "p90:", int(sizes[9*len(sizes)//10]/1024), "max:", int(sizes[-1]/1024))
# _next asset weight
js_assets = glob.glob(f"{ROOT}/out-gh/_next/static/chunks/*.js")
tot = sum(os.path.getsize(a) for a in js_assets)
print("JS chunks:", len(js_assets), "total MB:", round(tot/1048576, 2))
css_assets = glob.glob(f"{ROOT}/out-gh/_next/static/chunks/*.css")
print("CSS:", len(css_assets), "total KB:", round(sum(os.path.getsize(a) for a in css_assets)/1024))
img_assets = glob.glob(f"{ROOT}/out-gh/images/**/*", recursive=True)
print("images:", len([i for i in img_assets if os.path.isfile(i)]), "total MB:", round(sum(os.path.getsize(i) for i in img_assets if os.path.isfile(i))/1048576, 2))
