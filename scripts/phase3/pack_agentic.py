#!/usr/bin/env python3
"""Pack: Agentic AI & Hyperautomation (dom=agentic-ai-hyperautomation)."""

DOM = "agentic-ai-hyperautomation"

# ── Industry hooks (domain-flavored, sector-real) ──────────────────────────
HOOKS = {
    "banking-financial-services": "KYC refresh backlogs, sanctions-alert triage and reconcile-everything month-ends are high-volume, rule-bounded and examinable — exactly the workload where role-scoped agents out-perform both manual desks and brittle RPA.",
    "insurance": "FNOL intake, submission triage and reserve refresh run on ACORD-coded documents and PAS queues that surge at catastrophe season — agent pools absorb the surge while adjusters keep the judgment calls, with every step logged.",
    "healthcare-life-sciences": "Prior authorization, claims status and denials follow-up drown coding and RCM teams in X12 278/837 transactions and payer-portal hunts — agents that read the rule set, assemble the packet and log every step give the queue an owner.",
    "manufacturing": "Maintenance planners and quality engineers live in SAP PM work orders, MES transactions and supplier ASN exceptions — automation earns its keep here only when it clears the backlog without touching the safety-rated path.",
    "retail-consumer-goods": "EDI 850/855/856 exceptions, trade-promotion deduction disputes and supplier onboarding are pure document-and-decision churn across GS1 identifiers — the queue shrinks fastest when agents work the exception list under merchandiser-approved checkpoints.",
    "telecom-media": "Order fallout between OSS/BSS layers, usage-dispute tickets and churn-save queues are where TM Forum Open API journeys break — durable orchestration re-drives the fallout and hands judgment calls to humans with context attached.",
    "energy-utilities": "Outage tickets, switch-order packets, market-submission checks and billing exceptions stack across OMS/EMS and CIS estates — the wins sit in bounded, auditable workflows where a wrong write is recoverable and every action is logged.",
    "logistics-supply-chain": "Missed appointments, failed EDI messages, customs holds and detention disputes across TMS/WMS/telematics feeds — agentic pools triage, re-drive and document exceptions so the control tower shows truth, not noise.",
    "public-sector": "Permit, benefit and FOIA case backlogs move at the pace of document assembly and eligibility checks — agents that pre-fill, verify and route cut cycle time while every decision keeps a citable evidence trail for oversight bodies.",
    "education-research": "Admissions processing, aid-verification packets and grant-administration reporting scale with enrollment cycles — role-scoped agents clear the routine files and route judgment calls to registrars and aid officers with full context.",
    "technology-saas": "Support triage, entitlement checks and renewal-desk workflows scale linearly with ARR unless an agent layer absorbs the repeatable steps — with checkpoints where account teams keep pricing judgment and CRM history stays structured.",
    "agriculture-food": "Contract management, grading certificates, subsidy dossiers and harvest-logistics planning run on seasonal surges — agent pools absorb the surge with checkpoints where agronomists and traders keep commercial judgment.",
}

# ── Industry KPI specs (label, lo, hi, fmt) — industry language ────────────
KPIS = {
    "banking-financial-services": [
        ("STP rate, agent-handled ops", 58, 74, "pct"),
        ("Checkpoint fidelity at audit sampling", 96, 100, "pct"),
        ("Cost per completed action", 22, 44, "cents"),
    ],
    "insurance": [
        ("Claims auto-adjudicated to settlement", 46, 68, "pct"),
        ("FNOL intake cycle time", 2, 9, "hrs"),
        ("Adjuster override rate", 8, 22, "pct"),
    ],
    "healthcare-life-sciences": [
        ("Prior-auth auto-approval share", 24, 48, "pct"),
        ("Denials follow-up queue age p90", 3, 11, "days"),
        ("Action replay coverage", 100, 100, "pct"),
    ],
    "manufacturing": [
        ("Work orders auto-dispositioned", 38, 62, "pct"),
        ("NCR closure cycle", 6, 16, "days"),
        ("Actions with sealed evidence packet", 98, 100, "pct"),
    ],
    "retail-consumer-goods": [
        ("PO exceptions auto-resolved", 52, 74, "pct"),
        ("Deduction dispute cycle", 9, 24, "days"),
        ("Agent actions reconciled to ERP", 99, 100, "pct"),
    ],
    "telecom-media": [
        ("Order fallout auto-recovered", 44, 70, "pct"),
        ("Repeat-fallout rate", 2, 9, "pct"),
        ("Usage disputes closed within SLA", 78, 94, "pct"),
    ],
    "energy-utilities": [
        ("Field work orders auto-routed", 41, 66, "pct"),
        ("Outage-ticket backlog age p90", 10, 36, "hrs"),
        ("Switch-order packet completeness", 97, 100, "pct"),
    ],
    "logistics-supply-chain": [
        ("Exceptions auto-triaged", 55, 78, "pct"),
        ("Detention disputes resolved in", 3, 12, "days"),
        ("EDI messages re-driven in window", 92, 99, "pct"),
    ],
    "public-sector": [
        ("Cases auto-assembled for review", 34, 58, "pct"),
        ("Permit cycle-time reduction", 28, 52, "pct"),
        ("Decisions with citable evidence trail", 100, 100, "pct"),
    ],
    "education-research": [
        ("Applications auto-processed", 44, 70, "pct"),
        ("Verification packet cycle", 4, 12, "days"),
        ("Staff hours returned per week", 120, 340, "num"),
    ],
    "technology-saas": [
        ("Tickets auto-triaged", 48, 72, "pct"),
        ("First-response time", 2, 14, "min"),
        ("Entitlement checks automated", 90, 99, "pct"),
    ],
    "agriculture-food": [
        ("Contract milestones auto-tracked", 60, 86, "pct"),
        ("Certification doc prep time", 3, 12, "hrs"),
        ("Subsidy dossier completeness", 96, 100, "pct"),
    ],
}

# ── Systems & standards in scope, per industry ─────────────────────────────
SYSTEMS = {
    "banking-financial-services": ["KYC/case suites and watchlist tools", "SWIFT gpi and payment-rail events", "SR 11-7 / OCC 2011-12 evidence"],
    "insurance": ["PAS/claims suites (Guidewire-class)", "ACORD forms and ISO claim codes", "NAIC market-conduct evidence"],
    "healthcare-life-sciences": ["EHR/RCM estates (Epic-class)", "HL7 FHIR + X12 278/837", "HIPAA audit controls"],
    "manufacturing": ["SAP PM / CMMS work orders", "MES context via ISA-95", "IATF 16949 NCR-CAPA flows"],
    "retail-consumer-goods": ["EDI 850/855/856 + GS1 GTIN", "ERP order ledgers (SAP Retail-class)", "Trade-promotion deduction systems"],
    "telecom-media": ["OSS/BSS order orchestration", "TM Forum Open APIs (TMF622/641)", "Campaign and churn platforms"],
    "energy-utilities": ["OMS/EMS and CIS estates", "NERC and market-submission calendars", "Field-service scheduling"],
    "logistics-supply-chain": ["TMS/WMS/telematics event feeds", "EDIFACT / X12 carrier messages", "Customs and HS documentation"],
    "public-sector": ["Permit/benefit case systems", "FOIA and records statutory clocks", "Budget and procurement controls"],
    "education-research": ["SIS estates (Banner-class)", "Aid verification workflows", "Grant reporting portals"],
    "technology-saas": ["ITSM/CRM (ServiceNow-class)", "CPQ and entitlement registries", "SOC 2 evidence controls"],
    "agriculture-food": ["Procurement and contract ledgers", "Certification schemes (GLOBALG.A.P.-class)", "Subsidy and traceability portals"],
}

# ── Common node annotations (applied where a page has no page-specific sub) ─
COMMON_SUBS = {
    "Policy engine": "OPA/Rego bundle · deny-by-default",
    "Work queues": "depth + SLA clock, visible",
    "Human checkpoints": "sampled · SLA-timed · replayable",
    "Audit trail": "append-only, hash-linked",
    "Event buses": "typed topics, schema-checked",
    "Document queues": "age-banded, SLA-tracked",
    "Process logs": "XES-normalized event streams",
    "State store": "durable, versioned per case",
    "Schema registry": "contract versions enforced",
    "Event lake": "immutable, replay-ready",
    "Feature store": "point-in-time correct",
    "Idempotency ledger": "one write per key, provable",
    "Escalation policy": "timers route, nothing strands",
    "Drift monitors": "population & score shifts",
    "Contract tests": "CI gate on every release",
    "Integration gateway": "typed calls, replay on fail",
    "Case intake": "typed request objects",
    "Decision ledger": "every output, replayable",
    "Explanation layer": "reason codes on 100%",
    "Fairness tests": "disparate-impact gates",
    "Challenger models": "score silently, always",
    "Rule overlays": "signed policy deltas",
    "Eligibility rules": "versioned, examinable",
    "Action APIs": "scoped, idempotent writes",
    "Appeal path": "human review, logged",
    "Human override": "context attached, logged",
    "Audit sampling": "discrepancy-driven",
    "Evidence store": "sealed per-run packets",
    "Schedules": "calendar-aware triggers",
}

PAGES = {
    # ── Domain hub ──────────────────────────────────────────────────────────
    "services_agentic-ai-hyperautomation": {
        "archsubs": {
            "Process mining": "event logs → variants + cost",
            "Agent runtimes": "scoped tool belts, no shell",
            "Agent identity": "per-agent creds, rotated",
            "Replay store": "full traces, 18-mo retention",
        },
        "badges": [
            ("Practices in the domain", "7"),
            ("Reference gates", "4"),
            ("Industries served", "12"),
        ],
        "deep": {
            "h2": "The engineering argument behind this domain",
            "sub": "Why mining, fleet, policy and evidence are designed as one system rather than four procurement lines",
            "paras": [
                "Automation programs fail at the joints, and the joints are between practices, not inside them. A mined candidate list that nobody prices dies in procurement; an agent fleet without a policy spine dies at the first access review; a policy spine without a replay store dies at the first internal audit. The domain is therefore engineered as one execution spine: mining prices the work, design places the checkpoints, the fleet executes under policy, and the evidence store makes every claim reconstructable. Each practice can be bought separately — the spine cannot, which is why the reference architecture holds all four layers even for a single-practice engagement.",
                "The technical debate we settle with every client is where authority sits. Tool grants belong to role definitions, not to agent builders; checkpoint placement belongs to a signed risk matrix, not to developer convenience; the kill decision on a candidate belongs to the ROI ledger, not to stakeholder enthusiasm. Programs that leave these three calls informal produce impressive demos and indefensible operations. The gates in this domain encode exactly those calls — evidence, not narrative, moves a candidate from mining to design to production.",
            ],
            "bullets": [
                ("One spine, four practices", "Mining, design, fleet and evidence share identifiers, schemas and gates — no orphan artifacts."),
                ("Authority is explicit", "Tool grants from roles, checkpoints from risk matrix, kill decisions from the ROI ledger."),
                ("Replay is the contract", "Any action, any day, reconstructable from the trace within one business day."),
                ("Gates bind, not advise", "A candidate without priced economics does not advance; a cohort without evidence does not go live."),
            ],
        },
        "heads": {
            "Seven practices from mining to fleet management": ("Seven practices, one governed execution spine", "How mining, design, fleet and evidence divide the automation problem — and what joins them"),
            "Why automation programs stall — and what the discipline is instead": ("Where automation programs stall — and the operating discipline that prevents it", "Failure economics from delivery, distilled into four structural controls"),
            "The domain reference architecture — mined work to governed execution": ("The domain reference architecture — mined work to governed execution", "From event logs to a replayable evidence trail, with every hop owned and every grant expiring"),
            "The automation program on one screen": ("The automation program on one screen", "Coverage, checkpoint fidelity and unit cost as the console reads them"),
            "Candidate economics — where ideas die and why": ("Candidate economics — where ideas die and why", "The kill-reason ledger from mining cycles: the discipline that protects the build budget"),
            "Sector depth — where agentic automation runs deepest today": ("Sector depth — where agentic automation runs deepest today", "A twelve-industry lens with the targets we sign against and the sector briefs behind them"),
            "How automation engagements run": ("How automation engagements run", "Weekly evidence cadence from baseline audit to industrialized scale"),
            "Automation program gates — the domain-level contract": ("Automation program gates — the domain-level contract", "What each gate demands in evidence; nothing advances on narrative"),
        },
    },

    # ── Agentic Process Automation ──────────────────────────────────────────
    "services_agentic-ai-hyperautomation_agentic-process-automation": {
        "archsubs": {
            "Role agent": "role-derived scope, no ad hoc",
            "Tool belt (scoped)": "least-privilege, expiring grants",
            "Verifier steps": "assertions before any commit",
            "Supervisor review": "sampling + discrepancy SLAs",
        },
        "badges": [
            ("Straight-through target", "72%"),
            ("Policy breaches tolerated", "0"),
            ("Replay coverage", "100%"),
        ],
        "deep": {
            "h2": "Idempotency is the load-bearing wall",
            "sub": "The engineering property every agent action inherits — and what we build when a system cannot offer it",
            "paras": [
                "Every write an agent makes carries an idempotency key, and the key is semantic, not syntactic: two calls that would move the same business object to the same state share a key, so a retry after timeout cannot double-book, double-pay or double-file. Systems that support idempotent writes natively get used directly; systems that do not get a reconciliation shim that proves the intended end-state before the run is allowed to close. This is why our failure rate claims survive audit — a run that could not prove its end-state is a failed run by definition, and the failure is visible in the run ledger, not in a spreadsheet.",
                "The second wall is the retry budget. Agents do not retry until success; they retry within a budget — bounded attempts, bounded cost, bounded wall-clock — and when the budget exhausts, the run escalates with its trace attached. The economics matter: an agent that retries expensive LLM calls until the bill spikes is the most common cost failure we inherit from prior programs. The circuit breaker on spend is set at design time from the risk matrix, reviewed at every release gate, and it trips loudly when it trips.",
            ],
            "bullets": [
                ("Semantic idempotency keys", "Same business object + same end-state = same key; retries collapse, side effects stay single."),
                ("Reconciliation shims", "For systems without native idempotency, end-state is proven from source before a run closes."),
                ("Budgeted retries", "Bounded attempts, cost and wall-clock; exhaustion escalates with trace attached."),
                ("Spend circuit breakers", "Per-run and per-cohort ceilings from the risk matrix; trips are loud and reviewed at gates."),
            ],
            "note": "Design targets from the reference program model — gate thresholds from delivery, not a client's live telemetry.",
        },
        "heads": {
            "An agent is a junior employee with perfect attendance — staff it like one": ("The agent operating model — roles, grants and supervision", "Staffing discipline applied to software: explicit duties, bounded tools, inspected work"),
            "Four failure modes that erode agent programs": ("Four failure modes that erode agent programs", "Tool sprawl, loop economics, silent wrongness, checkpoint erosion — with the countermeasure that ships against each"),
            "Reference architecture — policy-bounded execution with risk-placed checkpoints": ("Reference architecture — policy-bounded execution with risk-placed checkpoints", "Scope from role definitions; autonomy earned step by step against a signed risk matrix"),
            "One task's journey — assignment, execution, checkpoint, replay": ("One task's journey — assignment, execution, checkpoint, replay", "The five-stage run anatomy from typed intake to sealed evidence packet"),
            "The agent console operations and compliance share": ("The agent console operations and compliance share", "Run ledger, policy denials and cost ceilings on one surface"),
            "Task economics across process families": ("Task economics across process families", "Straight-through targets and unit cost by family — where the next cohort gets staffed"),
            "Agent stack defaults — and documented deviations": ("Agent stack defaults — and documented deviations", "The default stack, and the deviations we sign for explicitly"),
            "Agent release gates — what blocks a cohort from going live": ("Agent release gates — what blocks a cohort from going live", "The evidence a cohort carries before production load"),
            "What the process owner inherits": ("What the process owner inherits", "Runbooks, consoles, the re-certification calendar and named owners"),
            "The build, week by week": ("The build, week by week", "Twelve weeks from baseline audit to an industrialized cohort"),
            "Integration surface — the tools agents are scoped to touch": ("Integration surface — the tools agents are scoped to touch", "ERP, CRM, ITSM and comms — named systems, typed calls, expiry on every grant"),
            "Control overlay — auditability of every autonomous action": ("Control overlay — auditability of every autonomous action", "Evidence packets, replay traces and the money path"),
        },
    },

    # ── Autonomous Workflow Orchestration ───────────────────────────────────
    "services_agentic-ai-hyperautomation_autonomous-workflow-orchestration": {
        "archsubs": {
            "Workflow definitions": "versioned, testable artifacts",
            "Durable executor": "resumes past partial failure",
            "Compensation logic": "tested undo, not improvised",
            "State-transition trail": "every hop, hash-linked",
        },
        "badges": [
            ("On-time completion", "93%"),
            ("Zombie cases after drills", "0"),
            ("Duplicate side effects", "0"),
        ],
        "deep": {
            "h2": "Partial failure is a normal operating event",
            "sub": "Durable execution semantics — and the compensation design that makes recovery boring",
            "paras": [
                "A workflow that spans an ERP, a document service and three human tasks will experience partial failure every week, and the design question is not whether to fail but what state means when it does. Durable execution is the answer: the orchestrator persists a versioned state record at every step boundary, and a crashed executor resumes from the last boundary with its inputs intact. Timers are first-class — an SLA clock that fires at 14:00 re-drives the case whether or not anyone remembered it — and duplicate triggers collapse through the same idempotency discipline the agent runtime uses.",
                "Compensation is where amateur orchestrations die. Every non-idempotent step carries a defined undo: the reversal is coded, tested in chaos drills and rehearsed against production-shaped data before go-live. Zombie detection closes the loop — a case with no state transition for N hours is surfaced to the escalation desk with its trail attached, so nothing strands silently. The chaos drill is the release gate that matters: injected failures at every step boundary, and the recovery path must complete before the cohort advances.",
            ],
            "bullets": [
                ("Step-boundary persistence", "Versioned state at every boundary; a crashed executor resumes, it does not restart."),
                ("First-class timers", "SLA clocks re-drive cases without human memory; timers are tested, not configured."),
                ("Coded compensation", "Every non-idempotent step has a tested undo — rehearsed, not improvised."),
                ("Zombie detection", "No-transition-for-N-hours cases surface to the escalation desk with full trail."),
            ],
        },
        "heads": {
            "Workflows fail on week three, not in the demo": ("Long-running workflows fail on week three — by design, not by accident", "Partial failure, duplicate triggers and calendar edges are normal operating events"),
            "Four failure modes that turn orchestration into case debt": ("Four failure modes that turn orchestration into case debt", "How silent stranding, timer amnesia, double-firing and improvised undo compound into backlog"),
            "Reference architecture — durable state and choreographed escalation": ("Reference architecture — durable state and choreographed escalation", "Durable executor, first-class timers, coded compensation and a hash-linked trail"),
            "A case under failure — the recovery path in motion": ("A case under failure — the recovery path in motion", "Injected partial failure, step-boundary resume and the escalation handoff"),
            "The orchestration console — recovery posture on one screen": ("The orchestration console — recovery posture on one screen", "Zombies, timer debt and retry budgets as the ops desk reads them"),
            "Completion and recovery under injected failure": ("Completion and recovery under injected failure", "Chaos-drill results: the release evidence a cohort carries"),
            "Orchestration defaults — and when we deviate": ("Orchestration defaults — and when we deviate", "The default engine and patterns, and the deviations we sign for"),
            "Orchestration release gates — evidence before production load": ("Orchestration release gates — evidence before production load", "What must be proven before production volume touches the workflow"),
            "What the platform and process teams inherit": ("What the platform and process teams inherit", "Definitions-as-code, drill calendar, escalation desk runbooks"),
            "Durability first, week by week": ("Durability first, week by week", "The build sequence, from state model to chaos certification"),
            "Integration surface — queues, systems and the escalation desk": ("Integration surface — queues, systems and the escalation desk", "Where workflows touch systems — and where they must not"),
            "Governance overlay — the audit trail of a running process": ("Governance overlay — the audit trail of a running process", "The state-transition trail as an examinable artifact"),
        },
    },

    # ── Decision Intelligence Systems ───────────────────────────────────────
    "services_agentic-ai-hyperautomation_decision-intelligence-systems": {
        "archsubs": {
            "Decision model": "champion within policy bounds",
            "Policy bounds": "signed envelope per decision class",
            "Benchmark panel": "human panel, refreshed quarterly",
            "Appeal path": "named reviewer, full context",
            "Decision ledger": "every output, replayable",
        },
        "badges": [
            ("Panel agreement", "91%"),
            ("Reason-code coverage", "100%"),
            ("Decisions replayable", "100%"),
        ],
        "deep": {
            "h2": "The challenger scores every case, silently",
            "sub": "Champion-challenger economics and the disagreement triggers that keep autonomy honest",
            "paras": [
                "Every production decision is scored twice: the champion decides, the challenger disagrees silently. The disagreement rate is the most honest model-health metric available — it detects population drift months before accuracy metrics move, because challengers built on different features or different vintages fail in different places. Disagreement above threshold forces a review of the affected stratum before the next release, and the review is quantitative: which strata, which feature regime, which direction. This is the discipline that turns model risk management from an annual document into a weekly measurement.",
                "The policy envelope is the second half of the defense. The champion only acts inside bounds signed by the risk owner — exposure ceilings, eligibility overlays, mandatory referral classes — and the explanation layer emits reason codes on every output, not on the samples an auditor requests. Reason-code coverage is therefore 100% by construction, and the appeal path routes to a named reviewer with the decision's full context, which is what a supervisory examination actually asks to see.",
            ],
            "bullets": [
                ("Silent challenger on 100% of cases", "Disagreement rate as leading indicator; stratum-level review above threshold."),
                ("Signed policy envelope", "Exposure ceilings, eligibility overlays and referral classes bound the champion."),
                ("Reason codes by construction", "Coverage is structural, not sampled — examinable line by line."),
                ("Named-reviewer appeals", "The appeal path carries full decision context to an accountable human."),
            ],
        },
        "heads": {
            "A decision system is judged by its worst defensible case": ("A decision system is judged by its worst defensible case", "Design for the decision a regulator will read, not the average case"),
            "Four failure modes that make decisions indefensible": ("Four failure modes that make decisions indefensible", "Unbounded autonomy, absent challengers, sampled explanations, drifting fairness"),
            "Reference architecture — challenger panels around every decision": ("Reference architecture — challenger panels around every decision", "Champion, challenger, policy envelope and explanation layer as one governed service"),
            "One decision, challenged and explained": ("One decision, challenged and explained", "The lifecycle of a single output, from features to reason codes to appeal path"),
            "The decision console the risk committee reads": ("The decision console the risk committee reads", "Agreement, drift and fairness as a standing agenda item"),
            "Decision quality against the human panel, quarter by quarter": ("Decision quality against the human panel, quarter by quarter", "Benchmark-panel methodology and what agreement actually measures"),
            "Decision stack defaults — and documented deviations": ("Decision stack defaults — and documented deviations", "The default stack, and the deviations we sign for"),
            "Decision release gates — what a supervisory review will ask": ("Decision release gates — what a supervisory review will ask", "The evidence pack a model-risk examination expects, prepared in advance"),
            "What risk and compliance inherit": ("What risk and compliance inherit", "Consoles, ledgers, drift reports and the review calendar"),
            "Wrap the model, week by week": ("Wrap the model, week by week", "The build sequence around the model — envelope first, autonomy last"),
            "Integration surface — policy engines and case systems": ("Integration surface — policy engines and case systems", "Where decisions land, and how overrides return into the ledger"),
            "Fairness and explainability overlay": ("Fairness and explainability overlay", "Disparate-impact monitoring with signed tolerances, audited continuously"),
        },
    },

    # ── Digital Workforce & Multi-Agent Orchestration ───────────────────────
    "services_agentic-ai-hyperautomation_digital-workforce-orchestration": {
        "archsubs": {
            "Agent registry": "identity, version, owner, scope",
            "Capacity scheduler": "demand curve → shift plan",
            "Retirement gate": "evidence before decommission",
            "Secret rotation": "90-day or shorter, automated",
            "Utilization (busy/blocked)": "state-honest, not calendar-based",
        },
        "badges": [
            ("Fleet utilization (state-honest)", "71%"),
            ("Credential rotation", "≤90 days"),
            ("Agents at retirement gate", "0 drift"),
        ],
        "deep": {
            "h2": "Utilization you can trust is a measurement problem",
            "sub": "Busy/blocked/idle as measured states — and why calendar-based utilization lies",
            "paras": [
                "Fleet programs misreport utilization because they measure occupancy on a calendar rather than state on the run ledger. An agent waiting on a human checkpoint is blocked, not idle; an agent rate-limited by a partner API is blocked, not idle; an agent holding a work item it cannot legally route further is blocked — and each blocked class has a different owner and a different fix. We instrument the three states from the run ledger, so the capacity plan is built on blockage causes: checkpoint latency, tool availability, routing rules. The number a COO reads is therefore actionable by construction.",
                "The second discipline is version currency. An agent is software with a lease: model versions deprecate, tool schemas move, policies tighten. The registry tracks every agent's model pin, grant expiry and last evidence packet, and the upgrade train moves cohorts through a canary ring before estate-wide promotion. Retirement is a gate, not a shutdown script: a decommissioning agent hands its queue to named successors, its credentials are revoked in the same change window, and its evidence is archived under the retention policy — because auditors ask about the agents you turned off as often as the ones you run.",
            ],
            "bullets": [
                ("State-honest utilization", "Busy, blocked and idle measured from the run ledger; blockage causes drive the capacity plan."),
                ("Version currency tracking", "Model pins, grant expiry and evidence recency in the registry; canary before promotion."),
                ("Retirement as a gate", "Queue handover to named successors, credential revocation in-window, evidence archived."),
                ("Shift discipline", "Demand curves → shift plans, with overflow rules signed by process owners."),
            ],
        },
        "heads": {
            "Fifty agents are a workforce, and workforces need management": ("The fleet as a managed workforce — capacity, shifts, versions", "Workforce management applied to agent estates: demand planning to retirement"),
            "Four ways fleets sprawl into liabilities": ("Four ways fleets sprawl into liabilities", "Orphaned agents, stale credentials, dishonest utilization, unmanaged retirement"),
            "Reference architecture — the fleet layer from capacity to retirement": ("Reference architecture — the fleet layer from capacity to retirement", "Registry, scheduler, version train and retirement gate as one control plane"),
            "A week in the fleet — demand, shifts, upgrades, retirement": ("A week in the fleet — demand, shifts, upgrades, retirement", "The operating rhythm the fleet manager actually runs"),
            "The fleet console — utilization you can trust": ("The fleet console — utilization you can trust", "State-honest busy/blocked/idle with blockage causes attached"),
            "Fleet state across a demand week": ("Fleet state across a demand week", "How capacity absorbs the Monday peak and the month-end surge"),
            "Fleet stack defaults — and deliberate deviations": ("Fleet stack defaults — and deliberate deviations", "The default control plane, and the deviations we sign for"),
            "Fleet change gates — what evidence an upgrade carries": ("Fleet change gates — what evidence an upgrade carries", "Canary evidence, regression deltas and rollback proof per cohort"),
            "What the digital-workforce manager inherits": ("What the digital-workforce manager inherits", "Registry, calendars, runbooks and the quarterly re-certification pack"),
            "Fleet quarter in motion, week by week": ("Fleet quarter in motion, week by week", "The quarterly cadence from demand review to retirement review"),
            "Integration surface — identity, queues and the demand systems": ("Integration surface — identity, queues and the demand systems", "Identity provider, work queues and the systems that generate demand"),
            "Credential and lifecycle governance": ("Credential and lifecycle governance", "Rotation SLAs, break-glass paths and the audit trail of the estate"),
        },
    },

    # ── Hyperautomation & Systems Integration ───────────────────────────────
    "services_agentic-ai-hyperautomation_hyperautomation-integration": {
        "archsubs": {
            "Schema registry": "typed contracts, versioned",
            "Contract tests": "break the build on drift",
            "Integration gateway": "typed calls, replay on fail",
            "Idempotency ledger": "exactly-once, provable",
            "Drift monitors": "schema + semantic drift",
        },
        "badges": [
            ("Seams under contract", "100%"),
            ("Month-end error budget", "0 breaches"),
            ("Replay on failed write", "always"),
        ],
        "deep": {
            "h2": "Typed seams, or the month-end will find you",
            "sub": "Contract-first integration — the discipline that makes cross-system writes survivable",
            "paras": [
                "Integration failures are calendar-driven: the seam that held all quarter breaks on the last business day of the month, when volumes triple and upstream schemas drift. The countermeasure is contract-first seams — every integration is a typed contract in the registry, versioned like code, with contract tests that break the build when a provider drifts. The drift monitors then watch the two failure classes tests cannot catch: semantic drift (a field that keeps its name and loses its meaning) and volume drift (a source that changes its shape under load). Both page the integration desk before the close, not after.",
                "The write path is engineered for exactly-once semantics under provable conditions: idempotency keys per business object, the idempotency ledger as the receipt of record, and replay queues that re-drive any write that landed nowhere. The seam console reads month-end as a load profile, not an incident — capacity shapes, back-pressure rules and rate limits are rehearsed against a replayed close before the live one. When a seam does break, the repair is a contract version bump with a migration note, not a hotfix that quietly widens a type.",
            ],
            "bullets": [
                ("Contracts in the registry", "Every seam typed, versioned and owned; drift breaks the build before it breaks the close."),
                ("Semantic + volume drift monitors", "The two failure classes tests miss, watched continuously."),
                ("Provable exactly-once", "Business-object idempotency keys and the ledger as receipt of record."),
                ("Month-end as a load profile", "Rehearsed against replayed closes; back-pressure and rate limits signed."),
            ],
        },
        "heads": {
            "Automation dies in the seams, not in the agents": ("Automation dies in the seams — the integration discipline that prevents it", "Contract-first seams with replay, drift monitors and month-end rehearsals"),
            "Four failure modes that break seams at month-end": ("Four failure modes that break seams at month-end", "Schema drift, semantic drift, volume cliffs and the unkeyed write"),
            "Reference architecture — typed seams with replay and drift monitors": ("Reference architecture — typed seams with replay and drift monitors", "Registry, gateway, ledger and monitors as the load-bearing structure"),
            "One write across three systems, guaranteed once": ("One write across three systems, guaranteed once", "The exactly-once path, step by step, with receipts"),
            "The seam console — health under real load": ("The seam console — health under real load", "Error budgets, replay queues and drift alarms on one surface"),
            "Seam health across month-end load": ("Seam health across month-end load", "Capacity shape and back-pressure under a replayed close"),
            "Integration defaults — and documented deviations": ("Integration defaults — and documented deviations", "The default patterns, and where we sign deviations"),
            "Seam release gates — evidence before the next close": ("Seam release gates — evidence before the next close", "What a seam must prove before month-end load"),
            "What the integration team inherits": ("What the integration team inherits", "Registry ownership, migration notes and the drill calendar"),
            "Seam by seam, week by week": ("Seam by seam, week by week", "The build sequence from contract to rehearsal"),
            "Integration surface — the systems list, honestly named": ("Integration surface — the systems list, honestly named", "ERP, CRM, ITSM, comms and queues — named, typed, owned"),
            "Integration governance — contracts as controlled artifacts": ("Integration governance — contracts as controlled artifacts", "Versioning, review and change control for every seam"),
        },
    },

    # ── Intelligent Document Processing ─────────────────────────────────────
    "services_agentic-ai-hyperautomation_intelligent-document-processing": {
        "archsubs": {
            "Field extraction": "model + rules ensemble",
            "Confidence gates": "route, do not guess",
            "Process match (PO/ledger)": "3-way match before post",
            "Evidence store": "page-level provenance",
            "Correction capture": "every fix trains the gate",
        },
        "badges": [
            ("Straight-through target", "68%"),
            ("Queue age p90 trend", "down 64%"),
            ("Extraction provenance", "page-level"),
        ],
        "deep": {
            "h2": "The confidence gate is the product",
            "sub": "Route-don't-guess adjudication — and why correction capture is the compounding asset",
            "paras": [
                "Document processing programs fail by optimizing extraction accuracy while ignoring the routing decision that actually protects the money path. The gate is the product: every extracted field carries a confidence score, and the gate routes on the score band — high confidence posts straight through after reconciliation, mid band goes to a human queue with the uncertain fields highlighted, low band goes back for recapture. The bands are set per document class from the risk matrix, because an invoice under $200 and a change order under $2M do not share a tolerance. Reconciliation against source — three-way match for PO flows, ledger match for accruals — runs before posting, so the queue measures exceptions, not errors.",
                "Correction capture is the compounding asset. Every human fix is recorded as a labeled correction bound to the page region and the field, and the correction stream feeds the monthly gate recalibration — which is why straight-through share climbs for months after go-live instead of decaying. The queue itself is managed as a product: age bands, root-cause tags and a monthly shrinkage review that kills the worst extraction failure class each cycle, rather than a support inbox that quietly grows.",
            ],
            "bullets": [
                ("Route, do not guess", "Confidence bands set per class from the risk matrix; nothing posts uncertain."),
                ("Reconcile before post", "Three-way match on PO flows, ledger match on accruals — exceptions, not errors."),
                ("Correction capture", "Every fix bound to page region and field; feeds monthly gate recalibration."),
                ("Queue as a product", "Age bands, root-cause tags and a monthly shrinkage review with owners."),
            ],
        },
        "heads": {
            "The queue is the product: what it says about your operation": ("The queue is the product — and it is measured like one", "Age bands, root causes and the shrinkage discipline that closes the backlog"),
            "Four failure modes that keep document queues eternal": ("Four failure modes that keep document queues eternal", "Unrouted confidence, unproven posting, uncaptured corrections, unowned aging"),
            "Reference architecture — adjudication wired into the process": ("Reference architecture — adjudication wired into the process", "Extraction, confidence gates, reconciliation and the correction loop as one flow"),
            "A document through the gate, the queue and the ledger": ("A document through the gate, the queue and the ledger", "The full journey from capture channel to posted, provable record"),
            "The document-ops console — queue age as the headline": ("The document-ops console — queue age as the headline", "Age bands, straight-through share and correction velocity on one surface"),
            "Queue shrinkage by root cause, month by month": ("Queue shrinkage by root cause, month by month", "The monthly review that kills the worst failure class each cycle"),
            "Extraction defaults — and when we deviate": ("Extraction defaults — and when we deviate", "Model ensembles and rule overlays, and the deviations we sign"),
            "Document-processing gates — evidence before volume": ("Document-processing gates — evidence before volume", "What must be proven before full-estate volume"),
            "What the operations team inherits": ("What the operations team inherits", "Consoles, band definitions, root-cause taxonomy and the review calendar"),
            "From pilot volume to full estate, week by week": ("From pilot volume to full estate, week by week", "The scale-up sequence with evidence at every doubling"),
            "Integration surface — capture channels and systems of record": ("Integration surface — capture channels and systems of record", "Scanners, portals and EDI in; ERP ledgers out — typed throughout"),
            "Controls overlay — evidence and the money path": ("Controls overlay — evidence and the money path", "Page-level provenance, maker-checker and the audit extract"),
        },
    },

    # ── Process & Task Mining ───────────────────────────────────────────────
    "services_agentic-ai-hyperautomation_process-task-mining": {
        "archsubs": {
            "Case keys": "join keys proven before mining",
            "Discovery models": "variants, not averages",
            "Conformance check": "delta to designed flow",
            "Candidate ranking": "priced, then ranked",
            "Continuous miner": "monthly refresh, versioned",
        },
        "badges": [
            ("Candidates priced at baseline", "100%"),
            ("Kill reasons logged", "every one"),
            ("Mining refresh cadence", "monthly"),
        ],
        "deep": {
            "h2": "Case keys before candidate lists",
            "sub": "Join-quality discipline — the reason our mining output survives procurement and audit",
            "paras": [
                "Mining programs produce fiction when the event log joins badly: two systems that number the same case differently produce phantom rework, invented loops and variants that exist only in the join error. We therefore prove join quality before any mining runs — key overlap ratios, case-fragmentation rates and a reconciliation sample against source records, reported in the baseline audit. Only then do discovery models run, and they run as variant discovery, not averages: the queue of candidates is priced per variant, with kill reasons logged for every candidate that dies, so the pipeline is an auditable artifact rather than a workshop poster.",
                "Conformance is the bridge from mining to delivery: the discovered flow is compared to the designed flow, and the delta — workarounds, shadow approvals, rework loops — is the actual automation backlog, ranked by priced economics. The continuous miner keeps the artifact alive: a monthly refresh with versioned models, so post-delivery conformance shows whether the automation moved the metric or merely moved the work. The mining console is built for that argument; process owners argue with it, which is exactly the point.",
            ],
            "bullets": [
                ("Join quality proven first", "Key overlap, fragmentation and reconciliation samples before any model runs."),
                ("Variants, not averages", "Candidates priced per variant; kill reasons logged for the auditable pipeline."),
                ("Conformance as backlog", "Delta between designed and discovered flow, ranked by priced economics."),
                ("Continuous miner", "Monthly versioned refresh; post-delivery conformance proves the metric moved."),
            ],
        },
        "heads": {
            "Your systems already recorded the truth about your processes": ("Your systems already recorded the process — mining makes it arguable", "Event logs to priced candidates, with join quality proven before discovery"),
            "Four ways mining programs produce fiction instead of pipelines": ("Four ways mining programs produce fiction instead of pipelines", "Bad joins, averaged variants, unpriced candidates, one-off workshops"),
            "Reference architecture — from event logs to a ranked candidate list": ("Reference architecture — from event logs to a ranked candidate list", "Extraction, join proof, discovery, pricing and the continuous miner"),
            "One mining cycle, stage by stage": ("One mining cycle, stage by stage", "From log extraction to a ranked, priced, auditable candidate list"),
            "The mining console process owners argue with": ("The mining console process owners argue with", "Variants, deltas and economics — designed for disagreement"),
            "Candidate disposition across a mining cycle": ("Candidate disposition across a mining cycle", "Where candidates die, and why the kill reasons are the asset"),
            "Mining stack defaults — and when we deviate": ("Mining stack defaults — and when we deviate", "The default toolchain, and the deviations we sign"),
            "Mining release gates — what evidence a candidate list carries": ("Mining release gates — what evidence a candidate list carries", "Join proof, pricing basis and the reconciliation sample"),
            "What the process excellence team owns at handover": ("What the process excellence team owns at handover", "The living model, the refresh calendar and the conformance cadence"),
            "The mining engagement, week by week": ("The mining engagement, week by week", "Eight weeks from log access to a governed candidate pipeline"),
            "Integration surface — the systems whose logs become evidence": ("Integration surface — the systems whose logs become evidence", "ERP, CRM, ITSM, comms — the log estate, honestly named"),
            "Governance overlay — mining as a repeatable audit artifact": ("Governance overlay — mining as a repeatable audit artifact", "Versioned models, retention and the evidence trail of every claim"),
        },
    },
}
