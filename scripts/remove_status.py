#!/usr/bin/env python3
"""Remove the fabricated /status/ page and every reference to it."""
import json, os, re, sys

SITE = "/home/z/my-project/site"

# 1. delete the page file
p = os.path.join(SITE, "src/content/pages/status.json")
if os.path.exists(p):
    os.remove(p)
    print("deleted src/content/pages/status.json")

def edit_json(path, fn):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    n = fn(data)
    if n:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        print(f"{path}: {n} change(s)")
    else:
        print(f"{path}: no change")

# 2. index.json — drop the row
def fix_index(data):
    before = len(data)
    data[:] = [r for r in data if r.get("url") != "/status/"]
    return before - len(data)
edit_json(os.path.join(SITE, "src/content/index.json"), fix_index)

# 3. nav.json — drop "System Status" child
def fix_nav(data):
    n = 0
    def walk(node):
        nonlocal n
        if isinstance(node, dict):
            if node.get("url") == "/status/" and "children" not in node:
                return True
            for k in list(node.keys()):
                v = node[k]
                if isinstance(v, list):
                    keep = []
                    for item in v:
                        if walk(item):
                            n += 1
                        else:
                            keep.append(item)
                    node[k] = keep
                elif isinstance(v, dict):
                    if walk(v):
                        del node[k]
                        n += 1
            return False
        return False
    walk(data)
    return n
edit_json(os.path.join(SITE, "src/content/nav.json"), fix_nav)

# 4. html-sitemap.json + legal pages — drop links to /status/
for name in ["html-sitemap.json", "privacy-policy.json", "terms-of-use.json",
             "cookie-policy.json", "accessibility.json"]:
    path = os.path.join(SITE, "src/content/pages", name)
    def strip(data):
        n = 0
        def walk(node):
            nonlocal n
            if isinstance(node, dict):
                for k in list(node.keys()):
                    v = node[k]
                    if isinstance(v, list):
                        keep = []
                        for item in v:
                            if isinstance(item, dict) and item.get("url") == "/status/":
                                n += 1
                            else:
                                walk(item)
                                keep.append(item)
                        node[k] = keep
                    elif isinstance(v, dict):
                        walk(v)
            return False
        walk(data)
        return n
    edit_json(path, strip)

# 5. SiteFooter.tsx — remove the Status link block
fp = os.path.join(SITE, "src/components/site/SiteFooter.tsx")
txt = open(fp, encoding="utf-8").read()
pat = re.compile(r'\n\s*<Link href="/status/"[^>]*>\s*\n?\s*Status\s*\n?\s*</Link>\s*', re.S)
new = pat.sub("\n", txt)
if new != txt:
    open(fp, "w", encoding="utf-8").write(new)
    print("SiteFooter.tsx: Status link removed")
else:
    print("SiteFooter.tsx: pattern not matched — manual fix needed")
    sys.exit(1)
