#!/usr/bin/env python3
"""Naming + confidentiality CI gate (BG-008 / BG-014 / BG-017).

HARD RULES enforced before any static export leaves the machine:
  1. Brand naming  — the only allowed brand string is "Dataq Software".
     Forbidden: "DataQ Soft", "DataQSoft", "DataQ Software", bare "DataQ".
  2. Confidentiality — the R&D programme source entity must never appear:
     forbidden: "Strategemist", "Pisupati", "VSS Ravi Shanker".
     (Note: Hyderabad as Dataq Software's own delivery-center city is ALLOWED;
      the forbidden strings are the secret entity and personnel names.)

Scans site/src + site/public (+ sitemap/robots feeds) for text-bearing files.
Exit 1 = gate failed; wired into `npm run export` so a bad build cannot ship.

Usage: python3 scripts/naming_ci.py [--fix]
      --fix attempts safe replacements for the brand-naming violations only.
"""
import re
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"
SCAN_ROOTS = [SITE / "src", SITE / "public"]
TEXT_EXT = {
    ".ts", ".tsx", ".js", ".jsx", ".json", ".css", ".scss", ".md", ".mdx",
    ".html", ".txt", ".xml", ".svg", ".webmanifest", ".csv",
}

BRAND_RULES = [
    # (compiled pattern, replacement, label)
    (re.compile(r"DataQ\s*Soft(ware)?"), "Dataq Software", "DataQ Soft/Software"),
    (re.compile(r"DataQSoft"), "Dataq Software", "DataQSoft joined"),
    (re.compile(r"(?<![A-Za-z])DataQ(?![A-Za-z])"), "Dataq", "bare DataQ"),
]

CONFIDENTIAL_RULES = [
    (re.compile(r"(?i)strategemist"), "our R&D programme", "secret entity name"),
    (re.compile(r"(?i)pisupati"), "[removed]", "secret personnel"),
    (re.compile(r"(?i)vss\s+ravi\s+shanker|ravi\s+shanker"), "[removed]", "secret personnel"),
]


def iter_files():
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if p.is_file() and (p.suffix.lower() in TEXT_EXT or p.name in ("CNAME", "robots.txt")):
                yield p


def main() -> int:
    fix = "--fix" in sys.argv
    brand_viol = []          # (path, label, count)
    confid_viol = []         # (path, label, count)
    brand_ok_count = 0
    for f in iter_files():
        try:
            s = f.read_text(encoding="utf-8")
        except Exception:
            continue
        orig = s
        # confidentiality first (higher severity, no auto-fix in CI)
        for pat, _repl, label in CONFIDENTIAL_RULES:
            n = len(pat.findall(s))
            if n:
                confid_viol.append((str(f.relative_to(SITE)), label, n))
        for pat, repl, label in BRAND_RULES:
            n = len(pat.findall(s))
            if n:
                brand_viol.append((str(f.relative_to(SITE)), label, n))
                if fix:
                    s = pat.sub(repl, s)
        brand_ok_count += len(re.findall(r"Dataq Software", s))
        if fix and s != orig:
            f.write_text(s, encoding="utf-8")

    print(f"[naming_ci] files scanned: {sum(1 for _ in iter_files())}")
    print(f"[naming_ci] 'Dataq Software' occurrences: {brand_ok_count}")

    if brand_viol:
        print("[naming_ci] BRAND VIOLATIONS:")
        for path, label, n in sorted(brand_viol):
            print(f"  {path}: {label} x{n}")
    if confid_viol:
        print("[naming_ci] CONFIDENTIALITY VIOLATIONS (never auto-fixed):")
        for path, label, n in sorted(confid_viol):
            print(f"  {path}: {label} x{n}")

    if brand_viol or confid_viol:
        print("[naming_ci] GATE FAILED — export blocked.")
        return 1
    print("[naming_ci] GATE PASSED — brand naming + confidentiality clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
