#!/usr/bin/env python3
"""Split PagePieces.tsx into a browser-safe PageBlocks.tsx (presentational)
and a slim server PagePieces.tsx (ContentPage etc.), with re-exports so all
existing consumers keep working."""
import re

P = 'src/components/site/PagePieces.tsx'
src = open(P, encoding='utf-8').read()

SPLIT = "/* ── Sibling paging + hub (CHG-329/330) + next-step map (CHG-337) ─────── */"
idx = src.index(SPLIT)
head, tail = src[:idx], src[idx:]

# presentational part = everything after the import block
imp_end = head.index('/* ── Breadcrumbs')
body = head[imp_end:]

blocks_header = '''import Link from "next/link";
import Image from "next/image";
import { ArrowRight, ArrowUpRight, ChevronRight, Info, Layers, Cog, Factory, FileBarChart2, BookOpen, Boxes, Building2, Compass, UserRound, Mail, Scale, Briefcase, Newspaper, Wrench, MapPin, Handshake, ShieldCheck } from "lucide-react";
import Reveal from "./Reveal";
import { CountUp } from "./Motion";
import { pick as pickImagery } from "./PageImagery";
import { TechDiagram, DIAGRAM_KINDS, type DiagramKind } from "./TechDiagrams";
import { ArchGraph, MetricsDash, DashStyles } from "./ArchDash";
import type { Block, Card, Crumb, PageData } from "@/lib/content";

/* ── PageBlocks — browser-safe presentational pieces.
   Split out of PagePieces so client components (CaseStudies) can import
   them without dragging the server-side content layer into the bundle.
   PagePieces re-exports everything below, so existing imports keep working. */
'''

open('src/components/site/PageBlocks.tsx', 'w', encoding='utf-8').write(blocks_header + body)

pieces_header = '''import Link from "next/link";
import { ArrowUpRight, ChevronRight } from "lucide-react";
import { PageHero, Blocks, CardGrid, RelatedRail, DashStyles } from "./PageBlocks";
import { PatentStrip, OfficesMap } from "./PageAugment";
import { brandData, pageIndex } from "@/lib/content";
import type { Block, PageData } from "@/lib/content";

export { Breadcrumbs, PageHero, Blocks, CtaBand, CardGrid, Quote, RelatedRail, StatsStrip, DashStyles } from "./PageBlocks";

'''
open(P, 'w', encoding='utf-8').write(pieces_header + tail)
print('PageBlocks.tsx written, PagePieces.tsx slimmed')
print('PagePieces now imports:', re.findall(r'import .*', open(P).read())[:6])
