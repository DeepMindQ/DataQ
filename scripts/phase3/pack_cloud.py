#!/usr/bin/env python3
"""Pack: Cloud, Edge & Platform Engineering (dom=cloud-edge-platform-engineering)."""

DOM = "cloud-edge-platform-engineering"

HOOKS = {
    "banking-financial-services": "Core-adjacent estates under change-control scrutiny: modernization waves with retirement gates, hybrid placement by policy, and reliability budgets a regulator can read.",
    "insurance": "Policy-admin estates carry decades of batch logic — strangler-wave modernization, edge capture at claims sites, and FinOps discipline across seasonal load.",
    "healthcare-life-sciences": "Clinical estates demand uptime and residency: hybrid placement with data-residency policy, mission-critical tiers for clinical systems, and SLOs that clinical operations sign.",
    "manufacturing": "Plant-floor to cloud: edge estates that survive partitions, modernization waves that retire mainframe-era MES wrappers, and unit-cost discipline across every plant.",
    "retail-consumer-goods": "Seasonal load is the design condition: elastic tiers for peak trading, edge for stores, and FinOps that prices commerce per transaction.",
    "telecom-media": "Network-adjacent workloads at true edge scale: regional clusters with store-and-forward discipline, latency budgets per tier, and SRE practice across OSS/BSS.",
    "energy-utilities": "OT-adjacent estates with safety constraints: segmented cloud zones, edge compute at substations, and reliability engineering that respects control-room change windows.",
    "logistics-supply-chain": "Control towers and WMS estates under 24/7 load: hybrid placement for track-and-trace, edge at hubs and doors, and SLOs priced against detention minutes.",
    "public-sector": "Citizen-critical services on public clouds: residency-bound placement, mission-critical tiers for benefits peak days, and cost allocation every agency can defend.",
    "education-research": "Term-cycle load spikes: elastic student-facing tiers, edge caching for campuses, and FinOps that survives procurement scrutiny.",
    "technology-saas": "Your product is the estate: platform engineering with golden paths, multi-region reliability budgets, and unit economics per customer.",
    "agriculture-food": "Field-to-cloud estates with connectivity gaps: store-and-forward edge at co-ops, seasonal compute bursts, and unit costs per hectare of data managed.",
}

KPIS = {
    "banking-financial-services": [
        ("Change failure rate, governed tiers", 2, 9, "pct"),
        ("MTTR on tier-1 services", 15, 45, "min"),
        ("Retirements completed per wave", 88, 100, "pct"),
    ],
    "insurance": [
        ("Batch-window parity at cutover", 96, 100, "pct"),
        ("Claims-site edge uptime", 98, 100, "pct"),
        ("Workload unit-cost reduction", 10, 30, "pct"),
    ],
    "healthcare-life-sciences": [
        ("Residency policy violations", 0, 0, "num"),
        ("Clinical tier MTTR", 10, 35, "min"),
        ("Failover drills passed", 92, 100, "pct"),
    ],
    "manufacturing": [
        ("Site autonomy while offline", 8, 48, "hrs"),
        ("Modernization retirement rate", 70, 95, "pct"),
        ("Compute cost per plant, monthly", 4, 18, "k"),
    ],
    "retail-consumer-goods": [
        ("Peak-trade availability", 99, 100, "pct"),
        ("Store-edge reconciliation lag", 1, 10, "min"),
        ("Cost per 1k transactions", 8, 40, "cents"),
    ],
    "telecom-media": [
        ("Latency budget met per tier", 92, 99, "pct"),
        ("Edge fleet heartbeat compliance", 96, 100, "pct"),
        ("OSS workload MTTR", 12, 40, "min"),
    ],
    "energy-utilities": [
        ("OT-zone segmentation violations", 0, 1, "num"),
        ("Substation edge uptime", 98, 100, "pct"),
        ("Change-window adherence", 95, 100, "pct"),
    ],
    "logistics-supply-chain": [
        ("Track-and-trace freshness p95", 5, 30, "sec"),
        ("Hub-edge autonomy", 6, 24, "hrs"),
        ("Cost per shipment tracked", 1, 6, "cents"),
    ],
    "public-sector": [
        ("Peak-day benefits availability", 99, 100, "pct"),
        ("Residency-bound placement compliance", 100, 100, "pct"),
        ("Cost allocation coverage", 92, 100, "pct"),
    ],
    "education-research": [
        ("Term-peak elasticity headroom", 30, 80, "pct"),
        ("Campus edge cache hit rate", 55, 85, "pct"),
        ("Cost per active student", 5, 40, "cents"),
    ],
    "technology-saas": [
        ("Golden-path adoption", 55, 85, "pct"),
        ("Error budget burn, multi-region", 40, 90, "pct"),
        ("Infra cost per customer", 60, 300, "cents"),
    ],
    "agriculture-food": [
        ("Store-and-forward data survival", 97, 100, "pct"),
        ("Seasonal burst elasticity", 40, 90, "pct"),
        ("Data cost per hectare managed", 2, 12, "cents"),
    ],
}

SYSTEMS = {
    "banking-financial-services": ["Governed change windows (CAB)", "Hybrid landing zones", "FinOps showback ledger"],
    "insurance": ["PAS batch schedulers", "Claims-site edge", "Tag enforcement"],
    "healthcare-life-sciences": ["Clinical SLO framework", "Residency policy engine", "Epic-class integration gates"],
    "manufacturing": ["Plant edge (store-and-forward)", "MES wrappers + retirement gates", "Plant FinOps showback"],
    "retail-consumer-goods": ["Elastic commerce tiers", "Store edge fleet", "Commerce unit-cost models"],
    "telecom-media": ["Regional edge clusters", "OSS/BSS estates", "Heartbeat SLO fleet"],
    "energy-utilities": ["OT segmentation zones", "Substation edge compute", "Change-window governance"],
    "logistics-supply-chain": ["Control-tower APIs", "Hub and door edge", "Shipment-cost telemetry"],
    "public-sector": ["Residency-bound landing zones", "Peak capacity models", "Agency showback ledger"],
    "education-research": ["Term-aware autoscaling", "Campus edge caches", "Grant-compliant allocation"],
    "technology-saas": ["Golden paths (as APIs)", "Multi-region runtime", "Per-customer unit ledger"],
    "agriculture-food": ["Co-op edge gateways", "Seasonal burst queues", "Per-hectare cost telemetry"],
}

COMMON_SUBS = {
    "Golden paths (as APIs)": "versioned scaffold contracts",
    "Kubernetes runtimes": "managed, version-pinned",
    "Edge clusters": "autonomy-tested per site",
    "SLO framework": "error budgets, tiered",
    "FinOps engine": "allocation with owners",
    "Refactor ladder": "strangler steps, exit gates",
    "State externalization": "session + data moved first",
    "Container platform": "pinned bases, signed",
    "Managed services": "used where parity holds",
    "Posture proof": "drift reverted, logged",
    "Retirement gate": "consumer count zero",
    "Edge OS & runtime": "atomic updates, auto-revert",
    "Hardware abstraction": "fleet heterogeneity absorbed",
    "Store-and-forward": "survives partitions",
    "Release trains": "staged waves, canary first",
    "Heartbeat SLOs": "site silence pages",
    "Tag enforcement": "untagged = un-deployable",
    "Allocation engine": "shared cost, priced fairly",
    "Unit-economics registry": "cost per business unit",
    "Rightsizing engine": "recommendations with owners",
    "Waste ledger": "zombies, listed monthly",
    "Budget gates": "forecasts gate commitments",
    "Signed SLAs": "business-signed tiers",
    "Hop budget table": "ms per hop, budgeted",
    "Redundancy fabric": "failure domains, tested",
    "Capacity model": "load-tested headroom",
    "Load program": "peak rehearsals, quarterly",
    "Placement engine": "policy-scored, not vibes",
    "Interconnect fabric": "egress-aware topology",
    "Federated identity": "one IdP, per-cloud SPs",
    "Unified policy model": "one policy, per-cloud output",
    "Platform product team": "roadmap, adoption-owned",
    "Service scaffold": "golden path in one command",
    "Security path": "compliance in the scaffold",
    "DevEx funnel": "time-to-first-deploy tracked",
    "SLO documents": "signed per service",
    "Budget calculator": "burn rate, live",
    "Release gating": "budget-exhaust = freeze",
    "Chaos program": "monthly, scoped drills",
    "Incident command": "named roles, trained",
    "Blameless review": "actions with owners",
}

PAGES = {
    "services_cloud-edge-platform-engineering": {
        "archsubs": {
            "Golden paths (as APIs)": "versioned scaffold contracts",
            "Kubernetes runtimes": "managed, version-pinned",
            "Edge clusters": "autonomy-tested per site",
            "SLO framework": "error budgets, tiered",
            "FinOps engine": "allocation with owners",
        },
        "badges": [
            ("Practices in the domain", "7"),
            ("Estate gates", "4"),
            ("Industries served", "12"),
        ],
        "deep": {
            "h2": "The estate is one system — reliability and economics together",
            "sub": "Why golden paths, SLOs and FinOps are engineered as a single operating surface",
            "paras": [
                "Estates drift because the three disciplines report to different rooms: platform teams ship golden paths nobody adopts, SRE teams publish SLOs that gate nothing, FinOps teams produce dashboards that change no decision. The domain design joins them — golden paths carry the SLO template and the tag schema by default, error budgets gate releases in CI rather than in meetings, and every workload's unit cost lands in a registry with a named owner. The console reads reliability and economics side by side, because the trade-off between them is the actual daily decision of estate management.",
                "The engagement sequence follows the same logic: baseline the estate (tiers, unit costs, failure history), sign the SLO framework with business owners, deploy the golden paths with compliance built in, and let the FinOps engine allocate from day one — allocation creates accountability, and accountability is what makes every other practice stick. Gates at each step demand evidence: a tier without signed SLOs does not carry production traffic, a wave without retirement criteria does not start.",
            ],
            "bullets": [
                ("One operating surface", "Paths, SLOs and allocation join at the scaffold — not in three dashboards."),
                ("Budgets that gate", "Error-budget exhaustion freezes releases automatically, by CI."),
                ("Named owners for every unit cost", "Allocation creates the accountability that adoption requires."),
                ("Gates with evidence", "Unsigned SLOs carry no production traffic; waves without exits do not start."),
            ],
        },
        "heads": {
            "Seven practices from golden paths to mission-critical tiers": ("Seven practices, from golden paths to mission-critical tiers", "Paths, modernization, edge, FinOps, mission-critical, hybrid and SRE as one estate system"),
            "Reliability and unit cost: the numbers the business feels": ("Reliability and unit cost — the numbers the business feels", "The two currencies of the estate, read side by side on one console"),
            "The domain reference architecture — estate as one system": ("The domain reference architecture — estate as one system", "From golden path scaffold to mission-critical tier in one governed map"),
            "The estate on one screen — reliability and economics together": ("The estate on one screen — reliability and economics together", "SLOs, unit costs and change posture as one reading"),
            "Change failure and MTTR by service tier — the reliability bands": ("Change failure and MTTR by service tier — the reliability bands", "Where the estate actually fails, and what the bands say about it"),
            "Sector depth — where the platform practice runs deepest today": ("Sector depth — where the platform practice runs deepest today", "Twelve-industry lens with targets we sign against and the sector briefs behind them"),
            "How estate engagements run": ("How estate engagements run", "Baseline, sign, deploy, allocate — the sequencing that sticks"),
            "Estate release gates — the domain contract": ("Estate release gates — the domain contract", "The evidence each gate demands; nothing advances on narrative"),
        },
    },

    "services_cloud-edge-platform-engineering_cloud-native-modernization": {
        "archsubs": {
            "Refactor ladder": "strangler steps, exit gates",
            "State externalization": "session + data moved first",
            "Container platform": "pinned bases, signed",
            "Managed services": "used where parity holds",
            "Posture proof": "drift reverted, logged",
            "Retirement gate": "consumer count zero",
        },
        "badges": [
            ("Retirements per wave target", "94%"),
            ("Dual-run parity gate", "before cutover"),
            ("Legacy estate shrinkage", "measured monthly"),
        ],
        "deep": {
            "h2": "Retirement is the deliverable",
            "sub": "Strangler waves with exit gates — why modernization is measured by what it turns off",
            "paras": [
                "Modernization programs stall halfway because they measure migration counts instead of retirements: a thousand workloads 'moved' and a legacy estate that never shrinks is a cost increase wearing a progress bar. The discipline runs strangler waves — each wave takes a bounded slice, externalizes its state first (sessions, data, queues), routes traffic through the strangler façade with dual-run parity checks, and ends at a retirement gate: the legacy component is switched off when its consumer count reaches zero and the parity evidence holds for the agreed window. The retirement ledger is the headline metric, reviewed monthly, with the legacy estate's shrinkage in workloads and run-rate cost.",
                "Behavior change is the hard wave. Teams must adopt the container platform's golden path, and the path has to be genuinely faster than the old way — one command to scaffold, compliance built in, deployment to production on the path in under a day. Posture proof closes the loop: drift from the golden path reverts automatically with a log entry, so the estate converges instead of diverging.",
            ],
            "bullets": [
                ("State externalization first", "Sessions, data and queues move before compute — the cutover risk lives in state."),
                ("Dual-run parity gates", "Old and new run against the same taps; parity evidence before cutover."),
                ("Retirement gate per wave", "Consumer count zero plus parity window — then the legacy component dies."),
                ("Golden path by proof", "The scaffold must beat the old way on speed, or adoption is theater."),
            ],
        },
        "heads": {
            "Modernization is a behavior change wearing a container costume": ("Modernization is a behavior change — the container is the costume", "Waves, strangler steps and retirement gates — measured by what turns off"),
            "Four failure modes that strand modernization halfway": ("Four failure modes that strand modernization halfway", "State blindness, parity theater, path bypass, retirement deferral"),
            "Reference architecture — waves, strangler, retirement": ("Reference architecture — waves, strangler, retirement", "The ladder from VM to retired legacy, with gates at each rung"),
            "One workload, from VM to resilient service": ("One workload, from VM to resilient service", "The move, step by step, with evidence at each step"),
            "The modernization console — retirement as the headline": ("The modernization console — retirement as the headline", "Retirements, parity results and legacy shrinkage on one surface"),
            "Cost per workload across the modernization waves": ("Cost per workload across the modernization waves", "The economics of each wave, before and after"),
            "Modernization defaults — and documented deviations": ("Modernization defaults — and documented deviations", "The default ladder, and where we sign deviations"),
            "Modernization release gates — evidence before each wave": ("Modernization release gates — evidence before each wave", "What a wave must prove before traffic moves"),
            "What the engineering teams inherit": ("What the engineering teams inherit", "Paths, runbooks, retirement ledger and the wave calendar"),
            "Waves with exit criteria, week by week": ("Waves with exit criteria, week by week", "The cadence from baseline to retirement"),
            "Integration surface — the legacy estate and its consumers": ("Integration surface — the legacy estate and its consumers", "Who still calls the legacy, and how that list shrinks"),
            "Resilience governance overlay": ("Resilience governance overlay", "Failure domains, drills and the posture proof per service"),
        },
    },

    "services_cloud-edge-platform-engineering_edge-computing-infrastructure": {
        "archsubs": {
            "Edge OS & runtime": "atomic updates, auto-revert",
            "Hardware abstraction": "fleet heterogeneity absorbed",
            "Store-and-forward": "survives partitions",
            "Release trains": "staged waves, canary first",
            "Heartbeat SLOs": "site silence pages",
        },
        "badges": [
            ("Partition survival", "by design"),
            ("Silent-site detection", "heartbeat SLO"),
            ("Fleet update success", "≥99%"),
        ],
        "deep": {
            "h2": "Design for the partition, not the datacenter",
            "sub": "Store-and-forward, autonomy budgets and heartbeat SLOs — the failure model that makes edge real",
            "paras": [
                "Edge estates fail differently from clouds: sites partition, devices go silent, and the fleet is heterogeneous by construction — three generations of gateways running three firmware lines. The design that survives assumes the partition as the normal case: store-and-forward queues at every site with bounded local autonomy (hours to days, priced per site), idempotent replay on reconnect, and a hardware-abstraction layer so the same release train rolls across the heterogeneous fleet. Atomic OS updates with automatic revert mean a bad rollout self-heals instead of bricking a region.",
                "Observability inverts at the edge: you cannot watch a thousand sites, so sites report heartbeats and the SLO is on silence — a site that stops reporting pages within its heartbeat budget rather than when a customer notices. Release trains stage waves with canary sites first, and the console treats sites as individuals (fleet averages hide the one dairy depot that matters). The fleet-security overlay keeps identity per site, signed artifacts end to end, and a kill path that revokes a site without touching the fleet.",
            ],
            "bullets": [
                ("Partition as normal case", "Store-and-forward with priced autonomy budgets per site."),
                ("Heartbeat SLOs on silence", "A silent site pages inside its budget — before a customer notices."),
                ("One release train, heterogeneous fleet", "Hardware abstraction makes the same train roll everywhere."),
                ("Atomic updates, auto-revert", "Bad rollouts self-heal; the fleet never bricks."),
            ],
        },
        "heads": {
            "The edge is defined by its failures: partitions, silence and heterogeneity": ("The edge is defined by its failures — partitions, silence, heterogeneity", "Store-and-forward, heartbeat SLOs and release trains built for the failure model"),
            "Four failure modes that make edge estates fragile": ("Four failure modes that make edge estates fragile", "Unbounded autonomy, silent sites, firmware drift, fleet-wide rollouts"),
            "Reference architecture — regional clusters with store-and-forward": ("Reference architecture — regional clusters with store-and-forward", "The topology from site to regional cluster to cloud"),
            "One partitioned site, from isolation to reconciliation": ("One partitioned site, from isolation to reconciliation", "The recovery path with idempotent replay on reconnect"),
            "The edge console — sites as individuals": ("The edge console — sites as individuals", "Per-site posture, not fleet averages"),
            "Fleet behavior across rollout waves": ("Fleet behavior across rollout waves", "Canary-first trains and the wave metrics"),
            "Edge defaults — and documented deviations": ("Edge defaults — and documented deviations", "The default stack, and the deviations we sign"),
            "Edge release gates — evidence before a wave": ("Edge release gates — evidence before a wave", "Autonomy tests and canary evidence before fleet rollout"),
            "What the fleet operations team inherits": ("What the fleet operations team inherits", "Consoles, train calendar, autonomy budgets and the kill path"),
            "Waves and windows, week by week": ("Waves and windows, week by week", "The rollout cadence against site maintenance windows"),
            "Integration surface — sites, backends and the device fleet": ("Integration surface — sites, backends and the device fleet", "What talks to what, across the store-and-forward seam"),
            "Fleet-security governance overlay": ("Fleet-security governance overlay", "Per-site identity, signed artifacts and the site kill path"),
        },
    },
}

PAGES["services_cloud-edge-platform-engineering_finops-sustainable-computing"] = {
    "archsubs": {
        "Tag enforcement": "untagged = un-deployable",
        "Allocation engine": "shared cost, priced fairly",
        "Unit-economics registry": "cost per business unit",
        "Rightsizing engine": "recommendations with owners",
        "Waste ledger": "zombies, listed monthly",
        "Budget gates": "forecasts gate commitments",
    },
    "badges": [
        ("Allocation coverage target", "95%"),
        ("Waste reclaims per quarter", "tracked"),
        ("Unit cost trend", "down and right"),
    ],
    "deep": {
        "h2": "Allocation creates accountability",
        "sub": "From meters to unit economics — the discipline that turns cloud spend into managed cost",
        "paras": [
            "Cloud bills stay foggy because nobody is accountable for shared cost and nothing gates commitments. The discipline allocates first: tag enforcement makes untagged workloads un-deployable in CI, the allocation engine prices shared cost fairly (with the formula documented, because allocation disputes are formula disputes), and every workload lands in the unit-economics registry with a named owner and a business metric — cost per transaction, per shipment, per student, per claim. The console reads unit cost as the headline, because a 20% discount on a 40% oversized estate is not savings; a downward unit-cost curve is.",
            "The waste ledger then makes the invisible visible: zombie storage, idle clusters, over-provisioned environments — listed monthly with owners and reclaim dates, reviewed in the same meeting as the budget gates. Commitment purchases are gated by forecast evidence and headroom analysis rather than vendor calendars, and the sustainability overlay carries the energy story: carbon per unit of work alongside dollars, because both are resources the estate spends.",
        ],
        "bullets": [
            ("Untaggable = undeployable", "Tag enforcement in CI; allocation starts at deploy time, not invoice time."),
            ("Unit cost as headline", "Cost per business unit of work, owner-named, trended monthly."),
            ("Waste ledger with owners", "Zombies listed, owned and reclaimed on a date — not shuffled into 'savings'."),
            ("Evidence-gated commitments", "Forecasts and headroom analysis gate purchases; vendor calendars do not."),
        ],
    },
    "heads": {
        "Nobody spends someone else's money carefully — allocate it first": ("Nobody spends someone else's money carefully — allocation comes first", "Tag enforcement, fair formulas and unit economics with named owners"),
        "Four failure modes that keep cloud bills foggy": ("Four failure modes that keep cloud bills foggy", "Untagged estates, unfair allocation, ownerless waste, calendar-driven commitments"),
        "Reference architecture — from meters to unit economics": ("Reference architecture — from meters to unit economics", "Meters, allocation, registry and gates as one flow"),
        "One invoice line, attributed to a decision": ("One invoice line, attributed to a decision", "How every line traces to an owner and a metric"),
        "The FinOps console — unit cost as the headline": ("The FinOps console — unit cost as the headline", "Unit curves, waste and commitment posture on one surface"),
        "Unit-cost trajectory across the workloads": ("Unit-cost trajectory across the workloads", "The curves the business reviews, not the invoice totals"),
        "FinOps defaults — and documented deviations": ("FinOps defaults — and documented deviations", "The default practices, and where we sign deviations"),
        "FinOps release gates — evidence before commitments": ("FinOps release gates — evidence before commitments", "What the forecast must show before spend is locked"),
        "What the FinOps practice inherits": ("What the FinOps practice inherits", "Registry, formulas, waste cadence and the gate calendar"),
        "Allocation to zombies, week by week": ("Allocation to zombies, week by week", "The operating rhythm from deploy-time tags to reclaim dates"),
        "Integration surface — billing, tagging and the finance systems": ("Integration surface — billing, tagging and the finance systems", "Where meters meet ledgers, typed throughout"),
        "Sustainability governance overlay": ("Sustainability governance overlay", "Carbon per unit of work — the second currency, measured"),
    },
}

PAGES["services_cloud-edge-platform-engineering_high-performance-mission-critical"] = {
    "archsubs": {
        "Signed SLAs": "business-signed tiers",
        "Hop budget table": "ms per hop, budgeted",
        "Redundancy fabric": "failure domains, tested",
        "Capacity model": "load-tested headroom",
        "Load program": "peak rehearsals, quarterly",
    },
    "badges": [
        ("Failover evidence", "timed, every drill"),
        ("Tail latency p99.9", "budgeted"),
        ("Peak rehearsal", "quarterly"),
    ],
    "deep": {
        "h2": "Latency budgets are contracts, not aspirations",
        "sub": "Hop tables, tail discipline and timed failovers — the engineering of mission-critical tiers",
        "paras": [
            "Mission-critical tiers earn the name through arithmetic: the latency budget is allocated down the stack as a hop table — every network hop, service call and queue wait gets milliseconds, and the sum must meet the signed SLA with headroom. Tail discipline is the craft: p99.9 is designed for explicitly (hedged requests, admission control, sharded hot paths), because averages lie about the requests that actually page someone. Redundancy is tested, not assumed — failure domains are drilled with timed failovers, and the drill evidence is the release gate that carries traffic onto the tier.",
            "Capacity is a model, not a feeling: the load program rehearses peak shapes quarterly against production-shaped data, with headroom targets signed per tier. The console reads availability with its tail — the p99.9 line lives next to the uptime number — and the budget review asks the only question that matters: which hop is eating the tail this month, and what is the fix with an owner and a date.",
        ],
        "bullets": [
            ("Hop budget table", "Milliseconds allocated per hop; the sum must fit the signed SLA."),
            ("Tail designed explicitly", "Hedged requests, admission control and hot-path sharding for p99.9."),
            ("Timed failover drills", "Redundancy is evidence when the failover is clocked and archived."),
            ("Quarterly peak rehearsals", "Production-shaped load against signed headroom targets."),
        ],
    },
    "heads": {
        "Mission-critical is a budget discipline, not a server label": ("Mission-critical is a budget discipline — not a server label", "Hop tables, tail engineering and timed failovers under signed SLAs"),
        "Four failure modes that make high availability paper": ("Four failure modes that make high availability paper", "Untested redundancy, ignored tails, unmodeled capacity, unowned budgets"),
        "Reference architecture — the budgeted mission-critical tier": ("Reference architecture — the budgeted mission-critical tier", "SLAs, hop tables, redundancy fabric and the load program as one tier"),
        "One failover, timed and evidenced": ("One failover, timed and evidenced", "The drill as an engineering artifact, archived as evidence"),
        "The mission-critical console — availability with its tail": ("The mission-critical console — availability with its tail", "p99.9 next to uptime, with the hop that eats the tail named"),
        "Latency budget allocation down the stack": ("Latency budget allocation down the stack", "The table, the sums and the headroom policy"),
        "Performance defaults — and documented deviations": ("Performance defaults — and documented deviations", "The default tier patterns, and where we sign deviations"),
        "Tier release gates — evidence before traffic": ("Tier release gates — evidence before traffic", "Drill evidence and capacity proof before production load"),
        "What the mission-critical platform team inherits": ("What the mission-critical platform team inherits", "Tables, drills, capacity models and the review cadence"),
        "Budgets to drills, week by week": ("Budgets to drills, week by week", "The build sequence from SLA signing to drill certification"),
        "Integration surface — network, data and the client estate": ("Integration surface — network, data and the client estate", "Every hop the budget pays for, honestly named"),
        "Tail-governance overlay": ("Tail-governance overlay", "The standing review that hunts the p99.9 regressions"),
    },
}

PAGES["services_cloud-edge-platform-engineering_hybrid-multicloud-architecture"] = {
    "archsubs": {
        "Placement engine": "policy-scored, not vibes",
        "Interconnect fabric": "egress-aware topology",
        "Federated identity": "one IdP, per-cloud SPs",
        "Unified policy model": "one policy, per-cloud output",
    },
    "badges": [
        ("Placement decisions", "policy-scored"),
        ("Egress surprises", "0 tolerated"),
        ("Parity target", "one policy everywhere"),
    ],
    "deep": {
        "h2": "Placement is a policy decision, not a meeting",
        "sub": "The unified policy model — one source of truth compiled to each cloud's controls",
        "paras": [
            "Hybrid estates go tribal when each cloud has its own policies, identity quirks and placement folklore — and the vendors are structurally uninterested in fixing it. The countermeasure is a unified policy model: placement rules, security controls and residency constraints written once, compiled to each cloud's native enforcement (IAM, guardrails, network policy), and diffed continuously so parity is measured, not claimed. The placement engine scores workloads against the policy — data gravity, residency, latency, unit cost, exit cost — and records the decision with its reasons, because a placement made in a meeting is unappealable.",
            "The interconnect fabric is the second discipline: egress-aware topology designed before the first cross-cloud call, because egress economics punish retrofit. Federated identity keeps one IdP with per-cloud service providers, and the identity-seam overlay audits token lifetime and trust drift monthly — the seam between clouds is where hybrid estates actually fail.",
        ],
        "bullets": [
            ("One policy, compiled everywhere", "Written once, compiled to native controls per cloud, diffed for parity."),
            ("Placement with reasons", "Policy-scored decisions recorded with the evidence, appealable like code."),
            ("Egress-aware topology", "Interconnect designed before cross-cloud calls exist, not after the bill."),
            ("One identity plane", "Federated IdP with per-cloud SPs; the seam is audited monthly."),
        ],
    },
    "heads": {
        "Multicloud is an operating-model problem the vendors will not solve for you": ("Multicloud is an operating-model problem — vendors will not solve it for you", "Unified policy, policy-scored placement and an egress-aware fabric"),
        "Four failure modes that make hybrid estates tribal": ("Four failure modes that make hybrid estates tribal", "Per-cloud folklore, unappealable placement, egress surprises, identity seams"),
        "Reference architecture — placement by policy, patterns by default": ("Reference architecture — placement by policy, patterns by default", "Policy model, placement engine and fabric as one structure"),
        "One workload, placed and moved without a rewrite": ("One workload, placed and moved without a rewrite", "The move mechanics with the parity evidence"),
        "The multicloud console — parity as the headline": ("The multicloud console — parity as the headline", "Policy diffs, placement records and egress posture on one surface"),
        "Placement and egress economics across the estate": ("Placement and egress economics across the estate", "The numbers that decide where workloads live"),
        "Multicloud defaults — and documented deviations": ("Multicloud defaults — and documented deviations", "The default patterns, and where we sign deviations"),
        "Multicloud release gates — evidence before placement": ("Multicloud release gates — evidence before placement", "What a placement decision must carry before execution"),
        "What the platform architecture team inherits": ("What the platform architecture team inherits", "Policy model, placement records and the parity cadence"),
        "Policies in order, week by week": ("Policies in order, week by week", "The build sequence from policy model to compiled enforcement"),
        "Integration surface — clouds, identity and the data estate": ("Integration surface — clouds, identity and the data estate", "The seams, named and audited"),
        "Identity-seam governance overlay": ("Identity-seam governance overlay", "Token lifetimes, trust drift and the monthly audit"),
    },
}

PAGES["services_cloud-edge-platform-engineering_platform-engineering-devex"] = {
    "archsubs": {
        "Platform product team": "roadmap, adoption-owned",
        "Service scaffold": "golden path in one command",
        "Security path": "compliance in the scaffold",
        "DevEx funnel": "time-to-first-deploy tracked",
    },
    "badges": [
        ("Golden-path adoption target", "72%"),
        ("Time-to-first-deploy", "under 1 day"),
        ("Path as product", "versioned + supported"),
    ],
    "deep": {
        "h2": "A golden path is a product with a roadmap",
        "sub": "Adoption economics, scaffold contracts and the DevEx funnel — why paths win or get bypassed",
        "paras": [
            "Internal platforms become mandatory-but-bypassed when they are built as infrastructure rather than products: no roadmap, no support promise, no telemetry on where developers drop off. The discipline treats every path as a product — a versioned scaffold contract ('one command to a compliant service'), a support SLO on the path itself, and a DevEx funnel that measures time-to-first-deploy, time-to-production and the step where engineers fork off the path. Fork-off analysis is the honesty mechanism: engineers bypass for reasons, and every major fork reason becomes a backlog item with a date.",
            "The security path is built into the scaffold rather than audited afterwards — compliance, posture and evidence generation ride the default — and the platform team's roadmap is published and adoption-owned: success is measured in path share of production deploys, not tickets closed. The console reads adoption with its reasons; the governance overlay keeps the product discipline honest (roadmaps, deprecations with notice, version contracts), because infrastructure that behaves like a product earns the adoption that infrastructure-by-mandate never does.",
        ],
        "bullets": [
            ("Path as product", "Roadmap, support SLO, version contract — the platform team sells, not polices."),
            ("Scaffold contracts", "One command to a compliant service; compliance rides the default."),
            ("DevEx funnel, measured", "Time-to-first-deploy and fork-off reasons drive the backlog."),
            ("Adoption as the KPI", "Path share of production deploys is the platform's number."),
        ],
    },
    "heads": {
        "Adoption is the metric; everything else is the product roadmap": ("Adoption is the metric — everything else is the roadmap", "Paths as products, scaffold contracts and the DevEx funnel"),
        "Four ways internal platforms become mandatory-but-bypassed": ("Four ways internal platforms become mandatory-but-bypassed", "Infrastructure framing, support vacuum, compliance tax, unmeasured forks"),
        "Reference architecture — golden paths as versioned APIs": ("Reference architecture — golden paths as versioned APIs", "Scaffolds, security path and the funnel as one product surface"),
        "One service, from scaffold to production on the path": ("One service, from scaffold to production on the path", "The journey a developer actually experiences, timed"),
        "The platform console — adoption with its reasons": ("The platform console — adoption with its reasons", "Path share, fork-off reasons and funnel steps, live"),
        "Delivery velocity on and off the path": ("Delivery velocity on and off the path", "The comparison that sells the path better than any mandate"),
        "Platform defaults — and documented deviations": ("Platform defaults — and documented deviations", "The default path set, and where we sign deviations"),
        "Platform release gates — evidence before a path ships": ("Platform release gates — evidence before a path ships", "What a path must prove before teams adopt it"),
        "What the platform product team inherits": ("What the platform product team inherits", "Roadmaps, contracts, telemetry and the adoption baseline"),
        "Paths as products, sprint by sprint": ("Paths as products, sprint by sprint", "The product cadence behind the scaffold"),
        "Integration surface — repos, CI and the runtime estate": ("Integration surface — repos, CI and the runtime estate", "What the scaffold wires, end to end"),
        "Platform governance — product discipline for infrastructure": ("Platform governance — product discipline for infrastructure", "Deprecations, version contracts and honest sunsets"),
    },
}

PAGES["services_cloud-edge-platform-engineering_sre-reliability-engineering"] = {
    "archsubs": {
        "SLO documents": "signed per service",
        "Budget calculator": "burn rate, live",
        "Release gating": "budget-exhaust = freeze",
        "Chaos program": "monthly, scoped drills",
        "Incident command": "named roles, trained",
        "Blameless review": "actions with owners",
    },
    "badges": [
        ("SLO-signed services", "target 100%"),
        ("Budget-gated releases", "automatic"),
        ("Drills", "monthly, scoped"),
    ],
    "deep": {
        "h2": "Error budgets convert reliability into a currency",
        "sub": "SLOs, budget-gated releases and incident craft — the system that makes reliability tradable",
        "paras": [
            "Reliability programs become decorative when SLOs are aspirations: published, admired and gating nothing. The working system treats the error budget as currency — every service carries a signed SLO document (what is measured, by whom, at what threshold), the calculator tracks burn live, and budget exhaustion freezes releases automatically in CI, converting the reliability-versus-velocity argument from a meeting into a number. The freeze is the discipline: teams may buy budget back with reliability work, and the trade is visible to everyone.",
            "Incident craft is the second half: incident command with named roles trained before the page, chaos drills monthly and scoped (a drill that takes the estate down teaches nothing but fear), and blameless reviews whose actions carry owners and dates — reviewed in the same meeting as the budget, because actions that never close are how programs become decorative. The console reads SLO adherence, budget burn and drill results; the review reads trends, not anecdotes.",
        ],
        "bullets": [
            ("Signed SLO documents", "Every service: what, who, threshold — signed by the business owner."),
            ("Budget-gated releases", "Exhaustion freezes deploys in CI; the trade is a number, not a meeting."),
            ("Scoped chaos, monthly", "Drills sized to teach, rehearsed against production shapes."),
            ("Blameless with owners", "Every review action carries a name and a date, reviewed to closure."),
        ],
    },
    "heads": {
        "Reliability is a budget conversation, not an uptime aspiration": ("Reliability is a budget conversation — not an uptime aspiration", "Signed SLOs, budget-gated releases and incident craft that closes its actions"),
        "Four ways SRE programs become decorative": ("Four ways SRE programs become decorative", "Unsigned SLOs, ungated budgets, unscoped chaos, ownerless reviews"),
        "Reference architecture — error budgets from SLO to release gate": ("Reference architecture — error budgets from SLO to release gate", "Documents, calculator, gating and drills as one system"),
        "One budget burn, from spike to freeze": ("One budget burn, from spike to freeze", "The lifecycle of a burn and what it triggers"),
        "The SRE console — the numbers the review reads": ("The SRE console — the numbers the review reads", "Adherence, burn and drills on one surface"),
        "SLO adherence and budget burn across the quarters": ("SLO adherence and budget burn across the quarters", "The trend line that predicts the next freeze"),
        "SRE defaults — and documented deviations": ("SRE defaults — and documented deviations", "The default practices, and where we sign deviations"),
        "Reliability release gates — evidence before traffic": ("Reliability release gates — evidence before traffic", "What a service must prove before it carries load"),
        "What the reliability team inherits": ("What the reliability team inherits", "SLO docs, calculators, drill calendar and the review cadence"),
        "SLOs in order, week by week": ("SLOs in order, week by week", "The build sequence from first SLO to estate coverage"),
        "Integration surface — observability, CI and paging": ("Integration surface — observability, CI and paging", "Where the budget touches the toolchain"),
        "Incident-craft governance overlay": ("Incident-craft governance overlay", "Command roles, drill scoping and the closure discipline"),
    },
}
