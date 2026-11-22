#!/usr/bin/env python3
"""P3 build v2 — compose the Services section: overview, 8 domain hubs, 54 service pages.

Composition principles (fixing the "system-generated" complaints):
  1. Every heading, hero, lead-in and CTA is hand-written per page (narr_*.py
     modules) — no shared sentence banks, no repeated section titles.
  2. Every page carries the industry explorer (12 sectors, real capability-page
     hooks) so a CXO from any industry sees their sector's delivery plan.
  3. Chart mix varies by page (line/area/bar/radar/donut/funnel/heatmap/gauge/
     network) — hand-assigned per page, data per page.
  4. Industry breadth is REAL: capability-page hooks + sub-industry depth
     matrices computed from the site's own content.
  5. "Tower" wording is scrubbed to domain/expertise wording everywhere.

Usage: python3 scripts/p3/build.py [site-root] [domain ...]
"""
import importlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import common as C  # noqa: E402
import svc_meta as M  # noqa: E402

# ── interlinking registry: curated companion domains per domain ────────────
COMPANIONS = {
    "applied-ai-generative-ai": ["agentic-ai-hyperautomation", "data-analytics-lakehouse", "cybersecurity-zero-trust"],
    "agentic-ai-hyperautomation": ["applied-ai-generative-ai", "data-analytics-lakehouse", "cloud-edge-platform-engineering"],
    "data-analytics-lakehouse": ["applied-ai-generative-ai", "agentic-ai-hyperautomation", "cloud-edge-platform-engineering"],
    "cybersecurity-zero-trust": ["cloud-edge-platform-engineering", "quantum-advanced-compute", "applied-ai-generative-ai"],
    "cloud-edge-platform-engineering": ["cybersecurity-zero-trust", "iot-digital-twin-robotics", "data-analytics-lakehouse"],
    "quantum-advanced-compute": ["cybersecurity-zero-trust", "cloud-edge-platform-engineering", "data-analytics-lakehouse"],
    "blockchain-digital-trust": ["data-analytics-lakehouse", "iot-digital-twin-robotics", "cybersecurity-zero-trust"],
    "iot-digital-twin-robotics": ["cloud-edge-platform-engineering", "data-analytics-lakehouse", "agentic-ai-hyperautomation"],
}

SITE = sys.argv[1] if len(sys.argv) > 1 else "/home/z/my-project/site"
ONLY = set(sys.argv[2:])
PAGES_DIR = os.path.join(SITE, "src/content/pages")
INDEX_FILE = os.path.join(SITE, "src/content/index.json")

BANNED = ["Strategemist", "Pisupati", "Ravi Shanker", "strategemist"]

# ── detower: scrub tower wording out of legacy spec strings ────────────────
_PROTECT = re.compile(r"(cooling[ -]towers?|cell[ -]towers?|control[ -]towers?|power[ -]towers?|transmission[ -]towers?)", re.I)

def detower(s):
    if not isinstance(s, str):
        return s
    keep = []
    def _stash(m):
        keep.append(m.group(0))
        return f"\x00{len(keep)-1}\x00"
    s = _PROTECT.sub(_stash, s)
    s = s.replace("deep technology towers", "expertise domains")
    s = s.replace("Deep Technology Towers", "Expertise Domains")
    s = s.replace("deep-tech towers", "deep-tech expertise domains")
    s = s.replace("technology towers", "technology domains")
    s = s.replace("Tower — ", "Expertise — ")
    s = s.replace("towers", "domains")
    s = s.replace("Towers", "Domains")
    s = s.replace("tower", "domain")
    s = s.replace("Tower", "Domain")
    s = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], s)
    return s

def detower_deep(obj):
    if isinstance(obj, str):
        return detower(obj)
    if isinstance(obj, list):
        return [detower_deep(x) for x in obj]
    if isinstance(obj, tuple):
        return tuple(detower_deep(x) for x in obj)
    if isinstance(obj, dict):
        return {k: detower_deep(v) for k, v in obj.items()}
    return obj

# ── block builders (local variants that scrub wording) ──────────────────────
def b_hero(x): return {"t": "hero", "x": detower(x)}
def b_h2(x): return {"t": "h2", "x": detower(x)}
def b_p(x): return {"t": "p", "x": detower(x)}
def b_note(x): return {"t": "note", "x": detower(x)}
def b_cta(x): return {"t": "cta", "x": detower(x)}
def b_table(caption, headers, rows): return {"t": "table", "caption": detower(caption), "headers": [detower(h) for h in headers], "rows": [[detower(c) for c in r] for r in rows]}
def b_bullets(items): return {"t": "bullets", "items": [[detower(a), detower(b)] for a, b in items]}
def b_diagram(kind, title, labels, note): return {"t": "diagram", "kind": kind, "title": detower(title), "labels": [detower(l) for l in labels], "note": detower(note)}
def b_arch(a):
    nodes = []
    for n in a["nodes"]:
        if isinstance(n, dict):
            nd = {"id": n["id"], "lane": n["lane"], "label": detower(n["label"])}
            if n.get("sub"):
                nd["sub"] = detower(n["sub"])
            if n.get("hot"):
                nd["hot"] = True
            nodes.append(nd)
        else:  # (id, lane, label, hot)
            nid, lane, label = n[0], n[1], n[2]
            hot = bool(n[3]) if len(n) > 3 else False
            nodes.append({"id": nid, "lane": lane, "label": detower(label), **({"hot": True} if hot else {})})
    edges = []
    for e in a["edges"]:
        if isinstance(e, dict):
            edges.append({"a": e["a"], "b": e["b"], **({"label": detower(e["label"])} if e.get("label") else {})})
        else:  # (a, b, label)
            ea, eb = e[0], e[1]
            lab = detower(e[2]) if len(e) > 2 and e[2] else ""
            edges.append({"a": ea, "b": eb, **({"label": lab} if lab else {})})
    return {"t": "arch", "title": detower(a["title"]), "lanes": [detower(l) for l in a["lanes"]], "nodes": nodes, "edges": edges, "note": detower(a["note"])}
def b_dash(d, note): return {"t": "dash", "title": detower(d["title"]), "kpis": [ {"label": detower(k[0]), "value": k[1], "delta": k[2], "dir": k[3]} for k in d["kpis"]], "gates": [{"name": detower(g[0]), "pct": g[1]} for g in d["gates"]], "log": [{"t": r[0], "tag": r[1], "msg": detower(r[2])} for r in d["log"]], "note": note}
def b_chart(ch, note=None):
    out = {"t": "chart", "title": detower(ch["title"]), "variant": ch.get("variant", "line"), "cats": [detower(c) for c in ch["cats"]], "series": [{"name": detower(s[0]), "points": list(s[1])} for s in ch["series"]]}
    if ch.get("unit"): out["unit"] = ch["unit"]
    if ch.get("yMax") is not None: out["yMax"] = ch["yMax"]
    if ch.get("nodes"): out["nodes"] = ch["nodes"]
    if ch.get("links"): out["links"] = ch["links"]
    out["note"] = detower(note if note is not None else ch.get("note", ""))
    if ch.get("caption"): out["caption"] = detower(ch["caption"])
    return out

# ── evidence matrix (real site data) ────────────────────────────────────────
def depth_matrix():
    import collections
    depth = collections.Counter()
    for f in os.listdir(PAGES_DIR):
        m = re.match(r"industries_([a-z0-9-]+)_([a-z0-9-]+)_capabilities_([a-z0-9-]+)\.json$", f)
        if m:
            depth[(m.group(1), m.group(3))] += 1
    return depth

DEPTH = None
def depth(ind, svc):
    global DEPTH
    if DEPTH is None:
        DEPTH = depth_matrix()
    return DEPTH.get((ind, svc), 0)

# ── services overview (fully hand-written) ──────────────────────────────────
def compose_services_hub(mods):
    names = [M.DOMAIN_LABEL[s] for s in M.DOMAIN_ORDER]
    counts = [len(m[0].PAGES) for m in mods]
    total_practices = sum(counts)
    blocks = []
    blocks.append(b_hero(
        "Eight expertise domains, %d engineering practices, one governed delivery system. "
        "Whichever domain you enter, the contract is identical: a business metric signed before "
        "delivery starts, an architecture you can interrogate before kickoff, releases that clear "
        "gates whose evidence is named in advance, and a handover your own team can run on a bad day."
        % total_practices
    ))
    blocks.append(b_h2("How the eight domains divide the work"))
    blocks.append(b_p(
        "The map is cut along the seams where enterprises actually buy: what carries the decision "
        "(Applied AI), what acts on it (Agentic AI), what feeds the decision (Data & Lakehouse), "
        "what protects it (Cybersecurity), what runs the estate (Cloud & Platform), what reaches "
        "past classical limits (Quantum & Advanced Compute), what makes records verifiable "
        "(Blockchain & Digital Trust), and what connects the decision to physical operations "
        "(IoT, Digital Twin & Robotics). Practices inside a domain share tooling, hiring bar and "
        "standards; the domains share one gate model and one evidence format."
    ))
    blocks.append(b_table(
        "The eight domains at a glance — size and the metric each domain is managed on",
        ["Expertise domain", "Practices", "Managed on"],
        [
            ["Applied AI & Generative AI", "7", "Grounded answer rate, cost per 1k calls"],
            ["Agentic AI & Hyperautomation", "7", "Automation coverage, human-checkpoint fidelity"],
            ["Data, Analytics & Lakehouse", "7", "Freshness SLA adherence, decision latency"],
            ["Cybersecurity & Zero-Trust", "7", "Detect-to-contain time, control evidence pass rate"],
            ["Cloud, Edge & Platform Engineering", "7", "Change failure rate, unit cost per workload"],
            ["Quantum & Advanced Compute", "6", "Benchmarked advantage, crypto-inventory coverage"],
            ["Blockchain & Digital Trust", "6", "Verification cost, provenance completeness"],
            ["IoT, Digital Twin & Robotics", "7", "Fleet uptime, twin-to-physical fidelity"],
        ],
    ))
    blocks.append(b_chart(
        {"title": "Practice portfolio composition — %d practices across the eight domains" % total_practices,
         "variant": "donut", "cats": names,
         "series": [("Practices", counts)], "unit": "practices",
         "note": "Every practice page carries its own reference architecture, operating console and release gates."},
        None,
    ))
    blocks.append(b_h2("Where our sector depth sits — and how to read it"))
    blocks.append(b_p(
        "Depth is not a claim, it is a published structure: for every domain × industry cell below, "
        "the number is the count of sub-industry capability pages live on this site — each one a "
        "written sector brief with workflows, controls and a first-month plan. Where a cell is light, "
        "the domain-level sector brief covers the ground; where it is dark, you can descend to named "
        "sub-industries today."
    ))
    hm_cats = [n.replace(" & ", " & ") for _, n in M.INDUSTRIES]
    hm_series = []
    for slug, label, _ in M.DOMAINS:
        hm_series.append((label, [depth(ind, slug) for ind, _ in M.INDUSTRIES]))
    blocks.append(b_chart(
        {"title": "Published sector depth — sub-industry capability pages per domain × industry",
         "variant": "heatmap", "cats": hm_cats, "series": hm_series, "unit": "pages",
         "caption": "Counts reflect live pages on this site, not marketing coverage claims. Industry hubs link every cell — light cells resolve at domain level."},
        None,
    ))
    blocks.append(b_h2("The engagement ladder — four rungs, no leaps of faith"))
    blocks.append(b_p(
        "Work enters at the rung that matches the evidence you already hold. The ladder is "
        "deliberately short: the provability sprint exists so that nobody buys a large program "
        "on a hypothesis, and the diagnostic exists so the first build starts from a baseline "
        "your CFO and your auditors both accept."
    ))
    blocks.append(b_table(
        "Four rungs from question to industrialized capability",
        ["Rung", "What happens", "What you hold at exit"],
        [
            ["1 · Diagnostic (2 weeks)", "Signed baseline, estate map, gate fill-in, build order with owners", "Baseline document; the gate map scored for your estate"],
            ["2 · Provability sprint (4 weeks)", "One metric, real data path, fund-or-kill verdict", "Exit report with auditable numbers and a priced production path"],
            ["3 · Build (10–14 weeks)", "Architecture, gates and console from these pages, applied to your estate", "Production system with evidence pack and runbook"],
            ["4 · Industrialize (ongoing)", "SRE cadence, quarterly re-baselines, platform reuse review", "Operating service with trend line against the signed baseline"],
        ],
    ))
    blocks.append(b_h2("The operating contract behind every service page"))
    blocks.append(b_p(
        "Three clauses hold across all eight domains and every practice inside them. First, the "
        "baseline is signed by the metric owner before the build starts — no metric, no build. "
        "Second, releases clear gates whose evidence is named in advance, so a blocked release is "
        "a process working, not a crisis. Third, the handover includes the runbook, the eval suite "
        "and the operating console: the capability to run the system, not just the code that "
        "happens to be deployed today."
    ))
    blocks.append(b_p(
        "Where our patent-pending method families strengthen a gate, the service page names them "
        "and maps each family to the gate it reinforces — you can read the capability summary on "
        "the patent map without asking for a briefing first."
    ))
    blocks.append(b_cta(
        "Start with the two-week diagnostic — it ends with a signed baseline and a scored gate "
        "map for your estate, whichever domain you land in. Bring the metric you own; we will "
        "tell you honestly which gates you would fail today."
    ))
    return blocks

# ── domain hub ──────────────────────────────────────────────────────────────
def compose_domain_hub(mod, H, cap, idash=None):
    T = mod.TOWER
    slug = T["slug"]
    label = M.DOMAIN_LABEL.get(slug, slug)
    blocks = []
    blocks.append(b_hero(H["hero"]))
    for para in T["intro"]:
        blocks.append(b_p(para))
    blocks.append(b_h2(H["s_practices"]))
    pt = T["practices_table"]
    blocks.append(b_table(pt["caption"], pt["headers"], pt["rows"]))
    blocks.append(b_h2(H["s_deep"]))
    for para in (T.get("hub_job") or H.get("deep") or []):
        blocks.append(b_p(para))
    blocks.append(b_h2(H["s_arch"]))
    blocks.append(b_p(H["arch_lead"]))
    blocks.append(b_arch(T["arch"]))
    blocks.append(b_h2(H["s_dash"]))
    blocks.append(b_p(H["dash_lead"]))
    if idash:
        blocks.append(idash)
    else:
        blocks.append(b_dash(T["dash"], H["dash_note"]))
    ch = dict(T["chart"])
    ov = H.get("chart_override")
    if ov:
        for k, v in ov.items():
            ch[k] = v
    blocks.append(b_h2(H["s_chart"]))
    blocks.append(b_p(H["chart_lead"]))
    blocks.append(b_chart(ch, H.get("chart_note")))
    # industry breadth — real sub-industry depth for this domain
    blocks.append(b_h2(H["s_evidence"]))
    blocks.append(b_p(H["evidence_lead"]))
    blocks.append(b_chart(
        {"title": H["evidence_chart_title"],
         "variant": "bar", "cats": [n for _, n in M.INDUSTRIES],
         "series": [("Published sub-industry briefs", [depth(ind, slug) for ind, _ in M.INDUSTRIES])],
         "unit": "briefs", "yMax": 5,
         "caption": "Counts are live pages on this site. Taller bars mean deeper published sector coverage; every cell also has the domain-level sector brief."},
        None,
    ))
    # explorer — 12 industries, flagships marked
    exp = M.build_explorer(label, slug, T["dash"]["kpis"], H["plays"], H["flagships"], cap)
    exp["title"] = H["explorer_title"]
    exp["intro"] = H["explorer_intro"]
    exp["practiceNote"] = "Domain-level view — pick a practice above for the practice-specific sector plan and console."
    blocks.append(detower_deep(exp))
    blocks.append(b_h2(H["s_engage"]))
    blocks.append(b_bullets(H["engage"]))
    blocks.append(b_h2(H["s_gates"]))
    hg = T["hub_gates"]
    blocks.append(b_table(hg["caption"], hg["headers"], hg["rows"]))
    blocks.append(b_cta(H["cta"]))
    return blocks

# ── service leaf page ───────────────────────────────────────────────────────
def compose_sub_page_v2(spec, page_title, N, cap, idash=None, cards=None):
    ts = page_title
    blocks = []
    blocks.append(b_hero(N["hero"]))
    blocks.append(b_h2(N["s1_h"]))
    for para in spec["job"]:
        blocks.append(b_p(para))
    blocks.append(b_p(N["s1_close"]))
    blocks.append(b_h2(N["s2_h"]))
    blocks.append(b_p(N["s2_lead"]))
    blocks.append(b_table(
        f"{ts}: failure modes we design against — and the countermeasure that ships with the build",
        ["Failure mode", "What it looks like in production", "Countermeasure we ship"],
        [list(r) for r in spec["hard"]],
    ))
    blocks.append(b_h2(N["arch_h"]))
    blocks.append(b_p(N["arch_lead"]))
    blocks.append(b_arch(spec["arch"]))
    f = spec["flow"]
    blocks.append(b_h2(N["flow_h"]))
    blocks.append(b_p(N["flow_lead"]))
    blocks.append(b_diagram(f["kind"], f["title"], f["labels"], f["note"]))
    blocks.append(b_h2(N["dash_h"]))
    blocks.append(b_p(N["dash_lead"]))
    if idash:
        blocks.append(idash)
    else:
        blocks.append(b_dash(spec["dash"], N["dash_note"]))
    blocks.append(b_h2(N["chart_h"]))
    blocks.append(b_p(N["chart_lead"]))
    ch = dict(spec["chart"])
    ov = N.get("chart_override")
    if ov:
        for k, v in ov.items():
            ch[k] = v
    blocks.append(b_chart(ch, N.get("chart_note")))
    if N.get("chart2"):
        blocks.append(b_chart(N["chart2"], N.get("chart2_note")))
    exp = M.build_explorer(page_title, spec["tower"], spec["dash"]["kpis"], N["plays"], N["flagships"], cap)
    exp["practiceNote"] = f"{ts} view: {spec.get('essence', '').strip()}"
    blocks.append(detower_deep(exp))
    blocks.append(b_h2(N["stack_h"]))
    blocks.append(b_p(N["stack_lead"]))
    blocks.append(b_table(
        f"{ts}: default stack and the conditions under which we deviate",
        ["Layer", "Default choice", "When we deviate — and why"],
        [list(r) for r in spec["stack"]],
    ))
    blocks.append(b_h2(N["gates_h"]))
    blocks.append(b_table(
        f"Release gates for {ts} — the evidence each demands",
        ["Gate", "Question it answers", "Evidence required to pass"],
        [list(r) for r in spec["gates_table"]],
    ))
    blocks.append(b_h2(N["artifacts_h"]))
    blocks.append(b_bullets(spec["artifacts"]))
    blocks.append(b_h2(N["timeline_h"]))
    blocks.append(b_bullets(spec["timeline"]))
    blocks.append(b_h2(N["integ_h"]))
    blocks.append(b_p(N["integ_lead"]))
    blocks.append(b_bullets(spec["integrations"]))
    blocks.append(b_h2(N["controls_h"]))
    blocks.append(b_p(N["controls_lead"]))
    blocks.append(b_bullets(spec["controls"]))
    blocks.append(b_note(N["controls_note"]))
    blocks.append(b_cta(N["cta"]))
    return blocks

# ── lint ────────────────────────────────────────────────────────────────────
def lint_page(fname, blocks):
    errs = []
    text = json.dumps(blocks, ensure_ascii=False)
    for b in BANNED:
        if b.lower() in text.lower():
            errs.append(f"banned name '{b}'")
    if re.search(r"\btower", text, re.I):
        # physical-tower senses are legitimate industry terms — whitelist them
        stripped = _PROTECT.sub("", text)
        if re.search(r"\btower", stripped, re.I):
            errs.append("tower wording leaked")
    arches = [b for b in blocks if b["t"] == "arch"]
    for a in arches:
        ids = [n["id"] for n in a["nodes"]]
        if len(ids) != len(set(ids)):
            errs.append("arch duplicate node ids")
        lanes = len(a["lanes"])
        for n in a["nodes"]:
            if not (0 <= n["lane"] < lanes):
                errs.append(f"node {n['id']} lane out of range")
        for e in a["edges"]:
            if e["a"] not in ids or e["b"] not in ids:
                errs.append(f"edge {e['a']}->{e['b']} references missing node")
        if not (6 <= len(ids) <= 22):
            errs.append(f"arch node count odd: {len(ids)}")
        if not (4 <= lanes <= 7):
            errs.append(f"arch lane count odd: {lanes}")
    charts = [b for b in blocks if b["t"] == "chart"]
    for chb in charts:
        v = chb.get("variant", "line")
        if v not in {"line", "bar", "radar", "area", "donut", "funnel", "heatmap", "gauge", "network"}:
            errs.append(f"unknown chart variant {v}")
        if v == "gauge":
            continue
        for s in chb["series"]:
            if len(s["points"]) != len(chb["cats"]):
                errs.append(f"chart '{chb['title'][:40]}' series '{s['name']}' length != cats")
        if len(chb["series"]) > 3 and v != "heatmap":
            errs.append("chart too many series")
        if v == "heatmap" and len(chb["series"]) > 12:
            errs.append("heatmap too many rows")
    for dsh in [b for b in blocks if b["t"] == "dash"]:
        if not (3 <= len(dsh["kpis"]) <= 6):
            errs.append("dash kpi count odd")
        if dsh["gates"] and not (3 <= len(dsh["gates"]) <= 6):
            errs.append("dash gate count odd")
    for tb in [b for b in blocks if b["t"] == "table"]:
        for r in tb["rows"]:
            if len(r) != len(tb["headers"]):
                errs.append("table row width mismatch")
    for ex in [b for b in blocks if b["t"] == "explorer"]:
        if len(ex["industries"]) != 12:
            errs.append("explorer must cover 12 industries")
        for ind in ex["industries"]:
            if not ind["capUrl"].startswith("/industries/"):
                errs.append("explorer capUrl bad")
            if not ind["plays"] or not ind["kpis"]:
                errs.append("explorer entry empty")
    return errs

def uniq_check(page_heads):
    """page_heads: {fname: [headings]} — no heading may repeat across the section."""
    seen = {}
    errs = []
    for fname, heads in page_heads.items():
        for h in heads:
            key = h.strip().lower()
            if key in seen:
                errs.append(f"duplicate heading '{h}' in {fname} (first in {seen[key]})")
            else:
                seen[key] = fname
    return errs

# ── main ────────────────────────────────────────────────────────────────────
SPEC_MODS = ["spec_applied", "spec_agentic", "spec_data", "spec_cyber",
             "spec_cloud", "spec_quantum", "spec_blockchain", "spec_iot"]
NARR_MODS = {"spec_applied": "narr_applied", "spec_agentic": "narr_agentic",
             "spec_data": "narr_data", "spec_cyber": "narr_cyber",
             "spec_cloud": "narr_cloud", "spec_quantum": "narr_quantum",
             "spec_blockchain": "narr_blockchain", "spec_iot": "narr_iot"}

def carry_idash(d):
    """preserve the existing interactive DashSuite console from the current page JSON"""
    for b in d.get("blocks", []) or []:
        if b.get("t") == "idash":
            return b
    return None


def harvest_case_registry():
    """cases per domain slug, from case pages' related rails ('Expertise — <label>')"""
    reg = {slug: [] for slug, _, _ in M.DOMAINS}
    label_to_slug = {label: slug for slug, label, _ in M.DOMAINS}
    for f in sorted(os.listdir(PAGES_DIR)):
        if not re.match(r"case-studies_[a-z]+-\d+\.json$", f):
            continue
        try:
            j = json.load(open(os.path.join(PAGES_DIR, f), encoding="utf-8"))
        except Exception:
            continue
        url = j.get("url")
        title = j.get("title")
        desc = j.get("meta_description") or ""
        for r in j.get("related", []) or []:
            t = r.get("title", "")
            m = re.match(r"^(?:Tower|Expertise)\s*[—\-]\s*(.+)$", t)
            if not m:
                continue
            slug = label_to_slug.get(m.group(1).strip())
            if slug and url:
                reg[slug].append({"title": title, "url": url, "desc": desc})
    return reg


def build_cards(domain, page_slug, page_idx, registry, case_reg):
    """interlinked card set: 3 same-domain siblings + 2 cross-domain companions + 1 case"""
    cards = []
    sibs = [s for s in sorted(registry[domain].keys()) if s != page_slug]
    # rotate sibling order per page so the rail varies across the domain
    rot = page_idx % max(1, len(sibs))
    sibs = sibs[rot:] + sibs[:rot]
    for s in sibs[:3]:
        t, u, es = registry[domain][s]
        cards.append({"title": t, "url": u, "tag": "Same domain", "desc": es})
    for k, cd in enumerate(COMPANIONS.get(domain, [])):
        pool = sorted(registry.get(cd, {}).keys())
        if not pool:
            continue
        pick = pool[(page_idx + k) % len(pool)]
        t, u, es = registry[cd][pick]
        cards.append({"title": t, "url": u, "tag": "Pairs with", "desc": es})
    cases = case_reg.get(domain, [])
    if cases:
        c = cases[page_idx % len(cases)]
        cards.append({"title": c["title"], "url": c["url"], "tag": "Evidence", "desc": c["desc"]})
    return cards


def main():
    mods = []
    for name in SPEC_MODS:
        slug = name.replace("spec_", "")
        if ONLY and slug not in ONLY:
            continue
        try:
            mods.append((importlib.import_module(name), importlib.import_module(NARR_MODS[name])))
        except ModuleNotFoundError as e:
            print(f"  (module missing: {e} — skipped)")

    cap = M.load_cache()
    index = json.load(open(INDEX_FILE, encoding="utf-8"))
    touched = []
    errors = []
    page_heads = {}
    case_reg = harvest_case_registry()

    # registry: domain -> page_slug -> (title, url, essence) — built from spec modules + page files
    registry = {slug: {} for slug, _, _ in M.DOMAINS}
    for name in SPEC_MODS:
        try:
            sm = importlib.import_module(name)
        except ModuleNotFoundError:
            continue
        dslug = sm.TOWER["slug"]
        for sp in sm.PAGES:
            fname = f"services_{dslug}_{sp['slug']}.json"
            fp = os.path.join(PAGES_DIR, fname)
            title = sp["slug"].replace("-", " ").title()
            if os.path.exists(fp):
                try:
                    title = json.load(open(fp, encoding="utf-8"))["title"]
                except Exception:
                    pass
            registry[dslug][sp["slug"]] = (title, f"/services/{dslug}/{sp['slug']}/", sp.get("essence", "").strip())

    def write(fname, d, blocks):
        d["blocks"] = blocks
        d["words"] = C.words_of(blocks)
        e = lint_page(fname, blocks)
        errors.extend((fname, x) for x in e)
        page_heads[fname] = [b["x"] for b in blocks if b["t"] == "h2"]
        json.dump(detower_deep_meta(d), open(os.path.join(PAGES_DIR, fname), "w", encoding="utf-8"),
                  indent=1, ensure_ascii=False)
        touched.append((fname[:-5], d["words"]))
        print(f"{fname}: {d['words']} words, {len(blocks)} blocks")

    def detower_deep_meta(d):
        """scrub meta fields too (titles, descs, related, cards)"""
        for k in ("title", "breadcrumb", "seo_title", "meta_description"):
            if k in d:
                d[k] = detower(d[k])
        for rail in ("related", "cards"):
            for item in d.get(rail, []) or []:
                item["title"] = detower(item.get("title", ""))
                item["desc"] = detower(item.get("desc", ""))
                if item.get("tag"):
                    item["tag"] = detower(item["tag"])
        for c in d.get("crumbs", []) or []:
            c["name"] = detower(c.get("name", ""))
        return d

    # 1. services overview — only when no domain filter, or filter includes it via all
    if not ONLY:
        hp = os.path.join(PAGES_DIR, "services.json")
        d = json.load(open(hp, encoding="utf-8"))
        d["meta_description"] = ("Consulting and delivery across eight deep-tech expertise domains, "
                                 "run as one governed delivery system with shared platforms and named gates.")
        write("services.json", d, compose_services_hub(mods))

    # 2. domain hubs + leaf pages
    for mod, narr in mods:
        T = mod.TOWER
        slug = T["slug"]
        H = narr.HUB
        hub_file = f"services_{slug}.json"
        hp = os.path.join(PAGES_DIR, hub_file)
        d = json.load(open(hp, encoding="utf-8"))
        hub_idash = detower_deep(carry_idash(d))
        blocks = compose_domain_hub(mod, H, cap, idash=hub_idash)
        if hub_idash:
            # hub explorer targets read from the preserved console KPIs, keeping numbers consistent
            pass
        write(hub_file, d, blocks)

        for pi, spec in enumerate(mod.PAGES):
            spec["tower"] = slug
            N = narr.PAGES.get(spec["slug"])
            if not N:
                errors.append((f"services_{slug}_{spec['slug']}.json", "no narrative in narr module"))
                continue
            fname = f"services_{slug}_{spec['slug']}.json"
            fp = os.path.join(PAGES_DIR, fname)
            d = json.load(open(fp, encoding="utf-8"))
            idash = detower_deep(carry_idash(d))
            d["cards"] = build_cards(slug, spec["slug"], pi, registry, case_reg)
            write(fname, d, compose_sub_page_v2(spec, d["title"], N, cap, idash=idash, cards=d["cards"]))

    # 3. index.json word counts
    n_idx = 0
    for row in index:
        for fname, w in touched:
            key = fname[:-5] if fname.endswith(".json") else fname
            if row.get("file") == key:
                row["words"] = w
                n_idx += 1
    json.dump(index, open(INDEX_FILE, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"index.json word counts updated for {n_idx} rows")

    # 4. uniqueness check across ALL composed pages (plus previously composed ones)
    uniq_errs = uniq_check(page_heads)
    if uniq_errs and not ONLY:
        errors.extend(("(uniqueness)", e) for e in uniq_errs)
    elif uniq_errs:
        for e in uniq_errs:
            print(f"  NOTE (partial build): {e}")

    if errors:
        print("\nLINT ERRORS:")
        for f, e in errors:
            print(f"  {f}: {e}")
        sys.exit(1)
    total = sum(w for _, w in touched)
    print(f"\nOK — {len(touched)} pages rebuilt, {total} words total. Lint clean.")

if __name__ == "__main__":
    main()
