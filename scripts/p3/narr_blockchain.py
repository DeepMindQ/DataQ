"""narr_blockchain — narrative layer for the Blockchain & Digital Trust domain."""

HUB = {
    "hero": ("Blockchain & Digital Trust is delivered as boring infrastructure: permissioned "
             "networks with real governance, contracts that pass audits at zero highs, identity "
             "that works offline, provenance that survives recalls — the verifiable record "
             "regulators accept, built with consensus nobody has to adore."),
    "s_practices": "Six practices from network charter to token lifecycle",
    "deep": [
        ("The practice's bias is deliberate dullness: boring consensus, boring cryptography, "
         "boring governance — because the value of a shared ledger is that nobody argues with "
         "it, and nobody argues with systems that behave predictably under stress. The "
         "exciting part is what the record enables: recalls resolved in minutes, credentials "
         "verified offline, settlements that reconcile to the ledger by construction."),
        ("Regulation is a design input, not an afterthought: transfer restrictions enforced in "
         "code, travel-rule workflows built into analytics, privacy domains engineered into "
         "the network charter. The practices assume the regulator reads the architecture — "
         "because eventually, one does."),
    ],
    "s_deep": "Boring on purpose: the engineering case for dull distributed systems",
    "s_arch": "The domain reference architecture — charter to verifiable surface",
    "arch_lead": ("The charter governs membership and privacy domains, consensus carries the "
                  "ledger, contracts and credentials build on it, analytics maps it to "
                  "regulatory duties, and every surface inherits the controls — one stack "
                  "where verifiability is structural, not aspirational."),
    "s_dash": "The network on one screen — trust with its numbers",
    "dash_lead": ("Transaction cost, network uptime, version currency and the governance ledger "
                  "— tiles that read like infrastructure because that is what trust requires."),
    "dash_note": ("Reference console — network targets; governance decisions are recorded on-"
                  "ledger with their votes, so every configuration change has a paper trail "
                  "the members can audit."),
    "s_chart": "The network as a system — membership and flow topology",
    "chart_lead": ("A permissioned network rendered as topology: members, endorsing nodes, "
                   "privacy domains and the anchoring points where external evidence enters the "
                   "ledger. The orange hubs are where governance actually happens."),
    "chart_override": {
        "variant": "network",
        "title": "Permissioned network topology — members, privacy domains, anchor points",
        "cats": [],
        "series": [],
        "nodes": [
            {"id": "anchor", "x": 0.5, "y": 0.12, "hub": True, "label": "Notary anchor"},
            {"id": "m1", "x": 0.12, "y": 0.38, "hub": True, "label": "Member A"},
            {"id": "m2", "x": 0.5, "y": 0.42, "hub": True, "label": "Member B"},
            {"id": "m3", "x": 0.88, "y": 0.38, "hub": True, "label": "Member C"},
            {"id": "m4", "x": 0.26, "y": 0.72, "label": "Member D"},
            {"id": "m5", "x": 0.74, "y": 0.72, "label": "Member E"},
            {"id": "reg", "x": 0.5, "y": 0.92, "label": "Regulator read"},
        ],
        "links": [[0, 1], [0, 2], [0, 3], [1, 2], [2, 3], [1, 4], [2, 4], [2, 5], [3, 5], [4, 6], [5, 6], [2, 6]],
        "caption": "Reference topology for a five-member permissioned network with a notary anchor and regulator read access — privacy domains sit between members.",
    },
    "chart_note": None,
    "s_evidence": "Sector depth — where the digital-trust practice runs deepest today",
    "evidence_lead": ("Trade finance, provenance and tokenization concentrate in different "
                      "sectors — and so does our published depth. The bars count sub-industry "
                      "briefs live on this site."),
    "evidence_chart_title": "Blockchain & Digital Trust — published sub-industry briefs by sector",
    "explorer_title": "Verifiable records in your sector — pick the industry and see the plan",
    "explorer_intro": ("A bank's settlement network and a grocer's provenance chain share the "
                       "ledger discipline but not the regulations. Select your sector: the "
                       "panel shows the entry problem, the deliverables, the targets and the "
                       "sector brief."),
    "plays": [
        "Permissioned networks with real charters, privacy domains and boring consensus",
        "Contracts and credentials that pass independent audits at zero highs",
        "Regulatory duties engineered into the stack — transfer controls, travel rule, evidence",
    ],
    "flagships": ["banking-financial-services", "insurance", "agriculture-food"],
    "s_engage": "How digital-trust engagements run",
    "engage": [
        ["Diagnostic — two weeks", "The charter drafted, privacy domains scoped, the governance ledger designed — you keep the network blueprint with member obligations spelled out."],
        ["Provability sprint — four weeks", "One verification problem runs a fund-or-kill slice: provenance completeness, verification latency or settlement delta on your real records."],
        ["Build — ten to fourteen weeks", "Network, contracts and surfaces built to the reference architecture, with audits scheduled before go-live — not after incidents."],
        ["Industrialize — ongoing", "Governance cadence with the members, version upgrades with zero-downtime coordination, and the analytics that keep regulators satisfied."],
    ],
    "s_gates": "Network release gates — the domain contract",
    "cta": ("Bring the record-keeping problem your auditors and your trading partners both "
            "distrust. The two-week diagnostic will draft the charter and price what verifiable "
            "evidence costs on your network."),
}

PAGES = {

"enterprise-dlt-networks": {
    "hero": ("Permissioned networks with real governance: membership charters with obligations "
             "on paper, privacy domains that end the data-sharing standoff, consensus chosen "
             "for dullness, and upgrades coordinated so every member runs the current version "
             "— at transaction costs your CFO will not notice."),
    "s1_h": "The network succeeds at the speed of its charter, not its consensus",
    "s1_close": ("Below: the failure modes that stall consortium networks, the reference "
                 "architecture of a governed network, and the console that keeps members "
                 "honest."),
    "s2_h": "Four failure modes that stall consortium networks",
    "s2_lead": ("Every one of these is a governance failure wearing a technical costume — the "
                "countermeasures put obligations, privacy rules and upgrade discipline in the "
                "charter where they belong."),
    "arch_h": "Reference architecture — the governed permissioned network",
    "arch_lead": ("Members join under a charter with obligations and exit clauses, privacy "
                  "domains scope what each member sees, consensus is chosen for predictability "
                  "over novelty, and the upgrade protocol runs with zero-downtime coordination "
                  "— governance and engineering as one design."),
    "flow_h": "One transaction, endorsed to finality",
    "flow_lead": ("From proposal through endorsement within its privacy domain, ordering, "
                  "commit and the audit record — including where a member's stale version is "
                  "caught before it forks the ledger."),
    "dash_h": "The network console — member health as the headline",
    "dash_lead": ("Transaction cost, network uptime and version currency across members — the "
                  "three numbers that decide whether the consortium is compounding or "
                  "fragmenting."),
    "dash_note": ("Reference console — network targets; a member lagging a version is a charter "
                  "obligation trigger, not a support ticket."),
    "chart_h": "Cost and throughput across network growth",
    "chart_lead": ("Transaction cost and throughput as membership grows — the curve that shows "
                   "whether the network's economics survive its own success."),
    "stack_h": "Network defaults — and documented deviations",
    "stack_lead": ("Defaults favor permissioned, charter-governed designs with predictable "
                   "consensus over public-chain experiments; deviation triggers are written "
                   "because each one moves trust from governance to tokenomics."),
    "gates_h": "Network release gates — evidence before member onboarding",
    "artifacts_h": "What the consortium inherits",
    "timeline_h": "Charter to mainnet, week by week",
    "integ_h": "Integration surface — member systems and the shared ledger",
    "integ_lead": ("Each member integrates their systems of record; these contracts define "
                   "event emission, identity onboarding and the privacy boundaries every "
                   "integration must respect."),
    "controls_h": "Governance overlay — the on-ledger charter",
    "controls_lead": ("Governance is executed, not laminated: votes, amendments and member "
                      "obligations recorded on-ledger — the charter your regulator can read "
                      "directly from the system itself."),
    "controls_note": ("Chain bloat is managed by design: archival policy, state pruning and "
                      "evidence retention are charter clauses with technical enforcement — "
                      "because a ledger that grows forever eventually stops serving anyone."),
    "cta": ("Bring the consortium that has met twelve times without shipping. The diagnostic "
            "will draft the charter with privacy domains scoped — and put the network on a "
            "build schedule."),
    "flagships": ["banking-financial-services", "insurance", "public-sector"],
    "plays": [
        "Membership charters with obligations, exit clauses and on-ledger governance",
        "Privacy domains that end the data-sharing standoff between members",
        "Zero-downtime upgrade coordination — every member current, or flagged",
    ],
},

"smart-contract-engineering": {
    "hero": ("Contracts that pass independent audits at zero highs: formal-verified cores with "
             "invariant coverage measured, fuzzing that runs around the clock, upgrade "
             "discipline that removes ambush risk — and a spec written before the first line "
             "of Solidity."),
    "s1_h": "The specification is the contract; the code is just its executable form",
    "s1_close": ("Below: the failure modes that put vulnerabilities on mainnet, the reference "
                 "architecture of the verification pipeline, and the console that tracks "
                 "audit readiness."),
    "s2_h": "Four failure modes that put vulnerabilities on mainnet",
    "s2_lead": ("Each of these has shipped eight-figure incidents — the countermeasures front-"
                "load specification, verification and upgrade discipline so the bugs never "
                "deploy."),
    "arch_h": "Reference architecture — from spec to audited contract",
    "arch_lead": ("The pipeline runs specification first: formal-verified cores with invariants "
                  "as testable properties, property-based fuzzing around the clock, coverage "
                  "measured against the spec, and an upgrade proxy pattern that makes every "
                  "change a governed release."),
    "flow_h": "One contract change, from spec diff to audited release",
    "flow_lead": ("From the spec change through invariant updates, fuzzing, formal "
                  "verification, independent audit and the staged deployment — including the "
                  "rollback path if any gate fails."),
    "dash_h": "The contract console — audit readiness as the headline",
    "dash_lead": ("Audit highs at zero, invariant coverage and fuzz uptime — the three numbers "
                  "that decide whether the next audit is a formality or an event."),
    "dash_note": ("Reference console — contract targets; no release ships while the fuzzer is "
                  "red, and invariant coverage is measured against the spec, not the tests."),
    "chart_h": "Invariant coverage across contract versions",
    "chart_lead": ("Coverage per contract version and per audit round — the shape that shows "
                   "the verification investment compounding instead of resetting at every "
                   "release."),
    "stack_h": "Contract defaults — and documented deviations",
    "stack_lead": ("Defaults favor formal verification and property-based fuzzing over test-"
                   "by-coverage; deviation triggers are written because each one widens the "
                   "gap between what is tested and what is trusted."),
    "gates_h": "Contract release gates — evidence before deployment",
    "artifacts_h": "What the engineering team inherits",
    "timeline_h": "Spec to audit, week by week",
    "integ_h": "Integration surface — ledgers, oracles and the business systems",
    "integ_lead": ("Contracts touch ledgers, oracles and the systems that trigger them; these "
                   "contracts define event boundaries and the data each side trusts."),
    "controls_h": "Upgrade-governance overlay",
    "controls_lead": ("Upgrades are governed releases: multi-party approval, timed locks, "
                      "spec-diff evidence and a rehearsed emergency pause — the discipline "
                      "that removes ambush risk from live contracts."),
    "controls_note": ("The fuzzer runs continuously between releases: 24/7 property-based "
                      "fuzzing means a newly discovered bug class is tested against your "
                      "contracts the same week it is published, not the next audit cycle."),
    "cta": ("Bring the contract your auditors keep reopening. The verification sprint will "
            "write the spec, pin the invariants and run the fuzzer — until the audit is a "
            "formality."),
    "flagships": ["insurance", "technology-saas", "banking-financial-services"],
    "plays": [
        "Specification-first development with formal-verified cores",
        "Property-based fuzzing around the clock, invariants measured against the spec",
        "Upgrade discipline: multi-party approval, timed locks, rehearsed pause",
    ],
},

"decentralized-identity": {
    "hero": ("DIDs and verifiable credentials that work offline: issuers governed by charter, "
             "holder wallets people keep using, selective disclosure that shares less, and "
             "revocation that actually propagates in minutes — verification in 210ms, without "
             "a phone call."),
    "s1_h": "Identity wallets live or die at the same intersection as consumer apps",
    "s1_close": ("Below: the failure modes that strand credential ecosystems, the reference "
                 "architecture of the trust triangle, and the console that keeps verification "
                 "fast and revocation real."),
    "s2_h": "Four failure modes that strand credential ecosystems",
    "s2_lead": ("Each of these kills adoption quietly — the countermeasures treat issuer "
                "governance, wallet UX and revocation as engineering deliverables, not "
                "roadmap promises."),
    "arch_h": "Reference architecture — the governed trust triangle",
    "arch_lead": ("Issuers operate under a charter with accreditation rules, holders get "
                  "wallets designed for retention, verifiers check credentials in milliseconds "
                  "— offline where possible — and revocation registries propagate in minutes, "
                  "because a credential that cannot be revoked is a liability, not a feature."),
    "flow_h": "One credential, issuance to offline verification",
    "flow_lead": ("From issuance under charter rules through holder consent, selective "
                  "disclosure and the offline verification path — including the revocation "
                  "check that catches a cancelled credential at the door."),
    "dash_h": "The identity console — adoption and trust as the headline",
    "dash_lead": ("Verification latency, offline verification rate and revocation propagation "
                  "— the three numbers that decide whether the ecosystem is trusted or merely "
                  "launched."),
    "dash_note": ("Reference console — identity targets; wallet retention is reviewed beside "
                  "latency, because a fast verifier with an abandoned wallet verifies nothing."),
    "chart_h": "Verification performance across issuer growth",
    "chart_lead": ("Latency and offline success rates as issuers and credential types grow — "
                   "the curve that shows whether the registry design scales past the pilot."),
    "stack_h": "Identity defaults — and documented deviations",
    "stack_lead": ("Defaults favor offline-capable verification and chartered issuers over "
                   "phone-home designs; deviation triggers are written because each one "
                   "creates a availability or governance gap."),
    "gates_h": "Identity release gates — evidence before ecosystem launch",
    "artifacts_h": "What the trust-framework team inherits",
    "timeline_h": "Charter to wallets, week by week",
    "integ_h": "Integration surface — issuer systems, wallets and verifier gates",
    "integ_lead": ("The triangle spans issuer back-ends, mobile wallets and verifier "
                   "infrastructure; these contracts define credential formats, consent flows "
                   "and the revocation protocol."),
    "controls_h": "Privacy and governance overlay",
    "controls_lead": ("Selective disclosure is structural — holders share claims, not "
                      "documents — and the issuer charter caps what may be requested, so the "
                      "ecystem minimizes data by design rather than by policy memo."),
    "controls_note": ("Revocation is tested like a control: synthetic cancelled credentials are "
                      "presented to verifiers weekly, and any acceptance is a sev-1 — "
                      "revocation fiction is the ecosystem's most dangerous failure."),
    "cta": ("Bring the credential your sector keeps reinventing on paper. The diagnostic will "
            "draft the issuer charter and price what offline-verifiable credentials cost on "
            "your trust framework."),
    "flagships": ["public-sector", "healthcare-life-sciences", "education-research"],
    "plays": [
        "Chartered issuers with accreditation rules — no issuer anarchy",
        "Wallets designed for retention, selective disclosure built in",
        "Revocation that propagates in minutes and is tested weekly",
    ],
},

"provenance-traceability": {
    "hero": ("End-to-end supply-chain evidence: anchored document hashes, event provenance at "
             "every handoff, capture coverage that reaches your partners — and recall drills "
             "that resolve the affected batch in minutes, not days of spreadsheet archaeology."),
    "s1_h": "Provenance is a capture problem before it is a ledger problem",
    "s1_close": ("Below: the failure modes that make provenance decorative, the reference "
                 "architecture of the capture chain, and the console that drills recalls."),
    "s2_h": "Four failure modes that make provenance decorative",
    "s2_lead": ("Every one of these survives a pilot and fails a recall — the countermeasures "
                "measure capture coverage at partner level and drill the recall path on "
                "schedule."),
    "arch_h": "Reference architecture — the capture chain from field to ledger",
    "arch_lead": ("Events are captured at each handoff under shared identifier standards, "
                  "documents are anchored as hashes with the originals in your systems of "
                  "record, and the ledger stitches the chain — so the recall query is a "
                  "lookup, not an investigation."),
    "flow_h": "One batch, from field event to recall drill",
    "flow_lead": ("From harvest or production events through partner handoffs, anchored "
                  "documents and the ledger chain to the recall drill — including the gap "
                  "analysis that runs when capture coverage drops."),
    "dash_h": "The provenance console — recall time as the headline",
    "dash_lead": ("Recall drill time, provenance completeness and partner capture coverage — "
                  "the three numbers that decide whether the chain is evidence or "
                  "decoration."),
    "dash_note": ("Reference console — provenance targets; partner capture coverage is reviewed "
                  "monthly, and a partner below threshold gets an onboarding plan, not a "
                  "pass."),
    "chart_h": "Capture coverage across the partner network",
    "chart_lead": ("Event capture coverage per partner tier and quarter — the shape that shows "
                   "where the chain breaks and which partners need integration work, not "
                   "reminders."),
    "stack_h": "Provenance defaults — and documented deviations",
    "stack_lead": ("Defaults favor shared identifier standards and anchored documents over "
                   "proprietary label schemes; deviation triggers are written because each one "
                   "re-creates identifier chaos downstream."),
    "gates_h": "Provenance release gates — evidence before partner onboarding",
    "artifacts_h": "What the supply-chain integrity team inherits",
    "timeline_h": "Partners in order, week by week",
    "integ_h": "Integration surface — partner systems, labels and the ledger",
    "integ_lead": ("The chain is only as strong as its weakest partner integration; these "
                   "contracts define identifier standards, event formats and the capture "
                   "guarantees each handoff carries."),
    "controls_h": "Recall-readiness governance overlay",
    "controls_lead": ("Recall drills run on schedule with live data: the affected batch is "
                      "traced, the affected downstream partners are enumerated and the "
                      "notification pack is generated — recall theater dies in rehearsal."),
    "controls_note": ("Paper analogs are detected, not assumed away: when a partner's events "
                      "arrive as week-late batch uploads, the drill treats that segment as "
                      "unproven — coverage claims must match capture cadence."),
    "cta": ("Time your last mock recall — or admit there wasn't one. The diagnostic will "
            "measure capture coverage across your partner network and drill the recall path "
            "until it resolves in minutes."),
    "flagships": ["retail-consumer-goods", "agriculture-food", "logistics-supply-chain"],
    "plays": [
        "Event provenance at every handoff under shared identifier standards",
        "Document anchoring with originals in your systems of record",
        "Recall drills on live data — batch traced in minutes, notifications generated",
    ],
},

"blockchain-analytics-compliance": {
    "hero": ("Ledger intelligence mapped to regulatory duties: transaction risk scoring with "
             "measured precision, travel-rule workflows that cover your counterparties, and "
             "case management that turns investigations from archaeology into a query — built "
             "for the auditor who arrives unannounced."),
    "s1_h": "Screening precision is a compliance outcome, not a vendor spec sheet",
    "s1_close": ("Below: the failure modes that flood compliance teams with noise, the "
                 "reference architecture of the analytics pipeline, and the console that keeps "
                 "case SLAs honest."),
    "s2_h": "Four failure modes that drown compliance teams in noise",
    "s2_lead": ("Every one of these converts a regulator's question into a week of work — the "
                "countermeasures measure precision, close travel-rule gaps and keep cases "
                "queryable from day one."),
    "arch_h": "Reference architecture — from ledger events to case files",
    "arch_lead": ("Address attribution runs continuously against known-entity registries, risk "
                  "scoring is calibrated against closed-case ground truth, travel-rule "
                  "workflows exchange originator and beneficiary data where required, and "
                  "every case lands in a queryable store with its evidence attached."),
    "flow_h": "One flagged transaction, from screen to case closure",
    "flow_lead": ("From the screening hit through attribution, risk scoring, the travel-rule "
                  "exchange where triggered and case disposition — including the false-positive "
                  "feedback that tunes precision."),
    "dash_h": "The analytics console — precision as the headline",
    "dash_lead": ("Screening precision, travel-rule coverage and case SLA adherence — the three "
                  "numbers that decide whether the compliance function scales with volume or "
                  "drowns under it."),
    "dash_note": ("Reference console — analytics targets; precision is calibrated against "
                  "closed-case outcomes, and false-positive feedback tunes the models "
                  "continuously."),
    "chart_h": "Precision and coverage across screening cycles",
    "chart_lead": ("Screening precision and travel-rule coverage across quarterly cycles — the "
                   "paired curve that shows the noise problem shrinking as coverage grows."),
    "stack_h": "Analytics defaults — and documented deviations",
    "stack_lead": ("Defaults favor measured attribution and calibrated scoring over "
                   "black-box risk feeds; deviation triggers are written because each one "
                   "moves the audit defense from evidence to assertion."),
    "gates_h": "Analytics release gates — evidence before deployment",
    "artifacts_h": "What the compliance function inherits",
    "timeline_h": "Attribution to cases, week by week",
    "integ_h": "Integration surface — ledgers, registries and the case systems",
    "integ_lead": ("The pipeline spans ledgers, attribution registries and your case systems; "
                   "these contracts carry flagged events into investigations with evidence "
                   "attached from the first minute."),
    "controls_h": "Regulatory-examination overlay",
    "controls_lead": ("Examination readiness is a systems property: case files, model cards "
                      "and screening calibrations are queryable — the unannounced examiner "
                      "meets a portal, not a panic."),
    "controls_note": ("Address blindness is hunted monthly: new protocol deployments and "
                      "mixing services are added to attribution within a published SLA — the "
                      "coverage ledger records when each new pattern became visible."),
    "cta": ("Ask what percentage of last month's screening hits your team closed as actionable. "
            "The diagnostic will calibrate precision against your closed cases — and price "
            "what a quieter, defensible compliance stack costs."),
    "flagships": ["banking-financial-services", "technology-saas", "insurance"],
    "plays": [
        "Continuous address attribution against known-entity registries",
        "Risk scoring calibrated to closed-case ground truth — precision measured",
        "Travel-rule workflows and case files an unannounced examiner can query",
    ],
},

"asset-tokenization": {
    "hero": ("Regulated token designs: legal-wrapper-first architecture, transfer controls that "
             "enforce restrictions in code, ledger and cap-table reconciliation at zero delta — "
             "and every lifecycle event from issuance to redemption designed before the token "
             "exists."),
    "s1_h": "The token is the easy part; the legal wrapper is the product",
    "s1_close": ("Below: the failure modes that strand tokenized assets, the reference "
                 "architecture of wrapper-first design, and the console that keeps the ledger "
                 "reconciled to reality."),
    "s2_h": "Four failure modes that strand tokenized assets",
    "s2_lead": ("Each of these turns a token launch into a legal incident — the countermeasures "
                "design the wrapper, the restrictions and the lifecycle before the first "
                "mint."),
    "arch_h": "Reference architecture — wrapper-first tokenization",
    "arch_lead": ("The legal wrapper defines what the token is; transfer controls enforce "
                  "eligibility, lockups and jurisdiction rules in code; the off-chain registry "
                  "reconciles to the ledger at zero delta; and every lifecycle event — "
                  "corporate actions, redemptions, wind-downs — has a designed path."),
    "flow_h": "One restricted transfer, controlled end to end",
    "flow_lead": ("From the transfer request through eligibility verification, restriction "
                  "checks, settlement and the cap-table reconciliation — including the block "
                  "events that prove the controls work by refusing."),
    "dash_h": "The tokenization console — reconciliation as the headline",
    "dash_lead": ("Settlement cycle, restricted-transfer blocks and the ledger-to-cap-table "
                  "delta — the three numbers that decide whether the token is a security "
                  "operation or a liability."),
    "dash_note": ("Reference console — tokenization targets; a non-zero ledger-cap-table delta "
                  "is a sev-1 by policy, because reconciliation drift is how tokens lose their "
                  "legal footing."),
    "chart_h": "Restriction enforcement across transfer attempts",
    "chart_lead": ("Transfer attempts, eligibility blocks and settled transfers across "
                   "quarters — the shape that shows the controls refusing what the prospectus "
                   "promises they would."),
    "stack_h": "Tokenization defaults — and documented deviations",
    "stack_lead": ("Defaults favor wrapper-first design and code-enforced restrictions over "
                   "token-first enthusiasm; deviation triggers are written because each one "
                   "moves a legal promise into a policy PDF nobody can enforce."),
    "gates_h": "Token release gates — evidence before issuance",
    "artifacts_h": "What the asset operations team inherits",
    "timeline_h": "Wrapper to lifecycle, week by week",
    "integ_h": "Integration surface — registries, transfer agents and settlement rails",
    "integ_lead": ("Tokenized assets live across registries, transfer agents and settlement "
                   "rails; these contracts define the reconciliation and the event flows that "
                   "keep the ledger legally meaningful."),
    "controls_h": "Lifecycle-governance overlay",
    "controls_lead": ("Corporate actions, redemptions and wind-down paths are designed and "
                      "rehearsed before issuance — the lifecycle blanks that strand tokenized "
                      "assets are filled in the design, not discovered in the incident."),
    "controls_note": ("Off-chain reality is tracked as a first-class risk: court orders, "
                      "probate events and registry corrections are modeled as ledger operations "
                      "with legal sign-off — the reconciliation stays zero because reality has "
                      "a designated path back into the ledger."),
    "cta": ("Bring the asset your firm wants to tokenize. The design sprint will architect the "
            "legal wrapper, the transfer controls and the lifecycle — before anyone mentions a "
            "token standard."),
    "flagships": ["banking-financial-services", "insurance", "technology-saas"],
    "plays": [
        "Legal-wrapper-first architecture — the token designed after the wrapper",
        "Transfer restrictions enforced in code, with block events as evidence",
        "Ledger-to-cap-table reconciliation at zero delta, lifecycle paths pre-designed",
    ],
},
}
