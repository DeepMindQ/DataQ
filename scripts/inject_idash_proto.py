#!/usr/bin/env python3
"""Inject an interactive DashSuite (idash) block into the realtime-streaming
service page — prototype for the Services rebuild. Replaces the static dash."""
import json

F = "site/src/content/pages/services_data-analytics-lakehouse_realtime-streaming-decisioning.json"
j = json.load(open(F))

idash = {
    "t": "idash",
    "title": "Streaming decision console — live model of the decision fabric",
    "badge": "Interactive · drag the sliders",
    "kpis": [
        {"label": "Decision p99", "value": "142", "delta": "target <150 ms", "dir": "flat", "spark": [161, 155, 158, 150, 146, 149, 143]},
        {"label": "Ingest rate", "value": "38.4k", "delta": "events/s sustained", "dir": "up", "spark": [28, 30, 31, 33, 34, 36, 38]},
        {"label": "Exactly-once violations", "value": "0.000%", "delta": "checkpointed state", "dir": "down", "spark": [0.1, 0.1, 0.05, 0, 0, 0, 0]},
        {"label": "Late-event recovery", "value": "99.7%", "delta": "watermark +600 s", "dir": "up", "spark": [98.1, 98.4, 99, 99.2, 99.5, 99.6, 99.7]},
        {"label": "Shadow disagreement", "value": "0.42%", "delta": "engine v4 vs v3", "dir": "flat", "spark": [1.8, 1.5, 1.1, 0.9, 0.6, 0.5, 0.42]},
    ],
    "tabs": [
        {
            "name": "Decision p99 by hop",
            "widgets": [
                {
                    "kind": "line",
                    "title": "Hop-by-hop latency at design load — 38k events/s",
                    "cats": ["Ingress", "Enrich", "State", "Score", "Policy", "Act", "Egress"],
                    "series": [
                        {"name": "p50", "points": [4, 6, 9, 12, 8, 5, 3]},
                        {"name": "p95", "points": [7, 11, 16, 21, 14, 9, 5]},
                        {"name": "p99", "points": [11, 17, 24, 38, 22, 14, 8]},
                    ],
                    "unit": "ms",
                    "note": "Hover the chart for exact values; click a series name to isolate it. Scoring is the first hop to break a 150 ms p99 budget under burst — that is where optimization starts.",
                },
                {
                    "kind": "slo",
                    "title": "Decision-availability error budget — 99.95% over 30 days",
                    "target": 99.95,
                    "windowDays": 30,
                    "traffic": 38000,
                    "errPct": 0.04,
                    "note": "Drag both sliders. Below 1× the budget recovers and feature work proceeds; above 6× we investigate the same day; above 14.4× pages the on-call.",
                },
            ],
        },
        {
            "name": "Backpressure what-if",
            "widgets": [
                {
                    "kind": "sim",
                    "title": "Burst what-if — consumers, partitions and lag",
                    "params": [
                        {"name": "Producer rate", "min": 5000, "max": 120000, "step": 5000, "value": 40000, "unit": "ev/s"},
                        {"name": "Consumer groups", "min": 2, "max": 12, "step": 1, "value": 6, "unit": "grp"},
                        {"name": "State TTL", "min": 5, "max": 60, "step": 5, "value": 15, "unit": "min"},
                    ],
                    "outputs": [
                        {"name": "Steady-state lag", "unit": "ms", "formula": "p0/(p1*9000)*100", "good": "250", "bad": "600"},
                        {"name": "State store GB", "unit": "GB", "formula": "p0*p2*0.000042", "good": "30", "bad": "80"},
                        {"name": "Recovery replay (est)", "unit": "s", "formula": "p0*p2/(p1*1200)", "good": "20", "bad": "60"},
                    ],
                    "curve": {"param": 0, "output": 0, "label": "Producer rate (ev/s) vs lag (ms)"},
                    "note": "The lag curve is the admission-control argument: below the knee consumers drain as fast as producers push; past it, checkpoint intervals stretch and exactly-once replays get expensive.",
                },
                {
                    "kind": "heat",
                    "title": "Late-arrival intensity — hour of day × event class",
                    "rows": ["Trading", "Fraud", "Pricing", "Ops telemetry"],
                    "cats": ["00–04", "04–08", "08–12", "12–16", "16–20", "20–24"],
                    "matrix": [
                        [2, 3, 9, 14, 22, 11],
                        [5, 6, 18, 26, 31, 14],
                        [1, 2, 7, 9, 12, 6],
                        [9, 8, 12, 13, 15, 10],
                    ],
                    "unit": "k late ev/h",
                    "note": "Hover cells to read exact late-event volumes. Trading and fraud classes dominate the 16–20 window — the watermark tolerance is tuned per class, not globally, or the tail eats the budget.",
                },
            ],
        },
        {
            "name": "Fabric topology",
            "widgets": [
                {
                    "kind": "arch",
                    "title": "The decision fabric — click any node for its contract",
                    "lanes": ["Producers", "Transport", "Stream core", "Decision", "Actions"],
                    "nodes": [
                        {"id": "src1", "lane": 0, "label": "Market / fraud feeds", "detail": "Idempotent producers with event-time timestamps stamped at source — the fabric refuses processing-time ordering because it cannot replay."},
                        {"id": "src2", "lane": 0, "label": "POS & edge events", "detail": "Batched with 50 ms linger; late joiners backfill through a dead-letter lane that replays into the same contracts."},
                        {"id": "bus", "lane": 1, "label": "Kafka log", "detail": "Keyed by decision subject to guarantee per-subject order; 7-day retention makes every decision replayable from the log itself."},
                        {"id": "schema", "lane": 1, "label": "Schema registry", "detail": "Compatibility enforced BACKWARD_TRANSITIVE — a producer cannot ship a payload that yesterday's decision core cannot parse."},
                        {"id": "proc", "lane": 2, "label": "Checkpointed state", "detail": "Exactly-once via two-phase commit between the stream operator and sinks; checkpoint interval is the recovery-time dial."},
                        {"id": "wm", "lane": 2, "label": "Watermark engine", "detail": "Per-class watermark tolerance; late events route to a correction stream instead of being dropped — the correction path is tested with chaos drills."},
                        {"id": "score", "lane": 3, "label": "Scoring models", "detail": "Versioned feature lookups pinned per release; shadow lane scores every event on the new model before promotion."},
                        {"id": "policy", "lane": 3, "label": "Decision policies", "detail": "Policies are code-reviewed artifacts; a change re-runs the replay suite against recorded traffic before it touches live decisions."},
                        {"id": "act", "lane": 4, "label": "Action writers", "detail": "Idempotent sinks keyed by decision ID — a replayed decision overwrites rather than duplicates."},
                        {"id": "case", "lane": 4, "label": "Case & hold queue", "detail": "Holds carry the decision evidence packet: inputs, model version, budget state — the artifact an incident review reads first."},
                    ],
                    "edges": [
                        {"a": "src1", "b": "bus", "label": "event-time"},
                        {"a": "src2", "b": "bus"},
                        {"a": "bus", "b": "proc"},
                        {"a": "schema", "b": "bus", "label": "govern"},
                        {"a": "proc", "b": "wm"},
                        {"a": "proc", "b": "score"},
                        {"a": "score", "b": "policy"},
                        {"a": "policy", "b": "act"},
                        {"a": "policy", "b": "case", "label": "hold"},
                    ],
                    "note": "Every node carries a written contract — ordering, idempotency, replay semantics. Click nodes to read them; the edges show where a failure propagates.",
                },
            ],
        },
    ],
    "note": "Console values are the reference program model: engineering targets and gate thresholds from delivery, not a client's live metrics.",
}

# replace the static dash block with the interactive suite
blocks = j["blocks"]
for i, b in enumerate(blocks):
    if b.get("t") == "dash":
        blocks[i] = idash
        break
else:
    raise SystemExit("no dash block found")

# bump words estimate
j["words"] = sum(len(str(b.get("x", "")).split()) for b in blocks if isinstance(b.get("x"), str))
json.dump(j, open(F, "w"), indent=1, ensure_ascii=False)
print("injected idash into", F)
