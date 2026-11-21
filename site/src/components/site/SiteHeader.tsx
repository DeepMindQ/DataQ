"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  ChevronDown, Menu, X, ArrowRight, Search, Sparkles, Bot, Database, ShieldCheck,
  Cloud, Atom, Link2, Factory, Landmark, HeartPulse, Building2, TrendingUp,
  ShieldAlert, Gauge, Users, Boxes, Compass as CompassIcon, BookOpen, Newspaper,
  Handshake, Phone, Layers, BrainCircuit, CircleDot,
} from "lucide-react";
import Logo from "./Logo";
import { SearchOverlay, SkipLink, AnnouncementBar, StickyMobileCTA } from "./Wave3";
import type { Brand, Nav } from "@/lib/content";

/* ── icon + blurb per mega column (professional megamenu) ─────────────── */
const COL_META: Record<string, { icon: React.ComponentType<{ className?: string }>; blurb: string }> = {
  // services
  "Applied AI & Generative AI": { icon: BrainCircuit, blurb: "Production AI measured on the P&L" },
  "Agentic AI & Hyperautomation": { icon: Bot, blurb: "Governed digital workers at scale" },
  "Data, Analytics & Lakehouse": { icon: Database, blurb: "Pipelines, models and governance" },
  "Cybersecurity & Zero-Trust": { icon: ShieldCheck, blurb: "Identity-first security architecture" },
  "Cloud, Edge & Platform Engineering": { icon: Cloud, blurb: "Reliable estates, lower unit cost" },
  "Quantum & Advanced Compute": { icon: Atom, blurb: "Optimization and PQC migration" },
  "Blockchain & Digital Trust": { icon: Link2, blurb: "Permissioned networks and credentials" },
  "IoT, Digital Twin & Robotics": { icon: Factory, blurb: "From sensor data to actuation" },
  // industries
  "Financial Services & Insurance": { icon: Landmark, blurb: "Banking, payments and insurance" },
  "Health, Public Sector & Education": { icon: HeartPulse, blurb: "Care, government and research" },
  "Industry, Retail & Commerce": { icon: Factory, blurb: "Plants, stores and supply chains" },
  "Energy, Infrastructure & Technology": { icon: Gauge, blurb: "Grids, networks and platforms" },
  // solutions
  "Growth & Revenue": { icon: TrendingUp, blurb: "Pricing, commerce and CX" },
  "Risk & Resilience": { icon: ShieldAlert, blurb: "Fraud, cyber and scenario risk" },
  "Operational Excellence": { icon: Gauge, blurb: "Automation, assets and IT ops" },
  "Workforce & Experience": { icon: Users, blurb: "Copilots and service orchestration" },
  // platforms
  "Dataq Nexus — Decision Intelligence": { icon: CircleDot, blurb: "Millisecond decisions with full replay" },
  "Dataq Forge — Data & Lakehouse": { icon: Database, blurb: "The estate every program builds on" },
  "Dataq Swarm — Agent Orchestration": { icon: Bot, blurb: "Agent fleets with queues and budgets" },
  "Dataq Sentinel — Security Fabric": { icon: ShieldCheck, blurb: "Controls for people, machines, models" },
  "Dataq Twinverse — Digital Twin Ops": { icon: Boxes, blurb: "Simulate, then act on physical assets" },
  "Dataq Quanta — Advanced Compute": { icon: Atom, blurb: "Quantum-inspired optimization, benchmarked" },
  "Dataq Ledger — Digital Trust": { icon: Link2, blurb: "Shared records regulators can inspect" },
  "Dataq Compass — AI Governance": { icon: CompassIcon, blurb: "Model risk, validation and monitoring" },
  // insights / about
  "AI & Data viewpoints": { icon: BrainCircuit, blurb: "Field notes on production AI" },
  "Automation & operations viewpoints": { icon: Bot, blurb: "What actually scales" },
  "Security, cloud & trust viewpoints": { icon: ShieldCheck, blurb: "Controls that survive audit" },
  "Emerging compute viewpoints": { icon: Atom, blurb: "Where the math pays back" },
  "Company": { icon: Building2, blurb: "Who we are and how we operate" },
  "Our Approach": { icon: Layers, blurb: "The method behind every program" },
  "Join & Contact": { icon: Handshake, blurb: "Careers, news and offices" },
};
function colMeta(label: string) {
  return COL_META[label] ?? { icon: Sparkles, blurb: "" };
}

/* group meta for insights columns rendered as link lists */

function MegaPanel({
  item,
  open,
  forceDrawer,
  onCancelClose,
  onScheduleClose,
}: {
  item: Nav["primary"][number];
  open: boolean;
  forceDrawer: boolean;
  onCancelClose: () => void;
  onScheduleClose: () => void;
}) {
  if (!item.mega) return null;
  const cols = item.mega.length;
  const gridCls =
    cols >= 8 ? "lg:grid-cols-4" : cols >= 4 ? "lg:grid-cols-4" : "md:grid-cols-3";
  return (
    /* Anchored to the full-width header bar (inset-x-0), NOT the nav item.
       The panel spans the viewport; content stays inside container-dq.
       When the fit-guard forces drawer mode, panels never render. */
    <div
      className={`absolute inset-x-0 top-full hidden xl:block ${forceDrawer ? "!hidden" : ""} ${open ? "" : "pointer-events-none"}`}
      style={{ visibility: open ? "visible" : "hidden" }}
      onMouseEnter={onCancelClose}
      onMouseLeave={onScheduleClose}
    >
      <div
        className={`mega-panel border-t border-line bg-white shadow-3 ${open ? "" : "mega-hidden"}`}
        role="region"
        aria-label={`${item.label} menu`}
      >
        <div className="container-dq py-7">
          <div className={`grid gap-x-7 gap-y-6 ${gridCls}`}>
            {item.mega.map((col) => {
              const meta = colMeta(col.label);
              const Icon = meta.icon;
              return (
                <div key={col.label + col.url} className="min-w-0">
                  <Link
                    href={col.url}
                    className="group flex items-start gap-3 rounded-lg p-2 -mx-2 transition-colors hover:bg-brand-tint/70"
                    tabIndex={open ? 0 : -1}
                  >
                    <span className="mt-0.5 flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-navy-800 text-white shadow-1 transition-colors group-hover:bg-brand">
                      <Icon className="h-4 w-4" aria-hidden="true" />
                    </span>
                    <span className="min-w-0">
                      <span className="flex items-center gap-1 text-[13.5px] font-semibold leading-snug text-navy-800 group-hover:text-brand-deep">
                        {col.label}
                        <ArrowRight className="h-3 w-3 shrink-0 text-brand transition group-hover:translate-x-0.5" aria-hidden="true" />
                      </span>
                      {meta.blurb && (
                        <span className="mt-0.5 block text-[11.5px] leading-snug text-slate-body/70">
                          {meta.blurb}
                        </span>
                      )}
                    </span>
                  </Link>
                  {col.children.length > 0 && (
                    <ul className="mt-1.5 space-y-0.5 border-l border-line pl-3 ml-[14px]">
                      {col.children.slice(0, 8).map((ch) => (
                        <li key={ch.label + ch.url}>
                          <Link
                            href={ch.url}
                            className="block truncate rounded px-1 py-1 text-[12.5px] leading-snug text-slate-body/80 transition-colors hover:bg-mist hover:text-navy-800"
                            tabIndex={open ? 0 : -1}
                          >
                            {ch.label}
                          </Link>
                        </li>
                      ))}
                      {col.children.length > 8 && (
                        <li className="px-1 pt-0.5 text-[11.5px] font-medium text-brand-deep">
                          +{col.children.length - 8} more
                        </li>
                      )}
                    </ul>
                  )}
                </div>
              );
            })}
          </div>
          {/* featured strip (CHG-352) — a next step on every wide panel */}
          <div className="mt-6 flex flex-wrap items-center justify-between gap-3 rounded-xl border border-brand/25 bg-brand-tint px-4 py-3">
            <p className="text-[12.5px] leading-snug text-slate-body/85">
              <span className="font-semibold text-navy-800">Not sure where to start?</span>{" "}
              A 45-minute briefing maps your metric to the right entry point.
            </p>
            <div className="flex flex-wrap gap-2">
              <Link
                href="/book-a-briefing/"
                tabIndex={open ? 0 : -1}
                className="inline-flex items-center gap-1 rounded-lg bg-brand px-3 py-1.5 text-[11.5px] font-semibold text-white transition hover:bg-brand-hover"
              >
                Book a briefing <ArrowRight className="h-3 w-3" aria-hidden="true" />
              </Link>
              <Link
                href="/value-assessment/"
                tabIndex={open ? 0 : -1}
                className="inline-flex items-center rounded-lg border border-line bg-white px-3 py-1.5 text-[11.5px] font-semibold text-navy-800 transition hover:border-brand"
              >
                Value assessment
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function SiteHeader({ nav, brand }: { nav: Nav; brand: Brand }) {
  const [openItem, setOpenItem] = useState<string | null>(null);
  const [mobileOpen, setMobileOpen] = useState(false);
  const [mobileSection, setMobileSection] = useState<string | null>(null);
  const [scrolled, setScrolled] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);
  /* fit-guard (round-2 hardening): if the desktop nav row cannot physically fit
     the viewport — Windows/Mac font metrics, browser zoom, 1280px laptops at
     100%/125% scaling — force the drawer mode instead of letting the menu
     overflow off-screen. Measured, not assumed: works on every device. */
  const [forceDrawer, setForceDrawer] = useState(false);
  const closeTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const rowRef = useRef<HTMLDivElement | null>(null);
  const navRef = useRef<HTMLElement | null>(null);
  const forceDrawerRef = useRef(false);
  const navRequired = useRef(0);
  forceDrawerRef.current = forceDrawer;
  const pathname = usePathname();

  useEffect(() => {
    // Slack = logo (~150px) + right cluster (~200px) + gaps/padding (~120px).
    // Two thresholds (overflow on force, generous margin on un-force) give
    // hysteresis so the mode can never ping-pong at a boundary width.
    const UNFORCE_SLACK = 480;
    const check = () => {
      const row = rowRef.current;
      const nav = navRef.current;
      if (!row || !nav) return;
      try {
        if (forceDrawerRef.current) {
          // drawer mode: nav is display:none — estimate from last known width
          if (row.clientWidth > navRequired.current + UNFORCE_SLACK) setForceDrawer(false);
        } else if (nav.offsetParent !== null) {
          // desktop mode: nav laid out — remember its real requirement, force
          // the drawer the moment it cannot fit its allotted space
          navRequired.current = nav.scrollWidth;
          if (nav.scrollWidth > nav.clientWidth + 2) setForceDrawer(true);
        }
      } catch {}
    };
    check();
    window.addEventListener("resize", check);
    const t1 = setTimeout(check, 300);
    try {
      (document as Document & { fonts?: { ready?: Promise<unknown> } }).fonts?.ready?.then(check).catch(() => {});
    } catch {}
    return () => {
      window.removeEventListener("resize", check);
      clearTimeout(t1);
    };
  }, []);

  useEffect(() => {
    // re-settle after every mode change (one short re-check, hysteresis damped)
    const t = setTimeout(() => {
      const row = rowRef.current;
      const nav = navRef.current;
      if (!row || !nav) return;
      try {
        if (!forceDrawer && nav.offsetParent !== null && nav.scrollWidth > nav.clientWidth + 2) {
          setForceDrawer(true);
        }
      } catch {}
    }, 80);
    return () => clearTimeout(t);
  }, [forceDrawer, pathname]);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    // close menus after navigation (deferred to avoid cascading render)
    const t = setTimeout(() => {
      setOpenItem(null);
      setMobileOpen(false);
      setMobileSection(null);
    }, 0);
    return () => clearTimeout(t);
  }, [pathname]);

  const scheduleClose = useCallback(() => {
    closeTimer.current = setTimeout(() => setOpenItem(null), 140);
  }, []);
  const cancelClose = useCallback(() => {
    if (closeTimer.current) clearTimeout(closeTimer.current);
  }, []);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setOpenItem(null);
        setMobileOpen(false);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  return (
    <header className="sticky top-0 z-50">
      <SkipLink />
      {/* announcement bar (CHG-381) */}
      <AnnouncementBar message="Eight patented method families now power every Dataq engagement — see how" href="/patented-intelligence/" />
      {/* utility bar — brand navy (CHG-010) */}
      <div className="bg-navy-900 text-white/70 text-[11.5px]">
        <div className="container-dq flex h-8 items-center justify-between">
          <p className="tracking-wide truncate">
            SOC 2 Type II · ISO 27001 · ISO 9001 · HIPAA-ready pods
          </p>
          <div className="hidden md:flex items-center gap-4">
            <Link href="/status/" className="hover:text-brand-300">System status</Link>
            <a href={`mailto:${brand.emails.general}`} className="hover:text-brand-300">
              {brand.emails.general}
            </a>
          </div>
        </div>
      </div>

      {/* main bar — `relative` anchors the full-width megamenu below */}
      <div
        className={`relative border-b border-line bg-white/95 backdrop-blur transition-shadow ${scrolled ? "shadow-2" : ""}`}
      >
        {/* scroll condense (CHG-357) + overflow-x-clip: nothing inside the bar can
            paint outside the viewport in any rendering condition. rowRef feeds the
            fit-guard below (menu collapses to drawer if it cannot fit). */}
        <div
          ref={rowRef}
          className={`container-dq flex flex-nowrap items-center justify-between gap-4 overflow-x-clip transition-[height] duration-300 ${scrolled ? "h-[56px]" : "h-[72px]"}`}
        >
          <Link href="/" aria-label="Dataq Software home" className="shrink-0">
            <Logo height={40} />
          </Link>

          {/* desktop nav — icon-free, compact items with chevrons; the fit-guard
              force-collapses it to the drawer whenever the row overflows, so on
              Windows/Mac laptops, browser zoom or unusual font metrics the menu
              can never leave the viewport — the drawer takes over instead. */}
          <nav
            ref={navRef}
            aria-label="Primary"
            className={`hidden xl:flex items-center gap-0.5 min-w-0 overflow-x-clip ${forceDrawer ? "!hidden" : ""}`}
          >
            {nav.primary.map((item) => {
              const isOpen = openItem === item.label;
              return (
                <div
                  key={item.label}
                  className="relative"
                  onMouseEnter={() => {
                    cancelClose();
                    setOpenItem(item.mega ? item.label : null);
                  }}
                  onMouseLeave={item.mega ? scheduleClose : undefined}
                >
                  <Link
                    href={item.url}
                    data-active={pathname.startsWith(item.url)}
                    aria-current={pathname === item.url ? "page" : undefined}
                    onClick={(e) => {
                      // first tap/click opens the panel; second click navigates.
                      if (item.mega && openItem !== item.label) {
                        e.preventDefault();
                        setOpenItem(item.label);
                      }
                    }}
                    className={`nav-link flex items-center gap-1 px-3.5 py-2.5 text-[13.5px] font-medium whitespace-nowrap rounded-md transition-colors ${
                      pathname.startsWith(item.url)
                        ? "text-brand-deep"
                        : "text-navy-800 hover:text-brand-deep"
                    }`}
                    aria-expanded={item.mega ? isOpen : undefined}
                    onFocus={() => setOpenItem(item.mega ? item.label : null)}
                  >
                    {item.label}
                    {item.mega && (
                      <ChevronDown
                        className={`h-3.5 w-3.5 opacity-55 transition-transform duration-200 ${isOpen ? "rotate-180" : ""}`}
                        aria-hidden="true"
                      />
                    )}
                  </Link>
                </div>
              );
            })}
          </nav>

          <div className="flex shrink-0 items-center gap-2.5">
            {/* header search entry (CHG-358) */}
            <button
              type="button"
              onClick={() => setSearchOpen(true)}
              aria-label="Search the site"
              className="inline-flex h-9 w-9 items-center justify-center rounded-[10px] border border-line text-navy-800 transition hover:border-brand hover:text-brand-deep"
            >
              <Search className="h-4 w-4" aria-hidden="true" />
            </button>
            {/* primary action: solid orange (CHG-012) with sheen (CHG-053) */}
            <Link
              href={nav.cta.url}
              className="btn-sheen hidden sm:inline-flex items-center rounded-[10px] bg-brand px-4 py-2.5 text-[13px] font-semibold text-white transition-colors hover:bg-brand-hover"
            >
              {nav.cta.label}
            </Link>
            <button
              className={`xl:hidden inline-flex h-10 w-10 items-center justify-center rounded-[10px] border border-line ${forceDrawer ? "!inline-flex" : ""}`}
              aria-label="Open menu"
              aria-expanded={mobileOpen}
              onClick={() => setMobileOpen((v) => !v)}
            >
              {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
            </button>
          </div>
        </div>

        {/* megamenu — one full-width panel per mega item, exactly viewport-wide */}
        {nav.primary
          .filter((item) => item.mega)
          .map((item) => (
            <MegaPanel
              key={item.label}
              item={item}
              open={openItem === item.label}
              forceDrawer={forceDrawer}
              onCancelClose={cancelClose}
              onScheduleClose={scheduleClose}
            />
          ))}
      </div>

      {/* mobile drawer — drawer-scroll caps height at the dynamic viewport
          (see .drawer-scroll in globals.css) so the CTA never slides under
          mobile browser toolbars */}
      {mobileOpen && (
        <div
          className={`drawer-scroll xl:hidden border-b border-line bg-white shadow-3 overflow-y-auto ${forceDrawer ? "!block" : ""}`}
        >
          <div className="container-dq space-y-1 pt-4 pb-[calc(1rem+env(safe-area-inset-bottom))]">
            {nav.primary.map((item) => (
              <div key={item.label} className="border-b border-line/70 last:border-0">
                <div className="flex items-center justify-between">
                  <Link href={item.url} className="py-3 text-[15px] font-semibold text-navy-800">
                    {item.label}
                  </Link>
                  {item.mega && (
                    <button
                      aria-label={`Expand ${item.label}`}
                      aria-expanded={mobileSection === item.label}
                      className="h-9 w-9 inline-flex items-center justify-center rounded-[10px] hover:bg-mist"
                      onClick={() => setMobileSection(mobileSection === item.label ? null : item.label)}
                    >
                      <ChevronDown
                        className={`h-4 w-4 transition-transform ${mobileSection === item.label ? "rotate-180" : ""}`}
                      />
                    </button>
                  )}
                </div>
                {item.mega && mobileSection === item.label && (
                  <div className="pb-4 space-y-3">
                    {item.mega.map((col) => {
                      const meta = colMeta(col.label);
                      const Icon = meta.icon;
                      return (
                        <div key={col.label + col.url}>
                          <Link href={col.url} className="flex items-center gap-2 text-[13px] font-semibold text-brand-deep">
                            <Icon className="h-3.5 w-3.5" aria-hidden="true" /> {col.label}
                          </Link>
                          {col.children.length > 0 && (
                            <ul className="mt-1 space-y-1 pl-3">
                              {col.children.map((ch) => (
                                <li key={ch.label + ch.url}>
                                  <Link href={ch.url} className="text-[12.5px] text-slate-body/80">
                                    {ch.label}
                                  </Link>
                                </li>
                              ))}
                            </ul>
                          )}
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            ))}
            <Link
              href={nav.cta.url}
              className="mt-3 flex items-center justify-center rounded-[10px] bg-brand px-4 py-3 text-[14px] font-semibold text-white hover:bg-brand-hover"
            >
              {nav.cta.label}
            </Link>
          </div>
        </div>
      )}
      {/* sticky mobile CTA bar (CHG-362) */}
      <StickyMobileCTA cta={nav.cta} />

      {/* instant search overlay (CHG-359) */}
      {searchOpen && <SearchOverlay close={() => setSearchOpen(false)} />}
    </header>
  );
}
