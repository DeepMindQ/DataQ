#!/usr/bin/env python3
"""svc_meta — shared metadata + harvesters for the Services composition rewrite.

Provides:
  - the 12 industries (slug, display name)
  - the 8 expertise domains (slug, display label, short label)
  - harvest of industry×service capability pages → per-combo hook + working
    pattern (real site content, no invented data)
  - case-evidence matrix: published case counts per (industry × domain) from
    the case pages themselves (real site data)
  - explorer block builder used by build.py

Writes/reads scripts/p3/cap_data.json as the cache.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HERE, "..", "..", "site"))
PAGES = os.path.join(SITE, "src", "content", "pages")
CACHE = os.path.join(HERE, "cap_data.json")

# ── the 12 industries (order matches industries.json) ──────────────────────
INDUSTRIES = [
    ("banking-financial-services", "Banking & Financial Services"),
    ("insurance", "Insurance & Risk"),
    ("healthcare-life-sciences", "Healthcare & Life Sciences"),
    ("manufacturing", "Manufacturing & Industrial"),
    ("retail-consumer-goods", "Retail & Consumer Goods"),
    ("telecom-media", "Telecom, Media & Entertainment"),
    ("energy-utilities", "Energy & Utilities"),
    ("logistics-supply-chain", "Logistics & Supply Chain"),
    ("public-sector", "Public Sector & Government"),
    ("education-research", "Education & Research"),
    ("technology-saas", "Technology & SaaS"),
    ("agriculture-food", "Agriculture & Food Systems"),
]
IND_NAME = {slug: name for slug, name in INDUSTRIES}

# ── the 8 expertise domains ────────────────────────────────────────────────
DOMAINS = [
    ("applied-ai-generative-ai", "Applied AI & Generative AI", "Applied AI"),
    ("agentic-ai-hyperautomation", "Agentic AI & Hyperautomation", "Agentic AI"),
    ("data-analytics-lakehouse", "Data, Analytics & Lakehouse", "Data & Lakehouse"),
    ("cybersecurity-zero-trust", "Cybersecurity & Zero-Trust", "Cybersecurity"),
    ("cloud-edge-platform-engineering", "Cloud, Edge & Platform Engineering", "Cloud & Platform"),
    ("quantum-advanced-compute", "Quantum & Advanced Compute", "Quantum & Compute"),
    ("blockchain-digital-trust", "Blockchain & Digital Trust", "Digital Trust"),
    ("iot-digital-twin-robotics", "IoT, Digital Twin & Robotics", "IoT & Twin"),
]
DOMAIN_LABEL = {slug: label for slug, label, _ in DOMAINS}
DOMAIN_SHORT = {slug: short for slug, _, short in DOMAINS}
DOMAIN_ORDER = [slug for slug, _, _ in DOMAINS]


def _trim_sentences(text, max_chars=230):
    """First 1-2 sentences of a string, cut at sentence boundary ≤ max_chars."""
    m = re.match(r"(.+?[.!?])(\s.+?[.!?])?", text)
    if not m:
        return text[:max_chars].rstrip()
    out = m.group(0).strip()
    if len(out) > max_chars:
        out = m.group(1).strip()
    return out


def harvest_capability_pages():
    """hook + working pattern per (industry, service) from the live capability pages."""
    out = {}
    for f in os.listdir(PAGES):
        m = re.match(r"industries_([a-z0-9-]+)_capabilities_([a-z0-9-]+)\.json$", f)
        if not m:
            continue
        ind, svc = m.group(1), m.group(2)
        try:
            j = json.load(open(os.path.join(PAGES, f), encoding="utf-8"))
        except Exception:
            continue
        hero = next((b["x"] for b in j["blocks"] if b["t"] == "hero"), "")
        hook = _trim_sentences(hero)
        # working pattern = first sentence of the paragraph after "What we put in place"
        pattern = ""
        for i, b in enumerate(j["blocks"]):
            if b["t"] == "h2" and "put in place" in b.get("x", "").lower():
                for nb in j["blocks"][i + 1 : i + 3]:
                    if nb["t"] == "p":
                        s = re.sub(r"^In [^,]+, the working pattern is\s*", "", nb["x"])
                        s = re.sub(r"^[A-Z][^:]*?:\s*", "", s) if len(s) > 200 else s
                        pattern = _trim_sentences(s, 200)
                        break
                break
        out[f"{ind}|{svc}"] = {"hook": hook, "pattern": pattern}
    return out


def harvest_case_matrix():
    """Published case counts per (industry, domain) straight off the case pages."""
    mat = {ind: {svc: 0 for svc in DOMAIN_ORDER} for ind, _ in INDUSTRIES}
    total = 0
    for f in os.listdir(PAGES):
        if not re.match(r"case-studies_[a-z]+-\d+\.json$", f):
            continue
        try:
            j = json.load(open(os.path.join(PAGES, f), encoding="utf-8"))
        except Exception:
            continue
        ind = j.get("l2", "")
        rel = [r["title"] for r in j.get("related", [])]
        # map industry name back to slug
        ind_slug = next((s for s, n in INDUSTRIES if n == ind), None)
        if not ind_slug:
            continue
        svcs = set()
        for t in rel:
            m = re.match(r"(?:Tower|Expertise) — (.+)$", t)
            if m:
                svc = next((s for s, label, _ in DOMAINS if label == m.group(1)), None)
                if svc:
                    svcs.add(svc)
        for svc in svcs:
            mat[ind_slug][svc] += 1
        total += 1
    return {"matrix": mat, "total_cases": total}


def build_cache():
    cap = harvest_capability_pages()
    cas = harvest_case_matrix()
    data = {"cap": cap, "cases": cas}
    json.dump(data, open(CACHE, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"cap_data.json: {len(cap)} industry×service combos, "
          f"{cas['total_cases']} cases indexed")
    return data


def load_cache():
    if not os.path.exists(CACHE):
        build_cache()
    return json.load(open(CACHE, encoding="utf-8"))


def _strip_sector_prefix(hook, industry_name):
    """Drop a leading '<Domain> in|against|for <Industry>' opener — the explorer
    panel header already names the service × sector pairing."""
    if not hook:
        return hook
    m = re.match(r"^[^.!?]{0,80}?\s(?:in|against|for)\s+" + re.escape(industry_name) + r"\b", hook)
    if not m:
        return hook
    rest = hook[m.end():].lstrip(" \u2014\u2013-").strip()
    if not rest:
        return hook
    rest = rest[0].upper() + rest[1:]
    if re.match(r"^(does|do|is|are|was|were|has|have|means|runs|buys|gets|stops|starts|ends|comes|turns|asks)\b", rest.lower()):
        rest = "The work here " + rest[0].lower() + rest[1:]
    return rest


def build_explorer(service_title, domain_slug, dash_kpis, plays, flagships, cap):
    """Assemble the explorer block for one service page.

    dash_kpis: [(label, value, delta, dir)] from the page spec
    plays:     3 hand-written service deliverables (from the domain narr file)
    flagships: 3 industry slugs where this service runs deepest
    cap:       harvested capability data dict
    """
    kpis = [{"label": k[0], "value": k[1]} for k in dash_kpis[:3]]
    inds = []
    for slug, name in INDUSTRIES:
        entry = cap.get("cap", {}).get(f"{slug}|{domain_slug}", {})
        hook = entry.get("hook") or (
            f"{name} teams buy {service_title} when the manual version of the work "
            "stops scaling and the manual controls stop passing audit."
        )
        hook = _strip_sector_prefix(hook, name)
        pattern = entry.get("pattern")
        items = list(plays)
        if pattern and len(pattern) > 40:
            items = items + [f"Sector working pattern: {pattern}"]
        inds.append({
            "slug": slug,
            "name": name,
            "flagship": slug in flagships,
            "hook": hook,
            "plays": items[:4],
            "kpis": kpis,
            "capUrl": f"/industries/{slug}/capabilities/{domain_slug}/",
        })
    return {
        "t": "explorer",
        "title": f"{service_title} across the twelve industries we serve",
        "intro": ("Pick your sector — the panel shows what we deliver for it, the targets we "
                  "sign against, and the sector brief with workflows, controls and reference cases."),
        "service": service_title,
        "industries": inds,
    }


if __name__ == "__main__":
    build_cache()
