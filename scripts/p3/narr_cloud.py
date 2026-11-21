"""narr_cloud — narrative layer for the Cloud, Edge & Platform Engineering domain."""

HUB = {
    "hero": ("Cloud, Edge & Platform Engineering runs the estate as an economic and reliability "
             "system: hybrid placement by policy, golden paths that carry SLOs and budgets by "
             "default, edge fleets that survive partitions, and unit costs that fall on a "
             "signed trend line — across clouds, without tribal dialects."),
    "s_practices": "Seven practices from golden paths to mission-critical tiers",
    "deep": [
        ("The platform conversation changed: engineering leaders no longer buy infrastructure, "
         "they buy change failure rates and unit costs. The seven practices here are managed on "
         "exactly those numbers — SLO adherence, path adoption, placement policy coverage, cost "
         "per workload — because those are the numbers the business actually experiences."),
        ("The edge adds a discipline the data center never taught: partition-tolerant behavior, "
         "store-and-forward resilience, fleet heterogeneity at scale and sites that fail "
         "silently. The practices treat edge as a first-class estate with its own gates, not "
         "as a cloud region with worse networking."),
    ],
    "s_deep": "Reliability and unit cost: the numbers the business feels",
    "s_arch": "The domain reference architecture — estate as one system",
    "arch_lead": ("Placement policy decides where workloads run, golden paths carry how they "
                  "deploy, SRE discipline decides when they change, and FinOps prices what it "
                  "all costs — one operating model across clouds, on-prem and the edge, with "
                  "drift caught by monitors instead of by incidents."),
    "s_dash": "The estate on one screen — reliability and economics together",
    "dash_lead": ("SLO adherence, change failure rate, path adoption and unit cost trend — the "
                  "four tiles the engineering leadership review reads weekly, rendered as they "
                  "appear there."),
    "dash_note": ("Reference console — estate targets; every tile is owned by a named team with "
                  "an evidence link, because shared dashboards breed shared blame."),
    "s_chart": "Change failure and MTTR by service tier — the reliability bands",
    "chart_lead": ("Radar profile across six gated axes; the posture-to-target gap is the funded "
                   "engineering program for the next two quarters, re-scored at every gate "
                   "review."),
    "chart_override": {
        "variant": "bar",
        "title": "Change failure rate and MTTR by service tier — design targets",
        "cats": ["Tier-0 mission critical", "Tier-1 customer facing", "Tier-2 internal", "Tier-3 batch & backoffice"],
        "series": [
            ("Change failure rate %", [4.5, 6.2, 8.0, 11.0]),
            ("MTTR (minutes)", [22, 31, 45, 90]),
        ],
        "unit": "",
        "caption": "Reference bands by service tier — the reliability bar scales with blast radius, and the gates enforce the pairing.",
    },
    "chart_note": None,
    "s_evidence": "Sector depth — where the platform practice runs deepest today",
    "evidence_lead": ("Retail chains buy edge resilience, banks buy mission-critical tiers, SaaS "
                      "companies buy developer velocity. The bars count published sub-industry "
                      "briefs on this site — the honest map of sector depth."),
    "evidence_chart_title": "Cloud, Edge & Platform Engineering — published sub-industry briefs by sector",
    "explorer_title": "Your estate, your sector — pick the industry and see the plan",
    "explorer_intro": ("A grid operator's edge estate and a retailer's store fleet are different "
                       "problems wearing the same protocols. Select your sector: the panel shows "
                       "the entry problem, the deliverables, the targets and the sector brief."),
    "plays": [
        "Golden paths as versioned APIs — SLOs and budgets carried by default",
        "One operating model across clouds, on-prem and edge, with policy parity",
        "Unit economics per workload with FinOps that has teeth",
    ],
    "flagships": ["technology-saas", "banking-financial-services", "telecom-media"],
    "s_engage": "How estate engagements run",
    "engage": [
        ["Diagnostic — two weeks", "Estate mapped by tier, SLOs and unit costs baselined, the gate model scored — with the platform-reuse opportunity priced before anything is built."],
        ["Provability sprint — four weeks", "One service family runs a fund-or-kill slice: golden path adoption, change failure rate and unit cost on your real workloads."],
        ["Build — ten to fourteen weeks", "Paths, placement policy and SLO machinery built to the reference architecture, with the console live from week two."],
        ["Industrialize — ongoing", "Quarterly re-baselines, path version reviews, FinOps trends with finance — and the drift monitors that keep the operating model honest."],
    ],
    "s_gates": "Estate release gates — the domain contract",
    "cta": ("Bring the workload whose unit cost nobody can state and whose SLO nobody signed. "
            "The two-week diagnostic will baseline both — and price what golden paths would "
            "change on your estate."),
}

PAGES = {

"platform-engineering-devex": {
    "hero": ("The platform as a product with developers as customers: golden paths published as "
             "versioned APIs, scaffolds that carry SLOs and budgets by default, bypass reasons "
             "logged and answered — adoption earned through experience, never mandated."),
    "s1_h": "Adoption is the metric; everything else is the product roadmap",
    "s1_close": ("Below: the failure modes that make internal platforms mandatory-but-bypassed, "
                 "the reference architecture of paths-as-products, and the console that tracks "
                 "adoption honestly — including why people leave the path."),
    "s2_h": "Four ways internal platforms become mandatory-but-bypassed",
    "s2_lead": ("Each failure mode drives a quiet fork around the platform — the countermeasures "
                "log the bypass reasons and fix the platform until leaving is harder than "
                "staying."),
    "arch_h": "Reference architecture — golden paths as versioned APIs",
    "arch_lead": ("A path is a product surface: versioned, documented, owned, carrying SLOs and "
                  "budget defaults, deprecated on a schedule. Scaffolds instantiate paths, not "
                  "templates — so every new service is observable and costed before its first "
                  "commit."),
    "flow_h": "One service, from scaffold to production on the path",
    "flow_lead": ("From scaffold instantiation through CI with SLO defaults, budget wiring, "
                  "progressive delivery and the review that logs any manual step — including "
                  "the bypass fork and what pulled the team off the path."),
    "dash_h": "The platform console — adoption with its reasons",
    "dash_lead": ("Repo-to-prod median, path adoption and logged bypass reasons — the three "
                  "numbers that run the platform backlog, because every bypass reason is a "
                  "feature request the product owes its customers."),
    "dash_note": ("Reference console — platform targets; bypass reasons are triaged monthly and "
                  "the top two become the roadmap, not a wall of shame."),
    "chart_h": "Delivery velocity on and off the path",
    "chart_lead": ("Lead time and change failure rate for teams on-path versus off-path — the "
                   "comparison that makes the platform's value statement unnecessary, because "
                   "the numbers argue for it."),
    "stack_h": "Platform defaults — and documented deviations",
    "stack_lead": ("Defaults favor paved-road opinionation with escape hatches over both "
                   "free-for-alls and mandates; deviation triggers are written because each one "
                   "is a bet on where the fork risk actually lives."),
    "gates_h": "Platform release gates — evidence before a path ships",
    "artifacts_h": "What the platform product team inherits",
    "timeline_h": "Paths as products, sprint by sprint",
    "integ_h": "Integration surface — repos, CI and the runtime estate",
    "integ_lead": ("Golden paths touch repos, pipelines and runtimes; these contracts define "
                   "what a path carries by default and where teams may legitimately diverge."),
    "controls_h": "Platform governance — product discipline for infrastructure",
    "controls_lead": ("Paths have roadmaps, versions and deprecation dates like any product; "
                      "the governance that keeps the platform credible is product management, "
                      "not enforcement memos."),
    "controls_note": ("Deprecation is enforced by migration support: an old path version is "
                      "removed only when its last consumer has a scheduled migration, and the "
                      "removal note includes the helping team's name."),
    "cta": ("Count the services created last quarter and ask which ran the paved road. The "
            "diagnostic will score adoption with bypass reasons attached — and turn the top "
            "two into the platform roadmap."),
    "flagships": ["technology-saas", "telecom-media", "banking-financial-services"],
    "plays": [
        "Golden paths as versioned APIs with SLO and budget defaults",
        "Bypass reasons logged, triaged and answered on the roadmap",
        "Scaffolds that make new services observable and costed before first commit",
    ],
},

"sre-reliability-engineering": {
    "hero": ("SLOs with teeth: error budgets that actually gate releases, chaos exercises that "
             "prove recovery instead of assuming it, and incident craft that turns every "
             "postmortem into a reliability deposit — not a lesson plan nobody reads."),
    "s1_h": "Reliability is a budget conversation, not an uptime aspiration",
    "s1_close": ("Below: the failure modes that make SRE programs decorative, the reference "
                 "architecture of budget-gated delivery, and the console that keeps the "
                 "honest numbers."),
    "s2_h": "Four ways SRE programs become decorative",
    "s2_lead": ("Every one of these ends with 'the SLO dashboard is green but the customer is "
                "angry' — the countermeasures bind budgets to release decisions and alerts to "
                "user pain."),
    "arch_h": "Reference architecture — error budgets from SLO to release gate",
    "arch_lead": ("The machinery is a loop: SLOs measured from user experience, error budgets "
                  "computed continuously, release gates that hard-stop when budgets exhaust, "
                  "and chaos exercises that verify the recovery paths the runbooks promise."),
    "flow_h": "One budget burn, from spike to freeze",
    "flow_lead": ("From the error-budget spike through gate thresholds, the release freeze, the "
                  "reliability work that earns the budget back and the chaos drill that "
                  "validates recovery — including where heroics are declined, on the record."),
    "dash_h": "The SRE console — the numbers the review reads",
    "dash_lead": ("SLO adherence, change failure rate and MTTR — three numbers, one story: "
                  "whether the estate is getting more reliable while shipping faster, or just "
                  "shipping."),
    "dash_note": ("Reference console — SRE targets; budget exhaustion is enforced by the gate, "
                  "and overrides are signed at director level, on the record."),
    "chart_h": "SLO adherence and budget burn across the quarters",
    "chart_lead": ("Adherence and burn rate per service tier across quarters — the shape that "
                   "shows where reliability investment pays back and where the tiering itself "
                   "is wrong."),
    "stack_h": "SRE defaults — and documented deviations",
    "stack_lead": ("Defaults favor user-journey SLOs and budget-gated releases over "
                   "machine-level SLAs; deviation triggers are written because each one "
                   "disconnects the metric from the pain."),
    "gates_h": "Reliability release gates — evidence before traffic",
    "artifacts_h": "What the reliability team inherits",
    "timeline_h": "SLOs in order, week by week",
    "integ_h": "Integration surface — observability, CI and paging",
    "integ_lead": ("The machinery spans observability, CI and the paging path; these contracts "
                   "carry SLO state into release gates without manual interpretation."),
    "controls_h": "Incident-craft governance overlay",
    "controls_lead": ("Postmortems carry owners, dates and re-test plans; chaos drills re-test "
                      "the last round's findings first — the reliability program compounds by "
                      "closing loops, not by accumulating documents."),
    "controls_note": ("Heroic recovery is celebrated once and then engineered away: any fix "
                      "that required a human with unusual context becomes a runbook entry, a "
                      "detection or an automation in the next sprint — and the ledger proves it."),
    "cta": ("Ask which release was frozen by an error budget last quarter. If none, the gate is "
            "decorative — bring the SLO inventory to a briefing and we will wire the teeth."),
    "flagships": ["technology-saas", "telecom-media", "manufacturing"],
    "plays": [
        "User-journey SLOs with error budgets that hard-stop releases",
        "Chaos exercises that prove the recovery paths runbooks promise",
        "Postmortems as reliability deposits — findings re-tested by the next drill",
    ],
},

"hybrid-multicloud-architecture": {
    "hero": ("One operating model across clouds and on-premises: workload placement by signed "
             "policy, portable patterns instead of dialects, egress budgets that hold, and "
             "identity seams that work — so the estate behaves like one system, not three "
             "vendors' territories."),
    "s1_h": "Multicloud is an operating-model problem the vendors will not solve for you",
    "s1_close": ("Below: the failure modes that make hybrid estates tribal, the reference "
                 "architecture of placement by policy, and the console that proves parity."),
    "s2_h": "Four failure modes that make hybrid estates tribal",
    "s2_lead": ("Each of these costs money or uptime in ways nobody attributes — the "
                "countermeasures make placement, parity and egress contractual rather than "
                "folklore."),
    "arch_h": "Reference architecture — placement by policy, patterns by default",
    "arch_lead": ("Placement is decided by signed policy — data gravity, latency, cost and "
                  "regulation — and enforced at deploy time; the pattern library stays portable "
                  "so a workload's second cloud is a configuration, not a rewrite."),
    "flow_h": "One workload, placed and moved without a rewrite",
    "flow_lead": ("From placement evaluation through policy enforcement, portable-pattern "
                  "deployment and the egress accounting — including the drift monitor that "
                  "catches manual divergence between clouds."),
    "dash_h": "The multicloud console — parity as the headline",
    "dash_lead": ("Placement policy coverage, policy parity and egress budget adherence — the "
                  "three numbers that decide whether the estate is one system or three "
                  "vendors' territories with a shared invoice."),
    "dash_note": ("Reference console — multicloud targets; egress surprises are attributed to "
                  "the workload and the architecture decision, retroactively and publicly."),
    "chart_h": "Placement and egress economics across the estate",
    "chart_lead": ("Workload distribution and egress spend by placement policy — the shape that "
                   "shows where data gravity is quietly taxing the business and which policies "
                   "are paying off."),
    "stack_h": "Multicloud defaults — and documented deviations",
    "stack_lead": ("Defaults favor portable patterns with policy-enforced placement over "
                   "per-cloud excellence; deviation triggers are written because each one "
                   "re-creates a dialect someone must learn to maintain."),
    "gates_h": "Multicloud release gates — evidence before placement",
    "artifacts_h": "What the platform architecture team inherits",
    "timeline_h": "Policies in order, week by week",
    "integ_h": "Integration surface — clouds, identity and the data estate",
    "integ_lead": ("The operating model spans clouds, identity planes and data gravity; these "
                   "contracts define where workloads may live and how identity follows them."),
    "controls_h": "Identity-seam governance overlay",
    "controls_lead": ("Federated identity across clouds is the seam where estates fail; the "
                      "overlay treats it as a product — tested failover, signed trust policies "
                      "and a break-glass path per cloud that is rehearsed, not assumed."),
    "controls_note": ("Egress surprises are attributed publicly: when a workload breaches its "
                      "egress budget, the architecture decision that caused it is named in the "
                      "review — tribalism dies by attribution."),
    "cta": ("Bring the workload everyone is afraid to move. The diagnostic will price its "
            "placement by policy — and show what portability would cost versus what the "
            "current dialect costs every month."),
    "flagships": ["banking-financial-services", "manufacturing", "energy-utilities"],
    "plays": [
        "Placement by signed policy — data gravity, latency, cost, regulation",
        "Portable pattern library so the second cloud is a configuration",
        "Egress budgets with attribution, and identity seams that are rehearsed",
    ],
},

"edge-computing-infrastructure": {
    "hero": ("Compute and delivery close to users and devices: regional clusters with "
             "store-and-forward resilience, fleet operations across heterogeneous hardware, "
             "rollout waves that respect site windows — and monitors that notice when a site "
             "goes silent instead of assuming it is fine."),
    "s1_h": "The edge is defined by its failures: partitions, silence and heterogeneity",
    "s1_close": ("Below: the failure modes that make edge estates fragile, the reference "
                 "architecture of partition-tolerant design, and the console that keeps a "
                 "thousand sites honest."),
    "s2_h": "Four failure modes that make edge estates fragile",
    "s2_lead": ("Each of these hides behind scale — a thousand sites make wonderful averages "
                "and terrible individual failures — the countermeasures measure sites as "
                "individuals."),
    "arch_h": "Reference architecture — regional clusters with store-and-forward",
    "arch_lead": ("Sites survive isolation by design: local decision-making on regional "
                  "clusters, store-and-forward queues that reconcile on reconnect, rollout "
                  "waves that respect site windows, and heartbeats that make silence a "
                  "monitored state rather than an assumption."),
    "flow_h": "One partitioned site, from isolation to reconciliation",
    "flow_lead": ("From link loss through local operation, bounded queues, reconnect and "
                  "reconciliation — including the conflict rules that decide what wins when "
                  "both sides moved."),
    "dash_h": "The edge console — sites as individuals",
    "dash_lead": ("Site heartbeat SLO, worst-site queue depth and rollout wave success — the "
                  "three numbers that run a fleet, because averages across a thousand sites "
                  "hide exactly the failure you care about."),
    "dash_note": ("Reference console — edge targets; the worst-site metric leads the review, "
                  "and silent sites are incidents by definition, never assumptions."),
    "chart_h": "Fleet behavior across rollout waves",
    "chart_lead": ("Wave success and rollback rates across site cohorts — the shape that shows "
                   "which hardware generations tolerate change and which need their own "
                   "windows."),
    "stack_h": "Edge defaults — and documented deviations",
    "stack_lead": ("Defaults favor store-and-forward autonomy with bounded conflicts over "
                   "split-brain optimism; deviation triggers are written because each one "
                   "changes what reconciliation means after a partition."),
    "gates_h": "Edge release gates — evidence before a wave",
    "artifacts_h": "What the fleet operations team inherits",
    "timeline_h": "Waves and windows, week by week",
    "integ_h": "Integration surface — sites, backends and the device fleet",
    "integ_lead": ("The estate spans sites, regional backends and devices; these contracts "
                   "define what each site must do alone, and how it must behave when the link "
                   "returns."),
    "controls_h": "Fleet-security governance overlay",
    "controls_lead": ("Physical access, device identity and signed updates are the controls "
                      "that make a distributed fleet survivable — each site's trust is "
                      "provisioned, rotated and revoked like any other principal."),
    "controls_note": ("Silence is an alarm: a site that stops heartbeating pages within minutes, "
                      "because the difference between 'offline' and 'compromised' is discovered "
                      "by going to look — the monitor's job is to make someone look."),
    "cta": ("Ask how long your quietest site ran without anyone noticing. The diagnostic will "
            "wire heartbeats, worst-site metrics and partition drills — and price what "
            "fleet-honest operations costs."),
    "flagships": ["retail-consumer-goods", "manufacturing", "energy-utilities"],
    "plays": [
        "Store-and-forward site autonomy with bounded conflict reconciliation",
        "Fleet operations across hardware generations with wave discipline",
        "Heartbeat SLOs where silence is an incident, never an assumption",
    ],
},

"finops-sustainable-computing": {
    "hero": ("Cost and carbon as engineering inputs: unit economics per workload with "
             "allocation coverage that reaches the invoice, rightsizing with teeth, zombie "
             "estates hunted on schedule — and sustainability reported from meters, not "
             "multipliers."),
    "s1_h": "Nobody spends someone else's money carefully — allocate it first",
    "s1_close": ("Below: the failure modes that keep cloud bills foggy, the reference "
                 "architecture of unit economics, and the console that trends cost and carbon "
                 "together."),
    "s2_h": "Four failure modes that keep cloud bills foggy",
    "s2_lead": ("Every one of these hides real money in averages — the countermeasures allocate "
                "to the workload, trend the unit cost and hunt the zombies on a schedule."),
    "arch_h": "Reference architecture — from meters to unit economics",
    "arch_lead": ("Allocation is the foundation: tagging that reaches 97% of spend, showback "
                  "per workload and team, rightsizing driven from utilization evidence, and "
                  "carbon reported from provider meters with documented factors — not "
                  "marketing multipliers."),
    "flow_h": "One invoice line, attributed to a decision",
    "flow_lead": ("From provider billing through allocation rules, workload showback, "
                  "rightsizing recommendation and the savings ledger — including where a "
                  "zombie resource is detected and who signs its retirement."),
    "dash_h": "The FinOps console — unit cost as the headline",
    "dash_lead": ("Allocation coverage, unit-cost trend and rightsizing savings — the three "
                  "numbers that turn the cloud bill from a surprise into an engineering input."),
    "dash_note": ("Reference console — FinOps targets; allocation coverage below 90% pauses "
                  "new provisioned spend, because unallocated spend is unmanaged spend."),
    "chart_h": "Unit-cost trajectory across the workloads",
    "chart_lead": ("Cost per unit of business work across workload families, quarter over "
                   "quarter — the curve that shows which efficiency bets paid and which "
                   "services are eating their margin quietly."),
    "stack_h": "FinOps defaults — and documented deviations",
    "stack_lead": ("Defaults favor showback-first with gated commitments over upfront reserved "
                   "sprees; deviation triggers are written because each one moves risk between "
                   "finance and engineering."),
    "gates_h": "FinOps release gates — evidence before commitments",
    "artifacts_h": "What the FinOps practice inherits",
    "timeline_h": "Allocation to zombies, week by week",
    "integ_h": "Integration surface — billing, tagging and the finance systems",
    "integ_lead": ("FinOps lives between provider billing and your ledger; these contracts "
                   "carry allocation into finance systems without manual reconciliation "
                   "spreadsheets."),
    "controls_h": "Sustainability governance overlay",
    "controls_lead": ("Carbon is reported from provider meters with documented emission factors "
                      "per region — reported beside cost, on the same trend line, because "
                      "efficiency is one metric wearing two currencies."),
    "controls_note": ("Zombie hunts run on schedule with a signed retirement ledger: a resource "
                      "unidentified for two cycles is suspended automatically, and "
                      "resurrections are cheaper than the monthly silence was."),
    "cta": ("Bring last month's invoice unexplained variance. The diagnostic will reach 97% "
            "allocation on your estate — and name the zombies, the rightsizing candidates and "
            "the unit-cost trend your CFO has been asking for."),
    "flagships": ["technology-saas", "retail-consumer-goods", "manufacturing"],
    "plays": [
        "Allocation coverage that reaches the invoice — 97%, gated",
        "Rightsizing from utilization evidence with a signed savings ledger",
        "Carbon from meters with documented factors, trended beside cost",
    ],
},

"cloud-native-modernization": {
    "hero": ("Workloads rebuilt for cloud-native operations — containerized, observable, "
             "resilient by default — moved on a strangler plan that escapes the lift-and-shift "
             "trap, retires the VM estate in waves, and shows the cost per workload falling "
             "with each one."),
    "s1_h": "Modernization is a behavior change wearing a container costume",
    "s1_close": ("Below: the failure modes that strand modernization halfway, the reference "
                 "architecture of the strangler waves, and the console that tracks the estate's "
                 "retirement honestly."),
    "s2_h": "Four failure modes that strand modernization halfway",
    "s2_lead": ("Each of these produces 'we are containerized' estates that still behave like "
                "VMs — the countermeasures make resilience and observability gates, not "
                "aspirations."),
    "arch_h": "Reference architecture — waves, strangler, retirement",
    "arch_lead": ("Workloads move in waves with explicit exit criteria: containerized, "
                  "observable, resilient under chaos drills, costed per workload — and the VM "
                  "estate shrinks on a published schedule instead of never."),
    "flow_h": "One workload, from VM to resilient service",
    "flow_lead": ("From assessment through containerization, observability wiring, chaos "
                  "validation and the cutover — including the rollback path and the state "
                  "migration that monoliths always hide."),
    "dash_h": "The modernization console — retirement as the headline",
    "dash_lead": ("Workloads modernized, VM estate remaining and cost per workload — the three "
                  "numbers that show whether the program is changing behavior or just "
                  "renaming servers."),
    "dash_note": ("Reference console — modernization targets; a workload is 'done' when its "
                  "chaos drill passes and its unit cost trend is signed, not when its "
                  "container starts."),
    "chart_h": "Cost per workload across the modernization waves",
    "chart_lead": ("Unit cost trend per wave — the honest curve that shows where "
                   "managed-service choices paid off and where the lift-and-shift trap quietly "
                   "priced itself in."),
    "stack_h": "Modernization defaults — and documented deviations",
    "stack_lead": ("Defaults favor strangler waves with chaos gates over big-bang cutovers; "
                   "deviation triggers are written because each one trades retirement "
                   "certainty for schedule hope."),
    "gates_h": "Modernization release gates — evidence before each wave",
    "artifacts_h": "What the engineering teams inherit",
    "timeline_h": "Waves with exit criteria, week by week",
    "integ_h": "Integration surface — the legacy estate and its consumers",
    "integ_lead": ("Waves succeed or die on the seams to the legacy estate; these contracts "
                   "cover the strangler routes, data synchronization and the consumers who "
                   "must move last."),
    "controls_h": "Resilience governance overlay",
    "controls_lead": ("Resilience is a gate, not a hope: chaos drills per wave, backup and "
                      "restore paths for stateful services, and the managed-service fallback "
                      "plan written before the outage, not during it."),
    "controls_note": ("Managed-service overreach is reviewed per wave: every managed dependency "
                      "carries an exit plan and its price — the lock-in ledger ships with the "
                      "wave's evidence pack."),
    "cta": ("Bring the monolith everyone protects and nobody loves. The diagnostic will price "
            "its wave with chaos gates included — and tell you what its retirement date "
            "actually requires."),
    "flagships": ["manufacturing", "insurance", "technology-saas"],
    "plays": [
        "Strangler waves with chaos-gated exit criteria — no container theater",
        "State migration and rollback paths planned before the cutover",
        "VM estate retirement on a published schedule, unit cost falling per wave",
    ],
},

"high-performance-mission-critical": {
    "hero": ("Low-latency, high-availability tiers with proofs: latency budgets engineered down "
             "the stack, failover rehearsed with clocks running, capacity planned from load "
             "models — availability measured on rolling windows that include the bad days."),
    "s1_h": "Mission-critical is a budget discipline, not a server label",
    "s1_close": ("Below: the failure modes that make 'HA' paper, the reference architecture of "
                 "budgeted tiers, and the console that reports the rolling numbers."),
    "s2_h": "Four failure modes that make high availability paper",
    "s2_lead": ("Every one of these survives a whiteboard and dies in a drill — the "
                "countermeasures put clocks on failover, budgets on latency and models on "
                "capacity."),
    "arch_h": "Reference architecture — the budgeted mission-critical tier",
    "arch_lead": ("Latency budgets are allocated down the stack — network, runtime, data, "
                  "serializations — and failover is rehearsed with the clock running: the "
                  "41-second drill time is a gate result, not a hope, and capacity comes from "
                  "load models signed per quarter."),
    "flow_h": "One failover, timed and evidenced",
    "flow_lead": ("From failure detection through leader election, state reconciliation, "
                  "traffic shift and the client recovery — including the p99 tail behavior "
                  "that decides whether users felt anything."),
    "dash_h": "The mission-critical console — availability with its tail",
    "dash_lead": ("Rolling availability, p99 end-to-end and failover drill time — the three "
                  "numbers that decide whether the tier is engineered or merely labeled."),
    "dash_note": ("Reference console — mission-critical targets; the rolling window includes "
                  "peak trading hours by design, and tail regressions gate releases like "
                  "availability breaches."),
    "chart_h": "Latency budget allocation down the stack",
    "chart_lead": ("Budget per layer at design load — network, runtime, data, serialization — "
                   "with the measured p99 beside each allocation, so the optimization order is "
                   "an engineering fact instead of a hunch."),
    "stack_h": "Performance defaults — and documented deviations",
    "stack_lead": ("Defaults favor measured budgets and rehearsed failover over vendor "
                   "availability claims; deviation triggers are written because each one "
                   "moves a proof into a promise."),
    "gates_h": "Tier release gates — evidence before traffic",
    "artifacts_h": "What the mission-critical platform team inherits",
    "timeline_h": "Budgets to drills, week by week",
    "integ_h": "Integration surface — network, data and the client estate",
    "integ_lead": ("The tier spans network, data and clients; these contracts define what each "
                   "layer must deliver for the end-to-end budget to hold under peak load."),
    "controls_h": "Tail-governance overlay",
    "controls_lead": ("The tail is governed as strictly as the average: p99 regressions gate "
                      "releases, load models are re-signed quarterly, and capacity headroom is "
                      "a reviewed number — because the users who leave live in the tail."),
    "controls_note": ("Failover drills run with production-like data volumes and the clock "
                      "published internally: a drill that exceeds its time budget produces "
                      "findings with owners, and the next drill re-tests them first."),
    "cta": ("Ask when your failover was last rehearsed with production-like volume. If the "
            "answer is 'never', bring the tier to a briefing — the first drill is "
            "complimentary, the outage is not."),
    "flagships": ["banking-financial-services", "telecom-media", "technology-saas"],
    "plays": [
        "Latency budgets allocated down the stack, measured at p99",
        "Failover rehearsed with clocks running and volumes that match production",
        "Capacity from signed load models, re-validated quarterly",
    ],
},
}
