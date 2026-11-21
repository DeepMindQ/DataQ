"""narr_applied — hand-written narrative layer for the Applied AI & Generative AI domain.

Every string here is unique to its page. No shared sentence banks: headings,
leads and CTAs are authored once, for one page, in its own voice.
"""

HUB = {
    "hero": ("Language is now an engineering surface. Applied AI & Generative AI runs seven "
             "practices that turn models into governed production systems — retrieval that cites "
             "its sources, tuning that never regresses silently, vision that feeds systems of "
             "record, and one platform that keeps every model call observable, bounded and "
             "affordable."),
    "s_practices": "Seven practices, one evaluation discipline",
    "s_deep": "What separates a production program from a stalled pilot",
    "s_arch": "The domain reference architecture — from corpus to cited answer",
    "arch_lead": ("The reference architecture below is the shape every engagement converges on, "
                  "whatever the use case: contracts at ingest, a permission-aware knowledge spine, "
                  "guarded reasoning services, an evaluation lane that can block any release, and "
                  "experience surfaces that inherit the controls. The orange nodes are the ones "
                  "auditors and CFOs both end up caring about."),
    "s_dash": "The domain on one screen — commitments, releases, decisions",
    "dash_lead": ("This console is the operating contract rendered honestly: tiles are the numbers "
                  "we sign for, bars show where each release stands gate by gate, and the log is a "
                  "real decision feed whose shapes match the runbook your team receives at handover."),
    "dash_note": ("Reference console for the Applied AI domain — targets are design bands this "
                  "practice is gated to, not client-identifiable figures."),
    "s_chart": "Capability posture and where the bar sits",
    "chart_lead": ("Radar profile against six axes we are gated on. The gap between current build "
                   "posture and target band is deliberate: it is the work program the next two "
                   "quarters fund, and it is re-scored at every gate review."),
    "s_evidence": "Sector depth — where Applied AI runs deepest today",
    "evidence_lead": ("Applied AI is bought differently in different sectors: banks buy grounded "
                      "answers under supervisory review, hospitals buy documentation time back, "
                      "software companies buy the platform. The bars below are live counts of "
                      "sub-industry capability briefs published on this site — the honest map of "
                      "where sector-calibrated depth already exists."),
    "evidence_chart_title": "Applied AI & Generative AI — published sub-industry briefs by sector",
    "explorer_title": "Applied AI in your sector — pick the industry and see the delivery plan",
    "explorer_intro": ("Twelve sectors, twelve different regulatory and operating realities. Select "
                       "yours: the panel shows the hook that usually starts the program, the "
                       "deliverables we build, the targets we sign, and the sector brief behind it."),
    "plays": [
        "Governed retrieval and generation with citations and refusal-by-default",
        "One platform door for every model call — authz, budgets, caching, traces",
        "An eval harness that blocks silent regressions before users see them",
    ],
    "flagships": ["banking-financial-services", "healthcare-life-sciences", "technology-saas"],
    "s_engage": "How engagements run in this domain",
    "engage": [
        ["Diagnostic — two weeks", "The metric is signed, the corpus and platform estate are mapped, and the gate model is scored for your reality. You keep the gate map whoever builds."],
        ["Provability sprint — four weeks", "One practice runs a fund-or-kill slice on your real data path: auditable numbers at exit, or a clean kill with the reasons written down."],
        ["Build — ten to fourteen weeks", "Architecture and gates from these pages applied to your estate, with the operating console live from week two and evidence packs accumulating per release."],
        ["Industrialize — ongoing", "Quarterly re-baselines, domain-level gate reviews, and the platform-reuse review that keeps the next use case cheap instead of another first project."],
    ],
    "s_gates": "Domain-level release gates",
    "cta": ("Bring one metric you own to a briefing — we will show you which practice carries it, "
            "which gates you would fail today, and what the first funded slice would look like."),
}

PAGES = {

"rag-knowledge-systems": {
    "hero": ("Retrieval that cites or refuses: permission-aware RAG over your regulated document "
             "estate, where every answer carries its sources, its freshness and its permission "
             "lineage — and where the corpus contracts that make that possible are built first, "
             "not last."),
    "s1_h": "Why corpus engineering decides the answer quality",
    "s1_close": ("Everything below is build-order material: the failure modes we design against, "
                 "the architecture that fixes them, and the gates a release clears before a user "
                 "sees an answer."),
    "s2_h": "Four failure modes that quietly kill enterprise RAG",
    "s2_lead": ("Each failure below has shipped in production somewhere; each has a countermeasure "
                "that lands with the build, not in a later phase."),
    "arch_h": "Reference architecture — permission-aware retrieval with citations",
    "arch_lead": ("Two properties matter more than model choice here: nothing reaches the answer "
                  "layer without passing the permission map, and every generated claim traces to a "
                  "span in a source the asker was allowed to read. The lanes below show how those "
                  "properties are enforced structurally rather than by prompt goodwill."),
    "flow_h": "The answer path, question by question",
    "flow_lead": ("Follow one question through the pipeline: rewrite, permission-filtered "
                  "retrieval, grounding assembly, guarded generation, citation check — and what "
                  "happens when any stage fails."),
    "dash_h": "The operating console for a retrieval estate",
    "dash_lead": ("Five numbers summarize whether a RAG system is healthy: grounded rate, citation "
                  "precision, cohort recall, latency budget and the refusal rate that proves the "
                  "system knows what it does not know."),
    "dash_note": ("Reference console — RAG service targets pinned to the signed baseline and "
                  "re-scored at each gate review."),
    "chart_h": "Retrieval quality across eval suite generations",
    "chart_lead": ("Three quality series tracked across four quarterly eval-suite versions: recall "
                   "improves as the corpus contracts mature, groundedness and citation precision "
                   "ride along, and the suite itself is versioned so any change is attributable."),
    "stack_h": "The stack we default to — and when we deliberately leave it",
    "stack_lead": ("Defaults exist so the first sprint spends its time on your corpus, not on "
                   "bikeshedding components. Deviations are allowed where your estate argues for "
                   "them; the conditions are written down so the deviation is a decision, not a drift."),
    "gates_h": "What a release must prove before promotion",
    "artifacts_h": "What your team owns at handover",
    "timeline_h": "How the build runs, week by week",
    "integ_h": "Where this service plugs into your estate",
    "integ_lead": ("RAG is an integration-heavy service: the value lives in your existing estate, "
                   "so the connector contracts below are the real scope, not an afterthought."),
    "controls_h": "The control surface — permission fidelity, trace discipline, egress policy",
    "controls_lead": ("Controls that make the system auditable in regulated sectors: permission "
                      "probing, egress scanning, trace retention and the evidence pack that ties "
                      "each answer to a reviewable decision path."),
    "controls_note": ("Permission fidelity probes run continuously in staging and nightly in "
                      "production shadows — any synthetic principal reading denied content pages "
                      "security before a user could ever see it."),
    "cta": ("Bring your worst document estate — the duplicated portals, the stale wikis, the ACLs "
            "nobody trusts. The two-week diagnostic will tell you exactly what grounded answers "
            "would cost there, and which gates you would fail today."),
    "flagships": ["banking-financial-services", "insurance", "public-sector"],
    "plays": [
        "Corpus contracts: canonical registry, freshness SLAs, permission scans",
        "Hybrid retrieval with reranking and span-level citations",
        "Eval suite vN that blocks promotion on groundedness or permission regressions",
    ],
},

"genai-platform-engineering": {
    "hero": ("One governed door for every model call in the enterprise: the gateway, registry, "
             "prompt CI, guardrails, caching and spend controls that let fifty use cases share "
             "infrastructure without sharing incidents — or budgets."),
    "s1_h": "The platform economics nobody prices until month three",
    "s1_close": ("The sections below are the platform build order: failure modes first, then the "
                 "reference architecture, then the console that keeps the platform honest in "
                 "production."),
    "s2_h": "Four ways GenAI platforms blow their mandate",
    "s2_lead": ("Platforms fail politically before they fail technically — these four failure "
                "modes are why internal platforms get bypassed, and the countermeasures that keep "
                "teams on the governed path."),
    "arch_h": "Reference architecture — the governed model gateway",
    "arch_lead": ("Every property the platform promises — observability, bounded spend, policy "
                  "enforcement — is a structural fact of this topology, not a policy document. "
                  "Notice that no lane talks to a model directly except through the gateway."),
    "flow_h": "A request through the governed door",
    "flow_lead": ("Trace one call end to end: authentication, quota check, prompt injection scan, "
                  "cache lookup, model routing, guardrail pass, metered response — with the "
                  "short-circuit paths where requests are stopped cheaply."),
    "dash_h": "The platform console finance and engineering share",
    "dash_lead": ("Latency, cache economics, unit cost, guardrail pressure and registry drift on "
                  "one screen — the same numbers in the steering pack and the on-call runbook."),
    "dash_note": ("Reference console — gateway targets at reference load; budgets are signed per "
                  "domain before the platform opens to consumers."),
    "chart_h": "Cost and latency posture across load tiers",
    "chart_lead": ("Design targets for the gateway under three load tiers: the caching and routing "
                   "policy that holds p95 under budget at peak, and the cost per thousand calls "
                   "finance signs against."),
    "stack_h": "Default platform components — and the deviations we allow",
    "stack_lead": ("The default stack optimizes for operability with a small senior team; each "
                   "deviation condition is a written trigger, so choosing differently is a "
                   "documented decision rather than an accumulation of exceptions."),
    "gates_h": "Platform release gates — evidence before exposure",
    "artifacts_h": "What the platform team hands over",
    "timeline_h": "The platform build, sprint by sprint",
    "integ_h": "Integration surface — identity, finance and every consuming team",
    "integ_lead": ("A platform is mostly integration: the contracts below are what make fifty "
                   "teams able to consume one gateway without fifty support tickets."),
    "controls_h": "Governance enforced once, inherited by every consuming team",
    "controls_lead": ("Platform-level controls multiply across every consuming use case, which is "
                      "exactly why they are enforced once, here — injection scanning, egress "
                      "policy, key vaulting and per-domain budget enforcement."),
    "controls_note": ("Guardrail configuration is versioned like code: a rule change is a pull "
                      "request with an eval run attached, never a dashboard edit at midnight."),
    "cta": ("If every team is wiring its own model calls today, the platform decision is already "
            "late. Bring the use-case inventory to a briefing and we will price the governed door "
            "against the sprawl you are currently funding."),
    "flagships": ["banking-financial-services", "technology-saas", "telecom-media"],
    "plays": [
        "Model gateway with authz, quotas, semantic caching and full traces",
        "Prompt CI with versioned guardrail suites and model-registry discipline",
        "Spend controls per domain with signed unit-cost targets and burn-down alerts",
    ],
},

"llm-fine-tuning-ops": {
    "hero": ("A tuning factory, not a notebook: decontaminated datasets, multi-task eval gates "
             "that block silent regressions, distillation that keeps quality while cutting serving "
             "cost, and canary rollout with a rehearsed rollback path."),
    "s1_h": "Fine-tuning is a data engineering program that occasionally involves a GPU",
    "s1_close": ("Below: the failure modes that produce quietly bad models, the factory "
                 "architecture that prevents them, and the gates a tuned model clears before it "
                 "serves a real user."),
    "s2_h": "Four ways tuning programs produce quietly bad models",
    "s2_lead": ("None of these failures announce themselves in the demo — they surface weeks later "
                "in production, which is why each countermeasure is structural rather than "
                "procedural."),
    "arch_h": "Reference architecture — the tuning factory from dataset to canary",
    "arch_lead": ("The factory has four hard boundaries: datasets are decontaminated before they "
                  "enter training, every candidate passes the multi-task eval gate, promotion "
                  "happens through canary with automatic rollback, and checkpoints are registered "
                  "or they do not exist."),
    "flow_h": "The promotion path — dataset to production traffic",
    "flow_lead": ("From raw corpora through decontamination and labeling, into training and "
                  "candidate eval, then canary exposure with the exact conditions that trigger "
                  "rollback written into the pipeline itself."),
    "dash_h": "The model-ops console for tuned fleets",
    "dash_lead": ("Task accuracy against base, multi-task regressions, contamination rate, "
                  "distillation retention and time-to-promotion — the five numbers that decide "
                  "whether tuning is compounding or thrashing."),
    "dash_note": ("Reference console — tuned-model fleet targets; promotion is blocked on any "
                  "regression outside the signed tolerance."),
    "chart_h": "Quality retention against serving cost across model sizes",
    "chart_lead": ("The distillation decision, quantified: task quality retained and serving cost "
                   "per thousand calls at each model size — the trade surfaced so the fleet mix "
                   "is an economic choice, not a default."),
    "stack_h": "Training and serving defaults — and when we deviate",
    "stack_lead": ("Defaults favor reproducibility and audit: pinned data snapshots, deterministic "
                   "eval, registered checkpoints. Deviation conditions are written because every "
                   "one of them has governance consequences."),
    "gates_h": "Model promotion gates — what evidence blocks a bad tune",
    "artifacts_h": "What you own when the factory is handed over",
    "timeline_h": "Factory build-out, week by week",
    "integ_h": "Integration surface — data platform to serving mesh",
    "integ_lead": ("The factory sits on your existing data platform and serving mesh; these are "
                   "the contracts that make the factory a system, not a set of scripts."),
    "controls_h": "Model governance — dataset-to-canary lineage",
    "controls_lead": ("Model lineage is the governance product here: every production model traces "
                      "to decontaminated dataset versions, eval results and approval records that "
                      "a model-risk committee can walk without a guide."),
    "controls_note": ("Contamination probes run against every dataset version: overlapping n-grams "
                      "against eval sets are measured and reported — zero is the only passing "
                      "number."),
    "cta": ("If your tuned model's last regression was discovered by a user, the eval gate is "
            "missing, not the talent. Bring the model inventory to a briefing and we will map "
            "your promotion path onto the factory."),
    "flagships": ["banking-financial-services", "healthcare-life-sciences", "technology-saas"],
    "plays": [
        "Dataset factory: decontamination, label consistency, hard-negative mining",
        "Multi-task eval gate with zero-regression promotion policy",
        "Distillation and adapter tuning with canary rollout and rehearsed rollback",
    ],
},

"multimodal-vision-systems": {
    "hero": ("Document and scene understanding wired into the systems of record: extraction with "
             "per-field confidence, ledger reconciliation that catches what models miss, and "
             "evidence trails that let auditors verify every posted value without leaving the "
             "console."),
    "s1_h": "Vision in the enterprise is a bookkeeping problem wearing a camera",
    "s1_close": ("The sections below cover the failure modes that erode trust in extraction, the "
                 "reference architecture that keeps humans in the loop where it matters, and the "
                 "gates that decide what posts straight through."),
    "s2_h": "Four failure modes that turn extraction into re-work",
    "s2_lead": ("Every one of these shows up as a review backlog rather than an error report — "
                "which is why the countermeasures target the review queue, not just the model."),
    "arch_h": "Reference architecture — confidence-gated extraction into systems of record",
    "arch_lead": ("The architecture's central decision is the confidence gate: fields above "
                  "threshold post straight through, fields below route to a review surface that "
                  "trains the loop. Reconciliation runs on the ledger side, so misposting is "
                  "caught where the money lives."),
    "flow_h": "A document's path — pixels to posted entries",
    "flow_lead": ("From capture through layout parsing, field extraction and validation, to the "
                  "posting decision and the review loop — including what happens when layout "
                  "drift breaks an extractor mid-week."),
    "dash_h": "The vision-ops console operations and finance share",
    "dash_lead": ("Field accuracy, straight-through rate, review queue depth, drift alerts and "
                  "page latency — the numbers that decide whether extraction is compounding or "
                  "quietly generating re-work."),
    "dash_note": ("Reference console — extraction targets by document class; thresholds are signed "
                  "with the process owner before go-live."),
    "chart_h": "Straight-through economics by document class",
    "chart_lead": ("Two series per document class: the straight-through share and the review load "
                   "it leaves behind. The classes are ordered by the volume your operation "
                   "actually processes, so the capacity plan falls out of the chart."),
    "stack_h": "Extraction stack defaults — and documented deviations",
    "stack_lead": ("Defaults bias toward per-field evidence and reconciliation over raw model "
                   "scores; deviations are permitted where document classes argue for them, with "
                   "the trigger conditions written alongside."),
    "gates_h": "Extraction release gates — what blocks a go-live",
    "artifacts_h": "The handover package for operations and finance",
    "timeline_h": "From capture to straight-through, week by week",
    "integ_h": "Integration surface — capture, records and the review bench",
    "integ_lead": ("Vision systems live or die on the systems of record they feed; these "
                   "integration contracts are the real scope of the service."),
    "controls_h": "Audit-ready extraction — evidence on every posted field",
    "controls_lead": ("Every posted field carries extraction evidence — source region, model "
                      "version, confidence and reviewer identity — so an auditor can verify a "
                      "posting without leaving the console."),
    "controls_note": ("Layout drift alerts are wired to the capture pipeline: a changed template "
                      "pages the owner before extraction quality degrades, not after the "
                      "misposting is reconciled."),
    "cta": ("Bring the document class your back office dreads most. The four-week provability "
            "sprint will show you the straight-through rate it can honestly reach, with the "
            "review load priced in."),
    "flagships": ["insurance", "logistics-supply-chain", "healthcare-life-sciences"],
    "plays": [
        "Confidence-gated extraction wired to your systems of record",
        "Ledger-side reconciliation with per-field evidence for auditors",
        "Review surfaces that train the loop instead of growing a back-office tax",
    ],
},

"conversational-ai-digital-humans": {
    "hero": ("Voice and chat agents that resolve more without losing trust: grounded answers, "
             "dignified handoffs that carry full context, streaming voice inside real-time "
             "budgets, and nightly dialog evaluation that measures containment honestly."),
    "s1_h": "Containment and trust are one metric, not two",
    "s1_close": ("What follows is the build anatomy: the failure modes that inflate containment "
                 "while destroying CSAT, the architecture that holds both, and the console that "
                 "keeps the trade visible every day."),
    "s2_h": "Four failure modes that inflate containment and destroy trust",
    "s2_lead": ("Each of these produces a dashboard that looks great in the monthly review and a "
                "customer base that quietly stops using the channel — the countermeasures target "
                "the trust side of the ledger."),
    "arch_h": "Reference architecture — grounded dialog with dignified escalation",
    "arch_lead": ("Grounding is the spine: intent understanding, retrieval against the knowledge "
                  "contracts, guarded generation and a handoff design that carries the full "
                  "conversation state to a human who never asks the customer to repeat themselves."),
    "flow_h": "A conversation's lifecycle, turn by turn",
    "flow_lead": ("From greeting through intent and grounding to resolution or handoff — with the "
                  "guard interventions, the emotion-aware escalation triggers and the timeout "
                  "paths marked where they actually fire."),
    "dash_h": "The conversation console — containment with its cost visible",
    "dash_lead": ("Containment next to CSAT, recontact within seven days next to voice latency, "
                  "guard interventions next to volume — pairs, not solo metrics, because every "
                  "one of them is a trade."),
    "dash_note": ("Reference console — conversational targets by intent family; containment is "
                  "never reported without its CSAT pair."),
    "chart_h": "The containment–satisfaction frontier by intent family",
    "chart_lead": ("Two series across intent families: containment share and CSAT for bot-handled "
                   "sessions. The families where the two series diverge are exactly where the "
                   "next tuning cycle is spent."),
    "stack_h": "Dialog stack defaults — and when we deviate",
    "stack_lead": ("Defaults favor grounding quality and handoff dignity over raw automation rate; "
                   "deviation conditions are written because each one moves the trust ledger."),
    "gates_h": "Dialog release gates — what blocks a channel launch",
    "artifacts_h": "What the contact center inherits",
    "timeline_h": "Channel build-out, week by week",
    "integ_h": "Integration surface — telephony, CRM and the agent desktop",
    "integ_lead": ("Conversations end in systems, not in chat windows: telephony, CRM, agent "
                   "desktop and the identity layer are the integration scope that decides whether "
                   "handoffs are dignified or amnesiac."),
    "controls_h": "Dialog governance — consent, guard decisions, trace retention",
    "controls_lead": ("Dialog traces are retained with consent state, guard decisions and "
                      "handoff context attached — the audit path a communications regulator "
                      "would ask for, already assembled."),
    "controls_note": ("Every guard intervention is reviewable as a transcript pair — the turn "
                      "attempted and the grounded alternative served — so policy tuning is "
                      "evidence-led, not anecdote-led."),
    "cta": ("Bring the intent family your contact center handles worst. The sprint will measure "
            "honest containment and the CSAT cost of chasing it — before you commit the channel."),
    "flagships": ["telecom-media", "retail-consumer-goods", "banking-financial-services"],
    "plays": [
        "Grounded voice and chat with streaming budgets inside real-time bounds",
        "Dignified handoffs that carry full context to the human desktop",
        "Nightly dialog eval that reports containment only beside its CSAT pair",
    ],
},

"enterprise-ai-strategy": {
    "hero": ("Portfolio management under uncertainty: provability screens that kill weak ideas "
             "cheaply, risk-tiered gates that match your regulatory reality, one platform decision "
             "made before the seventh pilot, and a stop-loss discipline that actually holds."),
    "s1_h": "Why AI strategy is a portfolio problem, not a roadmap",
    "s1_close": ("Below is the operating machinery of the portfolio: failure modes, the reference "
                 "architecture for the decision system itself, and the console the steering "
                 "committee reads."),
    "s2_h": "Four ways AI portfolios stall at the board level",
    "s2_lead": ("These are the governance and incentive failures, not the modeling ones — each "
                "countermeasure is a structural change to how the portfolio is funded and judged."),
    "arch_h": "Reference architecture — the decision system behind the portfolio",
    "arch_lead": ("The architecture below is deliberately boring: intake with provability screens, "
                  "a risk-tiered gate ladder, a single platform decision point, and the evidence "
                  "store that lets the steering committee audit its own choices a year later."),
    "flow_h": "From idea intake to funded slice",
    "flow_lead": ("How an idea moves through screening, baseline definition, gate scoring and the "
                  "fund-or-kill verdict — with the exit paths where most ideas correctly die."),
    "dash_h": "The portfolio console the steering committee reads",
    "dash_lead": ("Funded slices, baselines signed, median time to first gate, ideas stopped on "
                  "evidence and platform reuse — the five numbers that show whether strategy is "
                  "compounding or performing."),
    "dash_note": ("Reference console — portfolio-level targets for a mid-size program; allocation "
                  "bands are re-set quarterly with the CFO's office."),
    "chart_h": "Portfolio shape across quarters",
    "chart_lead": ("Allocation bands across four quarters: discovery, provability, build and "
                   "industrialize. The healthy signature is a portfolio that shifts weight right "
                   "as evidence accumulates — not one that stays in discovery forever."),
    "stack_h": "Standards the portfolio runs on — and where we deviate",
    "stack_lead": ("The strategy layer standardizes decisions, not tools: gate definitions, "
                   "evidence formats and re-baseline cadence. Where an enterprise standard "
                   "already exists, it wins; the conditions are explicit."),
    "gates_h": "Portfolio gates — the evidence each rung demands",
    "artifacts_h": "What the executive team owns at the end",
    "timeline_h": "How the strategy engagement runs",
    "integ_h": "Integration surface — finance, risk and the PMO",
    "integ_lead": ("Strategy lives in your existing governance machinery; these are the working "
                   "agreements that make the portfolio auditable inside it."),
    "controls_h": "Decision governance — the audit trail of funded and killed ideas",
    "controls_lead": ("Decision lineage is the deliverable: every funded and killed idea carries "
                      "its screen, baseline and verdict — the record that makes the next audit a "
                      "reading exercise instead of an archaeology project."),
    "controls_note": ("The stop-loss is signed at funding time: the conditions under which a "
                      "funded slice is stopped are written before the first sprint, so the "
                      "argument never happens after the money is spent."),
    "cta": ("Bring the pilot inventory — including the dead ones. The two-week diagnostic will "
            "tell you which of them were killable on evidence, and what the funded portfolio "
            "should have looked like instead."),
    "flagships": ["insurance", "manufacturing", "public-sector"],
    "plays": [
        "Provability screens and risk-tiered gates calibrated to your regulator",
        "One platform decision, made once, before the seventh pilot",
        "A stop-loss discipline signed at funding time and actually enforced",
    ],
},

"ai-poc-value-validation": {
    "hero": ("The four-week sprint that ends in a fund-or-kill verdict with auditable numbers: "
             "baseline signed before week one ends, a real data path instead of a demo set, and "
             "a written verdict your CFO can take to the bank."),
    "s1_h": "A PoC exists to produce a decision, not a demo",
    "s1_close": ("Below is the anatomy of the sprint: the failure modes that turn PoCs into "
                 "demo-ware, the reference architecture for a four-week evidence machine, and the "
                 "gates the verdict must clear."),
    "s2_h": "Four ways PoCs become demo-ware",
    "s2_lead": ("Each failure here is a shortcut taken in week one that costs a program in month "
                "six — the countermeasures are cheap, and none of them is optional in this sprint."),
    "arch_h": "Reference architecture — the four-week evidence machine",
    "arch_lead": ("The architecture is sized for four weeks: one baseline, one metric, one real "
                  "data path, one verdict. Everything that does not serve the verdict is "
                  "explicitly out of scope, and the out-of-scope list is written at kickoff."),
    "flow_h": "The sprint path — from kickoff to verdict",
    "flow_lead": ("Week-by-week flow from baseline signing through data-path construction to the "
                  "verdict review — including the mid-sprint checkpoint where weak ideas are "
                  "killed early and cheaply."),
    "dash_h": "The sprint console — verdicts, not velocity",
    "dash_lead": ("Sprints run, verdicts on time, ideas funded to production, ideas killed on "
                  "evidence and baselines signed — the record that shows whether the sprint "
                  "process is producing decisions or theater."),
    "dash_note": ("Reference console — sprint-program targets; every verdict carries its evidence "
                  "pack whether the answer is fund or kill."),
    "chart_h": "Where PoC ideas actually die",
    "chart_lead": ("Outcomes across one quarter of sprints, by the stage where each idea was "
                   "stopped: screening, baseline, data path or verdict. A healthy program kills "
                   "most ideas before the build — that is the point."),
    "stack_h": "Sprint stack defaults — and deliberate deviations",
    "stack_lead": ("The sprint stack optimizes for disposable speed inside your real controls: "
                   "production data governance applies from day one, which is exactly why the "
                   "verdict survives procurement."),
    "gates_h": "Sprint gates — the evidence a verdict carries",
    "artifacts_h": "What you hold at verdict time",
    "timeline_h": "The four weeks, gate by gate",
    "integ_h": "Integration surface — just enough production to be honest",
    "integ_lead": ("The sprint touches your real data path by design; these are the minimum "
                   "contracts that make the numbers auditable without building the platform twice."),
    "controls_h": "Sprint governance — production-grade data handling in miniature",
    "controls_lead": ("Sprints run under the same data governance as production: consent, PII "
                      "handling and access are inherited from your estate, so the verdict is "
                      "admissible in the steering meeting that counts."),
    "controls_note": ("Kill verdicts get the same evidence pack as funded ones — the auditable "
                      "record of why an idea died is the asset that keeps the next portfolio "
                      "honest."),
    "cta": ("Pick the idea your board keeps asking about. Four weeks, one metric, a real data "
            "path — and a verdict with numbers attached, whichever way it lands."),
    "flagships": ["retail-consumer-goods", "energy-utilities", "education-research"],
    "plays": [
        "Signed baseline and metric before the first build hour",
        "A real data path into your estate — no demo sets, no cherry-picked weeks",
        "A written fund-or-kill verdict with an evidence pack and a priced production path",
    ],
},
}
