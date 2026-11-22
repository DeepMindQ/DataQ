# -*- coding: utf-8 -*-
"""Wave 4 data — idash badge de-duplication (3 pairs shared across domains)."""

OPS = {
    # 'Interactive · portfolio model' shared by enterprise-ai-strategy + quantum-readiness-strategy
    'services_quantum-advanced-compute_quantum-readiness-strategy': {
        'idash': ('Reference program model: triage kill-rates and baseline-strength bands from delivery history, not client data.',
                  'Interactive · triage model'),
    },
    # 'Interactive · ratchet model' shared by cloud-native-modernization + lakehouse-architecture
    'services_data-analytics-lakehouse_lakehouse-architecture': {
        'idash': ('Reference program model: promotion thresholds and freshness bands from delivery history, not client data.',
                  'Interactive · promotion model'),
    },
    # 'Interactive · coverage model' shared by threat-intelligence-managed-soc + industrial-iot-sensor-fabric
    'services_iot-digital-twin-robotics_industrial-iot-sensor-fabric': {
        'idash': ('Reference program model: fidelity targets and buffer-autonomy bands from delivery history, not client data.',
                  'Interactive · fidelity model'),
    },
}
