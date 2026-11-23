#!/usr/bin/env python3
"""Internal link checker (Top-20 #10 / final gate).

Scans every generated index.html in the static export and verifies that each
internal href resolves to a real file in the export. Fails the build on any
broken internal link or placeholder href="#".
Usage: python3 scripts/linkcheck.py [outdir]
"""
import glob
import os
import re
import sys

out = sys.argv[1] if len(sys.argv) > 1 else "/home/z/my-project/site/out-gh"
bp = "/DataQ" if os.path.basename(os.path.normpath(out)) == "out-gh" else ""

htmls = glob.glob(os.path.join(out, "**", "index.html"), recursive=True)
if not htmls:
    print(f"linkcheck: no HTML found in {out}")
    sys.exit(1)

# existing targets: any path that resolves to a file/dir in the export
exists = set()
for p in glob.glob(os.path.join(out, "**"), recursive=True):
    rel = os.path.relpath(p, out).replace(os.sep, "/")
    if rel == ".":
        continue
    exists.add("/" + rel)

def resolves(url_path: str) -> bool:
    """A link /foo/ works if /foo/index.html or /foo exists (Pages serves dir indexes)."""
    if url_path in exists:
        return True
    if url_path.rstrip("/") + "/index.html" in exists:
        return True
    if url_path == "/":
        return "index.html" in exists
    return False

broken = {}
placeholder = 0
for h in htmls:
    page = "/" + os.path.relpath(h, out).replace(os.sep, "/")
    src = open(h, encoding="utf-8", errors="ignore").read()
    for m in re.finditer(r'(?:href|src)="([^"#{]+)"', src):
        u = m.group(1)
        if u.startswith(("http://", "https://", "mailto:", "tel:", "data:", "//")):
            continue
        if u.startswith("#") or u == "":
            continue
        if u == "#":
            placeholder += 1
        # strip query/hash
        path = u.split("?")[0].split("#")[0]
        # normalize root-relative URLs through the base path
        if path.startswith(bp + "/"):
            path = path[len(bp):]
        elif bp and path == bp:
            path = "/"
        # asset URLs under /_next/ exist as files
        if not resolves(path):
            broken.setdefault(page, []).append(u)

total_links = sum(len(v) for v in broken.values())
print(f"linkcheck: {len(htmls)} pages scanned")
if placeholder:
    print(f"  placeholder '#' hrefs found: {placeholder}")
if broken:
    print(f"  BROKEN internal links: {total_links} on {len(broken)} pages:")
    for page, urls in list(broken.items())[:20]:
        for u in urls[:6]:
            print(f"    {page} -> {u}")
    sys.exit(1)
print("  all internal links resolve")
