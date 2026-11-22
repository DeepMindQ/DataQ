"""narr_iot — narrative layer for the IoT, Digital Twin & Robotics domain."""

HUB = {
    "hero": ("IoT, Digital Twin & Robotics turns physical operations into self-monitoring "
             "systems: sensor fabrics that survive partitions, edge AI that meets its "
             "deadlines, twins that stay honest against reality, and robot fleets with safety "
             "cases — the operations stack where fidelity to the physical world is the metric "
             "that gates everything else."),
    "s_practices": "Seven practices from sensor fabric to smart infrastructure",
    "deep": [
        ("The domain's hardest problem is honesty: a twin that drifts from reality is worse "
         "than no twin, a model that missed its deadline is worse than no model, and a "
         "utilization number that flatters the fleet is worse than none. Every practice here "
         "carries a fidelity or truth metric — twin-to-physical delta, deadline miss rate, "
         "verified prediction outcomes — because physical operations punish flattery."),
        ("The engineering is brownfield by definition: existing PLCs, legacy protocols, "
         "twenty-year-old assets and vendors who never intended to interoperate. The "
         "practices are built for that reality — schema versioning per device class, "
         "store-and-forward capture, IT/OT segmentation done properly — so the modernization "
         "happens without stopping the plant, the grid or the warehouse."),
    ],
    "s_deep": "Fidelity to the physical world is the metric that gates everything",
    "s_arch": "The domain reference architecture — sensors to acts",
    "arch_lead": ("The loop runs sense, simulate, decide, act: versioned sensor schemas feed "
                  "partition-tolerant capture, twins synchronize with fidelity scores, "
                  "predictive models integrate with work orders, and robots act inside "
                  "envelopes with incident-ready telemetry — one stack, physical truth "
                  "end-to-end."),
    "s_dash": "The operations stack on one screen — continuity and fidelity",
    "dash_lead": ("Capture fidelity, twin sync lag, unplanned downtime and utilization — tiles "
                  "that read like an operations review because that is exactly who reads "
                  "them."),
    "dash_note": ("Reference console — operations targets; every fidelity metric traces to a "
                  "physical verification, because a twin that is never checked against reality "
                  "is fiction with a dashboard."),
    "s_chart": "The fleet on one gauge — and the trend behind it",
    "chart_lead": ("Fleet continuity as a single honest indicator: the composite uptime across "
                   "sensed, twinned and automated assets, gated against the signed target — "
                   "with the drill cadence that keeps it real."),
    "chart_override": {
        "variant": "gauge",
        "title": "Composite fleet continuity — sensed + twinned + automated estates",
        "cats": ["Composite fleet continuity (rolling 30d)"],
        "series": [("Continuity", [98.7])],
        "unit": "%",
        "yMax": 100,
        "caption": "Reference indicator for the operations stack — composite continuity across the sensed, twinned and automated estate, gated against the signed target of 98.5%.",
    },
    "chart_note": None,
    "s_evidence": "Sector depth — where the operations-stack practice runs deepest today",
    "evidence_lead": ("Manufacturing buys sensor fabrics and robots, utilities buy grid twins "
                      "and smart infrastructure, agriculture buys field telemetry. The bars "
                      "count published sub-industry briefs — the honest map of sector depth."),
    "evidence_chart_title": "IoT, Digital Twin & Robotics — published sub-industry briefs by sector",
    "explorer_title": "Your physical operations, digitized — pick the industry and see the plan",
    "explorer_intro": ("A production line, a distribution grid and a cold chain are different "
                       "physics wearing the same stack. Select your sector: the panel shows the "
                       "entry problem, the deliverables, the targets and the sector brief."),
    "plays": [
        "Instrumentation as infrastructure — versioned schemas, partition-tolerant capture",
        "Twins with fidelity scores verified against physical reality",
        "Predictive maintenance wired to work orders, with verified outcomes",
    ],
    "flagships": ["manufacturing", "energy-utilities", "logistics-supply-chain"],
    "s_engage": "How operations-stack engagements run",
    "engage": [
        ["Diagnostic — two weeks", "Assets inventoried by class, capture fidelity baselined, the gate model scored for your brownfield reality — you keep the build order with named owners."],
        ["Provability sprint — four weeks", "One asset class runs a fund-or-kill slice: capture fidelity, twin sync lag or prediction precision on your real equipment."],
        ["Build — ten to fourteen weeks", "Fabric, twin and automation built to the reference architecture, with the console live from week two and fidelity verified physically."],
        ["Industrialize — ongoing", "Quarterly fidelity audits, fleet reviews with the operations team, and the brownfield onboarding plan that keeps new asset classes cheap."],
    ],
    "s_gates": "Operations release gates — the domain contract",
    "cta": ("Bring the asset class whose failures cost the most and whose data nobody trusts. "
            "The two-week diagnostic will baseline capture fidelity — and price what honest "
            "sensing, twinning and prediction would cost on it."),
}

PAGES = {

"industrial-iot-sensor-fabric": {
    "hero": ("Instrumentation as infrastructure: versioned schemas per device class, "
             "store-and-forward capture that survives partitions, heartbeat monitoring that "
             "catches zombie devices — wired into brownfield PLCs and protocols that were "
             "never meant to interoperate."),
    "s1_h": "Every downstream promise rests on capture fidelity",
    "s1_close": ("Below: the failure modes that corrupt sensor estates, the reference "
                 "architecture of the fabric, and the console that keeps fidelity honest."),
    "s2_h": "Four failure modes that corrupt sensor estates",
    "s2_lead": ("Each of these silently poisons everything downstream — analytics, twins and "
                "predictions all inherit the rot — which is why the countermeasures live at "
                "the capture layer."),
    "arch_h": "Reference architecture — the sensor fabric from field to broker",
    "arch_lead": ("Device classes carry versioned schemas, gateways buffer through partitions "
                  "with store-and-forward guarantees, the broker normalizes without losing "
                  "provenance, and heartbeat monitors treat a silent device as an incident — "
                  "fidelity is enforced at the layer where it is won or lost."),
    "flow_h": "One sensor reading, field to decision-ready",
    "flow_lead": ("From the transducer through the gateway buffer, schema validation, "
                  "normalization and the downstream broker — including the partition path and "
                  "what reconciliation looks like when the link returns."),
    "dash_h": "The fabric console — fidelity as the headline",
    "dash_lead": ("Capture fidelity, heartbeat pass rate and forward loss — the three numbers "
                  "that decide whether everything downstream is built on truth."),
    "dash_note": ("Reference console — fabric targets; capture fidelity is verified against "
                  "physical ground-truth checks on a schedule, not asserted from broker "
                  "counts."),
    "chart_h": "Capture fidelity across device classes",
    "chart_lead": ("Fidelity per device class and quarter — the shape that shows which "
                   "brownfield protocols need gateway work and which device fleets are drifting "
                   "toward zombie-hood."),
    "stack_h": "Fabric defaults — and documented deviations",
    "stack_lead": ("Defaults favor schema-versioned capture with store-and-forward over "
                   "fire-and-forget telemetry; deviation triggers are written because each one "
                   "trades fidelity for integration convenience."),
    "gates_h": "Fabric release gates — evidence before downstream reliance",
    "artifacts_h": "What the operations technology team inherits",
    "timeline_h": "Device classes in order, week by week",
    "integ_h": "Integration surface — PLCs, gateways and the historians",
    "integ_lead": ("The fabric wraps brownfield reality: PLCs, legacy protocols and historians "
                   "are the integration scope, and the contracts define what each device class "
                   "must emit and how brownfield impedance is handled."),
    "controls_h": "Data-integrity governance overlay",
    "controls_lead": ("Provenance survives the pipeline: every reading carries device identity, "
                      "schema version and gateway path — so a suspect reading can be traced to "
                      "hardware, firmware or transport in one query."),
    "controls_note": ("Zombie sweeps run monthly: devices that heartbeat but emit flat-lined or "
                      "physically implausible values are flagged for field verification — "
                      "silent failure is the fabric's most expensive failure mode."),
    "cta": ("Bring the production line whose data nobody fully trusts. The diagnostic will "
            "baseline capture fidelity by device class — and price what honest instrumentation "
            "costs on your brownfield estate."),
    "flagships": ["manufacturing", "energy-utilities", "logistics-supply-chain"],
    "plays": [
        "Versioned schemas per device class, enforced at the gateway",
        "Store-and-forward capture with partition reconciliation guarantees",
        "Heartbeat and zombie sweeps — silence is an incident, flatlines get field checks",
    ],
},

"computer-vision-edge-ai": {
    "hero": ("Inference at the edge with model ops: quantized models deployed on constrained "
             "hardware, drift monitors on live feeds, thermal budgets respected — and decision "
             "p99 measured at the line, because a quality gate that misses its deadline is a "
             "scrap event."),
    "s1_h": "Edge AI is a hardware contract wearing a model costume",
    "s1_close": ("Below: the failure modes that make edge inference flaky, the reference "
                 "architecture of the model-ops loop, and the console that tracks deadline "
                 "honesty."),
    "s2_h": "Four failure modes that make edge inference flaky",
    "s2_lead": ("Every one of these appears only on real hardware under real thermal load — "
                "the countermeasures test quantization on-device and monitor drift on the "
                "live feed, not in the notebook."),
    "arch_h": "Reference architecture — model ops from lab to line",
    "arch_lead": ("Models ship through quantization with on-device validation, deploy across "
                  "the hardware fleet in waves, run inside thermal and latency budgets, and "
                  "drift monitors watch the live feed — with the retraining loop fed by the "
                  "edge's own discordant frames."),
    "flow_h": "One frame, capture to decision inside the deadline",
    "flow_lead": ("From sensor capture through preprocessing, quantized inference, decision "
                  "gating and the actuation call — including the deadline-miss path and what "
                  "the line does when inference is late."),
    "dash_h": "The edge-AI console — deadlines as the headline",
    "dash_lead": ("Decision p99 at the line, deadline miss rate and thermal throttling events "
                  "— the three numbers that decide whether the quality gate is engineering or "
                  "demonstration."),
    "dash_note": ("Reference console — edge-AI targets; a deadline miss is a scrap event by "
                  "definition, so the miss rate is a board-level number, not a dashboard "
                  "curiosity."),
    "chart_h": "Deadline performance across hardware generations",
    "chart_lead": ("Decision p99 and miss rate per hardware generation and model version — the "
                   "shape that shows which fleet segments can carry the next model and which "
                   "need their own windows."),
    "stack_h": "Edge-AI defaults — and documented deviations",
    "stack_lead": ("Defaults favor quantization with on-device validation and wave deploys "
                   "over lab-to-line leaps; deviation triggers are written because each one "
                   "moves risk onto the production line."),
    "gates_h": "Edge-AI release gates — evidence before line deployment",
    "artifacts_h": "What the operations and quality teams inherit",
    "timeline_h": "Lab to line, week by week",
    "integ_h": "Integration surface — cameras, PLCs and the quality systems",
    "integ_lead": ("Edge inference serves quality and safety systems; these contracts define "
                   "camera and PLC integration, actuation calls and the interlocks that keep "
                   "the line safe when models disagree."),
    "controls_h": "Model-drift governance overlay",
    "controls_lead": ("Drift monitors watch confidence distributions and discordant-frame "
                      "rates on the live feed; the retraining loop is fed from the line, so "
                      "the model tracks reality instead of the dataset it was born on."),
    "controls_note": ("Thermal budgets are enforced by the scheduler, not hoped for: sustained "
                      "load beyond the signed envelope triggers model down-shift with an "
                      "incident record — silent throttling is treated as a quality escape."),
    "cta": ("Bring the inspection your line does by eye because the model kept missing "
            "deadlines. The lab-to-line sprint will quantize, validate on-device and prove "
            "the p99 — before the first scrap event."),
    "flagships": ["manufacturing", "retail-consumer-goods", "agriculture-food"],
    "plays": [
        "Quantized models validated on-device before any line deployment",
        "Drift monitors on the live feed, retraining fed by discordant frames",
        "Thermal and latency budgets enforced by the scheduler — silent throttling is an incident",
    ],
},

"connected-products-devices": {
    "hero": ("Product fleets in the field managed as products: OTA updates that never brick, "
             "telemetry that earns its bandwidth, support APIs your service desk can actually "
             "use — and firmware attack surfaces treated with the same gates as your cloud."),
    "s1_h": "A connected product is a promise your support org has to keep",
    "s1_close": ("Below: the failure modes that turn product fleets into liabilities, the "
                 "reference architecture of fleet management, and the console that keeps "
                 "firmware current safely."),
    "s2_h": "Four failure modes that turn product fleets into liabilities",
    "s2_lead": ("Each of these surfaces as a support crisis or a security headline — the "
                "countermeasures make updates safe by design and telemetry earn its keep."),
    "arch_h": "Reference architecture — OTA to support, fleet as one system",
    "arch_lead": ("Updates deploy in waves with signed images and auto-revert on health "
                  "regression, telemetry is sampled against bandwidth budgets with value "
                  "per byte measured, and the support surface exposes device state that "
                  "answers customer calls without escalation."),
    "flow_h": "One firmware wave, from signing to auto-revert",
    "flow_lead": ("From image signing through staged rollout, health monitoring and the "
                  "auto-revert decision — including the cohort analysis that decides whether "
                  "the next wave ships."),
    "dash_h": "The fleet console — currency as the headline",
    "dash_lead": ("Fleet firmware currency, update success rate and auto-revert events — the "
                  "three numbers that decide whether the connected product is an asset or an "
                  "apology pipeline."),
    "dash_note": ("Reference console — fleet targets; firmware currency below threshold pauses "
                  "feature work, because a stale fleet is a security and support liability "
                  "compounding daily."),
    "chart_h": "Update success across hardware generations",
    "chart_lead": ("Success and revert rates per hardware generation and firmware version — "
                   "the shape that shows which cohorts tolerate change and where the fleet "
                   "needs a different update strategy."),
    "stack_h": "Fleet defaults — and documented deviations",
    "stack_lead": ("Defaults favor signed images, staged waves and auto-revert over "
                   "big-bang updates; deviation triggers are written because each one trades "
                   "brick-risk discipline for schedule speed."),
    "gates_h": "Fleet release gates — evidence before a wave",
    "artifacts_h": "What the product operations team inherits",
    "timeline_h": "Waves in order, week by week",
    "integ_h": "Integration surface — devices, mobile apps and the support desk",
    "integ_lead": ("The fleet touches devices, companion apps and the support desk; these "
                   "contracts define what state each surface sees and how support resolves "
                   "device issues without engineering escalation."),
    "controls_h": "Firmware-security governance overlay",
    "controls_lead": ("Signing keys, secure boot and vulnerability response run on the same "
                      "gates as the cloud: CVE response waves ship within the signed SLA, and "
                      "the firmware SBOM is maintained as a product artifact."),
    "controls_note": ("Telemetry earns its bandwidth by review: each signal is re-justified "
                      "quarterly against the decisions it informs — signals without decisions "
                      "are dropped, and the savings are real money at fleet scale."),
    "cta": ("Ask what percentage of your fleet runs current firmware — and what updating the "
            "rest would risk. The diagnostic will wire signed waves with auto-revert and make "
            "currency boring."),
    "flagships": ["technology-saas", "manufacturing", "healthcare-life-sciences"],
    "plays": [
        "Signed OTA waves with health-gated rollout and auto-revert",
        "Telemetry sampled against bandwidth budgets — every signal earns its keep",
        "Support APIs that resolve device issues without engineering escalation",
    ],
},

"digital-twin-platforms": {
    "hero": ("Twins that stay honest: state synchronization with fidelity scores verified "
             "against physical reality, simulation tiers for what-ifs, conflict rules that "
             "resolve ambiguity — and structure drift caught before the twin quietly stops "
             "describing the asset it was built for."),
    "s1_h": "A twin that drifts from reality is worse than no twin",
    "s1_close": ("Below: the failure modes that make twins lie, the reference architecture of "
                 "the synchronization spine, and the console that scores fidelity against "
                 "physical checks."),
    "s2_h": "Four failure modes that make twins lie",
    "s2_lead": ("Every one of these produces confident dashboards over silent divergence — the "
                "countermeasures verify the twin against physical ground truth on a schedule "
                "and resolve conflicts by rule, not by whoever shouted last."),
    "arch_h": "Reference architecture — the synchronization spine",
    "arch_lead": ("State flows from the sensor fabric through sync engines with measured lag, "
                  "fidelity is scored against physical verification probes, simulation tiers "
                  "run what-ifs without contaminating the operational twin, and structure "
                  "drift monitors diff the twin's model against the asset's as-built reality."),
    "flow_h": "One state change, physical to twin and back",
    "flow_lead": ("From the physical event through sync, conflict resolution and the twin's "
                  "updated state to the simulation tier — including the fidelity probe that "
                  "periodically asks reality whether the twin is still telling the truth."),
    "dash_h": "The twin console — fidelity as the headline",
    "dash_lead": ("Sync lag, fidelity score and unresolved conflicts — the three numbers that "
                  "decide whether the twin is a decision instrument or an expensive mirror "
                  "maze."),
    "dash_note": ("Reference console — twin targets; fidelity is scored against physical "
                  "verification probes, and a twin failing its probe loses decision authority "
                  "until it passes."),
    "chart_h": "Fidelity across asset classes and sync versions",
    "chart_lead": ("Fidelity scores per asset class across sync-engine versions — the shape "
                   "that shows where the twin is honest, where it is degrading and which "
                   "upgrade fixed what."),
    "stack_h": "Twin defaults — and documented deviations",
    "stack_lead": ("Defaults favor measured fidelity and rule-based conflict resolution over "
                   "last-write-wins convenience; deviation triggers are written because each "
                   "one makes the twin's confidence unearned."),
    "gates_h": "Twin release gates — evidence before decision authority",
    "artifacts_h": "What the operations engineering team inherits",
    "timeline_h": "Assets in order, week by week",
    "integ_h": "Integration surface — the sensor fabric and the simulation stack",
    "integ_lead": ("Twins consume the sensor fabric and feed planners; these contracts define "
                   "state schemas, sync guarantees and the simulation boundaries that keep "
                   "what-ifs safely fenced."),
    "controls_h": "Simulation-governance overlay",
    "controls_lead": ("Simulation tiers are fenced from operations: what-if runs cannot write "
                      "back, results carry their input snapshot, and decisions sourced from "
                      "simulations are labeled as such in the audit trail."),
    "controls_note": ("Fidelity probes are physical, not statistical: the twin's state is "
                      "compared against sensor readings and periodic human-verified checks — a "
                      "twin that only agrees with itself is the failure mode, not the proof."),
    "cta": ("Ask when your twin last disagreed with the asset and who noticed. The diagnostic "
            "will wire fidelity probes and conflict rules — until the twin earns its decision "
            "authority."),
    "flagships": ["energy-utilities", "manufacturing", "telecom-media"],
    "plays": [
        "State sync with measured lag and rule-based conflict resolution",
        "Fidelity scores verified against physical probes on a schedule",
        "Simulation tiers fenced from operations — what-ifs never contaminate the twin",
    ],
},

"predictive-asset-intelligence": {
    "hero": ("Maintenance scheduled by evidence: failure-mode-driven models instead of anomaly "
             " soup, work-order integration that closes the action gap, and verified outcomes "
             "that pay down truth debt — predictions that the maintenance team actually "
             "schedule against."),
    "s1_h": "A prediction that does not change the work order is a prototype",
    "s1_close": ("Below: the failure modes that make predictive maintenance theater, the "
                 "reference architecture of the evidence loop, and the console that tracks "
                 "verified outcomes."),
    "s2_h": "Four failure modes that make predictive maintenance theater",
    "s2_lead": ("Each of these produces dashboards the planners ignore — the countermeasures "
                "tie models to failure modes, alarms to work orders and every prediction to "
                "a verified outcome."),
    "arch_h": "Reference architecture — failure modes to verified outcomes",
    "arch_lead": ("Models are built per failure mode with labeled history, predictions carry "
                  "lead-time estimates planners can schedule against, work-order integration "
                  "closes the loop, and every intervention is verified — the truth ledger that "
                  "keeps precision honest and the planners trusting."),
    "flow_h": "One prediction, alarm to verified outcome",
    "flow_lead": ("From the model's flag through planner review, work-order creation, the "
                  "intervention and the verified outcome — including the false-alarm path and "
                  "what it feeds back into the model."),
    "dash_h": "The asset console — verified outcomes as the headline",
    "dash_lead": ("Unplanned downtime trend, prediction precision and verified outcomes — the "
                  "three numbers that decide whether maintenance is evidence-led or "
                  "calendar-led."),
    "dash_note": ("Reference console — asset-intelligence targets; precision is computed "
                  "against verified outcomes only, because unverified predictions are how "
                  "truth debt accumulates."),
    "chart_h": "Downtime and precision across asset classes",
    "chart_lead": ("Unplanned downtime trend and prediction precision per asset class — the "
                   "paired shape that shows where predictions are earning their keep and where "
                   "the failure modes need re-labeling."),
    "stack_h": "Predictive defaults — and documented deviations",
    "stack_lead": ("Defaults favor failure-mode-driven models with work-order integration over "
                   "generic anomaly detection; deviation triggers are written because each one "
                   "widens the gap between prediction and action."),
    "gates_h": "Asset-intelligence release gates — evidence before planner reliance",
    "artifacts_h": "What the maintenance organization inherits",
    "timeline_h": "Failure modes in order, week by week",
    "integ_h": "Integration surface — CMMS, sensor fabric and the planner's calendar",
    "integ_lead": ("Predictions matter when they reach the planner's calendar; these contracts "
                   "carry flags into the CMMS as work orders with lead times, parts and "
                   "verification steps attached."),
    "controls_h": "Truth-ledger governance overlay",
    "controls_lead": ("Every prediction is resolved against a verified outcome — component "
                      "opened, condition confirmed or alarm refuted — and the truth ledger "
                      "feeds precision metrics that planners can audit."),
    "controls_note": ("Alert floods are treated as model failures, not user problems: when "
                      "alarm volume exceeds the planners' processing capacity, the model is "
                      "recalibrated against the truth ledger — the action gap is closed by "
                      "design, not by heroics."),
    "cta": ("Ask what fraction of last quarter's predictions were verified against reality. "
            "The diagnostic will build the truth ledger for your worst asset class — and show "
            "what evidence-led maintenance would save."),
    "flagships": ["energy-utilities", "manufacturing", "logistics-supply-chain"],
    "plays": [
        "Failure-mode-driven models with labeled history — no anomaly soup",
        "Work-order integration with lead times planners can schedule against",
        "Verified outcomes on every prediction — the truth ledger that keeps precision honest",
    ],
},

"robotics-autonomous-systems": {
    "hero": ("Robot fleets with safety cases: autonomy bounded by signed envelopes, "
             "incident-ready telemetry on every platform, utilization measured honestly "
             "including blocked time — and dock congestion engineered away instead of "
             "normalized."),
    "s1_h": "Autonomy is granted by the safety case, not the sales brochure",
    "s1_close": ("Below: the failure modes that make robot fleets unsafe or theatrical, the "
                 "reference architecture of bounded autonomy, and the console that keeps "
                 "utilization honest."),
    "s2_h": "Four failure modes that make robot fleets unsafe or theatrical",
    "s2_lead": ("Every one of these shows up as an incident, a utilization number nobody "
                "believes, or both — the countermeasures bound autonomy by evidence and "
                "measure the fleet as it actually runs."),
    "arch_h": "Reference architecture — bounded autonomy with incident readiness",
    "arch_lead": ("Autonomy levels are signed per zone and task with envelope monitors "
                  "enforcing them in real time, telemetry is incident-ready by design, fleet "
                  "orchestration manages dock and corridor contention, and integration "
                  "friction with WMS and PLCs is a scoped contract — not a surprise."),
    "flow_h": "One mission, assignment to envelope-checked completion",
    "flow_lead": ("From mission assignment through path planning, envelope checks, the dock "
                  "and corridor contention and completion — including the violation path and "
                  "what the fleet does when a platform breaches its envelope."),
    "dash_h": "The fleet console — honest utilization as the headline",
    "dash_lead": ("Busy utilization, blocked time and envelope violations — the three numbers "
                  "that run the fleet, with blocked time reported beside busy time because "
                  "flattery is how fleets hide their real capacity."),
    "dash_note": ("Reference console — robotics targets; envelope violations are sev-1 by "
                  "policy, and utilization is computed from signed telemetry, not vendor "
                  "dashboards."),
    "chart_h": "Utilization and blocking across shifts",
    "chart_lead": ("Busy and blocked shares across shifts and zones — the shape that shows "
                   "where congestion lives, which zones need re-layout and what the fleet's "
                   "honest capacity actually is."),
    "stack_h": "Robotics defaults — and documented deviations",
    "stack_lead": ("Defaults favor signed envelopes and incident-ready telemetry over autonomy "
                   "expansion; deviation triggers are written because each one moves risk from "
                   "the safety case onto the floor."),
    "gates_h": "Robotics release gates — evidence before floor deployment",
    "artifacts_h": "What the operations and safety teams inherit",
    "timeline_h": "Zones in order, week by week",
    "integ_h": "Integration surface — WMS, PLCs and the safety systems",
    "integ_lead": ("Robots serve the WMS and respect the safety systems; these contracts "
                   "define task handoffs, interlocks and the PLC integration that keeps "
                   "humans and machines in designed coexistence."),
    "controls_h": "Safety-case governance overlay",
    "controls_lead": ("The safety case is a living document: envelope expansions require "
                      "evidence from clean telemetry hours, incidents feed the case as "
                      "findings, and the signed autonomy level per zone is visible on the "
                      "floor — not buried in a vendor folder."),
    "controls_note": ("Incident telemetry is designed before the first deployment: every "
                      "platform streams the signals an investigation will ask for — because "
                      "incident blindness is discovered during the incident, which is the "
                      "worst possible discovery context."),
    "cta": ("Ask who signed the autonomy level for your busiest robot zone — and when it was "
            "last re-validated. The diagnostic will wire envelope monitors and honest "
            "utilization before the fleet grows."),
    "flagships": ["logistics-supply-chain", "manufacturing", "agriculture-food"],
    "plays": [
        "Autonomy levels signed per zone and task, enforced by envelope monitors",
        "Incident-ready telemetry designed before the first deployment",
        "Utilization measured honestly — busy and blocked reported side by side",
    ],
},

"smart-infrastructure": {
    "hero": ("City and utility scale, same disciplines: segmented SCADA-safe architectures "
             "where IT/OT blur is designed out, service-continuity SLOs for water and energy, "
             "public data exposure governed, and vendor islands integrated into one operating "
             "picture — continuity measured, not claimed."),
    "s1_h": "Public infrastructure fails publicly — the architecture has to assume it",
    "s1_close": ("Below: the failure modes that make infrastructure programs fragile, the "
                 "reference architecture of segmented continuity, and the console that keeps "
                 "continuity honest."),
    "s2_h": "Four failure modes that make infrastructure programs fragile",
    "s2_lead": ("Each of these turns a modernization into a headline — the countermeasures "
                "segment the estate, sign continuity SLOs and govern what the public can "
                "see."),
    "arch_h": "Reference architecture — segmented, SCADA-safe, SLO'd",
    "arch_lead": ("IT and OT are segmented by design with controlled crossings, service "
                  "continuity carries signed SLOs per utility, public-facing data passes "
                  "through a governed exposure layer, and vendor islands integrate through "
                  "normalization contracts — so the operating picture is one, and the "
                  "failures stay small."),
    "flow_h": "One crossing, IT to OT and back, controlled",
    "flow_lead": ("From an IT-side request through the segmented crossing, OT-side enforcement "
                  "and the response — including the unidirectional paths and the anomaly "
                  "monitoring that watches the boundary."),
    "dash_h": "The infrastructure console — continuity as the headline",
    "dash_lead": ("Water and energy continuity SLOs and boundary anomalies — the three numbers "
                  "the utility board reads, because continuity is the product the public "
                  "buys."),
    "dash_note": ("Reference console — infrastructure targets; continuity SLOs are signed per "
                  "service with the regulator's definitions, and boundary anomalies are "
                  "investigated as potential incidents by default."),
    "chart_h": "Service continuity across the utility estate",
    "chart_lead": ("Continuity per service and quarter — the shape that shows where "
                   "modernization helped, where vendor islands still limit visibility and "
                   "which continuity SLOs are honestly held."),
    "stack_h": "Infrastructure defaults — and documented deviations",
    "stack_lead": ("Defaults favor segmentation with controlled crossings and continuity SLOs "
                   "over IT-led convergenge; deviation triggers are written because each one "
                   "moves critical services onto architectures the threat model has not "
                   "earned."),
    "gates_h": "Infrastructure release gates — evidence before cutover",
    "artifacts_h": "What the utility operations team inherits",
    "timeline_h": "Segments in order, week by week",
    "integ_h": "Integration surface — SCADA, vendor islands and the public layer",
    "integ_lead": ("The estate spans SCADA, legacy vendor systems and the public data layer; "
                   "these contracts define the crossings, the normalization and the exposure "
                   "rules that keep the picture one and the risks small."),
    "controls_h": "Public-exposure governance overlay",
    "controls_lead": ("Public-facing data is governed by an exposure review: every dataset is "
                      "classified for sensitivity, aggregated where needed and rate-limited — "
                      "openness by design, not by accident."),
    "controls_note": ("Vendor islands are inventoried with their protocols and support "
                      "horizons: a vendor approaching end-of-support triggers an integration "
                      "plan, because the island nobody can see into is the one that fails "
                      "during the event."),
    "cta": ("Bring the service whose continuity the press would report. The diagnostic will "
            "sign the SLOs, segment the crossings and price what one operating picture costs "
            "across your vendor islands."),
    "flagships": ["public-sector", "energy-utilities", "telecom-media"],
    "plays": [
        "IT/OT segmentation with controlled, monitored crossings",
        "Service-continuity SLOs signed per utility — water, energy, measured",
        "Public data exposure governed by review; vendor islands normalized into one picture",
    ],
},
}
