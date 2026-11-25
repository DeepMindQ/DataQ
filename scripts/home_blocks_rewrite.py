#!/usr/bin/env python3
"""Align home.json blocks with the rewritten HomeView copy (2026-11 rewrite).

The home template renders HomeView.tsx, not the blocks — but the blocks are
the page's canonical text layer (word counts, future re-renders). This patch
replaces the old "Ambition, engineered" copy with the plain-language copy now
visible on the page, keeping the block schema unchanged.
"""
import json

PATH = "/home/z/my-project/site/src/content/pages/home.json"

blocks = [
    {"t": "hero",
     "x": "We build, run and modernize the systems your business depends on. Dataq Software is a global IT "
          "services and consulting firm. From ERP and cloud to data, AI and security, we take on the programs "
          "enterprises depend on — and report every result against the business metric the program was funded "
          "to move."},
    {"t": "p",
     "x": "Dataq Software works on the estate enterprises actually run: SAP and ERP cores, enterprise data "
          "platforms and integrations, cloud infrastructure, and the AI now being layered on top of them. We "
          "advise, we build, and we run what we build. Delivery teams work onsite and offshore under one "
          "standard, managed operations run around the clock behind every program, and results are reported "
          "against the numbers agreed at the start."},
    {"t": "p",
     "x": "Eight proprietary platforms and eight patented method families give every engagement a configured "
          "starting point, so your budget goes to the work that is genuinely yours. Recent published results "
          "include 38% lower fraud losses at a top-10 European bank, OEE up 7.2 points across 14 plants at a "
          "global automotive OEM, and claims settled 55% faster at a top-5 global insurer."},
    {"t": "h2", "x": "What we do", "sub": "Eight expertise domains and a full consulting practice"},
    {"t": "p",
     "x": "Each domain pairs named practices with the platform they run on. Whichever door you enter, delivery "
          "follows the same rules: a named owner, a measurable result, and reporting against your own numbers. "
          "The consulting practice — transformation programs, migration factories, engineering pods, quality "
          "engineering, Azure estates, ERP cores, managed operations and end-user support — ends in delivery: "
          "the team that advises you is the team that builds it."},
    {"t": "bullets", "items": [
        ["Data, Analytics & Lakehouse", "Pipelines, lakehouse and governance: reports that reconcile, lineage you can trace, access under control."],
        ["Agentic AI & Hyperautomation", "Digital workers with defined roles, budgets and human checkpoints. Every action logged and reversible."],
        ["Applied AI & Generative AI", "Strategy, model selection, retrieval, evaluation and production operations. AI measured on the P&L."],
        ["Cybersecurity & Zero-Trust", "Identity-first architecture for people, machines and models, with detection and response in one program."],
        ["Cloud, Edge & Platform Engineering", "Hybrid and edge estates engineered for reliability and cost per workload, with platforms teams adopt."],
        ["IoT, Digital Twin & Robotics", "Sensor integration, digital twins and robotics: see, simulate and act on physical assets in one loop."],
        ["Blockchain & Digital Trust", "Permissioned networks, tokenization and verifiable credentials with the reporting supervisors expect."],
        ["Quantum & Advanced Compute", "Optimization, simulation and post-quantum migration where the mathematics pays back, benchmarked against classical methods."],
    ]},
    {"t": "h2", "x": "Global delivery model", "sub": "Onsite command, offshore scale, one delivery standard"},
    {"t": "p",
     "x": "Our teams work as one delivery organization: engineers who plug into your teams as extra capacity, "
          "while business ownership stays on your side. The same quality checks apply on both sides, so "
          "handovers stay clean across every geography. Four global delivery centers, 24x7 operations coverage "
          "and 40+ countries served."},
    {"t": "h2", "x": "Automation partnership", "sub": "RPA programs delivered end to end, with Automation Anywhere"},
    {"t": "bullets", "items": [
        ["Process analysis", "We measure which processes are worth automating before anything is built."],
        ["Vision & strategy", "Where robots pay for themselves first, and how the program scales from there."],
        ["Proof of concept", "A working robot on a real process, with the business case proven on live data."],
        ["Implementation", "Bots deployed into production under the same release checks as every build."],
        ["24x7 managed support", "Bots monitored, maintained and improved around the clock."],
    ]},
    {"t": "h2", "x": "Platforms & patented methods", "sub": "Every engagement starts from configured IP"},
    {"t": "p",
     "x": "Eight platforms, one job each: Nexus runs decisions, Forge runs data, Swarm runs agents, Sentinel "
          "guards access, Twinverse mirrors operations, Quanta readies compute, Ledger anchors trust and "
          "Compass keeps AI inspectable. Licensing is included in the engagement fee — and accelerators built "
          "specifically for you can carry co-ownership terms. The method families underneath are published in "
          "the patented-intelligence method map with their controls."},
    {"t": "h2", "x": "Case studies", "sub": "Client outcomes, with the numbers left in"},
    {"t": "p",
     "x": "Every case study in the library states what changed, by how much, and where it ran — indexed by "
          "industry and service area, each with the delivery notes behind the number."},
    {"t": "h2", "x": "How an engagement starts", "sub": "One page, signed in week two"},
    {"t": "p",
     "x": "The program charter records the metric the program must move, the owner of each control, and the "
          "boundaries of acceptable risk. Your board and your auditors read the same page delivery runs on. "
          "The metric is signed as a baseline in week two and reported every fortnight; if the owner changes, "
          "the baseline is re-signed before work continues."},
    {"t": "h2", "x": "Industries", "sub": "Where we work — and the rules you answer to"},
    {"t": "p",
     "x": "Twelve sectors, each brief mapping the regulations, systems and workflows your programs will touch: "
          "DORA for banking, Solvency II for insurance, HIPAA and GxP for healthcare, IEC 62443 for "
          "manufacturing, NERC CIP for energy, NIS2 for telecom, PCI DSS for retail and the rest."},
    {"t": "h2", "x": "Insights", "sub": "Field notes from live programs"},
    {"t": "p",
     "x": "What we are learning on live programs — retrieval layers, decision hubs, agent guardrails and the "
          "economics of GenAI — with the questions worth asking any vendor."},
    {"t": "cta",
     "x": "Tell us the outcome you need to move. We will show you the method, the platform and the plan we "
          "would sign against it — in a 45-minute briefing with a practice lead."},
]

with open(PATH, encoding="utf-8") as f:
    data = json.load(f)

data["blocks"] = blocks
words = 0
for b in blocks:
    words += len(str(b.get("x", "")).split())
    for it in b.get("items", []):
        words += sum(len(s.split()) for s in it)
data["words"] = words

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=1, ensure_ascii=False)

print(f"home.json blocks rewritten: {len(blocks)} blocks, ~{words} words")
