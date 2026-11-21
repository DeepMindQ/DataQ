"""narr_cyber — narrative layer for the Cybersecurity & Zero-Trust domain."""

HUB = {
    "hero": ("Cybersecurity & Zero-Trust runs as one control surface, not seven disconnected "
             "services: identity, detection, posture, resilience, compliance and AI security "
             "share one evidence model — so a control proven once is trusted everywhere, and "
             "audit becomes a reading exercise instead of a fire drill."),
    "s_practices": "Seven practices, one evidence model",
    "deep": [
        ("The modern security program is measured in two currencies: time and evidence. Time — "
         "how fast identity is revoked, how fast a threat is contained, how fast a "
         "misconfiguration is closed. Evidence — what proves each control worked, generated "
         "continuously rather than assembled annually. The seven practices here are cut along "
         "exactly those two axes."),
        ("What makes the program different is the AI layer: prompt-injection defense, corpus "
         "integrity, model theft resistance and agent abuse containment are first-class "
         "controls in the same gates as firewalls and identity. The estate that runs AI has "
         "attack surfaces the classic frameworks never named — and this domain treats them as "
         "named, gated, first-class citizens."),
    ],
    "s_deep": "Time and evidence: the two currencies of a security program",
    "s_arch": "The domain reference architecture — one control surface",
    "arch_lead": ("Identity issues the decisions, the mesh enforces them per request, detection "
                  "watches the estate, posture closes the misconfigurations, resilience "
                  "rehearses the worst day, and compliance generates the evidence continuously. "
                  "The lanes below show how the surface stays coherent instead of tribal."),
    "s_dash": "The security program on one screen",
    "dash_lead": ("Detect-to-contain time, control evidence pass rate, revocation SLA and "
                  "coverage — the tiles the CISO's weekly actually steers by, rendered as they "
                  "appear in the review."),
    "dash_note": ("Reference console — program targets; every tile carries a named control owner "
                  "and an evidence link, because a metric without an owner is a wish."),
    "s_chart": "Containment speed by threat class — the trajectory that matters",
    "chart_lead": ("Radar profile across six gated axes; the posture-to-target gap is the funded "
                   "control program for the next two quarters, re-scored at every gate review."),
    "chart_override": {
        "variant": "line",
        "title": "Detect-to-contain time by threat class — quarterly trajectory, design bands",
        "cats": ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"],
        "series": [
            ("Malware & ransomware", [46, 34, 26, 19, 15, 12]),
            ("Identity-based attacks", [58, 44, 33, 24, 18, 14]),
            ("Data exfiltration", [72, 57, 41, 30, 22, 17]),
        ],
        "unit": "min",
        "caption": "Reference trajectory for a maturing detection program — containment speed improves in the order threats are rehearsed.",
    },
    "chart_note": None,
    "s_evidence": "Sector depth — where the security practice runs deepest today",
    "evidence_lead": ("Regulated sectors buy controls differently: supervisory review in finance, "
                      "patient safety in health, critical-infrastructure rules in energy. The "
                      "bars count published sub-industry briefs — the honest map of sector "
                      "depth."),
    "evidence_chart_title": "Cybersecurity & Zero-Trust — published sub-industry briefs by sector",
    "explorer_title": "Your control surface, your sector — pick the industry and see the plan",
    "explorer_intro": ("A bank's regulator, a hospital's patient-safety board and a grid "
                       "operator's NERC obligations buy different controls. Select your sector: "
                       "the panel shows the entry problem, the deliverables, the targets and the "
                       "sector brief."),
    "plays": [
        "Per-request zero-trust decisions on identity, device and context",
        "Detection engineering with measured coverage and rehearsed containment",
        "Continuous evidence generation — audits become reading exercises",
    ],
    "flagships": ["banking-financial-services", "healthcare-life-sciences", "energy-utilities"],
    "s_engage": "How security engagements run",
    "engage": [
        ["Diagnostic — two weeks", "Estate and control surface mapped, gate model scored, detect-to-contain baseline measured on your real telemetry — you keep the scored gate map."],
        ["Provability sprint — four weeks", "One control family runs a fund-or-kill slice: coverage measured by attack simulation, evidence generated, dwell time priced."],
        ["Build — ten to fourteen weeks", "Controls, detection and evidence pipelines built to the reference architecture, with the console live from week two."],
        ["Industrialize — ongoing", "Purple-team cadence, quarterly re-baselines, evidence reviews that keep first-time audit pass rates above target — and the AI surface included, not bolted on."],
    ],
    "s_gates": "Control release gates — the domain contract",
    "cta": ("Bring the control your auditor doubts most. The two-week diagnostic will measure "
            "its real coverage and evidence trail — and tell you what passing would take, in "
            "named owners and hours."),
}

PAGES = {

"zero-trust-architecture": {
    "hero": ("Per-request policy decisions on identity, device and context: network location "
             "stops being a privilege, critical paths reach measured coverage, and the latency "
             "objection is answered with a p95 number instead of an argument."),
    "s1_h": "Zero trust is a decision architecture, not a product purchase",
    "s1_close": ("Below: the failure modes that turn zero-trust programs into coverage theater, "
                 "the reference architecture of per-request decisions, and the console that "
                 "shows real coverage — including what still bypasses."),
    "s2_h": "Four ways zero-trust programs become coverage theater",
    "s2_lead": ("Each failure mode produces a diagram that looks complete and an estate that "
                "isn't — the countermeasures measure real coverage and force the bypasses into "
                "the open."),
    "arch_h": "Reference architecture — the policy decision surface",
    "arch_lead": ("Every request meets the same decision point: identity, device posture and "
                  "context evaluated per call, decisions served inside a latency budget, and "
                  "legacy orphans carried by explicit exceptions with expiry dates — nothing "
                  "grants itself access by being old."),
    "flow_h": "One request, one decision, full trace",
    "flow_lead": ("From request through device posture check, identity evaluation, policy "
                  "decision and enforcement — including the break-glass path and the bypass "
                  "detection that catches quiet exemptions."),
    "dash_h": "The zero-trust console — coverage you can defend",
    "dash_lead": ("Critical-path coverage, bypass detections and decision p95 — three numbers "
                  "that decide whether the program is architecture or wallpaper in front of the "
                  "auditor."),
    "dash_note": ("Reference console — zero-trust targets; bypass detections are triaged weekly, "
                  "and every exception carries an owner and an expiry."),
    "chart_h": "Coverage and decision latency across rollout waves",
    "chart_lead": ("Critical-path coverage and decision p95 across rollout waves — the paired "
                   "curve that shows coverage rising while latency stays inside the budget the "
                   "business actually experiences."),
    "stack_h": "Enforcement defaults — and documented deviations",
    "stack_lead": ("Defaults favor policy-as-code with central decision points over per-app "
                   "snowflakes; deviation triggers are written because each one creates a "
                   "bypass class someone will eventually use."),
    "gates_h": "Zero-trust release gates — evidence before enforcement",
    "artifacts_h": "What the security architecture team inherits",
    "timeline_h": "Critical paths first, week by week",
    "integ_h": "Integration surface — identity, devices and the estate",
    "integ_lead": ("The decision surface is only as good as its signals; these contracts carry "
                   "identity, device posture and context into decisions reliably enough to "
                   "enforce on."),
    "controls_h": "Control overlay — exceptions with expiries",
    "controls_lead": ("Break-glass accounts, legacy protocols and vendor exemptions exist — the "
                      "control is that each carries an owner, an expiry and a bypass alarm, so "
                      "the exception list is an attack-surface inventory rather than a secret."),
    "controls_note": ("Bypass detections are reviewed weekly with the architecture council: an "
                      "unexplained bypass is treated as a live incident, and the exception "
                      "ledger ships in every audit pack."),
    "cta": ("Ask for the coverage number your current diagram can't prove. The diagnostic will "
            "measure critical-path coverage on real requests — bypasses, exceptions and "
            "latency included."),
    "flagships": ["banking-financial-services", "public-sector", "healthcare-life-sciences"],
    "plays": [
        "Per-request policy decisions with a signed latency budget",
        "Critical-path coverage measured by simulation, bypasses triaged weekly",
        "Exception ledger with owners and expiries — nothing grants itself access",
    ],
},

"identity-access-modernization": {
    "hero": ("Identity lifecycle done properly: joiner-mover-leaver automation that revokes on "
             "the leaver SLA, privileged access in vaults instead of spreadsheets, standing "
             "admin accounts driven to zero — and MFA that people actually complete."),
    "s1_h": "Identity is the perimeter now — and it runs on process, not enthusiasm",
    "s1_close": ("Below: the failure modes that turn identity programs into audit findings, the "
                 "reference architecture of the lifecycle, and the console that keeps "
                 "revocation honest."),
    "s2_h": "Four identity failures auditors find first",
    "s2_lead": ("Every one of these is a process failure, not a tool failure — the "
                "countermeasures bind the lifecycle to HR and operational reality so "
                "revocation is an event, not a TODO."),
    "arch_h": "Reference architecture — lifecycle from joiner to leaver",
    "arch_lead": ("The lifecycle is event-driven: joiners provisioned from HR truth, movers "
                  "re-scoped by role change, leavers revoked on SLA — and privileged access "
                  "checked out of vaults just-in-time, reviewed, and never standing."),
    "flow_h": "One leaver, from HR event to verified revocation",
    "flow_lead": ("From the HR trigger through downstream revocations, session invalidation, "
                  "shared-account rotation and the verification probe — including where the "
                  "SLA clock starts and what proves it stopped."),
    "dash_h": "The identity console — revocation as the headline",
    "dash_lead": ("Leaver revocation SLA, MFA coverage, standing admin count and service-account "
                  "hygiene — the four numbers that decide whether identity is a control or a "
                  "finding."),
    "dash_note": ("Reference console — identity targets; the leaver SLA is measured from HR "
                  "event to verified revocation, not from ticket creation."),
    "chart_h": "Revocation SLA and MFA coverage across the estate",
    "chart_lead": ("Two series across the estate's identity populations — workforce, contractor, "
                   "service and privileged. The populations where SLA adherence dips are where "
                   "the next automation investment goes."),
    "stack_h": "Identity stack defaults — and documented deviations",
    "stack_lead": ("Defaults favor HR-driven lifecycle and vaulted privilege over DIY "
                   "workflows; deviation triggers are written because each one re-creates the "
                   "manual gap auditors find."),
    "gates_h": "Identity release gates — evidence before enforcement",
    "artifacts_h": "What the IAM team inherits",
    "timeline_h": "Lifecycle in order, week by week",
    "integ_h": "Integration surface — HR truth and downstream estates",
    "integ_lead": ("Lifecycle automation lives or dies on HR truth; these contracts carry "
                   "joiner, mover and leaver events into every downstream estate that grants "
                   "anything."),
    "controls_h": "Privileged-access governance overlay",
    "controls_lead": ("Privileged access is vaulted, checked out just-in-time, session-recorded "
                      "and reviewed — the standing-admin count reaching zero is the program's "
                      "proof, not its slogan."),
    "controls_note": ("Verification probes run after every revocation wave: synthetic "
                      "authentication attempts against revoked identities, with any success "
                      "treated as a sev-1 and traced to the exact process gap."),
    "cta": ("Ask how fast your last leaver actually lost access — then ask who verified it. The "
            "diagnostic will measure your real revocation SLA and vault your privilege before "
            "your auditor asks."),
    "flagships": ["banking-financial-services", "healthcare-life-sciences", "public-sector"],
    "plays": [
        "HR-driven joiner-mover-leaver automation with a verified revocation SLA",
        "Privileged access vaulted, just-in-time, session-recorded and reviewed",
        "Standing admin accounts driven to zero — and kept there",
    ],
},

"threat-intelligence-managed-soc": {
    "hero": ("Detection engineering with measured coverage: threat-informed detection mapped to "
             "the techniques that actually target your sector, purple-teamed quarterly, and run "
             "by a SOC whose speed is measured from first signal to containment — not from "
             "alert to acknowledgement."),
    "s1_h": "Detection coverage is a measurement, not a maturity score",
    "s1_close": ("Below: the failure modes that flood SOCs and hide real threats, the reference "
                 "architecture of measured detection, and the console that reports speed "
                 "honestly."),
    "s2_h": "Four ways SOC programs drown in their own alerts",
    "s2_lead": ("Each failure mode exhausts the analysts while the real attack walks past — the "
                "countermeasures buy back precision and make coverage falsifiable."),
    "arch_h": "Reference architecture — from threat intel to rehearsed containment",
    "arch_lead": ("Intelligence enters as detection requirements, not newsletters: each mapped "
                  "technique gets a detection, each detection gets a test, and purple-team "
                  "exercises prove the coverage that dashboards only claim."),
    "flow_h": "One signal, triaged to containment",
    "flow_lead": ("From first signal through enrichment, triage, containment play and the "
                  "post-incident detection improvement — including where precision is measured "
                  "and where the analyst's minute is spent."),
    "dash_h": "The SOC console — speed and precision as the headline",
    "dash_lead": ("Detect-to-contain, triage SLA adherence and detection precision — the three "
                  "numbers that decide whether the SOC is a control or a cost center with a "
                  "dashboard."),
    "dash_note": ("Reference console — SOC targets; containment is measured from first signal, "
                  "and precision is computed against closed-case ground truth."),
    "chart_h": "Coverage by attack technique, before and after purple team",
    "chart_lead": ("Detection coverage across the technique matrix before and after each "
                   "purple-team exercise — the honest delta that shows which coverage was real "
                   "and which was slide-ware."),
    "stack_h": "SOC stack defaults — and documented deviations",
    "stack_lead": ("Defaults favor detection-as-code with versioned playbooks over tribal "
                   "analyst knowledge; deviation triggers are written because each one puts "
                   "coverage back into someone's head."),
    "gates_h": "Detection release gates — evidence before deployment",
    "artifacts_h": "What the SOC leadership inherits",
    "timeline_h": "Coverage in order, week by week",
    "integ_h": "Integration surface — telemetry, intel feeds and the response tooling",
    "integ_lead": ("Detection quality is bounded by telemetry quality; these contracts define "
                   "what each source must emit and how intel feeds become detection "
                   "requirements."),
    "controls_h": "Metrics governance — the anti-theater layer",
    "controls_lead": ("Every reported metric carries its computation: precision from closed-case "
                      "truth, containment from first signal, coverage from executed tests — "
                      "metrics theater is designed out, not discouraged."),
    "controls_note": ("Quarterly purple-team results are signed by both sides — red for what "
                      "got through, blue for what caught it — and the delta against claimed "
                      "coverage ships in the board pack, unedited."),
    "cta": ("Ask your SOC to state its detect-to-contain from first signal, by threat class. If "
            "the answer is a maturity score, bring the telemetry to a briefing — we will "
            "measure it for real."),
    "flagships": ["banking-financial-services", "energy-utilities", "technology-saas"],
    "plays": [
        "Threat-informed detection mapped to the techniques that target your sector",
        "Purple-team-proved coverage, quarterly, signed by both sides",
        "Containment speed measured from first signal — with playbooks rehearsed",
    ],
},

"cloud-security-posture": {
    "hero": ("Multi-cloud misconfiguration and entitlement control: infrastructure-as-code "
             "guardrails that block bad deploys, CSPM with dwell-time budgets instead of "
             "dashboard anxiety, and entitlement reduction you can trend — across clouds, "
             "without blind consoles."),
    "s1_h": "Cloud security is an engineering gate, not a compliance report",
    "s1_close": ("Below: the failure modes that turn cloud posture into churn, the reference "
                 "architecture of the guardrail system, and the console that trends dwell time "
                 "and entitlements."),
    "s2_h": "Four failure modes that turn posture into churn",
    "s2_lead": ("Each of these regenerates the same misconfigurations weekly — the "
                "countermeasures move the fix upstream into the pipeline, where it stays "
                "fixed."),
    "arch_h": "Reference architecture — guardrails from IaC to runtime",
    "arch_lead": ("The control point is the pipeline: IaC gates block non-compliant templates "
                  "before deploy, runtime posture monitors catch drift with dwell-time budgets, "
                  "and entitlement reviews trend downward on a schedule — across clouds, with "
                  "policy parity as a gate, not a hope."),
    "flow_h": "One deploy, guarded from commit to runtime",
    "flow_lead": ("From commit through IaC policy gate, deploy, runtime posture check and the "
                  "drift path — including where a blocked deploy teaches the team faster than "
                  "a dashboard would."),
    "dash_h": "The posture console — dwell time as the headline",
    "dash_lead": ("Critical misconfiguration dwell, IaC gate blocks and entitlement trend — the "
                  "three numbers that show whether posture control is compounding or "
                  "regenerating."),
    "dash_note": ("Reference console — posture targets; dwell-time budgets are signed per "
                  "severity, and breaches page the owning platform team, not a shared inbox."),
    "chart_h": "Dwell time and entitlements across the quarters",
    "chart_lead": ("Critical misconfiguration dwell and entitlement count across quarters — the "
                   "two curves that decide whether the guardrail investment is reducing risk or "
                   "just renaming it."),
    "stack_h": "Posture stack defaults — and documented deviations",
    "stack_lead": ("Defaults favor policy-as-code with pipeline enforcement over console "
                   "clicking; deviation triggers are written because each one re-opens the "
                   "drift-by-hand channel."),
    "gates_h": "Posture release gates — evidence before enforcement",
    "artifacts_h": "What the platform security team inherits",
    "timeline_h": "Guardrails in order, week by week",
    "integ_h": "Integration surface — repos, pipelines and the clouds",
    "integ_lead": ("The guardrail system lives in your repos and pipelines; these contracts "
                   "carry policy checks into every deploy path, including the ones teams "
                   "prefer to forget."),
    "controls_h": "Entitlement governance overlay",
    "controls_lead": ("Entitlement reviews run on schedules with trending targets — the "
                      "-31% style reductions are earned by removal sprints with owners, not by "
                      "dashboards that merely count the problem."),
    "controls_note": ("Console-blind spots are mapped quarterly: every resource class the "
                      "native consoles cannot see is listed with its compensating control, and "
                      "the list ships in the audit pack instead of surprising anyone."),
    "cta": ("Count how long your last critical misconfiguration lived before someone closed it. "
            "The diagnostic will measure your real dwell-time budget — and show what pipeline "
            "guardrails would catch first."),
    "flagships": ["technology-saas", "banking-financial-services", "telecom-media"],
    "plays": [
        "IaC guardrails that block bad deploys before they exist",
        "CSPM with signed dwell-time budgets — breaches page owners",
        "Entitlement reduction sprints with trending targets across clouds",
    ],
},

"cyber-resilience-incident-recovery": {
    "hero": ("Recovery that is rehearsed, not documented: immutable backups with integrity "
             "checks, clean-room restores that prove the RTO, and a command structure that has "
             "already survived its worst day — on a schedule, with evidence."),
    "s1_h": "Your RTO is whatever your last rehearsal proved — nothing else",
    "s1_close": ("Below: the failure modes that make recovery fictional, the reference "
                 "architecture of rehearsed resilience, and the console that reports drill "
                 "results as facts."),
    "s2_h": "Four failure modes that make recovery fictional",
    "s2_lead": ("Each of these is discovered during the real incident, which is the worst "
                "possible discovery context — the countermeasures surface them in rehearsals "
                "instead."),
    "arch_h": "Reference architecture — immutable, isolated, rehearsed",
    "arch_lead": ("Three properties carry the architecture: backups immutable and isolated from "
                  "the compromised estate, restores executed in clean rooms with integrity "
                  "verification, and business-service RTOs rehearsed with the command "
                  "structure — so the first real run is never the first run."),
    "flow_h": "One restore drill, from declaration to service handback",
    "flow_lead": ("From drill declaration through clean-room build, restore, integrity "
                  "verification, service validation and the timed handback — including where "
                  "the drill clock stops and what evidence each stage produces."),
    "dash_h": "The resilience console — drills as the headline",
    "dash_lead": ("Restore drill RTO adherence, immutability coverage and integrity pass rates — "
                  "the three numbers that separate rehearsed resilience from recovery fiction."),
    "dash_note": ("Reference console — resilience targets; drills run on the signed cadence per "
                  "business service, and failed drills publish their findings internally."),
    "chart_h": "Drill results across business services",
    "chart_lead": ("RTO adherence and restore integrity per business service across drill "
                   "rounds — the shape that shows which services are honestly recoverable and "
                   "which are carrying paper promises."),
    "stack_h": "Resilience defaults — and documented deviations",
    "stack_lead": ("Defaults favor immutability and isolation over speed of backup; deviation "
                   "triggers are written because each one trades rehearsed recovery for "
                   "convenient architecture."),
    "gates_h": "Resilience release gates — evidence before reliance",
    "artifacts_h": "What the incident command team inherits",
    "timeline_h": "Rehearsals in order, week by week",
    "integ_h": "Integration surface — backup estates and business services",
    "integ_lead": ("Recovery spans backup estates, network isolation and the business services "
                   "being restored; these contracts define what each drill must prove, per "
                   "service."),
    "controls_h": "Incident-command governance overlay",
    "controls_lead": ("Command roles, decision thresholds and communications templates are "
                      "rehearsed with the drills — because the command structure that only "
                      "exists in a PDF fails exactly when it is needed."),
    "controls_note": ("Every drill produces findings with owners and dates, and the next drill "
                      "re-tests them first — resilience programs compound by closing findings, "
                      "not by running more drills."),
    "cta": ("Set a date: the next restore drill on your crown-jewel service, in a clean room, "
            "with the clock running. We will bring the harness — and publish the findings with "
            "owners."),
    "flagships": ["banking-financial-services", "energy-utilities", "healthcare-life-sciences"],
    "plays": [
        "Immutable, isolated backups with integrity checks on every restore",
        "Clean-room restore drills with business-service RTOs timed and published",
        "Command structure rehearsed with the drills — not discovered during them",
    ],
},

"compliance-audit-digital-trust": {
    "hero": ("Evidence-grade compliance without theater: controls mapped once across frameworks, "
             "evidence generated continuously by the systems themselves, and audits that start "
             "from a portal instead of a document hunt — with vendor blind spots named, not "
             "assumed away."),
    "s1_h": "Audit readiness is a systems property, not an annual project",
    "s1_close": ("Below: the failure modes that turn compliance into archaeology, the reference "
                 "architecture of continuous evidence, and the console that keeps first-time "
                 "pass rates above target."),
    "s2_h": "Four failure modes that turn compliance into archaeology",
    "s2_lead": ("Every one of these costs the same audit twice — the countermeasures generate "
                "evidence where the control runs, so the artifact never goes stale."),
    "arch_h": "Reference architecture — controls mapped once, evidence generated continuously",
    "arch_lead": ("The architecture maps each control to every framework it satisfies, then "
                  "wires evidence generation into the system of record: access reviews, change "
                  "records, scan results and assertions land in the evidence store with "
                  "freshness SLAs of their own."),
    "flow_h": "One audit request, answered from the portal",
    "flow_lead": ("From auditor request through evidence lookup, freshness check, assertion "
                  "rendering and the exception path — including what happens when evidence "
                  "for a control is older than its SLA."),
    "dash_h": "The compliance console — readiness as a number",
    "dash_lead": ("First-time pass rate, assertion coverage and evidence freshness — the three "
                  "numbers that decide whether the next audit is a portal review or an "
                  "emergency."),
    "dash_note": ("Reference console — compliance targets; evidence freshness SLAs are signed "
                  "per control family, and stale evidence pages the control owner."),
    "chart_h": "Assertion coverage and evidence freshness by framework",
    "chart_lead": ("Coverage and freshness per framework across the audit year — the shape that "
                   "shows which frameworks are genuinely covered and which are carried by "
                   "overlapping claims."),
    "stack_h": "Compliance stack defaults — and documented deviations",
    "stack_lead": ("Defaults favor evidence automation in systems of record over GRC "
                   "spreadsheets; deviation triggers are written because each one re-creates "
                   "the archaeology problem."),
    "gates_h": "Compliance release gates — evidence before assertion",
    "artifacts_h": "What the compliance office inherits",
    "timeline_h": "Frameworks in order, week by week",
    "integ_h": "Integration surface — systems of record and the audit portal",
    "integ_lead": ("Evidence lives in your systems of record; these contracts carry it — with "
                   "freshness metadata — into the portal auditors actually use."),
    "controls_h": "Vendor and third-party governance overlay",
    "controls_lead": ("Vendor controls are in scope until proven otherwise: third-party "
                      "assertions are collected, freshness-tracked and spot-tested — the blind "
                      "spot that fails audits is mapped, not discovered."),
    "controls_note": ("Assertion coverage counts vendor controls explicitly: a framework claim "
                      "that leans on an unverified vendor assertion is flagged in the portal "
                      "before the auditor finds it."),
    "cta": ("Time your next audit's evidence hunt — then price never running it again. The "
            "diagnostic will score your evidence freshness per control family and show what "
            "portal-first audits would take."),
    "flagships": ["banking-financial-services", "healthcare-life-sciences", "public-sector"],
    "plays": [
        "Controls mapped once across every framework they satisfy",
        "Evidence generated continuously in systems of record, with freshness SLAs",
        "Vendor assertions collected, tracked and spot-tested — no blind spots",
    ],
},

"ai-security-model-protection": {
    "hero": ("Security for the models themselves: prompt-injection defense with measured block "
             "rates, jailbreak suites running in CI so regressions cannot merge, corpus "
             "integrity monitoring against poisoning, and containment for agents with real "
             "tool access — the attack surfaces the classic frameworks never named."),
    "s1_h": "AI security is a new surface on the same old adversary",
    "s1_close": ("Below: the failure modes specific to model-backed systems, the reference "
                 "architecture that defends them, and the console that measures the defenses "
                 "honestly."),
    "s2_h": "Four AI-specific failure modes classic frameworks never named",
    "s2_lead": ("Each of these exploits the layer between the model and the estate — the "
                "countermeasures treat prompts, corpora and agent tools as attack surface with "
                "owners, tests and gates."),
    "arch_h": "Reference architecture — defending the model layer",
    "arch_lead": ("Defense in depth, redone for AI: input sanitization and injection classifiers "
                  "at the boundary, corpus integrity monitoring in the knowledge spine, output "
                  "filtering and abuse containment at the surface, and agent tool scopes "
                  "treated as privileged credentials."),
    "flow_h": "One adversarial prompt, blocked in layers",
    "flow_lead": ("From the crafted input through injection classification, grounding "
                  "validation, output filtering and the abuse watch — including the jailbreak "
                  "regression suite that blocks any defense change that opens a gap."),
    "dash_h": "The AI-security console — defenses with measured rates",
    "dash_lead": ("Injection block rate, jailbreak CI regressions, corpus integrity alerts and "
                  "agent-abuse containment — the four numbers that decide whether the AI "
                  "estate is defended or merely prompt-policed."),
    "dash_note": ("Reference console — AI-security targets; every defense change runs the full "
                  "jailbreak regression suite before merge, no exceptions."),
    "chart_h": "Attack simulation results across the AI estate",
    "chart_lead": ("Block rates across attack classes and quarterly simulation rounds — the "
                   "honest curve that shows which defenses hold under novel techniques and "
                   "which are decomposing quietly."),
    "stack_h": "AI-security defaults — and documented deviations",
    "stack_lead": ("Defaults favor layered classifiers with versioned regression suites over "
                   "single-point filters; deviation triggers are written because each one "
                   "narrows the tested surface."),
    "gates_h": "AI-security release gates — evidence before exposure",
    "artifacts_h": "What the security engineering team inherits",
    "timeline_h": "Defenses in order, week by week",
    "integ_h": "Integration surface — AI platform, corpora and agent tooling",
    "integ_lead": ("The defense surface spans the model gateway, retrieval corpora and agent "
                   "tool scopes; these contracts define what each layer must emit for the "
                   "monitoring to work."),
    "controls_h": "Agent-abuse containment overlay",
    "controls_lead": ("Agents with tool access are treated as privileged principals: scoped "
                      "credentials, rate limits, egress policy and session replay — the abuse "
                      "containment that keeps an agentic platform from becoming an "
                      "open-and-shut incident."),
    "controls_note": ("Corpus integrity monitors hash and sample the retrieval index continuously: "
                      "poisoning attempts surface as integrity alerts with source attribution, "
                      "and any alert pauses the affected corpus until cleared."),
    "cta": ("Bring the AI use case your CISO keeps postponing. The diagnostic will run the "
            "attack suite against it — injection, jailbreak, corpus and agent abuse — and "
            "price what measured defense costs."),
    "flagships": ["banking-financial-services", "technology-saas", "public-sector"],
    "plays": [
        "Prompt-injection defense with measured block rates at the boundary",
        "Jailbreak suites in CI — no defense change merges with an open gap",
        "Agent tool scopes treated as privileged credentials, contained and replayed",
    ],
},
}
