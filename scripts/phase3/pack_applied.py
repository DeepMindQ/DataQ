#!/usr/bin/env python3
"""Pack: Applied AI & Generative AI (dom=applied-ai-generative-ai)."""

DOM = "applied-ai-generative-ai"

HOOKS = {
    "banking-financial-services": "Research desks, contact centers and KYC teams need grounded answers with citations an examiner can trace — RAG with permission fidelity and eval discipline, not a chatbot bolted to a search box.",
    "insurance": "Underwriting submissions, claims notes and policy wordings hold the answers; the work is retrieval with strict citations to wording versions, plus dialog systems that keep adjusters in the loop.",
    "healthcare-life-sciences": "Clinical and administrative knowledge sits in guideline PDFs, EHR notes and payer policies — grounded generation with citation discipline, PHI redaction and clinician review at the right points.",
    "manufacturing": "SOPs, failure-mode libraries and quality records are the corpus, and vision systems read the line — value shows up as fewer repeat defects and faster root-cause, not as demos.",
    "retail-consumer-goods": "Product content, service dialogs and demand chat run at consumer scale — containment with dignity: the assistant handles the routine, the human gets the judgment call with context attached.",
    "telecom-media": "Care and activation dialogs, network runbooks and billing knowledge — containment and first-contact resolution on the care side, grounded retrieval for the agents who take escalations.",
    "energy-utilities": "Field crews and control rooms need procedures and asset history at the point of work — grounded retrieval with version control over the procedure corpus, and voice interfaces that survive gloves and noise.",
    "logistics-supply-chain": "Exception handling, customs knowledge and carrier rules live in documents — retrieval that answers what applies to this lane, with citations, plus document AI that reads the paperwork.",
    "public-sector": "Citizen services and caseworker support need grounded answers bound to statute versions and eligibility rules, with every answer citable for oversight and appeal.",
    "education-research": "Faculty, advisors and students need answers grounded in catalogs, policy and course content — with accessibility and academic-integrity guards designed in from the start.",
    "technology-saas": "Support, docs and success knowledge scale with ARR — containment and deflection measured against CSAT, with the eval suite gating every prompt and model change.",
    "agriculture-food": "Agronomy advice, subsidy rules and certification standards as grounded answers for co-ops and growers — multilingual, season-aware, and citable to the standard that governs the crop.",
}

KPIS = {
    "banking-financial-services": [
        ("Containment on tier-1 intents", 38, 64, "pct"),
        ("Citation coverage on answers", 96, 100, "pct"),
        ("Answer latency p95", 2, 6, "sec"),
    ],
    "insurance": [
        ("Submission auto-summary adoption", 44, 72, "pct"),
        ("Wording-citation fidelity", 98, 100, "pct"),
        ("Adjuster review time saved", 6, 18, "min"),
    ],
    "healthcare-life-sciences": [
        ("Clinician acceptance of grounded answers", 62, 84, "pct"),
        ("PHI redaction coverage", 100, 100, "pct"),
        ("Prior-auth packet prep time", 4, 12, "min"),
    ],
    "manufacturing": [
        ("First-pass extraction accuracy", 88, 97, "pct"),
        ("Root-cause search time cut", 30, 58, "pct"),
        ("Edge inference within deadline", 97, 100, "pct"),
    ],
    "retail-consumer-goods": [
        ("Dialog containment", 42, 68, "pct"),
        ("CSAT on contained sessions", 74, 88, "pct"),
        ("Dignified escalation quality", 90, 98, "pct"),
    ],
    "telecom-media": [
        ("Care containment", 36, 62, "pct"),
        ("FCR lift on assisted calls", 12, 30, "pct"),
        ("Runbook freshness SLA", 2, 12, "hrs"),
    ],
    "energy-utilities": [
        ("Procedure retrieval at point of work", 82, 95, "pct"),
        ("Version-stale answers blocked", 100, 100, "pct"),
        ("Hands-free voice-task completion", 76, 92, "pct"),
    ],
    "logistics-supply-chain": [
        ("Lane-rule answers with citations", 88, 97, "pct"),
        ("Exception-doc processing time cut", 28, 55, "pct"),
        ("Customs doc first-pass yield", 84, 95, "pct"),
    ],
    "public-sector": [
        ("Statute-bound answer coverage", 90, 98, "pct"),
        ("Citable decision trail", 100, 100, "pct"),
        ("Caseworker research time cut", 24, 48, "pct"),
    ],
    "education-research": [
        ("Adviser-grounded query resolution", 64, 86, "pct"),
        ("Academic-integrity guard enforcement", 98, 100, "pct"),
        ("Faculty admin time returned", 3, 9, "hrs"),
    ],
    "technology-saas": [
        ("Support containment", 44, 70, "pct"),
        ("Eval-suite gate coverage", 100, 100, "pct"),
        ("Docs answer freshness", 1, 8, "hrs"),
    ],
    "agriculture-food": [
        ("Advisory answer acceptance", 68, 88, "pct"),
        ("Standard-citation fidelity", 97, 100, "pct"),
        ("Multilingual query coverage", 85, 97, "pct"),
    ],
}

SYSTEMS = {
    "banking-financial-services": ["Research portals and policy corpora", "Model-risk evidence (SR 11-7)", "Contact-center stacks (Genesys-class)"],
    "insurance": ["PAS/claims document estates", "Versioned wording libraries", "Adjuster workbenches"],
    "healthcare-life-sciences": ["Clinical guidelines + payer policy", "EHR notes via HL7 FHIR", "PHI de-identification pipeline"],
    "manufacturing": ["SOP / FMEA corpora", "Quality records (eDHR)", "Plant-floor capture (vision)"],
    "retail-consumer-goods": ["Commerce and CX platforms", "Versioned knowledge bases", "CRM agent desktops"],
    "telecom-media": ["Care platforms and runbooks", "Billing/CRM knowledge", "TM Forum API surfaces"],
    "energy-utilities": ["Versioned procedure management", "Asset history (EAM)", "Field tablets, hands-free UI"],
    "logistics-supply-chain": ["Customs and lane-rule corpora", "TMS exception queues", "Document-AI intake"],
    "public-sector": ["Statute and eligibility corpora", "Case-management systems", "Oversight/appeal evidence"],
    "education-research": ["Catalogs, policy, course content", "LMS/SIS estates", "Integrity and accessibility guards"],
    "technology-saas": ["Docs and support knowledge", "Eval CI on prompts/models", "Helpdesk stacks (Zendesk-class)"],
    "agriculture-food": ["Agronomy and subsidy corpora", "Certification standards (GLOBALG.A.P.)", "Multilingual advisory channels"],
}

COMMON_SUBS = {
    "Schema contracts": "typed corpus + tool surfaces",
    "Vector + lexical index": "BM25 + dense, hybrid ranked",
    "Permission map": "ACL-folded retrieval, enforced",
    "Grounded RAG service": "citations on every answer",
    "Eval harness": "golden set, CI-gated",
    "Model registry": "versioned, signed lineage",
    "Evidence store": "sealed per-answer packets",
    "Semantic cache": "content-hash keyed, TTL'd",
    "Guardrail stack": "topic, PII, injection guards",
    "Prompt & eval repo": "versioned, peer-reviewed",
    "Inference gateway": "routed, metered, budgeted",
    "Retrieval planner": "query decomposition + routing",
    "Hybrid index (BM25+dense)": "fusion with rerank",
    "Canonical registry": "one URI per fact",
    "Grounded generation": "no cite, no answer",
    "Confidence gating": "route, do not guess",
    "Trace store": "prompt + context + output",
    "PII scan": "detect + redact at ingest",
    "Drift monitors": "eval score + cost drift",
    "Model router": "class of service per intent",
    "Budgets & cutoffs": "per-use-case spend ceilings",
    "Cost meter": "tokens, cache hits, egress",
    "Model judges": "LLM-jury, calibrated",
    "Cross-encoder rerank": "top-k precision layer",
    "Eval set v1": "golden questions, versioned",
    "Baseline collection": "human time, measured",
}

PAGES = {
    "services_applied-ai-generative-ai": {
        "archsubs": {
            "Schema contracts": "typed corpus + tool surfaces",
            "Vector + lexical index": "BM25 + dense, hybrid ranked",
            "Permission map": "ACL-folded, query-time enforced",
            "Grounded RAG service": "no cite, no answer",
            "Eval harness": "golden set, CI-gated",
        },
        "badges": [
            ("Citation coverage", "100%"),
            ("Eval-gated releases", "all"),
            ("Industries served", "12"),
        ],
        "deep": {
            "h2": "The evaluation discipline is the product",
            "sub": "Golden sets, calibrated LLM juries and CI gates — why this domain ships reliability instead of demos",
            "paras": [
                "Generative programs fail at evaluation, not at generation: models answer everything, so teams stop asking whether the answer is right. The domain standard is an eval harness treated like a test suite — a versioned golden set per use case, LLM-jury scoring calibrated against human-labeled samples, and hard CI gates that block any prompt, model or index change that moves the wrong metric. Jury calibration is the craft: the judge model is scored against human labels every quarter, and its agreement is reported alongside the metric it certifies, because an uncalibrated judge certifies nothing.",
                "The second discipline is permission fidelity. Enterprise retrieval fails quietly when the index leaks a document the asker cannot legally read — so the permission map is folded into retrieval at query time, not filtered after generation, and every answer carries citations to the passages it used. The trace store keeps prompt, context and output for every answer, which turns 'the model said so' into an examinable artifact. That combination — evaluated, permissioned, cited — is what separates a production program from a stalled pilot.",
            ],
            "bullets": [
                ("Golden sets per use case", "Versioned question sets with labeled answers; the bar any release must clear."),
                ("Calibrated LLM juries", "Judge agreement against human labels reported quarterly — uncalibrated judges certify nothing."),
                ("CI gates on every change", "Prompt, model or index edits run the harness; regressions block the merge."),
                ("Permission-folded retrieval", "ACLs enforced at query time; citations prove what the answer saw."),
            ],
        },
        "heads": {
            "Seven practices, one evaluation discipline": ("Seven practices, one evaluation discipline", "Corpus to cited answer, PoC to platform, tuning to vision — every practice ships behind eval gates"),
            "What separates a production program from a stalled pilot": ("What separates a production program from a stalled pilot", "The four program properties we install: eval gates, permission fidelity, cost ceilings, named owners"),
            "The domain reference architecture — from corpus to cited answer": ("The domain reference architecture — from corpus to cited answer", "Ingest, index, permission, generation and evidence as one governed path"),
            "The domain on one screen — commitments, releases, decisions": ("The domain on one screen — commitments, releases, decisions", "Console-backed view of quality, cost and release posture"),
            "Capability posture and where the bar sits": ("Capability posture — and where the bar sits", "What we hold to be table stakes in 2026, and what still deserves a PoC"),
            "Sector depth — where Applied AI runs deepest today": ("Sector depth — where Applied AI runs deepest today", "Twelve-industry lens with targets we sign against and the sector briefs behind them"),
            "How engagements run in this domain": ("How engagements run in this domain", "Weekly evidence cadence, eval-first scoping, named metric owners"),
            "Domain-level release gates": ("Domain-level release gates", "The evidence each gate demands; nothing advances on narrative"),
        },
    },

    "services_applied-ai-generative-ai_ai-poc-value-validation": {
        "archsubs": {
            "Provability canvas": "metric + method + baseline",
            "Real data path": "production-shaped, governed",
            "Baseline collection": "human time, measured",
            "Eval set v1": "golden questions, versioned",
            "Integration probe": "just enough production honesty",
            "Fund / kill gate": "verdict with named owner",
        },
        "badges": [
            ("Sprint length", "4 weeks"),
            ("Verdicts with baselines", "100%"),
            ("Data path fidelity", "production-shaped"),
        ],
        "deep": {
            "h2": "A PoC verdict is an instrument reading",
            "sub": "The measurement discipline that makes a four-week verdict defensible in a steering committee",
            "paras": [
                "Most PoCs measure the wrong thing: demo delight instead of decision-grade deltas. The sprint is instrumented from day one — a provability canvas fixes the metric, the measurement method and the baseline before any model runs; baseline collection measures the human work the model would replace (minutes per case, error rates, rework shares); and the real data path runs production-shaped data under production-shaped governance, so the verdict survives contact with the estate. An integration probe touches at least one real system, because the honest friction — auth, schemas, latency — is where PoC timelines actually die.",
                "The fund/kill gate is the product. At week four the steering committee reads three numbers: delta against baseline on the golden set, cost per unit of work at sprint scale, and the integration gaps with named owners. Fund means a funded delivery slice with a metric; kill means a documented kill reason in the ledger — and both are wins, because the cheapest failed project is the one that costs four weeks.",
            ],
            "bullets": [
                ("Provability canvas first", "Metric, method and baseline signed before a model runs."),
                ("Real data path", "Production-shaped data under governance; synthetic only where PHI/PII forbids."),
                ("Integration probe", "One real system, early — friction is evidence, not noise."),
                ("Fund/kill with named owner", "Three numbers at the gate; kill reasons logged like fund decisions."),
            ],
        },
        "heads": {
            "A PoC exists to produce a decision, not a demo": ("A PoC exists to produce a decision, not a demo", "Four weeks, instrumented end to end, ending in a fund/kill verdict with named owners"),
            "Four ways PoCs become demo-ware": ("Four ways PoCs become demo-ware", "No baseline, no real data, no integration probe, no verdict owner — and the fix for each"),
            "Reference architecture — the four-week evidence machine": ("Reference architecture — the four-week evidence machine", "Canvas, data path, eval set and probe arranged to produce decision-grade evidence"),
            "The sprint path — from kickoff to verdict": ("The sprint path — from kickoff to verdict", "Week-by-week instrumentation, from canvas signing to gate reading"),
            "The sprint console — verdicts, not velocity": ("The sprint console — verdicts, not velocity", "Delta, unit cost and integration gaps as the standing scoreboard"),
            "Where PoC ideas actually die": ("Where PoC ideas actually die", "The kill-reason distribution across sprints — and why kills are the cheap outcome"),
            "Sprint stack defaults — and deliberate deviations": ("Sprint stack defaults — and deliberate deviations", "The default sprint stack, and where we sign deviations"),
            "Sprint gates — the evidence a verdict carries": ("Sprint gates — the evidence a verdict carries", "What each gate demands before the next week starts"),
            "What you hold at verdict time": ("What you hold at verdict time", "Baseline, golden set, cost model, gap list — the artifacts a decision needs"),
            "The four weeks, gate by gate": ("The four weeks, gate by gate", "Canvas, data, eval, verdict — with exit evidence per gate"),
            "Integration surface — just enough production to be honest": ("Integration surface — just enough production to be honest", "The probe boundary: real enough to trust, small enough to bound"),
            "Sprint governance — production-grade data handling in miniature": ("Sprint governance — production-grade data handling in miniature", "The data controls a four-week sprint still carries"),
        },
    },

    "services_applied-ai-generative-ai_conversational-ai-digital-humans": {
        "archsubs": {
            "Intent & state tracker": "typed slots, repair loops",
            "Dialogue policy": "goal-first, dignity-preserving",
            "Grounded retrieval": "policy-cited answers",
            "Topic & PII guards": "pre-gen filter chain",
            "Dialogue eval": "containment + trust, paired",
        },
        "badges": [
            ("Containment target", "56%"),
            ("Escalation with context", "100%"),
            ("Guard chain", "pre-generation"),
        ],
        "deep": {
            "h2": "Escalation is the moment the product is judged",
            "sub": "Dignified handoff design — what the human sees, and why containment without it is a churn machine",
            "paras": [
                "Containment numbers collapse in board reviews because they hide the escalation: a session the bot 'contained' but the customer experienced as stonewalling shows up later as churn, complaint volume and agent handle-time inflation. We therefore design the handoff as a first-class surface — the agent desktop receives the transcript, the detected intent, the customer's history and the bot's confidence, and the dialog policy chooses the handoff wording, never dumping the customer into a queue with 'transfer' as the last message. Containment and CSAT are measured as a pair per intent family; a family that gains containment while losing CSAT gets its policy rewritten, not its threshold raised.",
                "The guard chain runs before generation: topic bounds, PII filters and injection defenses are pre-generation filters, not post-hoc apologies. Barge-in and VAD tuning are treated as first-class engineering — voice containment dies at double-detection latency — and the dialog eval suite replays real transcript samples every release, because dialog quality drifts with every prompt edit.",
            ],
            "bullets": [
                ("Dignified handoff by design", "Transcript, intent, history and confidence reach the human — never a bare transfer."),
                ("Containment × CSAT, paired", "Measured per intent family; policy rewritten when the pair diverges."),
                ("Pre-generation guard chain", "Topic, PII and injection filters run before tokens are produced."),
                ("Voice engineering as first-class", "Barge-in, VAD and latency budgets tuned like any other p95."),
            ],
        },
        "heads": {
            "Containment and trust are one metric, not two": ("Containment and trust are one metric, not two", "Measured as a pair per intent family — divergence triggers policy rework, not threshold moves"),
            "Four failure modes that inflate containment and destroy trust": ("Four failure modes that inflate containment and destroy trust", "Stonewalling, ghost transfers, guard theater and unowned drift — with shipped countermeasures"),
            "Reference architecture — grounded dialog with dignified escalation": ("Reference architecture — grounded dialog with dignified escalation", "State tracking, grounded retrieval, pre-generation guards and the handoff surface"),
            "A conversation's lifecycle, turn by turn": ("A conversation's lifecycle, turn by turn", "From barge-in-tuned capture to sealed trace with citations"),
            "The conversation console — containment with its cost visible": ("The conversation console — containment with its cost visible", "Containment, CSAT and escalation quality on one surface"),
            "The containment–satisfaction frontier by intent family": ("The containment–satisfaction frontier by intent family", "Where each family sits, and which policies move it"),
            "Dialog stack defaults — and when we deviate": ("Dialog stack defaults — and when we deviate", "The default stack, and the deviations we sign for"),
            "Dialog release gates — what blocks a channel launch": ("Dialog release gates — what blocks a channel launch", "Eval replays, guard tests and handoff quality before a channel opens"),
            "What the contact center inherits": ("What the contact center inherits", "Consoles, intent taxonomy, policy repo and the drift watch"),
            "Channel build-out, week by week": ("Channel build-out, week by week", "Voice first or chat first — the sequencing logic"),
            "Integration surface — telephony, CRM and the agent desktop": ("Integration surface — telephony, CRM and the agent desktop", "Where dialogs touch the estate, typed throughout"),
            "Dialog governance — consent, guard decisions, trace retention": ("Dialog governance — consent, guard decisions, trace retention", "The audit trail a regulated channel carries"),
        },
    },

    "services_applied-ai-generative-ai_enterprise-ai-strategy": {
        "archsubs": {
            "Provability screen": "metric before mandate",
            "Risk tiering": "class-of-service gates",
            "Platform direction memo": "buy/build/partner with reasons",
            "Funded delivery slices": "quarterly, metric-bound",
            "KPI ledger": "every funded idea, tracked",
        },
        "badges": [
            ("Ideas priced at intake", "100%"),
            ("Kill criteria at funding", "always"),
            ("Board reporting", "quarterly"),
        ],
        "deep": {
            "h2": "The portfolio is priced at intake",
            "sub": "Expected-value discipline — why funded slices carry kill criteria and the ledger never closes",
            "paras": [
                "AI strategy fails as a roadmap because roadmaps promise; portfolios price. Every idea enters the intake with a value hypothesis and a cost class, gets a provability screen (what metric would move, measured how), and lands in a risk tier that dictates its evidence bar. Funded delivery slices are quarterly and metric-bound: each carries explicit kill criteria — the numbers that, unmet, stop the spend — and the KPI ledger tracks every funded idea from funding to retirement, so the steering committee argues from a ledger instead of from enthusiasm.",
                "The platform direction memo is the quiet core of the engagement: buy, build or partner per capability, with the reasoning written down and revisited on dates, not vibes. The audit trail matters more than the memo — the record of what was funded, killed and why is the artifact boards, auditors and (eventually) regulators read, and it is generated continuously by the governance surface rather than reconstructed after the fact.",
            ],
            "bullets": [
                ("Priced at intake", "Value hypothesis + cost class + provability screen before anything is funded."),
                ("Risk-tiered evidence bars", "Class of service dictates gates; high-risk ideas carry supervisory-grade evidence."),
                ("Kill criteria at funding", "Every slice ships with the numbers that stop it — decided while calm."),
                ("A living KPI ledger", "Funded, killed and retired ideas tracked continuously; the audit trail is the asset."),
            ],
        },
        "heads": {
            "Why AI strategy is a portfolio problem, not a roadmap": ("AI strategy as a portfolio problem — not a roadmap", "Priced ideas, tiered evidence bars and kill criteria beat promised timelines"),
            "Four ways AI portfolios stall at the board level": ("Four ways AI portfolios stall at the board level", "Unpriced enthusiasm, missing kill criteria, platform capture, silent ledgers"),
            "Reference architecture — the decision system behind the portfolio": ("Reference architecture — the decision system behind the portfolio", "Intake, screens, tiers and the ledger as one governed decision system"),
            "From idea intake to funded slice": ("From idea intake to funded slice", "The path an idea walks, with the evidence each step leaves"),
            "The portfolio console the steering committee reads": ("The portfolio console the steering committee reads", "Funded, killed and verdicts on one surface"),
            "Portfolio shape across quarters": ("Portfolio shape across quarters", "How the mix of bets shifts as evidence accumulates"),
            "Standards the portfolio runs on — and where we deviate": ("Standards the portfolio runs on — and where we deviate", "The standing standards, and the deviations we sign"),
            "Portfolio gates — the evidence each rung demands": ("Portfolio gates — the evidence each rung demands", "Screen, tier, slice, scale — what each rung requires"),
            "What the executive team owns at the end": ("What the executive team owns at the end", "The ledger, the standards and the standing cadence"),
            "How the strategy engagement runs": ("How the strategy engagement runs", "Interviews, intake design, first board cycle — the shape of the work"),
            "Integration surface — finance, risk and the PMO": ("Integration surface — finance, risk and the PMO", "Where portfolio data lands in the corporate machinery"),
            "Decision governance — the audit trail of funded and killed ideas": ("Decision governance — the audit trail of funded and killed ideas", "What the record shows, and who can read it"),
        },
    },

    "services_applied-ai-generative-ai_genai-platform-engineering": {
        "archsubs": {
            "Inference gateway": "routed, metered, budgeted",
            "Use-case authz": "per-use-case scopes",
            "Semantic cache": "content-hash keyed, TTL'd",
            "Model registry": "versioned, signed lineage",
            "Prompt & eval repo": "versioned, peer-reviewed",
            "Guardrail stack": "pre-generation filters",
            "Budgets & cutoffs": "spend ceilings, loud trips",
        },
        "badges": [
            ("Cache hit rate target", "34%"),
            ("Cost per answer, metered", "per use case"),
            ("Guard chain", "pre-generation"),
        ],
        "deep": {
            "h2": "The gateway is the product",
            "sub": "Routing, caching, budgeting and guardrails as one governed surface — and the economics that prove it",
            "paras": [
                "GenAI platforms justify themselves in month three, when the first per-team invoices land. The design that survives is the governed gateway: every request enters through one surface that routes by class of service, enforces use-case authz, applies the guard chain before generation, and meters cost per use case — so finance reads an allocation, engineering reads a router config, and neither reads a spreadsheet reconciliation. The semantic cache is the silent margin-maker: content-hash keyed, TTL-bounded and eval-safe, it turns repeated enterprise queries into a fraction of their token cost.",
                "Budgets and cutoffs are policy, not dashboards. Each use case carries a spend ceiling with a loud trip — the circuit breaker pattern the agent runtime uses — and the model registry pins versions with signed lineage, because a silent model swap is a compliance event wearing a deploy. The platform release gate asks one question: can a consuming team ship a use case without touching the platform team? If the answer is no, the golden path is not done.",
            ],
            "bullets": [
                ("One governed door", "Routing, authz, guards and metering at the gateway; nothing bypasses."),
                ("Semantic cache as margin", "Content-hash keyed and TTL-bounded; eval-safe by construction."),
                ("Budgets that trip loudly", "Per-use-case ceilings with circuit breakers — cost control is policy."),
                ("Signed model lineage", "Registry pins versions; a silent swap is a compliance event."),
            ],
        },
        "heads": {
            "The platform economics nobody prices until month three": ("The platform economics nobody prices until month three", "Metering, caching and allocation designed in — before the first invoice lands"),
            "Four ways GenAI platforms blow their mandate": ("Four ways GenAI platforms blow their mandate", "Bypass culture, unbudgeted spend, silent swaps, guardrail debt"),
            "Reference architecture — the governed model gateway": ("Reference architecture — the governed model gateway", "Gateway, registry, guard chain and the metering spine"),
            "A request through the governed door": ("A request through the governed door", "The hop-by-hop path, with the checks each hop runs"),
            "The platform console finance and engineering share": ("The platform console finance and engineering share", "Cost, latency and guard events on one surface"),
            "Cost and latency posture across load tiers": ("Cost and latency posture across load tiers", "How the posture holds as concurrency climbs"),
            "Default platform components — and the deviations we allow": ("Default platform components — and the deviations we allow", "The default stack, and where we sign deviations"),
            "Platform release gates — evidence before exposure": ("Platform release gates — evidence before exposure", "What must be proven before a use case is exposed"),
            "What the platform team hands over": ("What the platform team hands over", "Golden paths, runbooks, registry and the budget policy"),
            "The platform build, sprint by sprint": ("The platform build, sprint by sprint", "Gateway first, guardrails second, golden paths third"),
            "Integration surface — identity, finance and every consuming team": ("Integration surface — identity, finance and every consuming team", "IdP, chargeback systems and the consumer contract"),
            "Governance enforced once, inherited by every consuming team": ("Governance enforced once, inherited by every consuming team", "Why the gateway beats per-team policy"),
        },
    },

    "services_applied-ai-generative-ai_llm-fine-tuning-ops": {
        "archsubs": {
            "Decontamination": "eval leakage, blocked",
            "Trainer (LoRA/full)": "budget-matched method",
            "Multi-task eval matrix": "per-task regression gates",
            "Model registry": "signed dataset lineage",
            "Drift watch": "score + cost drift",
        },
        "badges": [
            ("Eval leakage tolerance", "0"),
            ("Regression gates per task", "all"),
            ("Canary before promotion", "always"),
        ],
        "deep": {
            "h2": "Decontamination is the first gate",
            "sub": "Dataset engineering as the program — leakage tests, task matrices and the promotion path",
            "paras": [
                "Tuned models fail quietly through contamination: eval questions leaking into training data make the golden set flatter than reality, and the regression appears only in production phrasing. The factory therefore runs decontamination as a hard gate — n-gram and embedding-similarity scans against every eval split, with provenance recorded per document — before any GPU hour is spent. The multi-task eval matrix then protects against the classic LoRA failure: gains on the target task that quietly degrade general capability, so every candidate runs the full matrix and regression on any off-task domain blocks promotion.",
                "Method selection is budget-matched engineering, not fashion: LoRA for narrow style/format shifts, full tuning when behavior must move and data supports it, distillation when serving cost dominates. The registry carries signed dataset lineage — every training document traceable to its source and license class — and the promotion path ends in a canary ring before estate-wide serving, because the last mile of a tune is operational, not academic.",
            ],
            "bullets": [
                ("Hard decontamination gate", "n-gram + embedding scans against eval splits; provenance per document."),
                ("Multi-task regression matrix", "Off-task degradation blocks promotion, not just target-task gains."),
                ("Budget-matched methods", "LoRA, full or distillation chosen by behavior delta and serving cost."),
                ("Signed dataset lineage", "Every document traceable to source and license; audit-ready."),
            ],
        },
        "heads": {
            "Fine-tuning is a data engineering program that occasionally involves a GPU": ("Fine-tuning as a data-engineering program — the GPU is the smallest part", "Dataset quality, leakage discipline and eval matrices decide the outcome"),
            "Four ways tuning programs produce quietly bad models": ("Four ways tuning programs produce quietly bad models", "Contamination, off-task regressions, unsigned lineage, no canary"),
            "Reference architecture — the tuning factory from dataset to canary": ("Reference architecture — the tuning factory from dataset to canary", "Curate, decontaminate, train, evaluate, canary — as one pipeline"),
            "The promotion path — dataset to production traffic": ("The promotion path — dataset to production traffic", "Gates from data freeze to estate-wide serving"),
            "The model-ops console for tuned fleets": ("The model-ops console for tuned fleets", "Scores, costs and drift for every tuned candidate"),
            "Quality retention against serving cost across model sizes": ("Quality retention against serving cost across model sizes", "The frontier the fleet actually sits on"),
            "Training and serving defaults — and when we deviate": ("Training and serving defaults — and when we deviate", "The default factory config, and the deviations we sign"),
            "Model promotion gates — what evidence blocks a bad tune": ("Model promotion gates — what evidence blocks a bad tune", "The matrix results a promotion carries"),
            "What you own when the factory is handed over": ("What you own when the factory is handed over", "Pipelines, lineage, eval suite and the retrain calendar"),
            "Factory build-out, week by week": ("Factory build-out, week by week", "From dataset audit to canary ring, sequenced"),
            "Integration surface — data platform to serving mesh": ("Integration surface — data platform to serving mesh", "Where the factory touches the estate"),
            "Model governance — dataset-to-canary lineage": ("Model governance — dataset-to-canary lineage", "The audit trail from document to served weight"),
        },
    },

    "services_applied-ai-generative-ai_multimodal-vision-systems": {
        "archsubs": {
            "Layout & object detection": "page grammar first",
            "Field extraction": "model + rules ensemble",
            "Ledger reconciliation": "prove end-state before post",
            "Confidence gating": "route, do not guess",
            "Evidence store": "page-level provenance",
        },
        "badges": [
            ("Straight-through target", "61%"),
            ("Posted-field provenance", "page-level"),
            ("Reconciliation before post", "always"),
        ],
        "deep": {
            "h2": "The posting is the deliverable, not the bounding box",
            "sub": "From pixels to posted entries — why reconciliation and provenance gate the vision pipeline",
            "paras": [
                "Enterprise vision programs succeed when they are measured as bookkeeping: a document class is done when its fields post to the system of record with provenance, not when the model's IoU looks good on a holdout. The pipeline therefore runs page grammar first — layout and object detection establish what the page is and where things are — before field extraction ensembles (model plus rules) read values, and confidence gates route on band: straight-through after reconciliation, human review with highlighted regions, or recapture. The reconciliation step is the money path: extracted totals match the ledger arithmetic before anything posts, so the queue measures exceptions rather than errors.",
                "Evidence is page-level by design: every posted field carries the crop, the confidence and the model version that produced it, which is what an auditor's sample request actually wants. Drift monitoring watches document scanners as much as models — a new copier preset silently shifts dewarp statistics — and release trains move document classes through canary volumes before estate-wide routing.",
            ],
            "bullets": [
                ("Page grammar before reading", "Layout and detection establish structure; extraction reads within it."),
                ("Reconcile before post", "Ledger arithmetic checked before anything lands in the system of record."),
                ("Page-level provenance", "Crop, confidence and model version ride every posted field."),
                ("Scanner-aware drift watch", "Capture drift is monitored alongside model drift."),
            ],
        },
        "heads": {
            "Vision in the enterprise is a bookkeeping problem wearing a camera": ("Enterprise vision is judged by what posts to the ledger", "Extraction is the middle; provenance, reconciliation and routing are the product"),
            "Four failure modes that turn extraction into re-work": ("Four failure modes that turn extraction into re-work", "Unrouted confidence, unproven posting, silent capture drift, unowned review benches"),
            "Reference architecture — confidence-gated extraction into systems of record": ("Reference architecture — confidence-gated extraction into systems of record", "Detection, extraction, gating, reconciliation and evidence as one path"),
            "A document's path — pixels to posted entries": ("A document's path — pixels to posted entries", "The journey with the checks each stage runs"),
            "The vision-ops console operations and finance share": ("The vision-ops console operations and finance share", "Straight-through share, exception mix and cost per document"),
            "Straight-through economics by document class": ("Straight-through economics by document class", "Where the volume pays and where humans stay by design"),
            "Extraction stack defaults — and documented deviations": ("Extraction stack defaults — and documented deviations", "The default stack, and the deviations we sign"),
            "Extraction release gates — what blocks a go-live": ("Extraction release gates — what blocks a go-live", "Class-level evidence before estate routing"),
            "The handover package for operations and finance": ("The handover package for operations and finance", "Consoles, band definitions, exception taxonomy and the review bench"),
            "From capture to straight-through, week by week": ("From capture to straight-through, week by week", "The build sequence with evidence at every doubling"),
            "Integration surface — capture, records and the review bench": ("Integration surface — capture, records and the review bench", "Scanners, portals, ledgers and the human queue"),
            "Audit-ready extraction — evidence on every posted field": ("Audit-ready extraction — evidence on every posted field", "What the sample request pulls, in one query"),
        },
    },

    "services_applied-ai-generative-ai_rag-knowledge-systems": {
        "archsubs": {
            "Canonical registry": "one URI per fact",
            "Hybrid index (BM25+dense)": "fusion with rerank",
            "Permission map": "ACL-folded, query-time",
            "Retrieval planner": "decompose + route",
            "Grounded generation": "no cite, no answer",
        },
        "badges": [
            ("Citation coverage", "100%"),
            ("Permission fidelity", "query-time enforced"),
            ("Freshness SLA per corpus", "signed"),
        ],
        "deep": {
            "h2": "Permission fidelity is the hard part",
            "sub": "ACL folding, corpus hygiene and the freshness contract — the three disciplines that decide enterprise RAG",
            "paras": [
                "Consumer RAG is a search problem; enterprise RAG is a permissions problem with search attached. The index must return only what the asker could have read — so ACLs fold into the retrieval layer at query time, denied documents never enter candidate sets, and permission fidelity is tested with adversarial probes (privileged questions from unprivileged accounts) on every release, not just at launch. The canonical registry is the corpus-hygiene discipline: one URI per fact, superseded versions marked, ownership named — because duplicate and stale content is what makes retrieval confidently wrong.",
                "The freshness contract closes the loop: every corpus carries a signed freshness SLA (how long a fact may serve before re-verification), the retrieval planner decomposes multi-hop questions rather than pretending one embedding finds them, and the eval suite is replayed on every index or prompt change. The operating console reads permission probes, freshness breaches and citation coverage as its headline numbers — those three decide whether the estate trusts the answers.",
            ],
            "bullets": [
                ("ACL-folded retrieval", "Denied documents never reach candidate sets; probes test fidelity every release."),
                ("Canonical registry", "One URI per fact, stale versions marked, owners named."),
                ("Signed freshness SLAs", "Corpus-level contracts; breaches surface on the console."),
                ("Multi-hop planning", "Decomposed queries instead of one-embedding answers."),
            ],
        },
        "heads": {
            "Why corpus engineering decides the answer quality": ("Why corpus engineering decides the answer quality", "Canonical registry, dedup and ownership — the unglamorous work behind every good answer"),
            "Four failure modes that quietly kill enterprise RAG": ("Four failure modes that quietly kill enterprise RAG", "Permission leaks, stale canon, multi-hop pretense, unsampled eval"),
            "Reference architecture — permission-aware retrieval with citations": ("Reference architecture — permission-aware retrieval with citations", "Index, permission fold, planner and grounded generation as one path"),
            "The answer path, question by question": ("The answer path, question by question", "From decomposed query to cited, trace-sealed answer"),
            "The operating console for a retrieval estate": ("The operating console for a retrieval estate", "Permission probes, freshness and citation coverage as headlines"),
            "Retrieval quality across eval suite generations": ("Retrieval quality across eval suite generations", "How the golden set grows and what the trend line says"),
            "The stack we default to — and when we deliberately leave it": ("The stack we default to — and when we deliberately leave it", "Default components, and the deviations we sign"),
            "What a release must prove before promotion": ("What a release must prove before promotion", "Eval replays, permission probes and freshness checks"),
            "What your team owns at handover": ("What your team owns at handover", "Registry, SLAs, eval suite and the drift watch"),
            "How the build runs, week by week": ("How the build runs, week by week", "Corpus first, permissions second, generation last"),
            "Where this service plugs into your estate": ("Where this service plugs into your estate", "SharePoint to data lakes — the honest source list"),
            "The control surface — permission fidelity, trace discipline, egress policy": ("The control surface — permission fidelity, trace discipline, egress policy", "The three controls auditors ask about first"),
        },
    },
}
