#!/usr/bin/env python3
"""Wave 3 content ops — batch 3: iot-digital-twin-robotics, quantum-advanced-compute."""

HUB_OPS = {

# ─────────────────────────── iot-digital-twin-robotics ───────────────────────────
"iot-digital-twin-robotics": {
 "h2": [
  (7,  "The domain reference architecture",
       "Sense, simulate, decide, act — the loop with an interlock",
       "Protocol translation, partition-tolerant capture, honest twins and signed commands in one map"),
  (10, "The operations stack on one screen",
       "The operations console — what the plant and fleet reviews read",
       "Capture fidelity, twin sync lag, downtime and utilization as one weekly reading"),
  (16, "Sector depth",
       "Where the operations stack has sector playbooks today",
       "Lines, grids, fleets and cold chains — twelve industries with live briefs"),
  (20, "How operations-stack engagements run",
       "From fidelity baseline to fleet operations",
       "Four phases; every claim verified physically before it earns authority"),
  (22, "Operations release gates",
       "Five gates between the twin and the physical world",
       "Schema, partition, safety, sync, OTA — the evidence each demands"),
 ],
 "p": [
  (17, "Manufacturing buys sensor fabrics and robots",
       "Manufacturing buys sensor fabrics and robots, utilities buy grid twins and smart infrastructure, agriculture buys field telemetry. The bars count published sub-industry briefs — a taller bar means the sector's brownfield realities, safety norms and telemetry conventions are already drawn into the playbooks."),
 ],
 "table_cap": [
  (4,  "Seven practices — from sensor fabric to smart infrastructure"),
  (23, "The five operations gates — between twin and physical world"),
 ],
 "arch": [
  (9,  "IoT, Digital Twin & Robotics — sense, simulate, decide, act",
       [("Practices in the domain", "7"), ("Fidelity gates", "signed"), ("Industries served", "12")]),
 ],
 "bar_cap": [
  (18, "Counts are live sub-industry brief pages on this site. Taller means the sector's asset classes, protocols and safety norms already have published playbooks."),
 ],
 "idash": [
  (12, "Reference operations-stack model: maturity bands and depth indices from delivery, not client telemetry.",
       "Interactive · operations console"),
 ],
 "explorer": [
  (19, "Domain-level view — pick a practice above for the practice-specific sector plan and fidelity bands."),
 ],
 "faq": [
  ("Bring the asset class whose failures cost the most",
   [("Our assets are twenty years old — is this still applicable?",
     "Brownfield is the default assumption: protocol translation at the edge, schema versioning per device class and store-and-forward capture exist precisely because the estate predates the program. Modernization happens without stopping the plant."),
    ("What makes a twin honest?",
     "A signed fidelity target per asset class, sync-lag metrics trended in the console, and conflict rules that resolve state mismatches by rule rather than by hope. Drift past target earns a work order — the twin cannot fail silently."),
    ("How do you keep robots safe around people?",
     "Rehearsed safety cases before floor entry: hardware interlocks on the command path, rate-limited signed commands, and drill evidence that fail-to-safe actually fails to safe. Autonomy expands only as the evidence allows."),
    ("Why is capture fidelity the first metric?",
     "Because every downstream promise spends it: predictions, twins and automations are only as true as the telemetry they read. The diagnostic baselines fidelity per asset class before anything downstream is priced."),
    ("Can this start with one production line?",
     "Yes — one line is the standard provability sprint: capture fidelity, twin sync and prediction precision on real equipment, with a fund-or-kill verdict at four weeks.")]),
 ],
 "meta": "IoT, Digital Twin & Robotics for physical operations: sensor fabrics that survive partitions, edge AI on deadline, honest twins, robot fleets with safety cases. Seven practices, fidelity-gated end to end.",
 "chip": ("7 practices · fidelity-gated", "Sense → twin → act"),
},

# ─────────────────────────── quantum-advanced-compute ───────────────────────────
"quantum-advanced-compute": {
 "h2": [
  (7,  "The domain reference architecture",
       "The hybrid frontier — classical first, quantum where proven",
       "Benchmarking harness, crypto inventory and migration waves in one governed map"),
  (10, "The program on one screen",
       "The benchmark console — what the frontier program is steered by",
       "Baselines beaten, improvement distributions and migration posture as one weekly reading"),
  (16, "Sector depth",
       "Where the compute frontier is on the sector clock",
       "PQC deadlines, scheduling margin and simulation throughput — twelve industries, live briefs"),
  (20, "How compute engagements run",
       "Triage, bake-off, migrate — evidence at every step",
       "Four phases; vendor claims reproduced before they enter any roadmap"),
  (22, "Compute release gates",
       "Five gates between claim and roadmap",
       "Formulation, baseline, benchmark, verification, inventory — the evidence each demands"),
 ],
 "p": [
  (17, "Quantum readiness concentrates in regulated finance",
       "Quantum readiness concentrates in regulated finance and defense-adjacent public sectors; optimization and HPC concentrate where scheduling and simulation carry margin. The bars count published sub-industry briefs — a taller bar means the sector's exposure clocks, optimization surfaces and benchmark baselines are already drawn."),
 ],
 "table_cap": [
  (4,  "Six practices — from triage to horizon scanning, one metric each"),
  (23, "The five compute gates — between claim and roadmap"),
 ],
 "arch": [
  (9,  "Quantum & Advanced Compute — the hybrid frontier",
       [("Advantage claims", "verified only"), ("PQC", "the urgent practice"), ("Industries served", "12")]),
 ],
 "bar_cap": [
  (18, "Counts are live sub-industry brief pages on this site. Taller means the sector's PQC clock, optimization surface or simulation load already has a published playbook."),
 ],
 "idash": [
  (12, "Reference frontier-program model: efficiency bands and envelope sizes from delivery benchmarks, not vendor claims.",
       "Interactive · benchmark console"),
 ],
 "explorer": [
  (19, "Domain-level view — pick a practice above for the practice-specific sector plan and benchmark posture."),
 ],
 "faq": [
  ("Bring the vendor deck that promised 1000x",
   [("Is quantum relevant to us this year?",
     "Two answers, both evidence-based: post-quantum cryptography is relevant now if you hold long-lived secrets — the inventory and migration waves are engineering work with real deadlines. Quantum advantage is relevant when a problem class beats your classical baseline on auditable instances; the triage tells you which, with numbers."),
    ("What is harvest-now-decrypt-later, practically?",
     "Adversaries recording your encrypted traffic today to decrypt when quantum hardware matures. Anything whose confidentiality must outlive the migration window is exposed — the crypto inventory scores that exposure endpoint by endpoint."),
    ("Can you prove an advantage claim before we fund it?",
     "That is the bake-off sprint: the claim runs against your signed classical baseline on pinned instances, with harness version and noise calibration documented. Reproduced claims become benchmarks; unreproduced ones become memos with revisit dates."),
    ("Which vendors do you represent?",
     "None. Roadmaps are vendor-neutral so the recommendation survives the next hardware generation — hardware access is brokered through cloud QPU programs, and the benchmark suite never changes to flatter a vendor."),
    ("What if the verdict is not yet?",
     "Then the memo says so with the numbers, the classical stack keeps the improvement the formulation work produced, and the revisit date is on the ledger. A defensible no is a deliverable.")]),
 ],
 "meta": "Quantum & Advanced Compute run as evidence, not evangelism: readiness triage, hybrid optimization against audited classical baselines, HPC today and PQC migration on a real clock. Six practices, five gates.",
 "chip": ("6 practices · evidence-first", "Classical first, quantum where proven"),
},

}
