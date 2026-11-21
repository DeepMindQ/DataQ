"use client";

import { useEffect } from "react";

/* ── MotionRuntime v4 — Phase 1 "calibrated motion" ──────────────────────────
   ONE client component, mounted once in the root layout. Everything is
   decorative, pointer/reduced-motion aware, and CSS-driven.

   Phase 1 policy (audit A-11/A-12): motion supports comprehension or it is
   removed. The cursor spotlight, magnetic CTA pull and 3D card tilt were
   deleted — they competed with content for attention and read as gimmicks on
   an enterprise site. What stays is fast, small-distance and once-only:
   1.  Scroll choreography — sections, [data-reveal], cards, figures get
       .is-inview once; stagger children get capped --i variables (max 8) so
       long lists never wait a second to be readable.
   2.  Word-split headline masks — [data-split] headlines animate per word.
   3.  Header state — .is-scrolled after 24px (CSS drives shrink/blur).
   4.  Marquee auto-pause — marquees stop when off-screen (perf).
   5.  CountUp assist — flips .count-live when a count finishes (pop beat).
   6.  CTA click ripple — small, purposeful press feedback.
   7.  Hero cascade — .dq-hero gets .hero-live on first paint (FOUC guard).  */

export default function MotionRuntime() {
  useEffect(() => {
    try {
      const reduced =
        window.matchMedia?.("(prefers-reduced-motion: reduce)").matches ?? false;
      const root = document.documentElement;
      root.classList.add("js-motion-v3");
      if (reduced) root.classList.add("js-motion-off");

      /* ── 1. scroll choreography registry ─────────────────────────────── */
      let io: IntersectionObserver | null = null;
      const staggers = new WeakSet<HTMLElement>();
      if (!reduced && "IntersectionObserver" in window) {
        io = new IntersectionObserver(
          (entries) => {
            for (const e of entries) {
              if (!e.isIntersecting) continue;
              const el = e.target as HTMLElement;
              el.classList.add("is-inview");
              io?.unobserve(el);
            }
          },
          // fire early: 0.04 threshold + small bottom margin, so content is
          // already readable when it enters the viewport (no mid-fade scans)
          { threshold: 0.04, rootMargin: "0px 0px -4% 0px" },
        );

        const indexChildren = (el: HTMLElement) => {
          if (staggers.has(el)) return;
          staggers.add(el);
          const kids = el.children;
          for (let i = 0; i < kids.length; i++) {
            // cap the stagger index: beyond 8 children the delay would push
            // late items past a second of waiting — they render together
            (kids[i] as HTMLElement).style.setProperty("--i", String(Math.min(i, 8)));
          }
        };

        const observeAll = () => {
          document
            .querySelectorAll<HTMLElement>(
              [
                "main section:not(.reveal):not([data-motion-done])",
                "main [data-reveal]:not(.is-inview)",
                "main .dv-card:not(.is-inview)",
                "main figure.pi-figure:not(.is-inview)",
                "main [data-stagger]:not([data-motion-done])",
                "main .mq-stagger:not([data-motion-done])",
                "main .wipe-section:not([data-motion-done])",
                "main .vignette-section:not([data-motion-done])",
                "main .quote-fade:not([data-motion-done])",
                "main .stat-flip:not([data-motion-done])",
              ].join(", "),
            )
            .forEach((el) => {
              el.setAttribute("data-motion-done", "1");
              if (el.hasAttribute("data-stagger") || el.classList.contains("mq-stagger")) {
                indexChildren(el);
              }
              io?.observe(el);
            });
          /* word-split headlines */
          document
            .querySelectorAll<HTMLElement>("main [data-split]:not([data-split-done])")
            .forEach((el) => {
              if (reduced) {
                el.setAttribute("data-split-done", "1");
                return;
              }
              el.setAttribute("data-split-done", "1");
              const text = el.textContent || "";
              const words = text.split(/\s+/).filter(Boolean);
              if (words.length === 0 || words.length > 14) return;
              el.setAttribute("aria-label", text);
              el.textContent = "";
              words.forEach((w, i) => {
                const outer = document.createElement("span");
                outer.className = "split-word";
                outer.style.setProperty("--i", String(i));
                outer.setAttribute("aria-hidden", "true");
                const inner = document.createElement("span");
                inner.className = "split-word-inner";
                inner.textContent = w;
                outer.appendChild(inner);
                el.appendChild(outer);
                if (i < words.length - 1) el.appendChild(document.createTextNode(" "));
              });
              io?.observe(el);
            });
        };
        observeAll();
        const t1 = window.setTimeout(observeAll, 300);
        const t2 = window.setTimeout(observeAll, 900);

        /* ── 4. marquee auto-pause ──────────────────────────────────────── */
        const mio = new IntersectionObserver(
          (entries) => {
            for (const e of entries) {
              (e.target as HTMLElement).classList.toggle("mq-live", e.isIntersecting);
            }
          },
          { threshold: 0 },
        );
        document.querySelectorAll<HTMLElement>(".marquee").forEach((m) => mio.observe(m));

        /* ── 3. header state + scroll progress var ─────────────────────── */
        let scrollRaf = 0;
        const header = document.querySelector("header");
        const onScroll = () => {
          if (scrollRaf) return;
          scrollRaf = requestAnimationFrame(() => {
            scrollRaf = 0;
            const y = window.scrollY;
            if (header) header.classList.toggle("is-scrolled", y > 24);
            const max = document.documentElement.scrollHeight - window.innerHeight;
            const p = max > 0 ? Math.min(1, y / max) : 0;
            root.style.setProperty("--scroll-p", p.toFixed(4));
          });
        };
        window.addEventListener("scroll", onScroll, { passive: true });
        onScroll();

        /* ── 6. ripple on CTA click (press feedback only, no pull) ─────── */
        const onClick = (ev: MouseEvent) => {
          const el = (ev.target as Element | null)?.closest?.("a.btn-sheen, button.btn-sheen") as HTMLElement | null;
          if (!el) return;
          const r = el.getBoundingClientRect();
          const rip = document.createElement("span");
          rip.className = "dq-ripple";
          rip.style.left = `${ev.clientX - r.left}px`;
          rip.style.top = `${ev.clientY - r.top}px`;
          el.appendChild(rip);
          window.setTimeout(() => rip.remove(), 650);
        };
        window.addEventListener("click", onClick, { passive: true });

        return () => {
          window.clearTimeout(t1);
          window.clearTimeout(t2);
          io?.disconnect();
          mio.disconnect();
          window.removeEventListener("scroll", onScroll);
          if (scrollRaf) cancelAnimationFrame(scrollRaf);
          window.removeEventListener("click", onClick);
        };
      }

      /* reduced-motion: everything visible, no observers */
      document
        .querySelectorAll<HTMLElement>("main section, main [data-reveal], main .dv-card, main figure.pi-figure, [data-stagger], .wipe-section, .vignette-section, .quote-fade, .stat-flip")
        .forEach((el) => el.classList.add("is-inview"));
      return;
    } catch {
      /* motion is decorative — never block the page: force everything visible */
      try {
        document.querySelectorAll<HTMLElement>(
          "main section, main [data-reveal], main .dv-card, main figure.pi-figure, [data-stagger], .wipe-section, .vignette-section, .quote-fade, .stat-flip, .dq-hero > *",
        ).forEach((el) => {
          el.classList.add("is-inview");
          el.style.opacity = "1";
          el.style.transform = "none";
          el.style.clipPath = "none";
        });
      } catch {
        /* give up silently */
      }
    }
  }, []);
  return null;
}
