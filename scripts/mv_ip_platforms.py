#!/usr/bin/env python3
"""Move the patents (IP differential) + platforms sections up, so the homepage reads:
services -> consulting -> IP differential -> platforms -> evidence -> charter -> industries."""
P = "site/src/components/site/HomeView.tsx"
src = open(P).read()

START = "      {/* patented intelligence (A-28..A-32) */}"
END_ANCHOR = "      {/* industries — regime chips + sector explorer (A-33/34/42/56) */}"
INS_ANCHOR = "      {/* evidence library (A-40..A-43, A-53) — proof, after the two offer tracks */}"

i = src.find(START); j = src.find(END_ANCHOR); k = src.find(INS_ANCHOR)
assert -1 not in (i, j, k), "markers not found"
print("positions:", i, j, k)
assert i < j, "extraction range invalid"

block = src[i:j].rstrip() + "\n\n"
src = src[:i] + src[j:]

# after removal, find the insert anchor again
k = src.find(INS_ANCHOR)
assert k != -1, "insert anchor missing after removal"
src = src[:k] + block + src[k:]

open(P, "w").write(src)

import re
order = [m.group(1) for m in re.finditer(r'<section id="([a-z]+)"', src)]
print("section order:", order)
assert order == ["top", "output", "services", "consulting", "patents", "platforms", "evidence", "value", "industries", "insights", "faq"], "section order wrong"
print("OK — IP differential + platforms now sit right after consulting.")
