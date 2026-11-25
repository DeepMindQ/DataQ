#!/usr/bin/env python3
"""Extend the 3 under-5000-word deep content files with additive sections.

Insertions go immediately BEFORE the final FAQ h2 ("Questions ... leaders ask us")
so the page's closing pattern (FAQ -> cta) is preserved and the first-paragraph
opener / CTA uniqueness gates are untouched.
"""
import json
import sys
from pathlib import Path

DEEP = Path("/home/z/my-project/scripts/deep_content")

# (file, h2, paragraphs)
ADD = {
    "industries_logistics-supply-chain_last-mile-mobility": (
        "Returns and the reverse leg nobody planned",
        [
            "Every parcel route has a shadow: the return leg. E-commerce return rates in softgoods run high enough that the reverse stream is not an exception queue but a second network operating over the same vans, the same lockers and the same couriers — with none of the same economics. A pickup at a consumer door costs more than the outward drop because it is unscheduled, needs label generation and reason capture at the doorstep, and lands as single units into a sortation flow built for batches. Most last-mile stacks treat returns as an accounting event and discover the operational cost only when courier utilization dips on days the reverse book runs heavy.",
            "The build is a reverse-leg plan inside the same dispatch loop: return-to-origin and locker-drop consignments scheduled against forward volume instead of bolted onto it, reason codes captured at the door and joined to the order record, disposition triage (restock, refurbish, liquidate) decided before the parcel re-enters the warehouse, and fraud signals — serial returners, empty-box claims, mismatched weights at induction — surfaced from scan data the network already produces. Dataq Software baselines the reverse economics first: cost per return by channel, recovery latency from doorstep to sellable, and the share of return volume riding routes paid for a different job. If the delta is small, the honest answer is that returns are fine and the effort belongs elsewhere.",
        ],
    ),
    "industries_retail-consumer-goods_cpg-brands": (
        None,  # single paragraph, no heading
        [
            "One pattern recurs across engagements: the fastest wins come from reconciling the plan nobody can defend with the deductions nobody can explain. When gross-to-net evidence, shipment truth and retail execution live in one reviewed model, the annual trade negotiation changes shape — the conversation moves from spend percentage to paid performance, and the funding decision follows shopper evidence rather than the largest historical number. Dataq Software does not replace the TPM suite; it gives the suite the baseline, audit and post-event spine it never had.",
        ],
    ),
    "industries_retail-consumer-goods_fashion-luxury": (
        "Allocation by door: consignment logic and sell-through evidence",
        [
            "Luxury distribution is negotiated door by door: concession terms, consignment versus outright, and sell-through thresholds that decide whether a style renews for the next season. The data behind those negotiations — door-level receipts, weekly sell-through by SKU, hold-back clauses, return rights at season end — usually lives in the wholesale team's spreadsheets while the ERP carries only shipment truth. When a door underperforms, the renewal argument is anecdotal; when a style overperforms, the reorder decision waits for a report that arrives after the buying window closes. The gap is not analytics talent, it is the missing contract-level data model that joins terms to movement.",
            "The build is a door-economics ledger: terms metadata (consignment flag, markdown rights, exclusivity windows) attached to every door, sell-through computed weekly against season pace targets, reorder and transfer proposals respecting concession law and brand adjacencies, and end-of-season returns priced against contractual rights before the goods move. Dataq Software keeps merchandisers in the loop — proposals land in planner-approved lanes with reasoning attached — and measures the program on one number: revenue per door per season against the pace plan the buying team signed. If the ledger does not move that number, the honest read is that the constraint sits elsewhere, and we say so.",
        ],
    ),
}


def faq_index(blocks):
    for i, b in enumerate(blocks):
        if b.get("t") == "h2" and b.get("x", "").startswith("Questions"):
            return i
    return None


def main():
    failed = False
    for name, (h2, paras) in ADD.items():
        path = DEEP / f"{name}.blocks.json"
        d = json.load(open(path, encoding="utf-8"))
        blocks = d["blocks"]
        if any(b.get("t") == "h2" and b.get("x") == h2 for b in blocks) and h2:
            print(f"{name}: section already present, skip")
            continue
        idx = faq_index(blocks)
        if idx is None:
            print(f"{name}: FAQ h2 not found, abort")
            failed = True
            continue
        new = []
        if h2:
            new.append({"t": "h2", "x": h2})
        for p in paras:
            new.append({"t": "p", "x": p})
        blocks[idx:idx] = new
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(d, fh, ensure_ascii=False, indent=1)
        added = sum(len(p.split()) for p in paras)
        print(f"{name}: inserted {len(new)} block(s), +{added} words")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
