#!/usr/bin/env python3
"""Phase 3 shared registry: industries, domains, deterministic value selection."""

import hashlib

# 12 industries (slug -> display name), mirrors site content
INDUSTRIES = [
    ("banking-financial-services", "Banking & Financial Services"),
    ("insurance", "Insurance & Risk"),
    ("healthcare-life-sciences", "Healthcare & Life Sciences"),
    ("manufacturing", "Manufacturing & Industrial"),
    ("retail-consumer-goods", "Retail & Consumer Goods"),
    ("telecom-media", "Telecom, Media & Entertainment"),
    ("energy-utilities", "Energy & Utilities"),
    ("logistics-supply-chain", "Logistics & Supply Chain"),
    ("public-sector", "Public Sector & Government"),
    ("education-research", "Education & Research"),
    ("technology-saas", "Technology & SaaS"),
    ("agriculture-food", "Agriculture & Food Systems"),
]

DOMAINS = {
    "agentic-ai-hyperautomation": "Agentic AI & Hyperautomation",
    "applied-ai-generative-ai": "Applied AI & Generative AI",
    "blockchain-digital-trust": "Blockchain & Digital Trust",
    "cloud-edge-platform-engineering": "Cloud & Edge Platform Engineering",
    "cybersecurity-zero-trust": "Cybersecurity & Zero Trust",
    "data-analytics-lakehouse": "Data Analytics & Lakehouse",
    "iot-digital-twin-robotics": "IoT, Digital Twin & Robotics",
    "quantum-advanced-compute": "Quantum & Advanced Compute",
}


# Domain slug for a page file stem: services_<dom>[_<svc>]
def domain_of(stem: str) -> str:
    parts = stem.split("_")
    if stem == "services":
        return "hub"
    return parts[1]


def stable_int(key: str, mod: int) -> int:
    h = hashlib.md5(key.encode("utf-8")).hexdigest()
    return int(h[:12], 16) % mod


def fmt_value(v: int, fmt: str) -> str:
    if fmt == "pct":
        return f"{v}%"
    if fmt == "cents":
        return f"${v / 100:.2f}"
    if fmt == "dollars":
        return f"${v}"
    if fmt == "days":
        return f"{v} days"
    if fmt == "hrs":
        return f"{v} hrs"
    if fmt == "min":
        return f"{v} min"
    if fmt == "sec":
        return f"{v}s"
    if fmt == "ms":
        return f"{v} ms"
    if fmt == "bp":
        return f"{v} bp"
    if fmt == "x":
        return f"{v}x"
    if fmt == "k":
        return f"${v}k"
    if fmt == "num":
        return str(v)
    if fmt == "per1k":
        return f"{v} / 1k"
    raise ValueError(f"unknown fmt {fmt}")


def pick_value(page_key: str, ind: str, label: str, lo: int, hi: int, fmt: str) -> str:
    span = hi - lo + 1
    v = lo + stable_int(f"{page_key}|{ind}|{label}", span)
    return fmt_value(v, fmt)


def pick_word(page_key: str, words: list) -> str:
    return words[stable_int(page_key, len(words))]
