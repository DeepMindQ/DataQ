#!/usr/bin/env python3
"""Move the consulting section on the homepage from after-industries to after-services,
and rewrite its header copy so consulting reads as a co-equal offer track."""
import re, sys

P = "site/src/components/site/HomeView.tsx"
src = open(P).read()

START = "      {/* consulting practices (A-23..A-27) */}"
END_ANCHOR = "      {/* insights (A-44/45) */}"
INS_ANCHOR = "      {/* evidence library — buyer-path position 2 (A-40..A-43, A-53) */}"

i = src.find(START)
j = src.find(END_ANCHOR)
k = src.find(INS_ANCHOR)
assert i != -1 and j != -1 and k != -1, "markers not found"
assert k < i < j, "unexpected marker order"

block = src[i:j].rstrip() + "\n\n"
src = src[:i] + src[j:]

# rewrite the header copy of the moved block
old_head = """      {/* consulting practices (A-23..A-27) */}
      <section id="consulting" className="scroll-mt-24 border-y border-line bg-white">
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Consulting practices
                </p>
                {/* A-23 */}
                <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                  Thirteen delivery practices — migration, engineering, cloud, ERP — under the same gate contract
                </h2>
                {/* A-24 */}
                <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                  Four practice groups cover the classic estate: data, engineering, cloud and ERP. Same contract as the
                  expertise domains — two-week diagnostic, signed baseline, evidence or stop.
                </p>
              </div>"""
new_head = """      {/* consulting practices (A-23..A-27) — co-equal offer track, repositioned after services */}
      <section id="consulting" className="scroll-mt-24 border-y border-line bg-white">
        <div className="container-dq section-y-sm">
          <Reveal>
            <div className="flex flex-wrap items-end justify-between gap-4">
              <div>
                <p className="kicker-bar text-[12px] font-semibold uppercase tracking-[0.2em] text-brand-deep">
                  Consulting &amp; IT services
                </p>
                {/* A-23 */}
                <h2 className="text-display-3 mt-1 text-navy-800 sm:text-[28px]">
                  Thirteen consulting practices — the advisor is the builder, under the same gate contract
                </h2>
                {/* A-24 */}
                <p className="mt-2 max-w-2xl text-[14.5px] text-slate-body/75">
                  Transformation programs, migration factories, engineering pods, quality engineering, Azure estates,
                  ERP cores, managed operations and end-user support. The team that recommends is the team that builds
                  it — the same two-week diagnostic, signed baseline and evidence-or-stop contract as every expertise
                  domain.
                </p>
              </div>"""
assert old_head in block, "consulting header block not matched inside extracted section"
block = block.replace(old_head, new_head)

assert INS_ANCHOR in src, "evidence anchor missing after removal"
src = src.replace(INS_ANCHOR, block + INS_ANCHOR)
src = src.replace(
    "evidence library — buyer-path position 2 (A-40..A-43, A-53)",
    "evidence library (A-40..A-43, A-53) — proof, after the two offer tracks",
)

open(P, "w").write(src)
# sanity: order of section ids in file
order = [m.group(1) for m in re.finditer(r'<section id="([a-z]+)"', src)]
print("section order:", order)
assert order.index("services") < order.index("consulting") < order.index("patents") < order.index("platforms") < order.index("evidence"), "section order wrong"
print("OK — consulting moved after services; headers rewritten.")
