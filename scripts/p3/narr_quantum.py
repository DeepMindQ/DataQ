"""narr_quantum — narrative layer for the Quantum & Advanced Compute domain."""

HUB = {
    "hero": ("Quantum & Advanced Compute is run as evidence, not evangelism: honest readiness "
             "triage, hybrid optimization with verified baselines, HPC that does the heavy "
             "lifting today, PQC migration as engineering — and an advisory practice whose "
             "favorite recommendation is still 'not yet, and here is the memo that proves it'."),
    "s_practices": "Six practices from triage to horizon scanning",
    "deep": [
        ("The domain's discipline is verifiability: every quantum claim is scored against a "
         "classical baseline you can audit, every advantage number carries its instance set, "
         "and every roadmap is vendor-neutral so the recommendation survives the next hardware "
         "generation. Hype is priced into the methodology — the practices are built to be "
         "boring precisely because the field is not."),
        ("The security half is not speculative: post-quantum migration is an inventory and "
         "engineering problem with real deadlines, and the harvest-now-decrypt-later exposure "
         "is measurable today. That is where most enterprises should spend their quantum "
         "budget this year — and the triage practice exists to tell you so, with numbers."),
    ],
    "s_deep": "Verifiability is the discipline; everything else is marketing",
    "s_arch": "The domain reference architecture — classical first, quantum where proven",
    "arch_lead": ("The architecture is deliberately hybrid: classical HPC and solvers carry the "
                  "production load, quantum access sits behind a benchmarking harness that "
                  "scores every candidate against the classical baseline, and the crypto "
                  "inventory runs its own migration pipeline — because the near-term value "
                  "lives in the discipline, not the hardware."),
    "s_dash": "The program on one screen — verified advantage, not press releases",
    "dash_lead": ("Baselines beaten, mean improvement, encoding efficiency and the kill ledger — "
                  "tiles that read like engineering because the program is one."),
    "dash_note": ("Reference console — quantum-program targets; every advantage claim is "
                  "reproducible against its signed classical baseline."),
    "s_chart": "Where quantum actually helps — and where it does not yet",
    "chart_lead": ("Verified advantage rate by problem class and technique, scored on auditable "
                   "instances: the honest map that keeps the portfolio funded where evidence "
                   "exists and parked where it does not."),
    "chart_override": {
        "variant": "heatmap",
        "title": "Verified advantage rate by problem class × technique — audited instances, design bands",
        "cats": ["Logistics routing", "Portfolio optimization", "Materials simulation", "Scheduling", "ML surrogates", "Chemistry"],
        "series": [
            ("Quantum annealing", [34, 41, 12, 28, 9, 22]),
            ("Gate-model hybrid", [18, 25, 31, 14, 17, 38]),
            ("Classical solver (baseline)", [46, 52, 44, 55, 61, 47]),
        ],
        "unit": "%",
        "caption": "Reference bands from audited benchmark instances — cells show the share of instances where the technique beat the signed classical baseline.",
    },
    "chart_note": None,
    "s_evidence": "Sector depth — where the compute practice runs deepest today",
    "evidence_lead": ("Quantum readiness concentrates in regulated finance and defense-adjacent "
                      "public sectors; optimization and HPC concentrate where scheduling and "
                      "simulation carry margin. The bars count published sub-industry briefs — "
                      "the honest map."),
    "evidence_chart_title": "Quantum & Advanced Compute — published sub-industry briefs by sector",
    "explorer_title": "Your compute frontier, your sector — pick the industry and see the plan",
    "explorer_intro": ("A bank's PQC deadline and a manufacturer's scheduling problem are both "
                       "'quantum conversations' — and both deserve evidence. Select your sector: "
                       "the panel shows the entry problem, the deliverables, the targets and "
                       "the sector brief."),
    "plays": [
        "Use-case triage on verifiable criteria — a roadmap that survives hardware generations",
        "Hybrid optimization scored against signed classical baselines",
        "PQC migration as engineering: inventory, hybrid deployments, migration waves",
    ],
    "flagships": ["banking-financial-services", "manufacturing", "public-sector"],
    "s_engage": "How compute engagements run",
    "engage": [
        ["Diagnostic — two weeks", "Use cases triaged on verifiable criteria, crypto inventory scoped, classical baselines identified — the roadmap ships with kill criteria attached."],
        ["Provability sprint — four weeks", "One problem class runs a scored bake-off: quantum or advanced technique against your signed classical baseline, instances documented."],
        ["Build — ten to fourteen weeks", "The hybrid pipeline, benchmarking harness and PQC migration waves built to the reference architecture, with the console live from week two."],
        ["Industrialize — ongoing", "Quarterly re-benchmarks against new hardware generations, migration-wave reviews, and horizon memos that convert vendor claims into decisions."],
    ],
    "s_gates": "Compute release gates — the domain contract",
    "cta": ("Bring the vendor deck that promised 1000x. The triage sprint will score the claim "
            "against your classical baseline — and either find your first real advantage or "
            "save you the program's budget."),
}

PAGES = {

"quantum-readiness-strategy": {
    "hero": ("Honest quantum strategy: use cases triaged on verifiable criteria, a "
             "vendor-neutral posture, baselines measured before any hardware is booked — and a "
             "roadmap whose milestones are kill criteria, not keynote dates."),
    "s1_h": "A quantum strategy is mostly a classical strategy with kill criteria",
    "s1_close": ("Below: the failure modes that capture strategies into vendor keynotes, the "
                 "reference architecture of the triage process, and the console that tracks "
                 "the roadmap honestly."),
    "s2_h": "Four ways quantum strategies get captured by hype",
    "s2_lead": ("Each failure mode spends real budget on unmeasurable outcomes — the "
                "countermeasures make every next step falsifiable and every claim reproducible."),
    "arch_h": "Reference architecture — the triage-to-roadmap pipeline",
    "arch_lead": ("Candidates enter through a scored rubric — problem structure, data readiness, "
                  "baseline availability, risk posture — and exit either into a benchmark "
                  "plan, the PQC track or a documented park. Nothing reaches a hardware budget "
                  "without a signed classical baseline."),
    "flow_h": "One use case, from pitch to scored verdict",
    "flow_lead": ("From the vendor pitch through rubric scoring, baseline definition, the "
                  "formulate-now test and the roadmap slot — including the park list where "
                  "most ideas correctly wait."),
    "dash_h": "The readiness console — triage as the headline",
    "dash_lead": ("Problems triaged, formulate-now count and baseline pass rate — the three "
                  "numbers that show whether the strategy is discovering advantage or "
                  "collecting slideware."),
    "dash_note": ("Reference console — readiness targets; every roadmap milestone carries kill "
                  "criteria, and a milestone that misses them dies on schedule."),
    "chart_h": "Baseline pass rates across candidate use cases",
    "chart_lead": ("The share of candidates whose classical baseline passed audit, by quarter — "
                   "the honest curve that shows how much of the quantum conversation survives "
                   "measurement."),
    "stack_h": "Readiness defaults — and documented deviations",
    "stack_lead": ("Defaults favor vendor-neutral rubrics and measured baselines over "
                   "platform-lock-in; deviation triggers are written because each one trades "
                   "optionality for a sales cycle."),
    "gates_h": "Readiness release gates — evidence before roadmap",
    "artifacts_h": "What the strategy office inherits",
    "timeline_h": "Triage in order, week by week",
    "integ_h": "Integration surface — business units, security and procurement",
    "integ_lead": ("The triage process touches security, procurement and the business units "
                   "that own the problems; these working agreements keep the roadmap funded "
                   "and honest."),
    "controls_h": "Governance overlay — the kill-criteria ledger",
    "controls_lead": ("Every roadmap milestone carries pre-signed kill criteria and the ledger "
                      "records outcomes — the strategy document your board can trust because "
                      "its failures are on the same page as its successes."),
    "controls_note": ("PQC complacency is treated as a strategy failure: the triage explicitly "
                      "scores harvest-now-decrypt-later exposure per data class, so 'wait for "
                      "standards' is a scored risk, not a shrug."),
    "cta": ("Bring the quantum slide from your last board deck. The two-week triage will score "
            "every claim on verifiable criteria — and hand back a roadmap your CFO can "
            "actually audit."),
    "flagships": ["banking-financial-services", "public-sector", "telecom-media"],
    "plays": [
        "Scored use-case triage with signed classical baselines",
        "Vendor-neutral posture — recommendations that survive hardware generations",
        "A roadmap with kill criteria attached to every milestone",
    ],
},

"quantum-optimization": {
    "hero": ("Hybrid optimization on real problems: QUBO formulations that respect encoding "
             "limits, annealer and gate-model access behind one benchmarking harness, classical "
             "polish on every quantum candidate — and advantage claimed only where the signed "
             "baseline says so."),
    "s1_h": "The encoding decides the answer before the hardware runs",
    "s1_close": ("Below: the failure modes that produce fake advantage, the reference "
                 "architecture of the benchmarking harness, and the console that tracks "
                 "verified wins."),
    "s2_h": "Four ways optimization programs manufacture fake advantage",
    "s2_lead": ("Every one of these turns a benchmark into a press release — the countermeasures "
                "pin the instance sets, respect the noise and finish the classical polish that "
                "makes results real."),
    "arch_h": "Reference architecture — the hybrid benchmarking harness",
    "arch_lead": ("Problem ingestion through QUBO and circuit formulations, encoding-efficiency "
                  "checks, annealer and gate-model execution, and the classical polish stage "
                  "where quantum candidates are refined until they beat — or honestly lose to — "
                  "the signed baseline."),
    "flow_h": "One instance, from formulation to verified verdict",
    "flow_lead": ("From the real problem instance through encoding, quantum execution, "
                  "classical polish and the baseline comparison — including the instance ledger "
                  "that makes every result reproducible."),
    "dash_h": "The optimization console — verified wins as the headline",
    "dash_lead": ("Baselines beaten with verification, mean improvement and encoding efficiency "
                  "— the three numbers that decide whether the portfolio funds the next bake-off."),
    "dash_note": ("Reference console — optimization targets; every win is reproducible on its "
                  "documented instance set, and losses are published beside wins."),
    "chart_h": "Verified advantage by problem class",
    "chart_lead": ("Wins and losses across problem classes and quarters — the shape that shows "
                   "where quantum earns its keep today and where the classical solver remains "
                   "the honest answer."),
    "stack_h": "Optimization defaults — and documented deviations",
    "stack_lead": ("Defaults favor hybrid pipelines with classical polish over pure-quantum "
                   "demonstrations; deviation triggers are written because each one trades "
                   "verifiability for narrative."),
    "gates_h": "Optimization release gates — evidence before claims",
    "artifacts_h": "What the optimization team inherits",
    "timeline_h": "Bake-offs in order, week by week",
    "integ_h": "Integration surface — solvers, schedulers and the business systems",
    "integ_lead": ("Verified advantage only matters when it reaches the planning systems; these "
                   "contracts carry improved solutions into the solvers and schedulers your "
                   "operations already run."),
    "controls_h": "Benchmark governance — the instance ledger",
    "controls_lead": ("Instance sets are documented, versioned and reproducible; cherry-picked "
                      "instances are a governance violation, and the ledger makes that "
                      "checkable in minutes."),
    "controls_note": ("Noise honesty is enforced in the harness: every quantum result carries "
                      "its calibration state and shot count, and results without noise "
                      "disclosures are rejected at the gate, not debated later."),
    "cta": ("Bring your hardest scheduling or routing instance. The bake-off will score quantum "
            "and classical on the same signed baseline — and either way you keep the "
            "reproducible result."),
    "flagships": ["logistics-supply-chain", "manufacturing", "energy-utilities"],
    "plays": [
        "QUBO formulation with encoding-efficiency checks before hardware runs",
        "One benchmarking harness across annealer and gate-model access",
        "Classical polish on every candidate — advantage claimed only when verified",
    ],
},

"quantum-ml-simulation": {
    "hero": ("Circuit-based ML and chemistry simulation with verification-first rigor: "
             "trainability screens before training runs, noise-aware benchmarks that survive "
             "real hardware, classical surrogates as the honest control — and sim-to-real "
             "validation before any claim ships."),
    "s1_h": "Trainability is discovered on paper, not after the GPU bill",
    "s1_close": ("Below: the failure modes that seduce quantum-ML programs, the reference "
                 "architecture of the verification pipeline, and the console that tracks "
                 "hardware agreement."),
    "s2_h": "Four ways quantum-ML programs get seduced",
    "s2_lead": ("Each of these produces a notebook result that evaporates on real hardware — "
                "the countermeasures screen trainability, respect noise and keep the classical "
                "surrogate honest."),
    "arch_h": "Reference architecture — the verification-first simulation pipeline",
    "arch_lead": ("Candidates pass trainability screens before training, benchmarks run "
                  "noise-aware against simulator and hardware, and every quantum result is "
                  "compared beside its classical surrogate — the surrogate is the control that "
                  "keeps the field honest."),
    "flow_h": "One chemistry problem, from ansatz to validated claim",
    "flow_lead": ("From problem encoding through trainability screening, circuit training, "
                  "hardware verification and sim-to-real comparison — including the drift check "
                  "that gates any claim leaving the lab."),
    "dash_h": "The simulation console — agreement as the headline",
    "dash_lead": ("Hardware agreement, surrogate wins and trainability pass rates — the three "
                  "numbers that show whether the pipeline is converging or cosplaying."),
    "dash_note": ("Reference console — quantum-ML targets; claims ship only after sim-to-real "
                  "validation, and the classical surrogate is re-benchmarked every quarter."),
    "chart_h": "Hardware agreement across benchmark rounds",
    "chart_lead": ("Simulator-to-hardware agreement across rounds and hardware generations — "
                   "the curve that shows when claims are safe to make and when the hardware "
                   "still lies to the simulator."),
    "stack_h": "Simulation defaults — and documented deviations",
    "stack_lead": ("Defaults favor verification-first pipelines with honest surrogates over "
                   "demonstration-first notebooks; deviation triggers are written because each "
                   "one trades reproducibility for speed to a slide."),
    "gates_h": "Simulation release gates — evidence before claims",
    "artifacts_h": "What the research engineering team inherits",
    "timeline_h": "Screens first, week by week",
    "integ_h": "Integration surface — simulators, hardware access and the lab systems",
    "integ_lead": ("The pipeline spans simulators, hardware access windows and the lab or "
                   "R&D systems that own the problem; these contracts keep the loop reproducible."),
    "controls_h": "Research governance — the claim gate",
    "controls_lead": ("No result leaves the program without its verification chain: ansatz, "
                      "shots, calibration, surrogate comparison and sim-to-real delta — the "
                      "claim gate that protects your credibility in a hype-heavy field."),
    "controls_note": ("Barren-plateau screens run before any training run: parameter-shift "
                      "variance is estimated on the ansatz, and a failing screen parks the "
                      "architecture with a documented reason instead of burning the compute."),
    "cta": ("Bring the chemistry or materials problem your R&D lab keeps circling. The "
            "verification pipeline will tell you — on evidence — whether quantum earns a place "
            "in its workflow this year."),
    "flagships": ["healthcare-life-sciences", "technology-saas", "manufacturing"],
    "plays": [
        "Trainability screens before training runs — barren plateaus found on paper",
        "Noise-aware benchmarks against simulator and real hardware",
        "Classical surrogates as the honest control in every comparison",
    ],
},

"hpc-simulation-engineering": {
    "hero": ("Classical HPC that does the heavy lifting today: benchmarked clusters, tuned "
             "solvers with folklore replaced by measurement, I/O pipelines that do not wall, "
             "and a cost-per-solve discipline that makes every simulation job justify itself."),
    "s1_h": "Most 'we need quantum' conversations are really HPC conversations",
    "s1_close": ("Below: the failure modes that rot compute estates, the reference architecture "
                 "of the benchmarked cluster, and the console that prices every solve."),
    "s2_h": "Four failure modes that rot compute estates",
    "s2_lead": ("Each of these wastes queue hours and compute budget invisibly — the "
                "countermeasures measure the folklore, break the I/O walls and bring order to "
                "ensemble chaos."),
    "arch_h": "Reference architecture — the benchmarked simulation estate",
    "arch_lead": ("The estate is managed like a product: application benchmarks with published "
                  "scores, solver tuning measured against them, an I/O pipeline engineered to "
                  "the workload, and an ensemble manager that schedules chaos into reproducible "
                  "runs."),
    "flow_h": "One ensemble, from submission to verified ensemble result",
    "flow_lead": ("From job submission through scheduling, solver execution, I/O staging and "
                  "the ensemble aggregation — including where queue-wait SLOs are enforced and "
                  "what happens when a class-A job waits too long."),
    "dash_h": "The HPC console — cost per solve as the headline",
    "dash_lead": ("Application benchmark score, cost per solve and class-A queue wait — the "
                  "three numbers that run the estate and justify every capacity request."),
    "dash_note": ("Reference console — HPC targets; solver changes are gated on benchmark "
                  "evidence, and queue-wait breaches are capacity decisions, not mysteries."),
    "chart_h": "Benchmark scores and cost across cluster generations",
    "chart_lead": ("Application benchmark score and cost per solve across cluster generations — "
                   "the curve that decides refresh timing and shows where tuning paid for "
                   "itself."),
    "stack_h": "HPC defaults — and documented deviations",
    "stack_lead": ("Defaults favor measured solver tuning and engineered I/O over folklore and "
                   "defaults; deviation triggers are written because each one reintroduces "
                   "invisible waste."),
    "gates_h": "HPC release gates — evidence before cluster changes",
    "artifacts_h": "What the computational engineering team inherits",
    "timeline_h": "Benchmarks to ensembles, week by week",
    "integ_h": "Integration surface — schedulers, storage and the simulation users",
    "integ_lead": ("The estate serves simulation users and their pipelines; these contracts "
                   "define submission interfaces, data staging and the SLOs each user class "
                   "experiences."),
    "controls_h": "Reproducibility governance overlay",
    "controls_lead": ("Solver versions, library stacks and run configurations are pinned per "
                      "published result — the reproducibility ledger that makes every "
                      "simulation citable inside the enterprise."),
    "controls_note": ("Solver folklore is retired by measurement: any tuning claim must carry "
                      "its benchmark delta or it does not reach the cluster — the benchmark "
                      "score is the estate's only oracle."),
    "cta": ("Bring the simulation that queues for days and costs a fortune per run. The "
            "benchmark sprint will tune the solver, break the I/O wall — and price every "
            "future solve honestly."),
    "flagships": ["manufacturing", "energy-utilities", "education-research"],
    "plays": [
        "Application benchmarks with published scores gating every solver change",
        "I/O pipelines engineered to the workload — walls broken before they form",
        "Ensemble management with cost-per-solve discipline and reproducibility ledgers",
    ],
},

"post-quantum-cryptography": {
    "hero": ("PQC migration as engineering: crypto inventory with endpoint-level truth instead "
             "of questionnaire guesses, hybrid deployments where standards allow, migration "
             "waves sequenced by harvest-risk — and embedded orphans hunted until the "
             "inventory is honest."),
    "s1_h": "The migration deadline is real; the inventory is where programs die",
    "s1_close": ("Below: the failure modes that stall PQC migrations, the reference architecture "
                 "of the migration pipeline, and the console that tracks coverage truthfully."),
    "s2_h": "Four failure modes that stall PQC migrations",
    "s2_lead": ("Each of these leaves the estate quietly exposed while the program looks "
                "active — the countermeasures make inventory truthful and migration "
                "continuous."),
    "arch_h": "Reference architecture — inventory to migration waves",
    "arch_lead": ("The pipeline starts with cryptographic discovery at endpoint level — code "
                  "scanning, protocol inspection, certificate analysis — then sequences "
                  "migration waves by harvest risk, with hybrid deployments where standards "
                  "allow and vendor dependencies tracked as first-class risks."),
    "flow_h": "One endpoint, from discovery to migrated",
    "flow_lead": ("From cryptographic discovery through inventory classification, wave "
                  "assignment, hybrid deployment and verification — including the orphan path "
                  "for embedded crypto nobody remembered."),
    "dash_h": "The PQC console — exposure as the headline",
    "dash_lead": ("Inventory coverage, PQC-ready endpoints and harvest-risk exposure — the "
                  "three numbers that tell the board where the estate actually stands."),
    "dash_note": ("Reference console — PQC targets; harvest-risk exposure is scored per data "
                  "class and reviewed with the security council quarterly."),
    "chart_h": "Migration coverage by estate segment",
    "chart_lead": ("Coverage across estate segments and migration waves — the shape that shows "
                   "where the long tail lives and which waves are honestly done versus "
                   "claimed."),
    "stack_h": "Migration defaults — and documented deviations",
    "stack_lead": ("Defaults favor hybrid deployment and continuous waves over freeze-and-swap "
                   "programs; deviation triggers are written because each one extends exposure "
                   "or breaks a compatibility contract."),
    "gates_h": "Migration release gates — evidence before each wave",
    "artifacts_h": "What the crypto migration team inherits",
    "timeline_h": "Waves sequenced, week by week",
    "integ_h": "Integration surface — code estates, vendor products and PKI",
    "integ_lead": ("Crypto lives in code, vendors and PKI; these contracts cover discovery "
                   "access, vendor attestation tracking and the certificate lifecycle the "
                   "waves depend on."),
    "controls_h": "Vendor-dependency governance overlay",
    "controls_lead": ("Vendor crypto is tracked with attestation deadlines — a supplier "
                      "shipping RSA-only firmware is a named risk with an owner and a date, "
                      "not a footnote in the inventory."),
    "controls_note": ("Embedded orphans get their own hunt: firmware blobs, IoT devices and "
                      "retired-but-powered systems are scanned on schedule, because the crypto "
                      "you forgot about is the crypto an adversary remembers."),
    "cta": ("Ask what percentage of your estate's crypto you can actually name today. The "
            "discovery sprint will produce the honest inventory — and sequence the waves that "
            "close your harvest risk first."),
    "flagships": ["banking-financial-services", "insurance", "public-sector"],
    "plays": [
        "Endpoint-level crypto discovery — code, protocols, certificates",
        "Hybrid deployments where standards allow, waves sequenced by harvest risk",
        "Vendor attestation tracking and embedded-orphan hunts on schedule",
    ],
},

"emerging-compute-advisory": {
    "hero": ("Neutral horizon scanning across photonic, neuromorphic, in-memory and beyond: "
             "vendor claims tested against your workloads, evidence memos that translate "
             "demos into decisions, and buy recommendations that stay rare because most "
             "horizons deserve watching, not spending."),
    "s1_h": "The advisory's product is the memo — and its favorite word is 'wait'",
    "s1_close": ("Below: the failure modes that turn horizon scanning into procurement theater, "
                 "the reference architecture of the claims-testing pipeline, and the console "
                 "that tracks the advisory's own discipline."),
    "s2_h": "Four ways horizon scanning becomes procurement theater",
    "s2_lead": ("Every one of these converts a conference demo into a purchase order — the "
                "countermeasures test claims on your workloads and time-stamp every verdict."),
    "arch_h": "Reference architecture — claims testing to decision memos",
    "arch_lead": ("The pipeline treats vendor claims like hypothesis tests: reproduce the demo "
                  "on your data shapes, benchmark against your incumbent stack, then write the "
                  "memo — watch, pilot or buy — with the evidence attached and the revisit date "
                  "set."),
    "flow_h": "One vendor claim, from keynote to decision memo",
    "flow_lead": ("From claim intake through reproduction, benchmarking on your workloads and "
                  "the memo verdict — including the watchlist entry where most claims "
                  "correctly land."),
    "dash_h": "The advisory console — discipline as the headline",
    "dash_lead": ("Claims tested per quarter, memos delivered on time and buy recommendations — "
                  "the three numbers that show whether the advisory is a decision engine or a "
                  "conference subscription."),
    "dash_note": ("Reference console — advisory targets; a low buy count is a feature, and every "
                  "recommendation carries its benchmark evidence and revisit date."),
    "chart_h": "Claims tested and verdicts across the year",
    "chart_lead": ("Claims tested, verdicts delivered and the watchlist composition across "
                   "quarters — the shape that shows how much of the frontier is real and how "
                   "much is well-lit."),
    "stack_h": "Advisory defaults — and documented deviations",
    "stack_lead": ("Defaults favor evidence memos with revisit dates over roadmap "
                   "declarations; deviation triggers are written because each one trades "
                   "optionality for conference-catalog enthusiasm."),
    "gates_h": "Advisory release gates — evidence before any memo",
    "artifacts_h": "What the technology office inherits",
    "timeline_h": "Claims in order, week by week",
    "integ_h": "Integration surface — the estate, vendors and the architecture council",
    "integ_lead": ("The advisory plugs into your architecture council and vendor management; "
                   "these working agreements turn memos into decisions without another "
                   "committee."),
    "controls_h": "Independence governance overlay",
    "controls_lead": ("The advisory carries no vendor incentives: benchmark evidence is "
                      "archived with every memo, recommendations are revisited on their dates, "
                      "and strategy whiplash — the annual reversal — is tracked as its own "
                      "risk metric."),
    "controls_note": ("Every buy recommendation ships with a reversal plan: the conditions under "
                      "which the decision would be unwound are written at signature time, "
                      "because emerging compute changes faster than procurement cycles."),
    "cta": ("Bring the claim your CTO keeps forwarding. The advisory will reproduce it on your "
            "workloads, benchmark it against your stack — and return a memo with a verdict, "
            "not a webinar."),
    "flagships": ["technology-saas", "telecom-media", "banking-financial-services"],
    "plays": [
        "Vendor claims reproduced on your data shapes before any verdict",
        "Evidence memos — watch, pilot or buy — with revisit dates",
        "A watchlist that keeps the frontier visible without spending on it",
    ],
},
}
