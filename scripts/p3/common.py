#!/usr/bin/env python3
"""Phase 3 — Services deep-technical content engine (shared banks + builders).

Client direction: the most detailed, most in-depth technical content, with the
most complex architectures, flows, graphs and charts, for every Services page.

Voice rules carried over from Phase 2 (p2_voice.py):
  1. Every page is written to ITS subject — no variable-swap boilerplate.
  2. Numbers on dashboards/charts are OUR engineering targets and reference
     bands, captioned as such — never presented as client outcomes.
  3. Human voice: plain sentences, practitioner tone, varied openings.
  4. Every visual carries per-page labels; a visual must earn its place.
"""
import hashlib

def h(key: str, n: int) -> int:
    return int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16) % max(n, 1)

def pick(key: str, items):
    return items[h(key, len(items))]

def words_of(blocks) -> int:
    n = 0
    for b in blocks:
        n += len(str(b.get("x", "")).split())
        n += len(str(b.get("title", "")).split())
        for it in b.get("items", []) or []:
            n += len(str(it[0]).split()) + len(str(it[1]).split())
        for row in b.get("rows", []) or []:
            n += sum(len(str(c).split()) for c in row)
        n += len(b.get("headers", []) or []) * 2
        for nd in b.get("nodes", []) or []:
            n += len(str(nd.get("label", "")).split())
        n += len(b.get("edges", []) or [])
        for s in b.get("series", []) or []:
            n += len(str(s.get("name", "")).split())
        for k in b.get("kpis", []) or []:
            n += len(str(k.get("label", "")).split())
    return n

# ── sentence banks (hash-picked per page so pages never share the same line) ──
JOB_OPEN = [
    "Most teams arrive at {t} after a first attempt stalled: the demo worked, the pilot drifted, and nobody owned the gap between the two.",
    "The honest way to describe {t} is unglamorous: it is instrumentation and plumbing first, intelligence second, and the order is not negotiable.",
    "{t} earns its budget the same way everything here does — one signed baseline metric, then a build that moves it and can prove it moved.",
    "Every {t} engagement starts with the same admission: the hard part is rarely the clever component. It is the data contracts, the failure handling and the audit trail around it.",
    "We treat {t} as an engineering discipline with a quality bar, not a consulting theme — the deliverable is a system someone else can operate on a bad day.",
    "{t} is where architecture opinions get tested against production reality: rate limits, partial failures, stale caches and auditors all show up on the same day.",
    "Teams usually find {t} after a pilot taught them an expensive lesson: the parts that matter were not the model, they were the contracts and the failure handling.",
    "The shortest honest pitch for {t}: we instrument first, build second, and hand over a system your own engineers can operate without us in the room.",
    "{t} succeeds when it is scoped like engineering — one metric, one owner, gates with named evidence — and fails when it is scoped like a slide.",
    "What makes {t} different here is the order of operations: baseline signed before build, gates before release, runbook before handover — no steps skipped.",
]
JOB_CLOSE = [
    "What follows is the system as we actually build it — the components, the failure modes we design against, and the gates a release has to clear.",
    "The sections below read like a design review because that is what they are: components, flows, dashboards, standards and the evidence each gate demands.",
    "Everything on this page is build-order material — the same decomposition we use in sprint one, published so your team can challenge it before the kickoff.",
    "Read it as an engineering brief: the architecture is drawn, the dashboard is scoped, the standards are named, and every gate lists the evidence it demands.",
]
HARD_INTRO = [
    "Programs of this kind fail in patterned ways. These are the failure modes we design against before the first line of production code exists.",
    "The difficulty concentrates in a handful of places. We name them up front because every one of them has a countermeasure that must ship with the build.",
    "Experience across engagements says the same four or five things go wrong first. The table is the countermeasure register we carry into delivery.",
]
FLOW_PARA = [
    "The flow below is the runbook view: what triggers work, which component holds state, where approvals block, and what the caller sees when something degrades.",
    "Requests, events and control loops are drawn separately on purpose — conflating them is how teams end up with systems nobody can reason about under failure.",
    "Every arrow in this flow has an owner, a timeout and a dead-letter path. The diagram is the contract; the runbook is its appendix.",
    "This is the path a unit of work takes from entry to evidence: where it is validated, where it is enriched, where policy can stop it, and where the audit row lands.",
]
DASH_INTRO = [
    "The console below is the operating view we stand up in the first weeks: KPI tiles for the metrics the service is judged on, gate bars for release state, and a log shaped like the one your team will page on.",
    "Reference posture, rendered the way the delivery team sees it: the tiles are the service's commit levels, the bars are gate progress, and the log rows are the event shapes that reach the on-call channel.",
    "The dashboard is part of the deliverable, not decoration. Its tiles bind to the same metrics the gates below test, and its log vocabulary matches the runbook.",
]
CHART_INTRO = [
    "Charts need honest numbers. Everything plotted here is a design target or reference band this service is built and gated against — not a client figure and not a benchmark we cannot defend.",
    "The profile below is our working posture: the levels we design to, re-baselined when the estate changes, and always labeled as targets rather than results.",
]
STANDARDS_OPEN = {
    "applied-ai-generative-ai": "Applied AI work lives or dies on evaluation discipline, so the standards bias toward reproducible eval sets, versioned prompts and models, and a cost line that is owned like any SLO.",
    "agentic-ai-hyperautomation": "Agentic builds are governed like a workforce: identity for every agent, least-privilege tools, bounded loops, and a replay trail that reconstructs any decision after the fact.",
    "data-analytics-lakehouse": "Data platform standards are contract-first: schemas are versioned, SLAs are typed, lineage is captured where the data moves, and every dataset has one owner with a page for it.",
    "cybersecurity-zero-trust": "Security engineering standards are evidence-first: every control maps to a testable assertion, every exception has an expiry, and detection is validated against rehearsed attack paths.",
    "cloud-edge-platform-engineering": "Platform standards are product standards: golden paths are versioned APIs, capacity and cost are budgeted per service, and reliability work is scheduled like feature work because it competes with it.",
    "quantum-advanced-compute": "Quantum and advanced-compute work is standards-heavy by nature: hybrid job orchestration, error-aware benchmarking, and crypto-inventory discipline that feeds the PQC migration ledger.",
    "blockchain-digital-trust": "Distributed-ledger standards favor boring cryptography: audited contracts, keyed access, offline key ceremonies, and off-chain state designs that keep the chain small and provable.",
    "iot-digital-twin-robotics": "IoT and twin programs are constrained-device engineering: schemas at the edge, store-and-forward everywhere, and a simulation tier that rehearses firmware and fleet changes before hardware moves.",
}
INTEG_INTRO = [
    "Nothing ships as an island. These are the seams this service routinely lands against, with the contract shape each side is held to.",
    "The integration surface below is where most schedule risk hides, so we contract it early: direction, schema, identity, rate limits and failure behavior for each seam.",
]
CONTROL_INTRO = [
    "The governance overlay is deliberately thin and testable — controls you can evidence in an afternoon, not a binder nobody opens.",
    "Security and governance arrive as part of the build, wired into the same gates: each control below has an owner, a check and an evidence artifact.",
]
CTA_BANK = [
    "Bring the metric {t} is written around to a briefing — we will map your estate against the architecture above and tell you which gate you would fail first.",
    "If two or three rows in the failure table read like your last post-mortem, bring the post-mortem to a briefing — {t} comes with the countermeasures and a delivery plan.",
    "The fastest next step for {t} is the two-week diagnostic: a signed baseline, the gate map above filled in for your estate, and a build order with owners.",
    "Book the {t} briefing with this page open — the architecture section doubles as the agenda, and the first hour usually ends with the baseline metric chosen.",
    "Start the {t} diagnostic: two weeks, one signed baseline, every gate on this page scored against your estate — fund or stop on evidence.",
    "Bring your hardest failure mode from the table above to a briefing; we will show you the {t} countermeasure running and the gate that proves it works.",
    "The {t} briefing is technical by design: bring an engineer, leave with the architecture mapped to your estate and a build order with named owners.",
    "One hour, this architecture, your estate: the {t} briefing ends with the baseline metric picked and the first gate date pencilled in.",
    "If the console above looks like reporting your program already owes someone, bring it to a briefing — we will wire {t} to produce it for real.",
    "Skip the discovery deck for {t}: run the two-week diagnostic and these pages become your build order with owners and gate dates attached.",
    "Take this console to your next steering meeting — then book the {t} briefing and we will tell you honestly which gates you would fail today.",
    "The honest entry point to {t} is the diagnostic: two weeks, one signed baseline, and the gate map above filled in for your systems — then you decide.",
]


# ── fragment-composed intro sentences (opener × closer ⇒ ~36 combos per bank) ──
CI_OPEN = [
    "The governance overlay for {t} is deliberately thin and testable",
    "Security and governance arrive as part of the {t} build",
    "Controls here are wired into the same gates as the {t} code",
    "The governance layer for {t} is built to be evidenced, not filed",
    "This practice treats {t} controls as shipped engineering",
    "Governance lands with the {t} build, not after it",
    "On {t}, the control set is small, owned and testable",
    "{t} carries its governance the way it carries its tests — in the pipeline",
]
CI_CLOSE = [
    "controls your team can evidence in an afternoon — {t} ships no binder nobody opens",
    "each {t} control carrying an owner, a check and an evidence artifact",
    "testable {t} assertions an auditor can walk in a single session",
    "evidence packs generated by the pipeline that does the work",
    "checks your team can run without calling us",
    "an audit trail assembled where the work actually happens",
    "artifacts your reviewers can pull on demand, not on request-with-notice",
    "evidence that lives in the gates, not in a policy PDF",
]
IN_OPEN = [
    "Nothing in {t} ships as an island",
    "No {t} build lands alone",
    "Every {t} engagement meets systems that already exist",
    "The seams are contracted before the {t} code is written",
    "Integration risk in {t} is priced up front, not discovered late",
    "The estate does not pause while {t} is built",
    "{t} succeeds or fails at its seams",
]
IN_CLOSE = [
    "the seams below carry {t} contracts: direction, schema, identity and failure behavior",
    "each integration below names its owner, its schema and its dead-letter path",
    "the {t} surface below is where schedule risk hides, so it is contracted in week one",
    "these are the routine landing points, each with rate limits and failure shapes agreed",
    "every seam below has a version, a timeout and a compensation path",
    "the contracts below are versioned like code and tested like code",
]
CH_OPEN = [
    "Charts for {t} need honest numbers",
    "Numbers on the {t} page earn their place with honest captions",
    "A chart without provenance is decoration, so {t} labels everything",
    "Plotting targets is only useful when the caption says so — {t} says so",
    "Graphs carry authority only when the numbers are labeled truthfully, and {t} labels them",
    "Data on the {t} page is target-shaped, and it says so",
]
CH_CLOSE = [
    "what is plotted below for {t} is a design target or reference band the service is built and gated against — not a client figure",
    "the series below are the levels we design to, labeled as targets rather than results",
    "everything plotted for {t} is our working posture, re-baselined when the estate changes and never mistaken for client outcomes",
    "the bands below are commitments gated on for {t}, stated as targets so nobody reads them as wins",
    "these are engineering targets with named gates behind them — the client's own numbers stay with the client",
    "the curves below are design posture, published so you can challenge them before the build starts",
]
DA_OPEN = [
    "The console below is scoped from the metrics {t} is judged on",
    "Reference posture for {t}, rendered the way the delivery team sees it",
    "The {t} dashboard is part of the deliverable, not decoration",
    "The operating view below is built like the one your team inherits with {t}",
    "This console is {t}'s contract made visible",
    "The view below is the one that reaches the {t} on-call channel",
]
DA_CLOSE = [
    "KPI tiles for the judged metrics, gate bars for release state, and a log shaped like the runbook",
    "tiles are commit levels, bars are gate position, and the log vocabulary matches the handover runbook",
    "each tile binds to a gate below, and the log rows speak the runbook's language",
    "if a tile would not survive a {t} steering meeting, it is not on the dashboard",
    "the tiles, bars and log rows below are wired to the same gates the build clears",
    "commit levels on top, gate position in the middle, and the paging shapes at the bottom",
]
HA_OPEN = [
    "Programs like {t} fail in patterned ways",
    "The difficulty in {t} concentrates in a handful of places",
    "Experience says the same {t} failures arrive first",
    "Most of the risk in {t} lives in four or five familiar places",
    "The failure modes below are the ones {t} is designed against first",
    "These are the ways {t} programs go wrong",
]
HA_CLOSE = [
    "these are the failure modes we design against before the first line of production code",
    "each one has a countermeasure that ships with the build, not after it",
    "the table below is the countermeasure register we carry into {t} delivery",
    "we name them up front because every row has a fix that must land with the build",
    "each row below pairs the failure with the engineering that prevents it",
    "the register below is argued in the briefing, not discovered in production",
]
FL_OPEN = [
    "The flow below is the runbook view for {t}",
    "The diagram below separates {t}'s request, control and evidence paths",
    "Read the {t} flow as ownership",
    "This is the {t} unit-of-work journey from entry to evidence",
    "The path below is drawn the way {t} operations reads it",
    "The {t} flow below is the contract operations tests against",
]
FL_CLOSE = [
    "what triggers work, which component holds state, where approvals block, and what the caller sees when something degrades",
    "every arrow names the component that holds state, the policy that can stop it, and the timeout that bounds it",
    "where {t} validation happens, where enrichment happens, and where the audit row is written",
    "three lifetimes — requests, control and evidence — kept apart on purpose",
    "each hop has an owner, a timeout and a dead-letter path",
    "the {t} diagram is the contract; the runbook is its appendix",
]
JC_OPEN = [
    "What follows is {t} as we actually build it",
    "The sections below read like a {t} design review because that is what they are",
    "Everything on this page is {t} build-order material",
    "Read this page as an engineering brief for {t}",
    "Below is the same {t} decomposition we use in sprint one",
    "What follows is the working {t} system, drawn and gated",
]
JC_CLOSE = [
    "components, failure modes and the gates a release has to clear",
    "the architecture, the flows, the standards and the evidence each gate demands",
    "published early so your team can challenge the {t} plan before the kickoff",
    "the {t} dashboard scoped, the standards named, the gates with their evidence listed",
    "with owners, gates and timelines attached",
    "and every claim on it is testable at a gate",
]
def compose_control_intro(title):
    return (pick("ci-o:"+title, CI_OPEN) + " — " + pick("ci-c:"+title, CI_CLOSE) + ".").format(t=title)
def compose_integ_intro(title):
    return (pick("in-o:"+title, IN_OPEN) + ": " + pick("in-c:"+title, IN_CLOSE) + ".").format(t=title)
def compose_chart_intro(title):
    return (pick("ch-o:"+title, CH_OPEN) + ": " + pick("ch-c:"+title, CH_CLOSE) + ".").format(t=title)
def compose_dash_intro(title):
    return (pick("da-o:"+title, DA_OPEN) + ": " + pick("da-c:"+title, DA_CLOSE) + ".").format(t=title)
def compose_hard_intro(title):
    return (pick("ha-o:"+title, HA_OPEN) + " — " + pick("ha-c:"+title, HA_CLOSE) + ".").format(t=title)
def compose_flow_para(title):
    return (pick("fl-o:"+title, FL_OPEN) + ": " + pick("fl-c:"+title, FL_CLOSE) + ".").format(t=title)
def compose_job_close(title):
    return (pick("jc-o:"+title, JC_OPEN) + " — " + pick("jc-c:"+title, JC_CLOSE) + ".").format(t=title)


# ── parameterized per-page framing (hash-picked so pages never share verbatim lines) ──

DASH_NOTE_VARIANTS = [
    "Reference posture for the operating console stood up in week two — {t} edition. Tiles bind to the gates below; log rows are the event shapes that reach the on-call channel.",
    "The console view {t} runs against: tiles are commit levels, bars are gate progress, and the log vocabulary matches the runbook your team inherits.",
    "Week-two operating view for {t}. The tiles carry the service's commit levels; the bars show gate position; the log rows are the shapes that page the on-call rota.",
    "How {t} reports to its owners: KPI tiles per judged metric, gate bars for release state, and log rows shaped like the channel your team will actually read at 3am.",
    "Reference console for {t} — the same tiles, gates and log vocabulary the delivery team runs internally, handed over as part of the build.",
    "The operating surface for {t}: each tile binds to a gate below, each bar is release position, and the log rows use the runbook's own vocabulary.",
    "This is {t} reporting honestly: commit levels as tiles, release position as bars, and a log whose shapes match the runbook handed over at exit.",
    "The console your team gets with {t} — same tiles, same gates, same log grammar the delivery team used to run it, now yours to operate.",
    "Reference operating view for {t}: tiles bind to the gates below and the log rows are the event shapes that page people — nothing decorative.",
]
REF_CAPTION_VARIANTS = [
    "Reference engineering bands for {t} — design targets this service is built and gated against, not client-reported outcomes.",
    "Design targets, not results: these are the levels {t} is engineered and gated to. Client numbers stay with the client, always.",
    "The bands {t} is designed against — stated as targets so nobody mistakes them for client figures or unverifiable benchmarks.",
    "Honest numbers: every point is a design target or reference band for {t}, captioned as such because the difference matters.",
    "Engineering targets for {t}, re-baselined when the estate changes — not client outcomes, and never presented as benchmark wins.",
    "What {t} is built to: these bands are the gated design targets, clearly marked as ours — the client's own figures are never repurposed here.",
    "Targets, plainly labeled: the series below shows where {t} is engineered to land, and the caption exists so nobody reads targets as results.",
]
HERO_SUFFIX_VARIANTS = [
    "Built under the same gates as every service here — and on {t} that means the baseline is signed first, releases are evidenced, and the handover ships a runbook.",
    "Shipped with the gate model attached: on {t}, the baseline is signed before build, releases clear named gates, and the runbook arrives with the keys.",
    "Delivered the house way for {t} — a signed baseline metric, gates with named evidence, and a system your engineers can run without us in the room.",
    "Same operating discipline as the rest of the estate, applied to {t}: baseline before build, evidence before release, runbook at handover.",
    "On {t}, engagement follows the house rules: the metric is signed up front, releases clear named gates, and the console ships with the code.",
    "Delivered against gates, not promises — {t} gets a signed baseline, named evidence per gate, and a runbook your team can operate on a bad day.",
    "The gates apply here too: {t} starts from a signed baseline, releases on evidence, and hands over a console your team already knows how to read.",
    "Engaged like every practice in this tower — {t} begins with the signed metric, clears gates with named evidence, and ends with a handover, not a farewell.",
]
CONTROLS_NOTE_VARIANTS = [
    "Every control above is evidenced in the gate reviews — the artifact list doubles as the audit checklist for {t}.",
    "Gate reviews test these controls directly; the artifacts you hold from {t} are the same evidence an auditor will ask for.",
    "On {t}, each control maps to a check in the gate reviews — no control exists that cannot produce its evidence artifact.",
    "These controls are gate-bound on {t}: reviews test them, and the evidence pack you receive doubles as the audit trail.",
    "Each control here has an owner, a check and an artifact on {t} — the checklist an auditor sees is the one your team runs.",
    "For {t}, controls ship as part of the build and carry their evidence through the gates — nothing is promised on paper alone.",
    "The controls above on {t} are testable by design: run the check, keep the artifact, and the audit answer is already in the handover pack.",
    "Nothing on this list is aspirational for {t} — each control has an owner, a working check, and an artifact your reviewers can pull on demand.",
]
CTA_BANK = [
    "Bring the metric this page is written around to a briefing — we will map your estate against the architecture above and tell you which gate you would fail first.",
    "If two or three rows in the failure table read like your last post-mortem, that is the fastest signal we know: bring the post-mortem, and we will bring the countermeasures and a delivery plan.",
    "The fastest next step is the two-week diagnostic: it produces the signed baseline, the gate map above filled in for your estate, and a build order with owners.",
    "Book the briefing with this page open — the architecture section doubles as the agenda, and the first hour usually ends with the baseline metric chosen.",
    "Start with the two-week diagnostic. It ends with a signed baseline and every gate on this page scored against your estate — fund or stop on evidence.",
    "Bring your hardest failure mode from the table above to a briefing; we will show you the countermeasure running and the gate that proves it works.",
    "The briefing is technical by design: bring an engineer, leave with the architecture mapped to your estate and a build order with named owners.",
    "One hour, this architecture, your estate: the briefing ends with the baseline metric picked and the first gate date pencilled in.",
    "If the dashboard above looks like the reporting your program already owes someone, that is the point — bring it to a briefing and we will wire it for real.",
    "Skip the discovery deck: run the two-week diagnostic, and the pages above become your build order with owners and gate dates attached.",
    "Bring the console to your next steering meeting — then book the briefing, and we will tell you honestly which gates you would fail today.",
    "The honest entry point is the diagnostic: two weeks, one signed baseline, and the gate map above filled in for your systems — then you decide.",
]

def dash_note_for(title):
    return pick("dashnote:" + title, DASH_NOTE_VARIANTS).format(t=title)

def ref_caption_for(title):
    return pick("refcap:" + title, REF_CAPTION_VARIANTS).format(t=title)

def hero_suffix_for(title):
    return pick("herosuf:" + title, HERO_SUFFIX_VARIANTS).format(t=title)

def controls_note_for(title):
    return pick("ctrlnote:" + title, CONTROLS_NOTE_VARIANTS).format(t=title)

# expanded narrative banks (title-token parameterized where noted)
HARD_INTRO = HARD_INTRO + [
    "Every practice here keeps a countermeasure register; for this page the patterned failures are the four below, each with a fix that ships in the build.",
    "We publish failure modes before writing code — it is cheaper to argue about this table in a briefing than to discover the same rows in production.",
    "The rows below come from programs like yours, stated plainly: what breaks, how it shows up on a dashboard, and what we build so it cannot repeat.",
]
DASH_INTRO = DASH_INTRO + [
    "The console below is scoped from the metrics the service is judged on — if a tile would not survive a steering meeting, it is not on the dashboard.",
    "Reference view, built like the real thing: tiles for the judged metrics, bars for gate position, and a log shaped to match the runbook handed over at exit.",
    "This is the operating contract rendered as a console: what we commit to (tiles), where releases stand (bars), and what pages people (log).",
]
CHART_INTRO = CHART_INTRO + [
    "Numbers belong on charts, and honesty belongs in captions: what follows are design targets and reference bands this service is gated to — clearly not client results.",
    "The profile below is the working posture for this service — targets we hold ourselves to, published so you can challenge them before the build starts.",
]
FLOW_PARA = FLOW_PARA + [
    "The diagram below separates request flow, control flow and evidence flow — three different lifetimes that teams routinely conflate until an audit disagrees.",
    "Read the flow as ownership: every arrow names the component that holds state, the policy that can stop it, and the timeout that bounds it.",
    "This is the unit-of-work journey from entry to evidence — where validation happens, where enrichment happens, and where the audit row is written.",
]
INTEG_INTRO = INTEG_INTRO + [
    "No practice ships as an island: the seams below are contracted early — direction, schema, identity and failure behavior per integration.",
    "Integration is where schedules slip, so the seams below carry contracts from week one: who calls whom, with what schema, and what happens when it fails.",
]
CONTROL_INTRO = CONTROL_INTRO + [
    "Governance arrives wired into the gates, not as a binder: every control below has an owner, a check, and an evidence artifact you will hold at exit.",
    "The overlay below is deliberately thin and testable — controls your team can evidence in an afternoon, wired to the same gates as the build.",
]

# ── block builders ──────────────────────────────────────────────────────────

def b_p(x): return {"t": "p", "x": x}

def b_h2(x): return {"t": "h2", "x": x}

def b_table(caption, headers, rows): return {"t": "table", "caption": caption, "headers": headers, "rows": rows}

def b_bullets(items): return {"t": "bullets", "items": items}

def b_note(x): return {"t": "note", "x": x}

def b_cta(x): return {"t": "cta", "x": x}

def b_diagram(kind, title, labels, note): return {"t": "diagram", "kind": kind, "title": title, "labels": labels, "note": note}

def b_arch(title, lanes, nodes, edges, note):
    return {
        "t": "arch", "title": title, "lanes": lanes,
        "nodes": [{"id": nid, "lane": lane, "label": label, **({"hot": True} if hot else {})}
                  for nid, lane, label, hot in nodes],
        "edges": [{"a": a, "b": bb, **({"label": lab} if lab else {})} for a, bb, lab in edges],
        "note": note,
    }

def b_dash(title, kpis, gates, log, note):
    return {
        "t": "dash", "title": title,
        "kpis": [{"label": k, "value": v, "delta": d, "dir": dr} for k, v, d, dr in kpis],
        "gates": [{"name": n, "pct": p} for n, p in gates],
        "log": [{"t": t, "tag": tg, "msg": m} for t, tg, m in log],
        "note": note,
    }

def b_chart(title, variant, cats, series, unit=None, yMax=None, note=None, caption=None):
    d = {"t": "chart", "title": title, "variant": variant, "cats": cats,
         "series": [{"name": n, "points": p} for n, p in series]}
    if unit: d["unit"] = unit
    if yMax: d["yMax"] = yMax
    if note: d["note"] = note
    if caption: d["caption"] = caption
    return d

REF_BAND_CAPTION = ("Reference engineering bands — design targets this service is built and gated "
                    "against. Not client-reported outcomes; client numbers stay with the client.")
DASH_NOTE = ("Reference posture for the operating console we stand up in week two. Tiles bind to the "
             "gates below; log rows are the event shapes that reach the on-call channel.")
