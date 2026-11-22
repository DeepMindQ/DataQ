# -*- coding: utf-8 -*-
"""Wave 4 data — d10b: the defaults-family ops that were dropped when duplicate
dict keys in d10 overwrote them. Idempotent: skips pages already retitled."""

OPS = {
'services_agentic-ai-hyperautomation_agentic-process-automation': {
    'h2': [('Defaults for the agent stack', 'What the agent stack ships as standard — and the four signed deviations', None)],
},
'services_agentic-ai-hyperautomation_autonomous-workflow-orchestration': {
    'h2': [('The orchestration defaults', 'Engine and pattern choices we standardize — and the two worth arguing', None)],
},
'services_agentic-ai-hyperautomation_digital-workforce-orchestration': {
    'h2': [('Fleet control-plane defaults', 'The control plane as standard, and the registry settings you may vary', None)],
},
'services_agentic-ai-hyperautomation_hyperautomation-integration': {
    'h2': [('The pattern defaults', 'Standard seam patterns by class — and the case where a seam earns an exception', None)],
},
'services_agentic-ai-hyperautomation_intelligent-document-processing': {
    'h2': [('Ensemble and rule defaults', 'Extraction ensembles by default, rules where they win — the signed exceptions', None)],
},
'services_agentic-ai-hyperautomation_process-task-mining': {
    'h2': [('The mining toolchain defaults', 'The toolchain we run by default — and when a different miner earns its place', None)],
},
'services_applied-ai-generative-ai_llm-fine-tuning-ops': {
    'h2': [('Training and serving defaults', 'What the factory runs as standard — training, serving and the signed exceptions', None)],
},
'services_applied-ai-generative-ai_multimodal-vision-systems': {
    'h2': [('Extraction defaults', 'Standard extraction stack per document class — and where we swap components', None)],
},
'services_blockchain-digital-trust_asset-tokenization': {
    'h2': [('Tokenization defaults', 'The token design we standardize — wrapper, controls and the signed exceptions', None)],
},
'services_blockchain-digital-trust_blockchain-analytics-compliance': {
    'h2': [('Screening defaults', 'Screening stack as standard — and the flow classes where we deviate', None)],
},
'services_blockchain-digital-trust_decentralized-identity': {
    'h2': [('Identity defaults', 'The trust framework as standard — and where we leave the standard path', None)],
},
'services_blockchain-digital-trust_enterprise-dlt-networks': {
    'h2': [('Network defaults', 'What every member gets as standard — and what the charter lets you vary', None)],
},
'services_blockchain-digital-trust_provenance-traceability': {
    'h2': [('Provenance defaults', 'Capture standards per partner class — and the deviations with a price', None)],
},
'services_blockchain-digital-trust_smart-contract-engineering': {
    'h2': [('Contract defaults', 'Proof coverage by contract layer — the standard and where it stops', None)],
},
'services_cloud-edge-platform-engineering_cloud-native-modernization': {
    'h2': [('Modernization defaults', 'The wave default — strangler, dual-run only where risk says so', None)],
},
'services_cloud-edge-platform-engineering_edge-computing-infrastructure': {
    'h2': [('Edge defaults', 'Site-class standards — autonomy budgets, updates and the signed exceptions', None)],
},
'services_cloud-edge-platform-engineering_finops-sustainable-computing': {
    'h2': [('FinOps defaults', 'Allocation as standard — drivers, reports and where we deviate', None)],
},
'services_cloud-edge-platform-engineering_high-performance-mission-critical': {
    'h2': [('Performance defaults', 'The tier standard — budgets, drills and the deviations we sign', None)],
},
'services_cloud-edge-platform-engineering_hybrid-multicloud-architecture': {
    'h2': [('Multicloud defaults', 'Placement patterns as standard — and the workload that earns an exception', None)],
},
'services_cloud-edge-platform-engineering_platform-engineering-devex': {
    'h2': [('Platform defaults', 'What the golden path guarantees — and the stages a team may replace', None)],
},
'services_cloud-edge-platform-engineering_sre-reliability-engineering': {
    'h2': [('SRE defaults', 'Budget policy as standard — freezes, targets and the signed exceptions', None)],
},
'services_cybersecurity-zero-trust_ai-security-model-protection': {
    'h2': [('AI-security defaults', 'Defense-in-depth as standard — and the surfaces where we relax a layer', None)],
},
'services_cybersecurity-zero-trust_cloud-security-posture': {
    'h2': [('Posture defaults', 'Guardrails as standard — and the exceptions with expiry dates', None)],
},
'services_cybersecurity-zero-trust_compliance-audit-digital-trust': {
    'h2': [('Compliance defaults', 'The evidence standard — and where a framework earns an exception', None)],
},
'services_cybersecurity-zero-trust_cyber-resilience-incident-recovery': {
    'h2': [('Resilience defaults', 'Resilience as standard — immutable, isolated and the signed exceptions', None)],
},
'services_cybersecurity-zero-trust_identity-access-modernization': {
    'h2': [('Identity defaults', 'Lifecycle standards per identity class — and the exceptions we sign', None)],
},
'services_cybersecurity-zero-trust_threat-intelligence-managed-soc': {
    'h2': [('SOC defaults', 'Detection standards — precision budgets and the deviations we sign', None)],
},
'services_cybersecurity-zero-trust_zero-trust-architecture': {
    'h2': [('Enforcement defaults', 'Enforcement as standard — and the exceptions that carry expiries', None)],
},
'services_data-analytics-lakehouse_advanced-risk-predictive-analytics': {
    'h2': [('Modeling defaults', 'The modeling standard — baselines, holdouts and the signed exceptions', None)],
},
'services_data-analytics-lakehouse_data-engineering-modernization': {
    'h2': [('Modernization defaults', 'Parity as standard — dual-run windows and where we deviate', None)],
},
'services_data-analytics-lakehouse_data-monetization-products': {
    'h2': [('Product defaults', 'Product standards per tier — SLOs, pricing and the signed exceptions', None)],
},
'services_data-analytics-lakehouse_enterprise-bi-executive-analytics': {
    'h2': [('BI defaults', 'Certification as standard — and the dashboards that stay uncertified', None)],
},
'services_data-analytics-lakehouse_lakehouse-architecture': {
    'h2': [('Table-format defaults', 'Table formats by tier — the standard choice and the case for the alternative', None)],
},
'services_data-analytics-lakehouse_master-data-governance': {
    'h2': [('Matching defaults', 'Matching standards per domain — thresholds and the signed exceptions', None)],
},
'services_data-analytics-lakehouse_realtime-streaming-decisioning': {
    'h2': [('Streaming defaults', 'The streaming standard — budgets, exactly-once and the deviations', None)],
},
'services_iot-digital-twin-robotics_computer-vision-edge-ai': {
    'h2': [('Edge-AI defaults', 'The hardware contract as standard — and the SKU that earns a deviation', None)],
},
'services_iot-digital-twin-robotics_connected-products-devices': {
    'h2': [('Fleet defaults', 'Fleet standards per line — update cadence and the legacy exception', None)],
},
'services_iot-digital-twin-robotics_digital-twin-platforms': {
    'h2': [('Twin defaults', 'Twin standards per asset class — fidelity floors and the signed exceptions', None)],
},
'services_iot-digital-twin-robotics_industrial-iot-sensor-fabric': {
    'h2': [('Fabric defaults', 'Fabric standards per device class — fidelity targets and the exceptions', None)],
    'idash': ('Reference program model: fidelity targets and buffer-autonomy bands from delivery history, not client data.',
              'Interactive · capture model'),
},
'services_iot-digital-twin-robotics_predictive-asset-intelligence': {
    'h2': [('Predictive defaults', 'The predictive standard — P-F gating and where we deviate', None)],
},
'services_iot-digital-twin-robotics_robotics-autonomous-systems': {
    'h2': [('Robotics defaults', 'Zone standards — autonomy envelopes and the signed exceptions', None)],
},
'services_iot-digital-twin-robotics_smart-infrastructure': {
    'h2': [('Infrastructure defaults', 'Segment standards — continuity floors and the legacy exception', None)],
},
'services_quantum-advanced-compute_emerging-compute-advisory': {
    'h2': [('Advisory defaults', 'The testing standard — benchmarks, memos and the deviations', None)],
},
'services_quantum-advanced-compute_hpc-simulation-engineering': {
    'h2': [('HPC defaults', 'Benchmark standards per workload — and where tuning earns an exception', None)],
},
'services_quantum-advanced-compute_post-quantum-cryptography': {
    'h2': [('Migration defaults', 'Algorithm standards per segment — hybrid modes and the legacy exception', None)],
},
'services_quantum-advanced-compute_quantum-ml-simulation': {
    'h2': [('Simulation defaults', 'The verification standard — screens, agreement and the deviations', None)],
},
'services_quantum-advanced-compute_quantum-optimization': {
    'h2': [('Optimization defaults', 'The bake-off standard — harness rules and the deviations we sign', None)],
},
'services_quantum-advanced-compute_quantum-readiness-strategy': {
    'h2': [('Readiness defaults', 'Scoring standards — criteria, baselines and the council exceptions', None)],
},
}
