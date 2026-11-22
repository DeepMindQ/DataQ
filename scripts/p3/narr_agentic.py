"""narr_agentic — narrative layer for the Agentic AI & Hyperautomation domain."""

HUB = {
    "hero": ("Hyperautomation succeeds as workforce design, not as tool rollout. Agentic AI & "
             "Hyperautomation runs seven practices that mine the work, prove the ROI before the "
             "build, deploy role-scoped agents under policy bounds, and manage the resulting "
             "digital workforce with the same discipline — capacity, shifts, versioning, "
             "retirement — you apply to people."),
    "s_practices": "Seven practices from mining to fleet management",
    "s_deep": "Why automation programs stall — and what the discipline is instead",
    "deep": [
        ("Hyperautomation fails as a program when it is run as a tool rollout: licenses bought, "
         "bots deployed, nobody owning the coverage number. It succeeds when it is run like "
         "workforce design — mine the work with event-log evidence, prove the ROI before the "
         "build, deploy role-scoped agents under policy bounds, and manage the resulting digital "
         "workforce with capacity, versioning and retirement discipline."),
        ("The governance argument is what wins the board: every agent action replays, checkpoints "
         "sit where the risk matrix says they must, and autonomy is earned by evidence rather "
         "than configured by enthusiasm. That discipline is the difference between a program the "
         "auditors sign off and one they suspend."),
    ],
    "s_arch": "The domain reference architecture — mined work to governed execution",
    "arch_lead": ("One loop spans the domain: event-log mining feeds a conformance-checked "
                  "candidate pipeline, funded candidates become policy-bounded agents, the "
                  "orchestration layer carries durable state, and the fleet layer runs the "
                  "resulting workforce. Checkpoints are placed by risk, and every action replays."),
    "s_dash": "The automation program on one screen",
    "dash_lead": ("Coverage, checkpoint fidelity, cost per task and the exception queue — the "
                  "tiles a COO actually steers by, rendered as they appear in the weekly review."),
    "dash_note": ("Reference console — program-level targets; every tile traces to a signed "
                  "baseline owned by a named process owner."),
    "s_chart": "Candidate economics — where ideas die and why",
    "chart_lead": ("The mining funnel is a kill pipeline by design: candidates die at conformance "
                   "checks, at ROI screening, at checkpoint design — and the kill reasons are "
                   "logged, because a defensible no is worth as much as a funded yes."),
    "chart_override": {
        "variant": "funnel",
        "title": "Automation candidate disposition across one mining cycle — reference bands",
        "cats": ["Mined candidates", "Conformance-verified", "ROI-positive", "Funded", "In production"],
        "series": [("Candidates", [412, 187, 74, 28, 19])],
        "unit": "cases",
        "caption": "Reference bands for a mature mining cycle. The steep drop is the discipline working: most mined work should not be automated.",
    },
    "chart_lead_note": None,
    "chart_note": None,
    "s_evidence": "Sector depth — where agentic automation runs deepest today",
    "evidence_lead": ("Automation concentrates where back-office volume meets regulatory "
                      "checkpoints: claims, onboarding, order-to-cash, service desks. The bars "
                      "count published sub-industry briefs on this site — the honest map of where "
                      "sector-calibrated playbooks already exist."),
    "evidence_chart_title": "Agentic AI & Hyperautomation — published sub-industry briefs by sector",
    "explorer_title": "Agentic automation in your sector — pick the industry and see the plan",
    "explorer_intro": ("Every sector automates a different bottleneck. Select yours: the panel "
                       "shows the entry problem we usually meet, the deliverables we build, the "
                       "targets we sign, and the sector brief with workflows and controls."),
    "plays": [
        "A conformance-checked automation pipeline with logged kill reasons",
        "Role-scoped agents under policy bounds with risk-placed human checkpoints",
        "Durable orchestration with replay, escalation choreography and audit",
    ],
    "flagships": ["banking-financial-services", "insurance", "logistics-supply-chain"],
    "s_engage": "How automation engagements run",
    "engage": [
        ["Diagnostic — two weeks", "Your event logs are mined against the signed metric; the gate map is scored and the first candidate list is ranked with owners and kill reasons."],
        ["Provability sprint — four weeks", "One process family runs a fund-or-kill slice: straight-through rate, checkpoint fidelity and cost per task on your real data path."],
        ["Build — ten to fourteen weeks", "Agents, orchestration and seams built to the reference architecture, with the console live from week two and every action replayable."],
        ["Industrialize — ongoing", "Fleet management takes over: capacity planning, version upgrades under SLA, credential rotation and quarterly re-baselines against the signed coverage number."],
    ],
    "s_gates": "Automation program gates — the domain-level contract",
    "cta": ("Bring the process your CFO calls expensive and your auditors call fragile — the "
            "two-week diagnostic will rank what should be automated, what should not, and what "
            "the checkpoint design would look like."),
}

PAGES = {

"process-task-mining": {
    "hero": ("Event-log forensics that turn system footprints into a defensible automation "
             "pipeline: conformance-checked, variant-ranked, ROI-screened — with kill reasons "
             "logged so the backlog your board funds is the backlog reality earned."),
    "s1_h": "Your systems already recorded the truth about your processes",
    "s1_close": ("What follows is the mining discipline end to end: failure modes, the reference "
                 "architecture of a mining pipeline, and the console that keeps the backlog "
                 "honest between cycles."),
    "s2_h": "Four ways mining programs produce fiction instead of pipelines",
    "s2_lead": ("Mining fails as politics before it fails as statistics — each countermeasure "
                "below makes the output arguable in a steering meeting, which is where it has to "
                "survive."),
    "arch_h": "Reference architecture — from event logs to a ranked candidate list",
    "arch_lead": ("The pipeline's integrity lives in two places: case correlation across "
                  "fragmented systems, and the conformance check that separates variants worth "
                  "automating from variants that should be fixed first."),
    "flow_h": "One mining cycle, stage by stage",
    "flow_lead": ("From log extraction through case building, variant analysis, conformance "
                  "scoring and ROI screening to the ranked candidate list — including where the "
                  "kill reasons get written."),
    "dash_h": "The mining console process owners argue with",
    "dash_lead": ("Correlation quality, conformance score, funded candidates and logged kill "
                  "reasons — the four numbers that make a backlog defensible or expose it as "
                  "theater."),
    "dash_note": ("Reference console — mining-cycle targets; every funded candidate carries its "
                  "conformance and ROI evidence."),
    "chart_h": "Candidate disposition across a mining cycle",
    "chart_lead": ("Where mined ideas die, by stage and count. A healthy cycle kills most "
                   "candidates at conformance and ROI screens — the kill reasons are the audit "
                   "trail that keeps the next cycle honest."),
    "stack_h": "Mining stack defaults — and when we deviate",
    "stack_lead": ("Defaults favor replayable analysis over one-off consulting artifacts; "
                   "deviation conditions are written because each one changes whether the mining "
                   "can be re-run next quarter."),
    "gates_h": "Mining release gates — what evidence a candidate list carries",
    "artifacts_h": "What the process excellence team owns at handover",
    "timeline_h": "The mining engagement, week by week",
    "integ_h": "Integration surface — the systems whose logs become evidence",
    "integ_lead": ("Mining quality is bounded by log quality; these are the extraction contracts "
                   "that decide whether case correlation is possible at all."),
    "controls_h": "Governance overlay — mining as a repeatable audit artifact",
    "controls_lead": ("The output must survive internal audit: case definitions, conformance "
                      "rules and kill reasons are versioned, so last quarter's decisions are "
                      "re-explainable from the artifacts alone."),
    "controls_note": ("Kill reasons are first-class records: each logged reason cites the "
                      "conformance or ROI evidence that produced it, and the ledger ships in the "
                      "handover pack."),
    "cta": ("Bring two quarters of event logs and one contested backlog. The mining cycle will "
            "tell you which candidates survive conformance — and which pet automation ideas the "
            "evidence kills."),
    "flagships": ["manufacturing", "banking-financial-services", "agriculture-food"],
    "plays": [
        "Case correlation across fragmented system footprints",
        "Conformance-scored variants with ROI screening and logged kill reasons",
        "A re-runnable mining pipeline the process team owns after handover",
    ],
},

"agentic-process-automation": {
    "hero": ("Role-scoped agents that execute process steps under explicit policy bounds: "
             "permissions derived from the role, checkpoints placed by risk, replay for every "
             "action, and an exception queue designed for humans — not a chat window bolted to "
             "an RPA bot."),
    "s1_h": "An agent is a junior employee with perfect attendance — staff it like one",
    "s1_close": ("Below: the failure modes that make agent programs fragile, the reference "
                 "architecture that makes them defensible, and the console that shows exactly "
                 "what the digital staff did today."),
    "s2_h": "Four failure modes that erode agent programs",
    "s2_lead": ("Each of these starts small and compounds quietly; the countermeasures are "
                "structural, because by the time the failure is visible in the KPIs the "
                "checkpoints have already eroded."),
    "arch_h": "Reference architecture — policy-bounded execution with risk-placed checkpoints",
    "arch_lead": ("Two design decisions carry the architecture: agent scopes are derived from "
                  "role definitions rather than granted ad hoc, and checkpoint placement follows "
                  "a risk matrix signed by the process owner — so autonomy is earned by "
                  "evidence, step by step."),
    "flow_h": "One task's journey — assignment, execution, checkpoint, replay",
    "flow_lead": ("From queue assignment through execution under policy bounds to the checkpoint "
                  "decision and the replay record — with the paths where the agent escalates "
                  "instead of guessing."),
    "dash_h": "The agent console operations and compliance share",
    "dash_lead": ("Straight-through rate beside policy breaches, cost per task beside checkpoint "
                  "discrepancy — pairs that keep speed and control in the same conversation, "
                  "exactly where they belong."),
    "dash_note": ("Reference console — agent-fleet targets by process family; autonomy expansions "
                  "require two clean quarters at checkpoint fidelity."),
    "chart_h": "Task economics across process families",
    "chart_lead": ("Volume, straight-through share and unit cost per family — the chart that "
                   "decides where the next agent cohort is staffed, and which families stay "
                   "human-led by design."),
    "stack_h": "Agent stack defaults — and documented deviations",
    "stack_lead": ("Defaults bias toward typed tool access and bounded autonomy; deviations are "
                   "permitted where the process argues for them, with the risk delta written "
                   "next to each trigger condition."),
    "gates_h": "Agent release gates — what blocks a cohort from going live",
    "artifacts_h": "What the process owner inherits",
    "timeline_h": "The build, week by week",
    "integ_h": "Integration surface — the tools agents are scoped to touch",
    "integ_lead": ("Agents are only as disciplined as their tool access; these contracts define "
                   "what each role can touch, in which order, with which replay guarantees."),
    "controls_h": "Control overlay — auditability of every autonomous action",
    "controls_lead": ("Every action replays: inputs, policy version, checkpoint outcome and "
                      "side effects are recorded — the evidence pack internal audit asks for, "
                      "assembled by default."),
    "controls_note": ("Autonomy expansion is earned, not configured: a cohort's scope widens only "
                      "after two consecutive quarters inside the checkpoint-fidelity tolerance, "
                      "and the widening is itself a gated change."),
    "cta": ("Pick the process where the exception queue eats your best people. The sprint will "
            "show the straight-through rate agents can honestly reach there — with checkpoints "
            "designed by risk, not by pressure."),
    "flagships": ["insurance", "banking-financial-services", "telecom-media"],
    "plays": [
        "Role-scoped agents with policy bounds derived from role definitions",
        "Human checkpoints placed by a signed risk matrix, autonomy earned by evidence",
        "Full replay of every action with an exception queue designed for humans",
    ],
},

"autonomous-workflow-orchestration": {
    "hero": ("Long-running workflows with durable state, recovery by design and escalation "
             "choreography: orchestration that survives partial failure, duplicate triggers and "
             "the Tuesday afternoon when the third-party API goes down mid-process."),
    "s1_h": "Workflows fail on week three, not in the demo",
    "s1_close": ("The sections below cover the failure modes that produce zombie work, the "
                 "architecture that makes state durable, and the console that shows recovery "
                 "behavior under injected failure."),
    "s2_h": "Four failure modes that turn orchestration into case debt",
    "s2_lead": ("Every one of these leaves work stranded rather than failed — which is why they "
                "hide until SLA breaches surface them, and why each countermeasure is a "
                "structural property of the runtime."),
    "arch_h": "Reference architecture — durable state and choreographed escalation",
    "arch_lead": ("The design centers on three guarantees: state survives process restarts, "
                  "side effects are idempotent under duplicate triggers, and escalation follows "
                  "a choreography with timers — so nothing waits forever and nothing fires twice."),
    "flow_h": "A case under failure — the recovery path in motion",
    "flow_lead": ("Follow one long-running case through a partial failure: timeout, replay from "
                  "durable state, idempotent re-execution, escalation timers — and where the "
                  "audit record is written."),
    "dash_h": "The orchestration console — recovery posture on one screen",
    "dash_lead": ("On-time completion, zombie count, duplicate side effects and escalation "
                  "success — the four numbers that tell you whether the runtime is managing "
                  "work or generating case debt."),
    "dash_note": ("Reference console — orchestration targets; zombie work is defined, measured "
                  "and retired weekly, never left to age quietly."),
    "chart_h": "Completion and recovery under injected failure",
    "chart_lead": ("Design targets for completion rates and recovery time as failure load "
                   "increases — the curve that proves the runtime degrades gracefully instead of "
                   "silently stranding cases."),
    "stack_h": "Orchestration defaults — and when we deviate",
    "stack_lead": ("Defaults favor durable execution engines with replay semantics over "
                   "in-memory flows; deviation triggers are written because each one moves "
                   "recovery from a property to a hope."),
    "gates_h": "Orchestration release gates — evidence before production load",
    "artifacts_h": "What the platform and process teams inherit",
    "timeline_h": "Durability first, week by week",
    "integ_h": "Integration surface — queues, systems and the escalation desk",
    "integ_lead": ("Orchestration is mostly seam management: the contracts below define how "
                   "steps join systems without duplicating side effects or losing escalations."),
    "controls_h": "Governance overlay — the audit trail of a running process",
    "controls_lead": ("Durable state comes with a durable record: every state transition, retry "
                      "and escalation is journaled, so a regulator's question about any case has "
                      "a definitive answer."),
    "controls_note": ("Chaos drills are part of the gate evidence: injected failures at design "
                      "load are run before promotion, and the recovery traces ship with the "
                      "release."),
    "cta": ("Bring the workflow that currently fails quietly at month-end. The diagnostic will "
            "map its zombie cases and escalation holes — then price what recovery-by-design "
            "would cost."),
    "flagships": ["logistics-supply-chain", "healthcare-life-sciences", "telecom-media"],
    "plays": [
        "Durable workflow state with replay from any checkpoint",
        "Idempotent side effects under duplicate triggers and partial failure",
        "Escalation choreography with timers — nothing strands, nothing fires twice",
    ],
},

"decision-intelligence-systems": {
    "hero": ("Decision models wrapped in policy bounds, challenger benchmarks and explainable "
             "outputs: decisions a regulator can read, a panel can challenge, and a board can "
             "defend — with defer-to-human paths that are designed, not improvised."),
    "s1_h": "A decision system is judged by its worst defensible case",
    "s1_close": ("Below: the failure modes that make decision models indefensible, the reference "
                 "architecture that wraps them in challenge and explanation, and the console the "
                 "risk committee reads."),
    "s2_h": "Four failure modes that make decisions indefensible",
    "s2_lead": ("Each of these survives a demo and dies in a supervisory review — the "
                "countermeasures are the difference between a score and a decision."),
    "arch_h": "Reference architecture — challenger panels around every decision",
    "arch_lead": ("The architecture wraps the primary model in a challenger panel: agreement "
                  "thresholds gate autonomy, disparate-impact monitors run continuously, and "
                  "every output carries reason codes a human panel can audit line by line."),
    "flow_h": "One decision, challenged and explained",
    "flow_lead": ("From feature assembly through primary and challenger scoring, agreement "
                  "gating, reason-code generation and the defer-to-human path — including what "
                  "happens when the panel disagrees."),
    "dash_h": "The decision console the risk committee reads",
    "dash_lead": ("Panel agreement, disparate impact, reason-code coverage and deferral quality "
                  "— four numbers that decide whether the model earns more autonomy or a "
                  "mandatory human review."),
    "dash_note": ("Reference console — decision-system targets; autonomy expands only with panel "
                  "agreement and fairness metrics inside tolerance."),
    "chart_h": "Decision quality against the human panel, quarter by quarter",
    "chart_lead": ("Benchmarks across quarterly suites: model agreement with the expert panel, "
                   "and the disagreement cases where the model was later shown right — the "
                   "evidence that earns autonomy step by step."),
    "stack_h": "Decision stack defaults — and documented deviations",
    "stack_lead": ("Defaults favor challenger coverage and reason-code completeness over raw "
                   "accuracy; deviation triggers are written because each one has fairness or "
                   "explainability consequences."),
    "gates_h": "Decision release gates — what a supervisory review will ask",
    "artifacts_h": "What risk and compliance inherit",
    "timeline_h": "Wrap the model, week by week",
    "integ_h": "Integration surface — policy engines and case systems",
    "integ_lead": ("Decisions land in policy engines and case systems; these contracts carry the "
                   "reason codes and deferral states that keep the human loop real."),
    "controls_h": "Fairness and explainability overlay",
    "controls_lead": ("Disparate-impact monitors, reason-code audits and deferral-quality "
                      "reviews run on schedules — the model's social license is maintained as "
                      "operational discipline, not annual paperwork."),
    "controls_note": ("Defer-to-human is measured, not assumed: deferral quality is scored "
                      "against panel outcomes quarterly, and eroding deferral quality narrows "
                      "model autonomy automatically."),
    "cta": ("Bring the decision your regulator keeps asking about. The diagnostic will show "
            "where the challenger panel, reason codes and deferral design would sit — and what "
            "evidence you could produce tomorrow."),
    "flagships": ["banking-financial-services", "insurance", "public-sector"],
    "plays": [
        "Challenger benchmarks with agreement-gated autonomy",
        "Continuous disparate-impact monitoring with signed tolerances",
        "Reason-code coverage on every output, audited line by line",
    ],
},

"digital-workforce-orchestration": {
    "hero": ("Agent-fleet management run like workforce management: capacity plans against demand "
             "curves, shift and version discipline, credential rotation, utilization that is "
             "measured honestly — and SLAs that hold while the fleet upgrades underneath the "
             "business."),
    "s1_h": "Fifty agents are a workforce, and workforces need management",
    "s1_close": ("Below: the failure modes that grow fleets into liabilities, the reference "
                 "architecture of the fleet layer, and the console that runs the digital "
                 "workforce like the human one."),
    "s2_h": "Four ways fleets sprawl into liabilities",
    "s2_lead": ("Each failure mode is an HR problem wearing a DevOps costume — the "
                "countermeasures borrow deliberately from workforce management practice."),
    "arch_h": "Reference architecture — the fleet layer from capacity to retirement",
    "arch_lead": ("The fleet layer owns what nobody owned in the tool-rollout era: demand-based "
                  "capacity, version trains with canary cohorts, credential lifecycle, and the "
                  "retirement path that stops zombie agents from drawing budget forever."),
    "flow_h": "A week in the fleet — demand, shifts, upgrades, retirement",
    "flow_lead": ("From demand forecasting through shift assignment, version rollout across "
                  "cohorts and the retirement queue — including how SLAs hold during the "
                  "upgrade window."),
    "dash_h": "The fleet console — utilization you can trust",
    "dash_lead": ("Utilization, blocked time, queue SLA breaches and upgrade success — measured "
                  "honestly, because inflated utilization is how fleets hide their real "
                  "capacity."),
    "dash_note": ("Reference console — fleet-management targets; utilization is computed from "
                  "busy time against signed demand, never from license counts."),
    "chart_h": "Fleet state across a demand week",
    "chart_lead": ("Busy, idle, blocked and upgrading shares across the demand curve — the shape "
                   "that decides fleet size, shift policy and where blocked time is a design "
                   "problem rather than a staffing one."),
    "stack_h": "Fleet stack defaults — and deliberate deviations",
    "stack_lead": ("Defaults favor version trains and cohort canaries over big-bang fleet "
                   "upgrades; deviation triggers are written because each one moves SLA risk "
                   "onto the business."),
    "gates_h": "Fleet change gates — what evidence an upgrade carries",
    "artifacts_h": "What the digital-workforce manager inherits",
    "timeline_h": "Fleet quarter in motion, week by week",
    "integ_h": "Integration surface — identity, queues and the demand systems",
    "integ_lead": ("The fleet layer plugs into identity, work queues and the systems that "
                   "forecast demand; these contracts make capacity real instead of nominal."),
    "controls_h": "Credential and lifecycle governance",
    "controls_lead": ("Credential rotation, least-privilege scopes and retirement discipline run "
                      "on schedules — because a fleet's security posture is exactly as current "
                      "as its oldest credential."),
    "controls_note": ("Retirement is enforced by ledger: an agent that misses its review window "
                      "is suspended automatically, and the ledger of retirements ships in the "
                      "handover pack."),
    "cta": ("If your agent count is growing and nobody owns the fleet, the next incident is "
            "already scheduled. Bring the inventory to a briefing and we will price the "
            "management layer against the sprawl."),
    "flagships": ["telecom-media", "retail-consumer-goods", "technology-saas"],
    "plays": [
        "Demand-based capacity plans and shift policy for agent fleets",
        "Version trains with cohort canaries and SLA-held upgrade windows",
        "Credential lifecycle and retirement discipline with an enforced ledger",
    ],
},

"intelligent-document-processing": {
    "hero": ("Extraction and adjudication inside the process, not beside it: documents become "
             "decisions with confidence gates, per-field evidence and a human queue that shrinks "
             "by design — because the root causes of the queue are fixed, not just staffed."),
    "s1_h": "The queue is the product: what it says about your operation",
    "s1_close": ("Below: the failure modes that keep document queues eternal, the architecture "
                 "that wires adjudication into the process, and the console that shows the queue "
                 "shrinking by root cause."),
    "s2_h": "Four failure modes that keep document queues eternal",
    "s2_lead": ("Each of these survives a pilot and bankrupts the operation at scale — the "
                "countermeasures target root causes so the queue shrinks instead of being "
                "staffed."),
    "arch_h": "Reference architecture — adjudication wired into the process",
    "arch_lead": ("Confidence gates route fields, not documents: high-confidence fields post, "
                  "low-confidence fields route to an adjudication surface whose verdicts feed "
                  "the extractor — so every human minute makes the next hundred documents "
                  "cheaper."),
    "flow_h": "A document through the gate, the queue and the ledger",
    "flow_lead": ("From capture through field-level gates and adjudication to posting and "
                  "root-cause logging — including the money-path checks that hold high-value "
                  "documents for review by design."),
    "dash_h": "The document-ops console — queue age as the headline",
    "dash_lead": ("Straight-through rate beside adjudicated field accuracy, queue age beside "
                  "hold rate — the pairing that keeps speed honest and the money path "
                  "protected."),
    "dash_note": ("Reference console — document-processing targets; hold-rate thresholds are "
                  "signed with finance before go-live."),
    "chart_h": "Queue shrinkage by root cause, month by month",
    "chart_lead": ("Queue depth decomposed by root-cause class across six months — template "
                   "drift, missing fields, edge cases, upstream data debt. The shrinking shape "
                   "is the evidence the program is fixing causes, not hiring reviewers."),
    "stack_h": "Extraction defaults — and when we deviate",
    "stack_lead": ("Defaults favor adjudication loops and root-cause logging over raw model "
                   "swaps; deviation triggers are written because each one changes whether the "
                   "queue can shrink at all."),
    "gates_h": "Document-processing gates — evidence before volume",
    "artifacts_h": "What the operations team inherits",
    "timeline_h": "From pilot volume to full estate, week by week",
    "integ_h": "Integration surface — capture channels and systems of record",
    "integ_lead": ("Documents arrive from channels and land in systems of record; these "
                   "contracts define the whole battlefield where queues are won or lost."),
    "controls_h": "Controls overlay — evidence and the money path",
    "controls_lead": ("Per-field evidence, adjudicator identity and money-path holds are "
                      "structural — the audit question 'who decided this value and why' has a "
                      "one-click answer."),
    "controls_note": ("Money-path documents carry mandatory dual review above signed value "
                      "thresholds — automation stops there by design, and the stop is logged as "
                      "a control, not a failure."),
    "cta": ("Bring the queue your team works nights to clear. The sprint will decompose it by "
            "root cause and price what straight-through would honestly cost — hold rates "
            "included."),
    "flagships": ["insurance", "banking-financial-services", "logistics-supply-chain"],
    "plays": [
        "Field-level confidence gates with adjudication wired into the process",
        "Root-cause logging that shrinks the human queue by design",
        "Money-path holds with dual review above signed value thresholds",
    ],
},

"hyperautomation-integration": {
    "hero": ("The contracted seams that make automation real: typed contracts across ERP, CRM, "
             "ITSM and comms, replayable failure handling, rate-limit aware traffic shaping and "
             "monitors that catch API drift before the month-end close does."),
    "s1_h": "Automation dies in the seams, not in the agents",
    "s1_close": ("Below: the failure modes that break integrations at the worst moment, the "
                 "reference architecture of contracted seams, and the console that keeps seam "
                 "health visible through month-end load."),
    "s2_h": "Four failure modes that break seams at month-end",
    "s2_lead": ("Every one of these fires during peak load, which is exactly when nobody can "
                "afford it — the countermeasures are contractual and structural, not heroic."),
    "arch_h": "Reference architecture — typed seams with replay and drift monitors",
    "arch_lead": ("Seams are contracts, not credentials: typed request/response schemas, "
                  "idempotency keys, replay queues and drift monitors that diff live API "
                  "behavior against the contract — so a vendor's silent change is caught by a "
                  "monitor, not by a failed close."),
    "flow_h": "One write across three systems, guaranteed once",
    "flow_lead": ("From the automation's action through contract validation, rate shaping and "
                  "the idempotent write to the replay path when a system rejects mid-flight — "
                  "including where duplicates would otherwise be born."),
    "dash_h": "The seam console — health under real load",
    "dash_lead": ("Seam success rate, replay queue depth, duplicate writes and drift detections "
                  "— the four numbers that predict whether month-end will be boring, which is "
                  "the highest compliment an integration can earn."),
    "dash_note": ("Reference console — seam targets at design load; drift monitors diff live "
                  "API behavior against contracts on every release train."),
    "chart_h": "Seam health across month-end load",
    "chart_lead": ("Success rate and replay depth across the load curve — the signature that "
                   "shows where rate limits bite and where the traffic shaping holds."),
    "stack_h": "Integration defaults — and documented deviations",
    "stack_lead": ("Defaults favor typed contracts and replay queues over point-to-point "
                   "credentials; deviation triggers are written because each one moves failure "
                   "from a queue to a pager."),
    "gates_h": "Seam release gates — evidence before the next close",
    "artifacts_h": "What the integration team inherits",
    "timeline_h": "Seam by seam, week by week",
    "integ_h": "Integration surface — the systems list, honestly named",
    "integ_lead": ("The scope is the estate itself: ERP, CRM, ITSM, communications and the "
                   "queues between them — each with the contract fields that make automation "
                   "survive contact with reality."),
    "controls_h": "Integration governance — contracts as controlled artifacts",
    "controls_lead": ("Contracts are versioned with owners and change windows; a seam change is "
                      "a reviewed release, and the drift monitor holds the vendor honest "
                      "between reviews."),
    "controls_note": ("Sandbox parity is verified before every release: if the vendor's sandbox "
                      "drifts from production behavior, the seam gate stays closed — sandbox "
                      "fiction is treated as a failed gate."),
    "cta": ("Map the seams your last close depended on, then count how many have owners and "
            "contracts. The diagnostic will score every one — and price what boring month-ends "
            "cost."),
    "flagships": ["manufacturing", "energy-utilities", "education-research"],
    "plays": [
        "Typed seam contracts across ERP, CRM, ITSM and comms",
        "Replayable failure handling with idempotency and duplicate prevention",
        "Drift monitors that diff live API behavior against signed contracts",
    ],
},
}
