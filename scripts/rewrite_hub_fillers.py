#!/usr/bin/env python3
"""Replace the generic 'How this section is organized' / 'Choosing an entry point'
boilerplate on the five hub pages with page-specific human copy."""
import json

REPL = {
    "platforms": {
        "h2a": "Eight platforms, one governed stack",
        "pa": ("Each platform packages a patented method family as a product you can run: "
               "Nexus decides in milliseconds with a replayable trail, Forge keeps the lakehouse "
               "contracted and affordable, Swarm runs agent fleets inside policy envelopes, Sentinel "
               "encrypts collaboration, Twinverse mirrors physical operations, Quanta benchmarks every "
               "optimization run against the best classical solver, Ledger makes records auditable, and "
               "Compass governs the whole decision estate."),
        "h2b": "Where to start",
        "pb": ("Start from the platform that matches the metric you are accountable for, or bring the "
               "use case to a briefing and we will show the same scenario running on your data rather "
               "than on a demo script."),
    },
    "services": {
        "h2a": "Eight towers, one delivery standard",
        "pa": ("Every tower runs on the same operating discipline: a named business metric signed "
               "before delivery, fortnightly evidence against the baseline, and a named control owner "
               "for everything regulated. The tower pages spell out the practice mix, the seniority you "
               "get on day one, and the handover artifacts you own at the end."),
        "h2b": "How to pick your tower",
        "pb": ("Pick the tower that owns your metric — AI outcomes live in Applied AI and Agentic AI, "
               "the decision substrate in Data & Lakehouse, the control surface in Cybersecurity, the "
               "estate in Cloud & Platform, the frontier in Quantum, trust records in Blockchain and the "
               "physical loop in IoT & Robotics."),
    },
    "industries": {
        "h2a": "Twelve industries, measured where it bites",
        "pa": ("Regulated industries get the strictest treatment first: banking and insurance pages "
               "lead with decision evidence, healthcare leads with clinical signal governance, public "
               "sector leads with auditability. Each industry page shows the programs we run there, the "
               "controls they live under, and the deltas the clients' own systems reported."),
        "h2b": "Your industry, your baseline",
        "pb": ("Open your industry, find the program closest to your problem, and bring the metric to "
               "a briefing — the two-week diagnostic that locked each baseline is the same one we would "
               "run for you."),
    },
    "solutions": {
        "h2a": "Solutions named for the problem, not the product",
        "pa": ("Every solution here is a full pattern: the decision being made, the data and models "
               "behind it, the controls that make it defensible in audit, and the measured delta when "
               "the pattern landed in production. Nothing is a slide-ware umbrella — each page names "
               "the systems it touches and the metric it moves."),
        "h2b": "Match your problem",
        "pb": ("Start from the problem your board is actually asking about — revenue mechanics, fraud "
               "and risk, throughput economics, or frontline leverage — and read the pattern end to end "
               "before you shortlist vendors."),
    },
    "insights": {
        "h2a": "Field notes from production, not a content calendar",
        "pa": ("These viewpoints come from the delivery floor: what shipped, what scaled, what stalled, "
               "and what we would do differently. Where a claim depends on a client number, the case "
               "page it comes from is linked — the reasoning chain is always walkable."),
        "h2b": "Where to begin",
        "pb": ("Start with the viewpoint closest to your current decision — retrieval economics, "
               "decision hubs versus model sprawl, process mining, or where quantum math pays back — "
               "then bring your own metric to a briefing."),
    },
}

for name, rep in REPL.items():
    p = f"/home/z/my-project/site/src/content/pages/{name}.json"
    d = json.load(open(p, encoding="utf-8"))
    blocks = d["blocks"]
    out, i = [], 0
    while i < len(blocks):
        b = blocks[i]
        x = b.get("x", "")
        if b.get("t") == "h2" and x == "How this section is organized":
            out.append({"t": "h2", "x": rep["h2a"]})
            i += 1
            # rewrite following p
            if i < len(blocks) and blocks[i].get("t") == "p":
                out.append({"t": "p", "x": rep["pa"]}); i += 1
        elif b.get("t") == "h2" and x == "Choosing an entry point":
            out.append({"t": "h2", "x": rep["h2b"]})
            i += 1
            if i < len(blocks) and blocks[i].get("t") == "p":
                out.append({"t": "p", "x": rep["pb"]}); i += 1
        else:
            out.append(b); i += 1
    d["blocks"] = out
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(name, "->", [b["x"][:44] for b in out if b.get("t") == "h2"])
