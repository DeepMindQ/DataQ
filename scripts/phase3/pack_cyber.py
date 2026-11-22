#!/usr/bin/env python3
"""Pack: Cybersecurity & Zero-Trust (dom=cybersecurity-zero-trust)."""

DOM = "cybersecurity-zero-trust"

HOOKS = {
    "banking-financial-services": "Supervisory scrutiny sets the bar: model-risk evidence for AI defenses, entitlement analytics that survive examinations, and containment drills timed against regulator expectations.",
    "insurance": "Policy and claims data under market-conduct rules — identity lifecycle that passes audit, posture gates on underwriting platforms, and recovery drills that prove the RTO.",
    "healthcare-life-sciences": "Clinical uptime is patient safety: zero-trust segmentation around clinical networks, AI-model protection for diagnostic tools, and recovery rehearsals that respect HIPAA evidence.",
    "manufacturing": "The OT boundary is the perimeter: IEC 62443-informed segmentation, identity for machines and humans, and incident response that keeps the line running safely.",
    "retail-consumer-goods": "PCI-scoped estates and consumer trust: posture gates on commerce platforms, identity lifecycle across seasonal workforces, and fraud-adjacent detection tuned to checkout.",
    "telecom-media": "Carrier-grade availability duties: zero-trust across OSS/BSS, threat intel tuned to telecom attack paths, and resilience drills that respect network change windows.",
    "energy-utilities": "NERC CIP-class obligations: segmented OT zones, controlled IT-OT crossings, identity for field workforces, and recovery drills rehearsed against grid scenarios.",
    "logistics-supply-chain": "Attack surface across EDI, carrier portals and partner APIs: zero-trust for the control tower, identity for 3PL partners, and recovery that protects the customs calendar.",
    "public-sector": "Citizen trust and sovereign obligations: zero-trust architecture on legacy estates, evidence-ready compliance, and identity lifecycle across political turnover cycles.",
    "education-research": "Open estates with sensitive records: identity lifecycle across academic calendars, research-data segmentation, and ransomware resilience for the registrar's systems.",
    "technology-saas": "Your product is the attack surface: model protection for AI features, posture gates in CI/CD, and SOC practice that scales with the customer count.",
    "agriculture-food": "Seasonal and dispersed estates: zero-trust for co-op networks, identity for field workforces, and provenance-system recovery that protects the certification calendar.",
}

KPIS = {
    "banking-financial-services": [
        ("Containment time, critical threats", 10, 40, "min"),
        ("Entitlement review findings closed", 90, 100, "pct"),
        ("Evidence pack prep time", 2, 10, "days"),
    ],
    "insurance": [
        ("Leaver revocation within SLA", 92, 100, "pct"),
        ("Critical posture findings dwell", 2, 14, "days"),
        ("Recovery drill RTO vs target", 85, 100, "pct"),
    ],
    "healthcare-life-sciences": [
        ("Clinical network segmentation coverage", 88, 100, "pct"),
        ("Model-layer incidents contained", 100, 100, "pct"),
        ("Restore drill RTO adherence", 88, 100, "pct"),
    ],
    "manufacturing": [
        ("IT-OT crossings under control", 95, 100, "pct"),
        ("Machine identity coverage", 70, 92, "pct"),
        ("Line-impact incidents per quarter", 0, 2, "num"),
    ],
    "retail-consumer-goods": [
        ("PCI-scoped asset posture compliance", 92, 100, "pct"),
        ("Seasonal-joiner provisioning fidelity", 90, 100, "pct"),
        ("Checkout-path detections tuned", 95, 100, "pct"),
    ],
    "telecom-media": [
        ("OSS/BSS enforcement-point coverage", 82, 96, "pct"),
        ("Threat-path drill coverage", 78, 95, "pct"),
        ("Change-window incident rate", 0, 2, "num"),
    ],
    "energy-utilities": [
        ("OT-zone policy compliance", 95, 100, "pct"),
        ("Field identity lifecycle fidelity", 90, 100, "pct"),
        ("Grid-scenario drill pass rate", 85, 100, "pct"),
    ],
    "logistics-supply-chain": [
        ("Partner access via zero-trust gates", 78, 96, "pct"),
        ("EDI endpoint posture compliance", 90, 100, "pct"),
        ("Customs-calendar incidents", 0, 1, "num"),
    ],
    "public-sector": [
        ("Enforcement points on critical paths", 80, 96, "pct"),
        ("Assertion evidence freshness", 90, 100, "pct"),
        ("Legacy-segment isolation coverage", 75, 95, "pct"),
    ],
    "education-research": [
        ("Term-cycle identity fidelity", 92, 100, "pct"),
        ("Research-segment isolation", 85, 98, "pct"),
        ("Ransomware drill RTO adherence", 85, 100, "pct"),
    ],
    "technology-saas": [
        ("Model-layer defense coverage", 90, 100, "pct"),
        ("Posture gates blocking bad deploys", 95, 100, "pct"),
        ("MTTD on emulated intrusions", 5, 30, "min"),
    ],
    "agriculture-food": [
        ("Co-op network segmentation", 78, 95, "pct"),
        ("Field identity lifecycle fidelity", 88, 99, "pct"),
        ("Certification-system recovery drills", 85, 100, "pct"),
    ],
}

SYSTEMS = {
    "banking-financial-services": ["Supervisory evidence frameworks", "Entitlement analytics", "Purple-team programs"],
    "insurance": ["PAS/claims identity estates", "CSPM + plan-time policy", "Immutable backup vaults"],
    "healthcare-life-sciences": ["Clinical network segmentation", "Model-layer guard stack", "HIPAA evidence controls"],
    "manufacturing": ["IEC 62443-informed zones", "Machine identity (SPIFFE-class)", "OT-safe incident playbooks"],
    "retail-consumer-goods": ["PCI-scoped posture gates", "Seasonal JML automation", "Checkout-path detection"],
    "telecom-media": ["OSS/BSS enforcement points", "Telecom threat intel feeds", "Network change windows"],
    "energy-utilities": ["NERC CIP-informed zones", "Field identity (MDM-linked)", "Grid-scenario drills"],
    "logistics-supply-chain": ["Partner zero-trust gates", "EDI endpoint posture", "Customs-calendar resilience"],
    "public-sector": ["Legacy-segment isolation", "Continuous evidence collection", "Sovereign identity policy"],
    "education-research": ["Academic-calendar JML", "Research data segmentation", "Ransomware clean rooms"],
    "technology-saas": ["Model-protection guard stack", "CI/CD posture gates", "Cloud-native SOC tooling"],
    "agriculture-food": ["Co-op network segmentation", "Field identity systems", "Certification-system recovery"],
}

COMMON_SUBS = {
    "Detection engine": "rules + models, versioned",
    "Identity provider": "one IdP, federated SPs",
    "Policy decision point": "deny-by-default, logged",
    "Control register": "owner, evidence, review",
    "IaC guardrails": "plan-time policy checks",
    "Posture engine": "continuous, per control",
    "Drift revert": "auto, with log entry",
    "Evidence collector": "continuous, signed",
    "Immutable snapshots": "write-once, air-gapped",
    "Isolated vault": "separate identity plane",
    "Clean-room restore": "network-segregated",
    "Incident command": "named roles, trained",
    "Rehearsals": "timed, evidence kept",
    "Joiner-Mover-Leaver": "HR-driven, SLA'd",
    "Federation & SSO": "one IdP, audited trusts",
    "MFA & step-up": "risk-based prompts",
    "Privileged vault": "brokered, session-recorded",
    "Workload identity": "SPIFFE-class, short-lived",
    "Hygiene scoring": "per account, trended",
    "Detection rules": "MITRE-mapped, tested",
    "Attack-path mapping": "graph-based, per estate",
    "Response playbooks": "rehearsed, versioned",
    "Purple-team drills": "monthly, scoped",
    "Policy enforcement points": "every critical path",
    "Injection firewall": "pre-model filter chain",
    "Corpus integrity": "signed, versioned",
    "Model-data policy": "classification-driven",
    "Output guards": "post-model, redaction",
    "Abuse detection": "rate + intent signals",
    "Red-team evals": "adversarial suite, CI",
    "Assertions": "framework-mapped",
    "Evidence packs": "examiner-ready",
    "Business services": "RTO/RPO named per service",
}

PAGES = {
    "services_cybersecurity-zero-trust": {
        "archsubs": {
            "Detection engine": "rules + models, versioned",
            "Identity provider": "one IdP, federated SPs",
            "Policy decision point": "deny-by-default, logged",
            "Control register": "owner, evidence, review",
        },
        "badges": [
            ("Practices in the domain", "7"),
            ("Evidence model", "continuous"),
            ("Industries served", "12"),
        ],
        "deep": {
            "h2": "Time and evidence are the two currencies",
            "sub": "Containment speed and examinable proof — the two numbers every security decision serves",
            "paras": [
                "Security programs fail on two currencies: time (how fast a threat is contained once detected) and evidence (whether the control state can be proven to an auditor without an archaeology project). The domain architecture is built around both — a single control surface where identity, device, network and AI-model policies are decided and logged, detection tuned per attack path rather than per product, and the control register as the spine: every control carries an owner, an evidence source and a review date, so compliance is generated continuously rather than reconstructed annually.",
                "The seven practices divide the surface deliberately: identity lifecycle, zero-trust enforcement, posture, threat intelligence, resilience, AI-model protection and compliance engineering. Each can be engaged alone; the evidence model binds them — one register, one evidence collector, one console — because fragmented programs produce the two failure modes that boards actually experience: slow containment (the breach that grew) and audit theater (the report that proved nothing).",
            ],
            "bullets": [
                ("One control surface", "Identity, device, network and model policies decided and logged in one place."),
                ("Containment as headline", "Time-to-contain per threat class, drilled and trended."),
                ("Continuous evidence", "The register collects proof as controls run; audits read, not reconstruct."),
                ("Attack-path tuning", "Detection mapped to how this estate is actually attacked."),
            ],
        },
        "heads": {
            "Seven practices, one evidence model": ("Seven practices, one evidence model", "Identity, zero trust, posture, intel, resilience, model protection and compliance on one surface"),
            "Time and evidence: the two currencies of a security program": ("Time and evidence — the two currencies of a security program", "Containment speed and examinable proof as the design targets"),
            "The domain reference architecture — one control surface": ("The domain reference architecture — one control surface", "Policy decision points, detection and the register as one map"),
            "The security program on one screen": ("The security program on one screen", "Containment, coverage and evidence freshness as the console reads them"),
            "Containment speed by threat class — the trajectory that matters": ("Containment speed by threat class — the trajectory that matters", "Where minutes are won and what buys them"),
            "Sector depth — where the security practice runs deepest today": ("Sector depth — where the security practice runs deepest today", "Twelve-industry lens with targets we sign against and the sector briefs behind them"),
            "How security engagements run": ("How security engagements run", "Baseline, register, enforce, rehearse — the sequencing that survives"),
            "Control release gates — the domain contract": ("Control release gates — the domain contract", "The evidence each gate demands; nothing advances on narrative"),
        },
    },

    "services_cybersecurity-zero-trust_ai-security-model-protection": {
        "archsubs": {
            "Injection firewall": "pre-model filter chain",
            "Corpus integrity": "signed, versioned",
            "Model-data policy": "classification-driven",
            "Output guards": "post-model redaction",
            "Abuse detection": "rate + intent signals",
            "Red-team evals": "adversarial suite, CI",
        },
        "badges": [
            ("Guard chain", "pre + post model"),
            ("Red-team suite", "CI-gated"),
            ("Model layer incidents", "0 tolerated"),
        ],
        "deep": {
            "h2": "Defend the model layer like a production service",
            "sub": "Injection firewalls, corpus integrity and abuse detection — the new surface, engineered",
            "paras": [
                "AI security fails when the model is treated as a feature and defended as an afterthought: prompt injection walks through the retrieval layer, corpus poisoning waits weeks to be noticed, and exfiltration rides the tool calls nobody scoped. The defense is layered at the surfaces — an injection firewall before the model (filter chain, not a hopeful system prompt), corpus integrity with signed and versioned documents, a model-data policy that keeps classified data out of prompts by construction, and output guards that redact before tokens reach the user. Abuse detection treats the model endpoint like any other production service: rate signals, intent signals and anomaly detection on the traffic.",
                "Measurement makes it credible: an adversarial red-team eval suite runs in CI (every prompt, guard or model change attacks the defenses), and attack simulations are scored and trended per defense layer. The agent-abuse containment overlay closes the loop for agentic surfaces — tool scoping, spend ceilings and blast-radius limits — because the newest attack surface is the one your own automation provides.",
            ],
            "bullets": [
                ("Injection firewall, pre-model", "A filter chain at the surface, not a system prompt's good intentions."),
                ("Signed corpus integrity", "Documents versioned and signed; poisoning becomes detectable."),
                ("Adversarial evals in CI", "Every change runs the attack suite; regressions block the release."),
                ("Agent blast-radius limits", "Tool scoping and spend ceilings on your own automation."),
            ],
        },
        "heads": {
            "AI security is a new surface on the same old adversary": ("AI security is a new surface on the same old adversary", "Injection, poisoning, exfiltration and abuse — engineered as production surfaces"),
            "Four AI-specific failure modes classic frameworks never named": ("Four AI-specific failure modes classic frameworks never named", "The new failure classes, and the countermeasures that ship against each"),
            "Reference architecture — defending the model layer": ("Reference architecture — defending the model layer", "Pre-model filters, model-data policy, output guards and abuse detection"),
            "One adversarial prompt, blocked in layers": ("One adversarial prompt, blocked in layers", "The layered defense, hop by hop"),
            "The AI-security console — defenses with measured rates": ("The AI-security console — defenses with measured rates", "Block rates, eval scores and abuse signals as standing numbers"),
            "Attack simulation results across the AI estate": ("Attack simulation results across the AI estate", "Per-layer scores and the trend the review reads"),
            "AI-security defaults — and documented deviations": ("AI-security defaults — and documented deviations", "The default guard stack, and where we sign deviations"),
            "AI-security release gates — evidence before exposure": ("AI-security release gates — evidence before exposure", "Eval suite results and probe evidence before a model goes live"),
            "What the security engineering team inherits": ("What the security engineering team inherits", "Guard configs, eval suites, consoles and the drill calendar"),
            "Defenses in order, week by week": ("Defenses in order, week by week", "The build sequence from surface mapping to CI-gated defense"),
            "Integration surface — AI platform, corpora and agent tooling": ("Integration surface — AI platform, corpora and agent tooling", "Where the guards attach, honestly named"),
            "Agent-abuse containment overlay": ("Agent-abuse containment overlay", "Scoping, ceilings and blast radius for agentic systems"),
        },
    },

    "services_cybersecurity-zero-trust_cloud-security-posture": {
        "archsubs": {
            "IaC guardrails": "plan-time policy checks",
            "Plan-time policy": "block before apply",
            "Posture engine": "continuous, per control",
            "Entitlement analytics": "identity-to-permission graph",
            "Drift revert": "auto, with log entry",
        },
        "badges": [
            ("Plan-time blocks", "before apply"),
            ("Critical findings dwell", "≤14 days"),
            ("Drift revert", "automatic"),
        ],
        "deep": {
            "h2": "Guardrails at plan time, not findings at audit time",
            "sub": "The deploy-time gate, entitlement analytics and the dwell-time metric that drives the backlog",
            "paras": [
                "Cloud security becomes churn when it reports: findings arrive weeks late, get triaged into oblivion, and the same misconfiguration returns with the next sprint. The engineering gate inverts it — policy checks run at plan time in the IaC pipeline, blocking non-compliant infrastructure before it applies, with developer-readable messages and golden-path alternatives. The posture engine then watches runtime continuously, and drift reverts automatically with a log entry, because an unowned drift is an incident in rehearsal.",
                "Entitlement analytics is where cloud estates actually bleed: the identity-to-permission graph finds the standing admin grants, the stale cross-account roles and the service principals nobody can name. Dwell time — how long a critical finding lives — is the headline metric, because it converts posture from a count into a clock, and the review reads the trend: which finding classes dwell longest, and which team owns the fix.",
            ],
            "bullets": [
                ("Plan-time blocking", "Policy checks in the pipeline; non-compliant infra never applies."),
                ("Automatic drift revert", "Runtime drift reverts with a log entry — no unowned drift."),
                ("Entitlement graph", "Standing grants and stale roles surfaced with named owners."),
                ("Dwell time as headline", "Findings become a clock; the trend drives the backlog."),
            ],
        },
        "heads": {
            "Cloud security is an engineering gate, not a compliance report": ("Cloud security is an engineering gate — not a compliance report", "Plan-time guardrails, entitlement analytics and the dwell-time clock"),
            "Four failure modes that turn posture into churn": ("Four failure modes that turn posture into churn", "Late findings, triage oblivion, drifting gates, ownerless entitlements"),
            "Reference architecture — guardrails from IaC to runtime": ("Reference architecture — guardrails from IaC to runtime", "Plan-time checks, runtime posture and revert as one loop"),
            "One deploy, guarded from commit to runtime": ("One deploy, guarded from commit to runtime", "The gate path with the checks each stage runs"),
            "The posture console — dwell time as the headline": ("The posture console — dwell time as the headline", "Dwell, entitlements and drift as standing numbers"),
            "Dwell time and entitlements across the quarters": ("Dwell time and entitlements across the quarters", "The trend that shows the program is real"),
            "Posture stack defaults — and documented deviations": ("Posture stack defaults — and documented deviations", "The default stack, and where we sign deviations"),
            "Posture release gates — evidence before enforcement": ("Posture release gates — evidence before enforcement", "What must be proven before guardrails block builds"),
            "What the platform security team inherits": ("What the platform security team inherits", "Policies, engines, consoles and the review cadence"),
            "Guardrails in order, week by week": ("Guardrails in order, week by week", "The build sequence from baseline to auto-revert"),
            "Integration surface — repos, pipelines and the clouds": ("Integration surface — repos, pipelines and the clouds", "Where the gate attaches, honestly named"),
            "Entitlement governance overlay": ("Entitlement governance overlay", "The standing grants review that never lapses"),
        },
    },

    "services_cybersecurity-zero-trust_compliance-audit-digital-trust": {
        "archsubs": {
            "Control register": "owner, evidence, review",
            "Assertions": "framework-mapped",
            "Evidence collector": "continuous, signed",
            "Evidence packs": "examiner-ready",
        },
        "badges": [
            ("Evidence freshness", "continuous"),
            ("Assertion coverage", "mapped per framework"),
            ("Audit request turnaround", "hours, not weeks"),
        ],
        "deep": {
            "h2": "Audit readiness is a systems property",
            "sub": "The control register, continuous evidence and assertion coverage — compliance as engineering",
            "paras": [
                "Compliance becomes archaeology when controls live in documents and evidence lives in screenshots: every audit is a dig, every framework a re-mapping. The systems answer is the control register — every control with an owner, an evidence source and a review date — wired to a collector that gathers proof as the controls run: config states, access reviews, drill results, signed policy versions. Assertions are mapped per framework once; the collector keeps the evidence fresh; and an audit request is answered from the portal in hours, with the pack an examiner expects.",
                "The quarterly rhythm makes it durable: assertion coverage and evidence freshness are reported per framework, gaps become backlog items with owners, and vendor/third-party assurance rides the same register (their SOC 2s, their pen-tests, tracked to review dates). The console reads readiness as a number — coverage and freshness — because a number trends, and a trend is what a board or a regulator actually trusts.",
            ],
            "bullets": [
                ("Register as spine", "Owner, evidence source and review date on every control."),
                ("Continuous collection", "Proof gathered as controls run — no screenshot archaeology."),
                ("Framework-mapped once", "Assertions mapped per framework; freshness maintained by the collector."),
                ("Hours-not-weeks turnaround", "Audit requests answered from the portal, examiner-ready."),
            ],
        },
        "heads": {
            "Audit readiness is a systems property, not an annual project": ("Audit readiness is a systems property — not an annual project", "The register, continuous evidence and coverage that trends"),
            "Four failure modes that turn compliance into archaeology": ("Four failure modes that turn compliance into archaeology", "Document-only controls, stale evidence, remapped frameworks, vendor blindness"),
            "Reference architecture — controls mapped once, evidence generated continuously": ("Reference architecture — controls mapped once, evidence generated continuously", "Register, collector and portal as one loop"),
            "One audit request, answered from the portal": ("One audit request, answered from the portal", "The path from request to examiner-ready pack"),
            "The compliance console — readiness as a number": ("The compliance console — readiness as a number", "Coverage and freshness per framework, trending"),
            "Assertion coverage and evidence freshness by framework": ("Assertion coverage and evidence freshness by framework", "Where each framework stands, and what ages first"),
            "Compliance stack defaults — and documented deviations": ("Compliance stack defaults — and documented deviations", "The default stack, and where we sign deviations"),
            "Compliance release gates — evidence before assertion": ("Compliance release gates — evidence before assertion", "What must be fresh before an assertion is made"),
            "What the compliance office inherits": ("What the compliance office inherits", "Register, portal, calendars and the vendor tracker"),
            "Frameworks in order, week by week": ("Frameworks in order, week by week", "The build sequence across frameworks"),
            "Integration surface — systems of record and the audit portal": ("Integration surface — systems of record and the audit portal", "Where evidence originates, honestly named"),
            "Vendor and third-party governance overlay": ("Vendor and third-party governance overlay", "Their evidence, on your review calendar"),
        },
    },

    "services_cybersecurity-zero-trust_cyber-resilience-incident-recovery": {
        "archsubs": {
            "Business services": "RTO/RPO named per service",
            "Immutable snapshots": "write-once, air-gapped",
            "Isolated vault": "separate identity plane",
            "Clean-room restore": "network-segregated",
            "Incident command": "named roles, trained",
            "Rehearsals": "timed, evidence kept",
        },
        "badges": [
            ("RTO = last drill", "nothing else"),
            ("Vault identity plane", "separate"),
            ("Rehearsal cadence", "per service tier"),
        ],
        "deep": {
            "h2": "The RTO is whatever the last drill proved",
            "sub": "Immutable vaults, clean-room restores and timed rehearsals — recovery as measured fact",
            "paras": [
                "Recovery plans are fictional until rehearsed: the runbook references a backup nobody tested, the vault shares identity with the domain the ransomware owns, and the RTO on the slide has never been measured. The discipline makes recovery a systems property — business services carry named RTO/RPO targets, snapshots are immutable and air-gapped, the vault sits on a separate identity plane (compromised domain credentials cannot reach it), and the clean-room restore rebuilds into a segregated network before anything touches production. Rehearsals are timed, per service tier, and the drill evidence — actual restore duration — is the only RTO anyone is allowed to state.",
                "Incident command is trained like a fire drill: named roles, a communication plan with pre-drafted holding statements, and decision thresholds written while calm. The console reads drill results per business service; the review asks the hard question — which service's RTO slipped, and what changes before the next drill.",
            ],
            "bullets": [
                ("Drilled RTO only", "Recovery claims come from timed drills; slides do not count."),
                ("Vault on a separate plane", "Immutable, air-gapped, unreachable by compromised domain credentials."),
                ("Clean-room restore", "Rebuild segregated first; production touch is a decision, not a default."),
                ("Trained incident command", "Named roles and decision thresholds written while calm."),
            ],
        },
        "heads": {
            "Your RTO is whatever your last rehearsal proved — nothing else": ("Your RTO is whatever your last rehearsal proved — nothing else", "Immutable vaults, clean rooms and timed drills as the only honest recovery story"),
            "Four failure modes that make recovery fictional": ("Four failure modes that make recovery fictional", "Untested backups, shared vault identity, unmeasured restores, untrained command"),
            "Reference architecture — immutable, isolated, rehearsed": ("Reference architecture — immutable, isolated, rehearsed", "Snapshots, vault, clean room and command as one system"),
            "One restore drill, from declaration to service handback": ("One restore drill, from declaration to service handback", "The timed path with the evidence each step keeps"),
            "The resilience console — drills as the headline": ("The resilience console — drills as the headline", "RTO adherence and drill coverage per service, trending"),
            "Drill results across business services": ("Drill results across business services", "Which services meet their RTO and which slip"),
            "Resilience defaults — and documented deviations": ("Resilience defaults — and documented deviations", "The default patterns, and where we sign deviations"),
            "Resilience release gates — evidence before reliance": ("Resilience release gates — evidence before reliance", "What must be proven before a service is called recoverable"),
            "What the incident command team inherits": ("What the incident command team inherits", "Roles, playbooks, drill calendar and the evidence vault"),
            "Rehearsals in order, week by week": ("Rehearsals in order, week by week", "The drill sequence from backup test to full handback"),
            "Integration surface — backup estates and business services": ("Integration surface — backup estates and business services", "What restores touch, honestly named"),
            "Incident-command governance overlay": ("Incident-command governance overlay", "Decision thresholds and the communication plan, maintained"),
        },
    },

    "services_cybersecurity-zero-trust_identity-access-modernization": {
        "archsubs": {
            "Joiner-Mover-Leaver": "HR-driven, SLA'd",
            "Federation & SSO": "one IdP, audited trusts",
            "MFA & step-up": "risk-based prompts",
            "Privileged vault": "brokered, session-recorded",
            "Workload identity": "SPIFFE-class, short-lived",
            "Hygiene scoring": "per account, trended",
        },
        "badges": [
            ("Leaver revocation SLA", "≤24 hrs"),
            ("Standing admin grants", "0 target"),
            ("Session recording", "all privileged"),
        ],
        "deep": {
            "h2": "Revocation is the metric that matters",
            "sub": "Lifecycle fidelity, brokered privilege and workload identity — where auditors look first",
            "paras": [
                "Identity programs are judged on the unglamorous metric: how fast access disappears when it should. The lifecycle runs HR-driven — joiner, mover and leaver events drive provisioning with SLAs, and the leaver path is verified, not assumed: revocation is confirmed across every downstream estate (IdP, SaaS, VPN, legacy LDAP), with the confirmation logged per system. Privileged access is brokered, not owned: standing admin grants are eliminated in favor of just-in-time elevation from a vault, with session recording on every privileged minute.",
                "Workload identity is the modern frontier — service principals with static secrets are the new service accounts nobody rotated; the modernization replaces them with short-lived, SPIFFE-class workload identities where the platform supports it, and hygiene scoring keeps the honest count everywhere else. The console reads revocation SLA adherence, MFA coverage and hygiene scores; auditors read the same numbers, which is the point.",
            ],
            "bullets": [
                ("Verified leaver path", "Revocation confirmed per downstream system, logged — never assumed."),
                ("Brokered privilege", "Just-in-time elevation from a vault; standing admin grants eliminated."),
                ("Short-lived workload identity", "Static service-principal secrets replaced where the platform allows."),
                ("Hygiene scoring, trended", "Per-account scores the auditors read with you."),
            ],
        },
        "heads": {
            "Identity is the perimeter now — and it runs on process, not enthusiasm": ("Identity is the perimeter now — and it runs on process", "Lifecycle fidelity, brokered privilege and workload identity as the program"),
            "Four identity failures auditors find first": ("Four identity failures auditors find first", "Slow leavers, standing admins, stale service secrets, unowned exceptions"),
            "Reference architecture — lifecycle from joiner to leaver": ("Reference architecture — lifecycle from joiner to leaver", "HR-driven JML, federation, step-up and the vault as one system"),
            "One leaver, from HR event to verified revocation": ("One leaver, from HR event to verified revocation", "The path with the confirmation log per system"),
            "The identity console — revocation as the headline": ("The identity console — revocation as the headline", "SLA adherence, coverage and hygiene as standing numbers"),
            "Revocation SLA and MFA coverage across the estate": ("Revocation SLA and MFA coverage across the estate", "The trend auditors sample against"),
            "Identity stack defaults — and documented deviations": ("Identity stack defaults — and documented deviations", "The default stack, and where we sign deviations"),
            "Identity release gates — evidence before enforcement": ("Identity release gates — evidence before enforcement", "What must be proven before policy blocks access"),
            "What the IAM team inherits": ("What the IAM team inherits", "Runbooks, SLAs, consoles and the exception register"),
            "Lifecycle in order, week by week": ("Lifecycle in order, week by week", "The build sequence from HR integration to verified revocation"),
            "Integration surface — HR truth and downstream estates": ("Integration surface — HR truth and downstream estates", "The systems that must obey, honestly named"),
            "Privileged-access governance overlay": ("Privileged-access governance overlay", "Brokered elevation, recorded sessions, audited exceptions"),
        },
    },

    "services_cybersecurity-zero-trust_threat-intelligence-managed-soc": {
        "archsubs": {
            "Detection rules": "MITRE-mapped, tested",
            "Attack-path mapping": "graph-based, per estate",
            "Response playbooks": "rehearsed, versioned",
            "Purple-team drills": "monthly, scoped",
        },
        "badges": [
            ("Coverage measured", "per technique"),
            ("MTTD on emulations", "minutes"),
            ("Playbooks rehearsed", "versioned"),
        ],
        "deep": {
            "h2": "Coverage is measured per technique",
            "sub": "Attack-path mapping, purple-team truth and the anti-theater metrics layer",
            "paras": [
                "SOC programs drown when alerts are counts and maturity is a slide: the honest program measures coverage per attack technique — which MITRE-mapped detections fire, which were tested this month, which exist only in vendor documentation. Purple-team drills provide the truth: emulated techniques run against production telemetry, MTTD is measured on the emulation, and the miss list becomes the detection backlog with owners and dates. The SOC console reads speed and precision — MTTD, false-positive rate and coverage per technique — because those three numbers predict the incident the program will actually handle.",
                "Response playbooks are rehearsed, versioned artifacts, not wiki pages: containment steps carry pre-approvals for the actions that need them (isolating a segment, revoking tokens at scale), and the metrics layer is deliberately anti-theater — it reports what the program cannot do as loudly as what it can, because a SOC that cannot say where it is blind is a SOC that will find out during an incident.",
            ],
            "bullets": [
                ("Technique-level coverage", "Every MITRE-mapped detection tested; the miss list drives the backlog."),
                ("Purple-team truth", "Emulations measure MTTD on production telemetry, monthly."),
                ("Pre-approved containment", "Isolation and revocation actions carry standing approvals."),
                ("Anti-theater metrics", "Blind spots reported as loudly as wins."),
            ],
        },
        "heads": {
            "Detection coverage is a measurement, not a maturity score": ("Detection coverage is a measurement — not a maturity score", "Technique-level testing, purple-team truth and the anti-theater metrics"),
            "Four ways SOC programs drown in their own alerts": ("Four ways SOC programs drown in their own alerts", "Untested detections, unmapped paths, unrehearsed playbooks, vanity metrics"),
            "Reference architecture — from threat intel to rehearsed containment": ("Reference architecture — from threat intel to rehearsed containment", "Telemetry, intel, detection and response as one loop"),
            "One signal, triaged to containment": ("One signal, triaged to containment", "The path with the evidence each step keeps"),
            "The SOC console — speed and precision as the headline": ("The SOC console — speed and precision as the headline", "MTTD, precision and coverage as standing numbers"),
            "Coverage by attack technique, before and after purple team": ("Coverage by attack technique, before and after purple team", "What emulation moved, month over month"),
            "SOC stack defaults — and documented deviations": ("SOC stack defaults — and documented deviations", "The default stack, and where we sign deviations"),
            "Detection release gates — evidence before deployment": ("Detection release gates — evidence before deployment", "What a rule must prove before it pages anyone"),
            "What the SOC leadership inherits": ("What the SOC leadership inherits", "Coverage maps, drill results and the backlog discipline"),
            "Coverage in order, week by week": ("Coverage in order, week by week", "The build sequence from estate mapping to scoped drills"),
            "Integration surface — telemetry, intel feeds and the response tooling": ("Integration surface — telemetry, intel feeds and the response tooling", "What the loop touches, honestly named"),
            "Metrics governance — the anti-theater layer": ("Metrics governance — the anti-theater layer", "How the numbers stay honest"),
        },
    },

    "services_cybersecurity-zero-trust_zero-trust-architecture": {
        "archsubs": {
            "Policy enforcement points": "every critical path",
            "Policy decision point": "deny-by-default, logged",
            "Attack-path drills": "scoped, monthly",
        },
        "badges": [
            ("Critical paths covered", "waves, gated"),
            ("Decision latency", "budgeted"),
            ("Exceptions with expiry", "100%"),
        ],
        "deep": {
            "h2": "Enforcement points, not product purchases",
            "sub": "The decision architecture — waves over critical paths, logged decisions and expiring exceptions",
            "paras": [
                "Zero trust becomes coverage theater when it is purchased rather than architected: identity, device and network products stack up while the enforcement decision — who may call what, decided where — remains informal. The architecture starts from the decision surface: a policy decision point with deny-by-default semantics, enforcement points placed on critical paths first (crown-jewel services, partner APIs, admin planes), and every decision logged with its inputs. Rollout proceeds in waves ordered by attack-path analysis, not by org chart, and each wave carries drill evidence — attack-path drills scoped to the paths it protects.",
                "Exceptions are the governance frontier: every exception carries an expiry and an owner, the exception register is reviewed on a cadence, and the console reads coverage (paths under enforcement) and decision latency (the budget the PDP must meet). The overlay that keeps programs honest is the expiring exception — because permanent exceptions are how zero-trust estates quietly become flat networks with marketing.",
            ],
            "bullets": [
                ("Decision surface first", "Deny-by-default PDP with logged decisions, before product choices."),
                ("Critical paths first", "Waves ordered by attack-path analysis, each with drill evidence."),
                ("Expiring exceptions", "Every exception has an owner and an expiry; the register is reviewed."),
                ("Decision latency budgeted", "Enforcement must be fast enough to keep, not bypass."),
            ],
        },
        "heads": {
            "Zero trust is a decision architecture, not a product purchase": ("Zero trust is a decision architecture — not a product purchase", "Decision surfaces, critical-path waves and expiring exceptions"),
            "Four ways zero-trust programs become coverage theater": ("Four ways zero-trust programs become coverage theater", "Product stacking, flat exceptions, unmeasured latency, org-chart waves"),
            "Reference architecture — the policy decision surface": ("Reference architecture — the policy decision surface", "PEPs, PDP and the drill program as one structure"),
            "One request, one decision, full trace": ("One request, one decision, full trace", "The decision path with the log the auditor reads"),
            "The zero-trust console — coverage you can defend": ("The zero-trust console — coverage you can defend", "Path coverage, latency and exceptions as standing numbers"),
            "Coverage and decision latency across rollout waves": ("Coverage and decision latency across rollout waves", "The wave-by-wave trend"),
            "Enforcement defaults — and documented deviations": ("Enforcement defaults — and documented deviations", "The default patterns, and where we sign deviations"),
            "Zero-trust release gates — evidence before enforcement": ("Zero-trust release gates — evidence before enforcement", "What a wave must prove before paths are enforced"),
            "What the security architecture team inherits": ("What the security architecture team inherits", "Policy model, wave plan, exception register and drills"),
            "Critical paths first, week by week": ("Critical paths first, week by week", "The build sequence from path mapping to enforcement"),
            "Integration surface — identity, devices and the estate": ("Integration surface — identity, devices and the estate", "What the decision surface reads, honestly named"),
            "Control overlay — exceptions with expiries": ("Control overlay — exceptions with expiries", "The register that keeps the estate from going flat"),
        },
    },
}
