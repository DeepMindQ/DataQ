"""narr_data — narrative layer for the Data, Analytics & Lakehouse domain."""

HUB = {
    "hero": ("Data is the substrate every other domain stands on. Data, Analytics & Lakehouse "
             "runs seven practices built on contract-first engineering: schemas are versioned "
             "agreements with owners, SLAs are typed and measured, and every table, metric and "
             "model carries the governance that makes it usable in front of an auditor."),
    "s_practices": "Seven practices from bronze to billed product",
    "deep": [
        ("The discipline that separates a data platform from a data swamp is contracts: every "
         "pipeline consumes and produces typed agreements with named owners, freshness SLAs and "
         "quarantine behavior. When something breaks, the contract tells you who is paged and "
         "what downstream is safe — before anyone opens a dashboard to guess."),
        ("The economics matter as much as the engineering: storage growth, compute per query and "
         "duplicate estates are signed line items, reviewed quarterly with finance. A platform "
         "that cannot state its unit cost per workload is not governed; it is merely hosted."),
    ],
    "s_deep": "Contracts, not culture: what makes data governed",
    "s_arch": "The domain reference architecture — ingest to decision",
    "arch_lead": ("The spine below is the shape every engagement converges on: contract-gated "
                  "ingest, a lakehouse with promotion gates between bronze, silver and gold, "
                  "serving layers keyed to decision latency, and governance woven through rather "
                  "than bolted on the end."),
    "s_dash": "The platform on one screen — freshness, quarantine, cost",
    "dash_lead": ("Freshness SLA adherence, quarantine dwell, compaction lag and storage growth — "
                  "the four tiles the platform steering reads weekly, rendered as they appear in "
                  "the review."),
    "dash_note": ("Reference console — platform targets; SLA definitions are signed with the "
                  "data owners before the platform opens to consumers."),
    "s_chart": "Freshness by tier — the maturing platform curve",
    "chart_lead": ("Radar profile across six axes we are gated on: the gap between posture and "
                   "target band is the funded work program, re-scored at every quarterly gate "
                   "review."),
    "chart_override": {
        "variant": "area",
        "title": "Freshness SLA adherence by tier — quarterly trajectory, design bands",
        "cats": ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"],
        "series": [
            ("Gold tier (executive)", [93.0, 94.6, 95.8, 96.7, 97.2, 97.6]),
            ("Silver tier (operational)", [88.5, 90.8, 92.4, 93.9, 94.8, 95.3]),
            ("Bronze tier (exploration)", [82.0, 84.9, 86.8, 88.6, 89.7, 90.4]),
        ],
        "unit": "%",
        "yMax": 100,
        "caption": "Reference trajectory for a platform maturing under contract discipline — tiers improve in order of business criticality.",
    },
    "chart_note": None,
    "s_evidence": "Sector depth — where the data practice runs deepest today",
    "evidence_lead": ("Every sector thinks its data is uniquely messy; the contracts that fix it "
                      "are sector-specific anyway. The bars count published sub-industry briefs "
                      "on this site — where sector-calibrated data playbooks already exist."),
    "evidence_chart_title": "Data, Analytics & Lakehouse — published sub-industry briefs by sector",
    "explorer_title": "Your data estate, your sector — pick the industry and see the plan",
    "explorer_intro": ("Regulated banks, national grids and retail chains buy different data "
                       "discipline. Select yours: the panel shows the entry problem, the "
                       "deliverables, the targets we sign and the sector brief behind them."),
    "plays": [
        "Contract-gated pipelines with typed SLAs and named owners",
        "Lakehouse promotion paths with quality gates and honest storage economics",
        "Governance that survives audit — lineage, catalogs, purpose limits",
    ],
    "flagships": ["banking-financial-services", "healthcare-life-sciences", "telecom-media"],
    "s_engage": "How data platform engagements run",
    "engage": [
        ["Diagnostic — two weeks", "Estate mapped, SLAs scored, the gate model filled in against your estate — with the dual-run cost of any migration priced before you commit."],
        ["Provability sprint — four weeks", "One pipeline or one metric runs a fund-or-kill slice: contract coverage, freshness and cost per query on your real data."],
        ["Build — ten to fourteen weeks", "The lakehouse spine, contracts and serving layers built to the reference architecture, with the console live from week two."],
        ["Industrialize — ongoing", "Quarterly re-baselines, contract reviews with data owners, and the storage/compute economics review that keeps the platform honest with finance."],
    ],
    "s_gates": "Platform release gates — the domain contract in evidence",
    "cta": ("Bring the metric nobody trusts and the pipeline nobody owns. The two-week "
            "diagnostic will score your estate's contracts — and show which gates you would "
            "fail today, in front of your own auditors."),
}

PAGES = {

"lakehouse-architecture": {
    "hero": ("Bronze to silver to gold on open table formats: a promotion path with quality "
             "gates between layers, time travel for every audit question, and storage economics "
             "signed with finance — instead of a swamp with dashboards on top."),
    "s1_h": "The lakehouse is a governance decision before it is a technology choice",
    "s1_close": ("Below: the failure modes that turn lakehouses into swamps, the reference "
                 "architecture that keeps layers honest, and the console that keeps storage "
                 "economics visible."),
    "s2_h": "Four ways lakehouses become swamps",
    "s2_lead": ("Each failure mode starts as a convenience and compounds into an audit finding — "
                "the countermeasures are promotion gates, not policies nobody enforces."),
    "arch_h": "Reference architecture — the promotion path from bronze to gold",
    "arch_lead": ("Layers are earned, not configured: bronze accepts raw with contracts, silver "
                  "requires quality gates to pass, gold serves decisions with freshness SLAs. "
                  "Time travel and quarantine make the path reversible and auditable."),
    "flow_h": "One record's promotion, gate by gate",
    "flow_lead": ("From raw landing through dedup, quality gates, schema evolution and compaction "
                  "to gold serving — including where a record is quarantined and who is paged."),
    "dash_h": "The lakehouse console — freshness and cost on one screen",
    "dash_lead": ("Freshness SLA adherence, quarantine dwell, compaction lag and deduped storage "
                  "growth — the pairing that keeps performance and economics in the same "
                  "conversation."),
    "dash_note": ("Reference console — lakehouse targets by tier; storage growth is reviewed "
                  "quarterly with finance against the signed unit-economics plan."),
    "chart_h": "Latency and storage efficiency by table class",
    "chart_lead": ("Query latency and storage cost per table class — the shape that decides "
                   "compaction policy, tiering and which tables earn gold-level SLAs."),
    "stack_h": "Table-format defaults — and documented deviations",
    "stack_lead": ("Defaults favor open table formats with time travel and schema evolution; "
                   "deviation triggers are written because each one changes what audits can "
                   "reconstruct later."),
    "gates_h": "Lakehouse release gates — evidence before promotion",
    "artifacts_h": "What the platform team inherits",
    "timeline_h": "Layers in order, week by week",
    "integ_h": "Integration surface — sources, catalogs and consumers",
    "integ_lead": ("The lakehouse serves consumers, not architects; these contracts define how "
                   "sources land and how catalogs expose tables without creating shadow copies."),
    "controls_h": "Governance overlay — lineage and the audit trail",
    "controls_lead": ("Lineage from landing to serving is captured as data, not documentation — "
                      "the audit question 'where did this number come from' resolves to a query, "
                      "not a meeting."),
    "controls_note": ("Quarantine is a first-class state with owners and dwell SLAs: records that "
                      "fail gates are never silently dropped, and quarantine age pages the data "
                      "owner before consumers notice."),
    "cta": ("Bring the table everyone quotes and nobody trusts. The diagnostic will score your "
            "promotion path — and show what a gold-tier SLA would cost on your real estate."),
    "flagships": ["banking-financial-services", "telecom-media", "technology-saas"],
    "plays": [
        "Bronze-silver-gold promotion with quality gates and quarantine SLAs",
        "Time travel and lineage that answer audit questions as queries",
        "Storage economics signed with finance — dedup, compaction, tiering",
    ],
},

"data-engineering-modernization": {
    "hero": ("Legacy pipelines rebuilt as typed, contract-gated, observable jobs — moved on a "
             "strangler pattern that retires the old estate in waves, with dual-run diffs "
             "proving parity before every retirement."),
    "s1_h": "Modernization is consumer management, not code migration",
    "s1_close": ("Below: the failure modes that stall migration programs, the reference "
                 "architecture of the strangler pattern, and the console that tracks parity and "
                 "retirement honestly."),
    "s2_h": "Four failure modes that stall migration programs",
    "s2_lead": ("Each of these is organizational gravity — the countermeasures make parity "
                "provable and retirement contractual, so the old estate cannot quietly survive."),
    "arch_h": "Reference architecture — the strangler pattern for pipeline estates",
    "arch_lead": ("Dual-run is the spine: new pipelines run beside old ones with automated diffs, "
                  "consumers shift by contract, and retirement happens only when diffs are clean "
                  "and consumers are moved — never on a calendar promise."),
    "flow_h": "One pipeline's move, from undocumented logic to retirement",
    "flow_lead": ("From logic archaeology through contract extraction, dual-run with diffs, "
                  "consumer shift and the retirement checklist — including where hidden "
                  "consumers are caught before they break."),
    "dash_h": "The migration console — parity as the headline",
    "dash_lead": ("Pipelines migrated, diff mismatches, consumers shifted and legacy retirements "
                  "— four numbers that show whether the program is moving work or moving "
                  "PowerPoints."),
    "dash_note": ("Reference console — migration targets; no retirement clears without a clean "
                  "diff window and signed consumer sign-off."),
    "chart_h": "Dual-run economics across the program",
    "chart_lead": ("Cost of running both estates across the migration — the honest curve that "
                   "shows the temporary premium, where it peaks, and the retirement milestones "
                   "that bring it down."),
    "stack_h": "Modernization defaults — and when we deviate",
    "stack_lead": ("Defaults favor typed orchestration with contract gates over wholesale "
                   "re-platforming; deviation triggers are written because each one changes the "
                   "retirement math."),
    "gates_h": "Migration gates — evidence before each retirement",
    "artifacts_h": "What the data platform team inherits",
    "timeline_h": "Waves and retirements, week by week",
    "integ_h": "Integration surface — schedulers, catalogs and the old estate",
    "integ_lead": ("The program lives between two estates; these contracts cover schedulers, "
                   "catalogs and the legacy systems whose quirks are the real migration scope."),
    "controls_h": "Governance overlay — auditability across two estates",
    "controls_lead": ("Every wave carries its diff evidence, consumer sign-offs and retirement "
                      "records — the program's audit trail is built as it runs, not "
                      "reconstructed at the end."),
    "controls_note": ("Hidden-consumer sweeps run before every retirement: access logs, scheduler "
                      "exports and network flows are diffed against the declared consumer list, "
                      "and unexplained readers block the wave."),
    "cta": ("Bring the pipeline nobody dares touch. The diagnostic will price its move with "
            "dual-run diffs included — and tell you what retirement would actually require."),
    "flagships": ["insurance", "manufacturing", "public-sector"],
    "plays": [
        "Strangler-pattern waves with automated dual-run diffs",
        "Consumer shift by contract — no reader left behind undocumented",
        "Retirement milestones with signed evidence, not calendar promises",
    ],
},

"realtime-streaming-decisioning": {
    "hero": ("Sub-second decision paths on streams: exactly-once state, replay semantics and "
             "latency budgets measured hop by hop — because a decision path that cannot state "
             "its own latency is guessing, and a guess is not a control."),
    "s1_h": "Real-time is a budget, not a marketing adjective",
    "s1_close": ("Below: the failure modes that make streaming paths lie, the reference "
                 "architecture that budgets latency honestly, and the console that shows "
                 "decision health under real load."),
    "s2_h": "Four ways streaming paths lie about themselves",
    "s2_lead": ("Every one of these produces a demo that works and a production incident that "
                "surprises nobody who measured — the countermeasures make the path's own "
                "behavior observable and bounded."),
    "arch_h": "Reference architecture — the decision path and its budget",
    "arch_lead": ("The budget is designed before the code: hop-by-hop allocations, exactly-once "
                  "state with checkpointed replay, and shadow lanes that compare decisions "
                  "against the previous engine — disagreement is measured, not assumed away."),
    "flow_h": "One event, 150 milliseconds, six hops",
    "flow_lead": ("From ingress through state lookup, scoring and the action write — with the "
                  "late-event handling, out-of-order tolerance and replay path marked where "
                  "they actually trigger."),
    "dash_h": "The streaming console — p99 and exactly-once as the headline",
    "dash_lead": ("Decision p99, exactly-once violations, late-event drops and shadow "
                  "disagreement — the four numbers that decide whether the path is a control "
                  "or a liability."),
    "dash_note": ("Reference console — streaming targets at design load; the p99 budget is "
                  "signed per decision class, not averaged across the estate."),
    "chart_h": "Where the latency budget actually goes",
    "chart_lead": ("Allocation per hop at design load — ingress, state, scoring, policy, action, "
                   "egress. The chart decides optimization order and shows which hop breaks the "
                   "p99 promise first under stress."),
    "stack_h": "Streaming defaults — and documented deviations",
    "stack_lead": ("Defaults favor checkpointed state stores with idempotent sinks over "
                   "at-least-once shortcuts; deviation triggers are written because each one "
                   "changes what a replay means after an incident."),
    "gates_h": "Streaming release gates — evidence before live decisions",
    "artifacts_h": "What the platform and decision teams inherit",
    "timeline_h": "Budget first, then hops, week by week",
    "integ_h": "Integration surface — streams, state and the action systems",
    "integ_lead": ("The path touches streams, state stores and the systems that receive "
                   "decisions; these contracts carry the idempotency and replay semantics that "
                   "keep actions safe."),
    "controls_h": "Governance overlay — decisions that survive an incident review",
    "controls_lead": ("Every decision records its inputs, model version and budget state at "
                      "decision time — the incident review question 'what did the system know "
                      "when it acted' has a definitive answer."),
    "controls_note": ("Shadow lanes run through every release: the new engine decides in "
                      "parallel with the old, disagreements are scored before any traffic "
                      "shifts, and the shift itself is gated on the disagreement curve."),
    "cta": ("Bring the decision your traders or operators say is too slow. The diagnostic will "
            "budget your path hop by hop — and show exactly where the p99 promise breaks."),
    "flagships": ["banking-financial-services", "telecom-media", "logistics-supply-chain"],
    "plays": [
        "Hop-by-hop latency budgets, measured and signed per decision class",
        "Exactly-once state with checkpointed replay after any failure",
        "Shadow lanes that score disagreement before traffic shifts",
    ],
},

"master-data-governance": {
    "hero": ("Golden records with owners, survivorship rules and a catalog people actually trust: "
             "master data as engineering — match logic that is measurable, stewardship with SLAs, "
             "and duplicate rates that fall on a schedule instead of in a slide deck."),
    "s1_h": "Every metric argument is secretly a master-data argument",
    "s1_close": ("Below: the failure modes that keep master data contested, the reference "
                 "architecture that makes golden records defensible, and the console that tracks "
                 "trust as an engineering metric."),
    "s2_h": "Four failure modes that keep master data contested",
    "s2_lead": ("Each of these survives a committee and dies in reconciliation — the "
                "countermeasures make matching measurable and stewardship contractual."),
    "arch_h": "Reference architecture — golden records with survivorship and ownership",
    "arch_lead": ("Match precision is designed, not hoped for: deterministic and fuzzy matchers "
                  "with measured precision, survivorship rules signed by data owners, and a "
                  "catalog where every golden record carries its steward and its lineage."),
    "flow_h": "One customer record, resolved and defended",
    "flow_lead": ("From source contributions through match scoring, survivorship application and "
                  "the steward queue — including the merge audit trail that answers 'who "
                  "decided these were the same customer'."),
    "dash_h": "The governance console — trust as a number",
    "dash_lead": ("Duplicate rate, match precision, steward SLA adherence and catalog coverage — "
                  "the four numbers that decide whether the catalog is trusted or quietly "
                  "bypassed by spreadsheet shadows."),
    "dash_note": ("Reference console — governance targets by domain; survivorship changes are "
                  "gated releases with before/after match evidence."),
    "chart_h": "Duplicate and trust metrics across domains",
    "chart_lead": ("Duplicate rate and steward SLA adherence per master-data domain — the shape "
                   "that decides where the next matching investment lands and which domains are "
                   "trustworthy enough to serve executive metrics."),
    "stack_h": "Matching stack defaults — and documented deviations",
    "stack_lead": ("Defaults favor measured match pipelines with audit trails over black-box "
                   "MDM suites; deviation triggers are written because each one changes what "
                   "reconciliation can prove later."),
    "gates_h": "Governance release gates — evidence before golden status",
    "artifacts_h": "What the data governance office inherits",
    "timeline_h": "Domain by domain, week by week",
    "integ_h": "Integration surface — source systems and the steward workflow",
    "integ_lead": ("Golden records are assembled from source systems and maintained through "
                   "steward queues; these contracts define the whole surface where duplicates "
                   "are born or die."),
    "controls_h": "Governance overlay — the merge audit trail",
    "controls_lead": ("Every merge, survivorship decision and steward override is recorded with "
                      "its evidence — the reconciliation dispute that used to take a meeting now "
                      "resolves to a record."),
    "controls_note": ("Steward overload is monitored as a risk: when queue age or override rates "
                      "exceed tolerance, the matching logic gets the investigation — not the "
                      "steward's calendar."),
    "cta": ("Bring the two systems that disagree about your customers. The diagnostic will "
            "measure match precision on your real records — and price what one trusted golden "
            "record would cost."),
    "flagships": ["healthcare-life-sciences", "retail-consumer-goods", "banking-financial-services"],
    "plays": [
        "Measured match pipelines with precision you can defend in reconciliation",
        "Survivorship rules signed by owners, applied as gated releases",
        "A catalog with stewards, lineage and SLAs people actually trust",
    ],
},

"advanced-risk-predictive-analytics": {
    "hero": ("Risk and forecasting models with signed baselines, time-based holdouts and "
             "governance that survives the quarter they are judged in: predictions built to be "
             "checked, not presentations built to be believed."),
    "s1_h": "A forecast earns trust by being falsifiable",
    "s1_close": ("Below: the failure modes that make analytics theater, the reference "
                 "architecture that keeps models honest, and the console the risk function "
                 "reads."),
    "s2_h": "Four failure modes that make analytics theater",
    "s2_lead": ("Every one of these produces beautiful numbers that collapse in the quarter they "
                "were meant to serve — the countermeasures make the model falsifiable and the "
                "action real."),
    "arch_h": "Reference architecture — baselines, holdouts and the action loop",
    "arch_lead": ("The architecture enforces humility structurally: every model ships beside its "
                  "signed baseline, holdouts are time-based rather than random, leakage screens "
                  "run on every feature set, and the action loop records what the prediction "
                  "actually caused."),
    "flow_h": "One forecast, from features to accountability",
    "flow_lead": ("From feature assembly through leakage screens, backtesting against time "
                  "holdouts, baseline comparison and the action record — including the drift "
                  "watch that triggers re-baselining."),
    "dash_h": "The risk console — skill against the baseline",
    "dash_lead": ("Forecast accuracy, baseline status, leakage findings and drift score — the "
                  "four numbers that decide whether the model keeps its mandate or goes back "
                  "for re-work."),
    "dash_note": ("Reference console — analytics targets by horizon; the baseline is re-signed "
                  "quarterly, and 'beaten' is a recorded fact, not a claim."),
    "chart_h": "Forecast skill against baselines, horizon by horizon",
    "chart_lead": ("Skill versus naive and seasonal baselines across forecast horizons — the "
                   "shape that shows where the model genuinely adds value and where the "
                   "seasonal baseline remains embarrassingly hard to beat."),
    "stack_h": "Modeling defaults — and documented deviations",
    "stack_lead": ("Defaults favor interpretable models with audited feature stores over "
                   "black-box accuracy; deviation triggers are written because each one changes "
                   "what a model-risk review can reconstruct."),
    "gates_h": "Model release gates — evidence before the mandate",
    "artifacts_h": "What the risk and planning teams inherit",
    "timeline_h": "Baseline to accountability, week by week",
    "integ_h": "Integration surface — feature stores and planning systems",
    "integ_lead": ("Predictions matter only when they reach a decision system; these contracts "
                   "carry features in and actions out, with the loop closed by design."),
    "controls_h": "Model-risk governance overlay",
    "controls_lead": ("Feature lineage, holdout definitions and drift scores are retained per "
                      "model version — the model-risk inventory a supervisor asks for is "
                      "generated as the work runs."),
    "controls_note": ("Leakage screens run on every feature change: temporal overlap, target "
                      "proxies and group leakage are tested automatically, and a finding blocks "
                      "promotion until explained."),
    "cta": ("Bring the forecast that embarrasses itself every quarter. The diagnostic will "
            "baseline it honestly, screen the features for leakage, and price what real skill "
            "would cost."),
    "flagships": ["insurance", "energy-utilities", "agriculture-food"],
    "plays": [
        "Signed baselines beside every model — skill is a recorded fact",
        "Time-based holdouts and leakage screens on every feature change",
        "An action loop that records what each prediction actually caused",
    ],
},

"enterprise-bi-executive-analytics": {
    "hero": ("Decision-grade reporting with one truth per metric: certified datasets, metric "
             "contracts with owners, and an executive layer fast enough that nobody rebuilds the "
             "number in a spreadsheet before the board meeting."),
    "s1_h": "The spreadsheet shadow is a product of slow truth",
    "s1_close": ("Below: the failure modes that multiply versions of the truth, the reference "
                 "architecture that certifies metrics, and the console that tracks trust in the "
                 "BI estate."),
    "s2_h": "Four failure modes that multiply versions of the truth",
    "s2_lead": ("Each of these grows the spreadsheet shadow — the countermeasures make certified "
                "metrics faster and more trusted than the private rebuild."),
    "arch_h": "Reference architecture — metric contracts to the executive layer",
    "arch_lead": ("Metrics are contracts: definitions with owners, certified datasets underneath, "
                  "change control on definitions, and an executive serving layer whose p95 is "
                  "itself an SLA — speed is why the shadow exists, so speed is part of the "
                  "governance."),
    "flow_h": "One metric, from dispute to certification",
    "flow_lead": ("From definition argument through contract drafting, certification, "
                  "downstream adoption and the dispute ledger — including what happens when a "
                  "definition change is requested mid-quarter."),
    "dash_h": "The BI console — trust, measured",
    "dash_lead": ("Certified coverage, dispute rate, executive query p95 and the shrinking "
                  "spreadsheet count — the four numbers that tell you whether the estate is "
                  "gaining or losing the trust war."),
    "dash_note": ("Reference console — BI targets; metric disputes are logged, triaged and "
                  "resolved by owners, never argued in meetings."),
    "chart_h": "Trust metrics across the BI estate",
    "chart_lead": ("Certification coverage, dispute rates and query performance across domains — "
                   "the shape that shows where the shadow spreads and where certification is "
                   "winning."),
    "stack_h": "BI stack defaults — and documented deviations",
    "stack_lead": ("Defaults favor semantic layers with certified datasets over dashboard "
                   "sprawl; deviation triggers are written because each one re-opens the door "
                   "to private truth."),
    "gates_h": "BI release gates — evidence before certification",
    "artifacts_h": "What the analytics office inherits",
    "timeline_h": "Metrics in order, week by week",
    "integ_h": "Integration surface — sources, semantic layer and the board pack",
    "integ_lead": ("The estate serves the board pack, the ops reviews and the regulators; these "
                   "contracts carry certified metrics into each without forks."),
    "controls_h": "Governance overlay — the dispute ledger",
    "controls_lead": ("Metric definitions are versioned with change control; the dispute ledger "
                      "records every challenge and its resolution — the institutional memory "
                      "that stops the same argument restarting each quarter."),
    "controls_note": ("Executive-layer p95 is an SLA, not an aspiration: when the suite slows "
                      "past budget, the incident is real and the shadow spreads — so latency "
                      "regressions are treated as trust regressions."),
    "cta": ("Count the spreadsheets that rebuild the same metric. The diagnostic will score "
            "your estate's certified coverage — and price what one trusted number, served fast, "
            "would cost."),
    "flagships": ["retail-consumer-goods", "education-research", "public-sector"],
    "plays": [
        "Metric contracts with owners, certification and change control",
        "An executive layer whose query p95 is itself an SLA",
        "A dispute ledger and the shrinking spreadsheet shadow as the KPI",
    ],
},

"data-monetization-products": {
    "hero": ("Data as a product for external consumption: contracts and SLAs your customers can "
             "rely on, purpose limits that bind, billing that reconciles to the byte, and "
             "onboarding measured in days — with controls that get stricter the moment revenue "
             "appears."),
    "s1_h": "Selling data is a controls business wearing a revenue costume",
    "s1_close": ("Below: the failure modes that make data products liabilities, the reference "
                 "architecture of a governed data product, and the console that runs it like "
                 "the product business it is."),
    "s2_h": "Four failure modes that turn data products into liabilities",
    "s2_lead": ("Every one of these is survivable as an internal dashboard and fatal as a billed "
                "product — the countermeasures assume revenue, regulators and lawyers are "
                "watching."),
    "arch_h": "Reference architecture — the governed data product surface",
    "arch_lead": ("Product surface and control plane are one design: entitlement and purpose "
                  "limits enforced at query time, usage metering that reconciles to billing, "
                  "SLAs with error budgets, and the onboarding pipeline that makes the sixth "
                  "customer cheaper than the first."),
    "flow_h": "One subscription, from entitlement to invoice",
    "flow_lead": ("From contract signing through entitlement provisioning, purpose-limited "
                  "queries, metered usage and the billing reconciliation — including where a "
                  "purpose-limit block is logged and reviewed."),
    "dash_h": "The product console — SLOs and invoices that agree",
    "dash_lead": ("SLO adherence, onboarding time, billing accuracy and purpose-limit blocks — "
                  "the four numbers that decide whether the product is a business or a "
                  "regulatory incident waiting for a date."),
    "dash_note": ("Reference console — data-product targets; billing reconciliation is exact by "
                  "policy, and any mismatch is a sev-2, not a rounding note."),
    "chart_h": "Product economics by consumer tier",
    "chart_lead": ("Revenue and serving cost per consumer tier — the shape that decides pricing "
                   "reviews, tier design and where serving costs threaten margin before "
                   "someone else finds out."),
    "stack_h": "Product stack defaults — and documented deviations",
    "stack_lead": ("Defaults favor entitlement-first design with metered egress over "
                   "export-and-hope; deviation triggers are written because each one moves "
                   "purpose limits from enforced to promised."),
    "gates_h": "Product release gates — evidence before revenue",
    "artifacts_h": "What the data product team inherits",
    "timeline_h": "Product launch path, week by week",
    "integ_h": "Integration surface — entitlement, billing and the customer estate",
    "integ_lead": ("The product touches your commercial stack as much as your data platform; "
                   "these contracts carry entitlements, meters and invoices without manual "
                   "reconciliation."),
    "controls_h": "Compliance overlay — purpose limits that bind",
    "controls_lead": ("Purpose limitations are enforced at query time with logged blocks, "
                      "reviewed by the privacy office — the control a regulator tests first, "
                      "built as a structural property rather than a contract clause."),
    "controls_note": ("Purpose-limit blocks are reviewed weekly with the privacy office: a block "
                      "is the control working, and the review is where product scope and legal "
                      "scope stay aligned."),
    "cta": ("If your data is valuable enough to sell, it is regulated enough to control. Bring "
            "the use case to a briefing — we will price the governed product surface against "
            "the liability of shipping without it."),
    "flagships": ["technology-saas", "telecom-media", "healthcare-life-sciences"],
    "plays": [
        "Entitlement and purpose limits enforced at query time, logged and reviewed",
        "Usage metering that reconciles to billing — exactly",
        "Onboarding measured in days, with the sixth customer cheaper than the first",
    ],
},
}
