#!/usr/bin/env python3
"""Deep industry content toolkit — validate + merge for the 5000-word industry rewrite.

Subcommands:
  validate [--file NAME.blocks.json | --all]   schema, depth, style, uniqueness gates
  merge   [--file NAME.blocks.json | --all]    merge validated blocks into site pages
          + refresh meta_description in page JSON and index.json row + recompute words

Word counting mirrors scripts/wave6_content.py count_words (all strings in blocks,
keys "t"/"kind" excluded) so the numbers match the site's own convention.
"""
import json
import os
import re
import sys
from pathlib import Path

SITE = Path("/home/z/my-project/site")
PAGES = SITE / "src" / "content" / "pages"
INDEX = SITE / "src" / "content" / "index.json"
DEEP = Path("/home/z/my-project/scripts/deep_content")
MIN_WORDS = 5000

ALLOWED_T = {"hero", "p", "h2", "h3", "bullets", "table", "note", "arch", "chart",
             "dash", "idash", "diagram", "cta", "explorer"}

FORBIDDEN_STRINGS = [
    "DataQSoft", "DataQ Soft", "DataQ Software",
    "Strategemist", "Pisupati", "VSS Ravi Shanker",
]

GENERIC_PHRASES = [
    "in today's fast-paced", "fast-paced world", "digital transformation journey",
    "unlock the full potential", "unlock the true potential", "cutting-edge solutions",
    "seamlessly integrate", "seamless integration of", "empower your business",
    "take your business to the next level", "game-changer", "game changing",
    "in an era of", "in the ever-evolving", "ever-changing landscape",
    "one-stop shop", "best-in-class solutions", "world-class solutions",
    "leverage our expertise to", "we are passionate about", "your trusted partner",
    "holistic approach to digital", "next-generation solutions",
    "revolutionize the way", "transform the way you do business",
    "industry experts predict", "according to market research",
    "market reports suggest", "studies show that companies",
    "the future of work is here", "embrace the future",
    " Lorem ", "TODO", "TBD", "[placeholder", "XXXX", "\u3010",
]

PLACEHOLDER_RES = [re.compile(r"\bTODO\b"), re.compile(r"\bTBD\b"),
                   re.compile(r"lorem ipsum", re.I), re.compile(r"\u3010")]


def count_words(obj):
    if isinstance(obj, str):
        return len(obj.split())
    if isinstance(obj, dict):
        return sum(count_words(v) for k, v in obj.items() if k not in ("t", "kind"))
    if isinstance(obj, list):
        return sum(count_words(v) for v in obj)
    return 0


def all_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("t", "kind"):
                continue
            yield from all_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from all_strings(v)


def first_p_opener(blocks):
    for b in blocks:
        if b.get("t") == "p" and isinstance(b.get("x"), str) and len(b["x"]) > 60:
            return " ".join(b["x"].split()[:8])
    return None


def cta_key(blocks):
    for b in blocks:
        if b.get("t") == "cta" and isinstance(b.get("x"), str) and len(b["x"]) > 40:
            return b["x"][:140]
    return None


def validate_blocks(d, name, errs):
    blocks = d.get("blocks")
    if not isinstance(blocks, list) or not blocks:
        errs.append(f"{name}: missing/empty blocks")
        return 0
    wc = count_words(blocks)
    if wc < MIN_WORDS:
        errs.append(f"{name}: word count {wc} < {MIN_WORDS}")

    # schema per block type
    for i, b in enumerate(blocks):
        t = b.get("t")
        if t not in ALLOWED_T:
            errs.append(f"{name}: block {i} unknown type {t!r}")
            continue
        if t in ("hero", "p", "note", "cta") and not isinstance(b.get("x"), str):
            errs.append(f"{name}: block {i} ({t}) missing string x")
        if t in ("h2", "h3") and not isinstance(b.get("x"), str):
            errs.append(f"{name}: block {i} ({t}) missing string x")
        if t == "bullets":
            items = b.get("items")
            ok = isinstance(items, list) and len(items) >= 2 and all(
                isinstance(it, list) and len(it) == 2 and isinstance(it[0], str) and isinstance(it[1], str)
                and it[0] and it[1] for it in items)
            if not ok:
                errs.append(f"{name}: block {i} bullets malformed (need items=[[title,desc],...], len>=2)")
        if t == "table":
            if not isinstance(b.get("headers"), list) or not isinstance(b.get("rows"), list):
                errs.append(f"{name}: block {i} table missing headers/rows")
            else:
                ncol = len(b["headers"])
                for r in b["rows"]:
                    if not isinstance(r, list) or len(r) != ncol or any(not isinstance(c, str) for c in r):
                        errs.append(f"{name}: block {i} table row width mismatch")
                        break
        if t == "arch":
            for f in ("title", "lanes", "nodes", "edges"):
                if f not in b:
                    errs.append(f"{name}: block {i} arch missing {f}")
            for n in b.get("nodes", []):
                if not n.get("label") or "lane" not in n or "id" not in n:
                    errs.append(f"{name}: block {i} arch node malformed")

    # content sanity: every h2 followed by at least one non-heading block
    for i, b in enumerate(blocks):
        if b.get("t") == "h2":
            j = i + 1
            while j < len(blocks) and blocks[j].get("t") in ("h2", "h3"):
                j += 1
            if j >= len(blocks):
                errs.append(f"{name}: h2 '{b['x'][:40]}' has no content after it")

    # forbidden + generic strings
    blob = "\n".join(all_strings(blocks)) + "\n" + d.get("meta_description", "")
    for s in FORBIDDEN_STRINGS:
        # case-sensitive for brand rules (the correct brand "Dataq Software" must not
        # trip "DataQ Software"); confidentiality names checked case-insensitively
        if s.startswith(("Strategemist", "Pisupati", "VSS")):
            if s.lower() in blob.lower():
                errs.append(f"{name}: forbidden string {s!r} present")
        elif s in blob:
            errs.append(f"{name}: forbidden string {s!r} present")
    low = blob.lower()
    for ph in GENERIC_PHRASES:
        if ph.lower() in low:
            errs.append(f"{name}: generic phrase {ph!r} present")
    for rx in PLACEHOLDER_RES:
        if rx.search(blob):
            errs.append(f"{name}: placeholder pattern {rx.pattern!r} present")

    # brand naming positive check: at least one "Dataq Software" mention per page
    if "Dataq Software" not in blob:
        errs.append(f"{name}: brand 'Dataq Software' never mentioned")

    md = d.get("meta_description", "")
    if not (120 <= len(md) <= 340):
        errs.append(f"{name}: meta_description length {len(md)} outside 120-340")

    # raw newlines inside strings (prose must be single-line)
    for i, s in enumerate(all_strings(blocks)):
        if "\n" in s:
            errs.append(f"{name}: raw newline inside block string (block {i})")
            break
    return wc


def target_arg(argv):
    """argv: [--file NAME | --all]"""
    if not argv or argv[0] == "--all":
        return "--all"
    if argv[0] == "--file":
        if len(argv) < 2:
            print("--file needs a name")
            sys.exit(1)
        name = argv[1]
        return name if name.endswith(".blocks.json") else f"{name}.blocks.json"
    return argv[0] if argv[0].endswith(".blocks.json") else f"{argv[0]}.blocks.json"


def load_deep_files(which):
    if which == "--all":
        files = sorted(DEEP.glob("*.blocks.json"))
        if not files:
            print("no blocks files found")
            sys.exit(1)
        return files
    f = DEEP / which
    if not f.exists():
        print(f"not found: {f}")
        sys.exit(1)
    return [f]


def cmd_validate(argv):
    files = load_deep_files(target_arg(argv))
    errs, opener_map, cta_map, counts = [], {}, {}, {}
    for f in files:
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            errs.append(f"{f.name}: JSON parse error: {e}")
            continue
        name = d.get("file", f.stem)
        wc = validate_blocks(d, name, errs)
        counts[name] = wc
        op = first_p_opener(d.get("blocks", []))
        if op:
            opener_map.setdefault(op, []).append(name)
        ck = cta_key(d.get("blocks", []))
        if ck:
            cta_map.setdefault(ck, []).append(name)

    # cross-file uniqueness (ratchet: opener shared across >2 pages fails the site gate)
    for op, pages in sorted(opener_map.items()):
        if len(pages) > 2:
            errs.append(f"first-paragraph opener shared by {len(pages)} pages: {' '.join(op.split()[:8])!r} -> {pages[:4]}...")
    for ck, pages in sorted(cta_map.items()):
        if len(pages) > 1:
            errs.append(f"CTA first-140-chars shared by {len(pages)} pages: {pages[:4]}...")

    for name in sorted(counts):
        print(f"  {name}: {counts[name]} words")
    if errs:
        print(f"\nVALIDATE FAIL — {len(errs)} error(s):")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    print(f"VALIDATE OK — {len(files)} file(s), min {min(counts.values())} words, all gates clean")


def cmd_merge(argv):
    files = load_deep_files(target_arg(argv))
    # validate first
    sys.argv = ["x", "validate"] + argv
    validate_errs = []
    payloads = {}
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        errs = []
        validate_blocks(d, d.get("file", f.stem), errs)
        if errs:
            validate_errs.extend(errs)
        else:
            payloads[d["file"]] = d
    if validate_errs:
        print("MERGE ABORTED — validation errors:")
        for e in validate_errs:
            print(f"  - {e}")
        sys.exit(1)

    idx = json.load(open(INDEX, encoding="utf-8"))
    idx_by_file = {r.get("file"): r for r in idx}

    merged = []
    for fname, d in sorted(payloads.items()):
        page_path = PAGES / f"{fname}.json"
        if not page_path.exists():
            print(f"  !! target page missing: {page_path}")
            sys.exit(1)
        page = json.load(open(page_path, encoding="utf-8"))
        page["blocks"] = d["blocks"]
        if d.get("meta_description"):
            page["meta_description"] = d["meta_description"]
        page["words"] = count_words(page["blocks"])
        with open(page_path, "w", encoding="utf-8") as fh:
            json.dump(page, fh, ensure_ascii=False, indent=1)
        row = idx_by_file.get(fname)
        if row:
            row["metaDescription"] = page["meta_description"]
        merged.append(f"{fname}: {page['words']} words")

    with open(INDEX, "w", encoding="utf-8") as fh:
        json.dump(idx, fh, ensure_ascii=False, indent=1)
    print(f"MERGE OK — {len(merged)} page(s):")
    for m in merged:
        print(f"  {m}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("validate", "merge"):
        print(__doc__)
        sys.exit(1)
    if sys.argv[1] == "validate":
        cmd_validate(sys.argv[2:])
    else:
        cmd_merge(sys.argv[2:])
