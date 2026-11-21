"use client";

import { useEffect } from "react";

/* ── MotionRuntime v3 — "Motion 100X" ───────────────────────────────────────
   ONE client component, mounted once in the root layout. Everything is
   decorative, pointer/reduced-motion aware, and CSS-driven: the JS here only
   toggles classes/variables, it never animates styles per frame except the
   two rAF loops that must stay smooth (spotlight, parallax).

   Capabilities:
   1.  Scroll choreography registry — sections, [data-reveal], cards, figures
       get .is-inview once; children get index variables (--i) for staggers.
   2.  Word-split headline masks — [data-split] headlines animate per word.
   3.  Scroll-linked parallax — [data-parallax] layers track scroll (rAF).
   4.  3D tilt cards — .tilt-card tracks the pointer (rotateX/Y + glare).
   5.  Magnetic CTAs v2 — pull + tilt + click ripple.
   6.  Cursor spotlight v2 — brand glow that expands over interactive elements.
   7.  Header state — .is-scrolled after 24px (CSS drives shrink/blur).
   8.  Marquee auto-pause — marquees stop when off-screen (perf).
   9.  CountUp assist — flips .count-done when a count finishes (pop beat).
   10. Hero cascade — .dq-hero gets .hero-live on first paint (FOUC guard). */

export default function MotionRuntime() {
  useEffect(() => {
    try {
      const reduced =
        window.matchMedia?.("(prefers-reduced-motion: reduce)").matches ?? false;
      const finePointer =
        window.matchMedia?.("(hover: hover) and (pointer: fine)").matches ?? false;
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
          { threshold: 0.08, rootMargin: "0px 0px -7% 0px" },
        );

        const indexChildren = (el: HTMLElement) => {
          if (staggers.has(el)) return;
          staggers.add(el);
          const kids = el.children;
          for (let i = 0; i < kids.length; i++) {
            (kids[i] as HTMLElement).style.setProperty("--i", String(i));
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
        const t1 = window.setTimeout(observeAll, 350);
        const t2 = window.setTimeout(observeAll, 1200);

        /* ── 8. marquee auto-pause ──────────────────────────────────────── */
        const mio = new IntersectionObserver(
          (entries) => {
            for (const e of entries) {
              (e.target as HTMLElement).classList.toggle("mq-live", e.isIntersecting);
            }
          },
          { threshold: 0 },
        );
        document.querySelectorAll<HTMLElement>(".marquee").forEach((m) => mio.observe(m));

        /* ── 7. header state + scroll progress var ─────────────────────── */
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
            /* parallax layers */
            if (!reduced) {
              document
                .querySelectorAll<HTMLElement>("[data-parallax]")
                .forEach((el) => {
                  const speed = parseFloat(el.getAttribute("data-parallax") || "0.12");
                  const r = el.getBoundingClientRect();
                  const mid = r.top + r.height / 2 - window.innerHeight / 2;
                  el.style.transform = `translate3d(0, ${(-mid * speed).toFixed(1)}px, 0)`;
                });
            }
          });
        };
        window.addEventListener("scroll", onScroll, { passive: true });
        onScroll();

        /* ── 4 + 5 + 6. pointer effects (fine pointers only) ───────────── */
        let cleanupPointer: (() => void) | null = null;
        if (finePointer) {
          /* 6 — spotlight v2 */
          const glow = document.createElement("div");
          glow.id = "dq-cursor-glow";
          glow.setAttribute("aria-hidden", "true");
          document.body.appendChild(glow);
          let mx = -600, my = -600, gx = mx, gy = my;
          let active = false;
          let raf = 0;
          const tick = () => {
            gx += (mx - gx) * 0.14;
            gy += (my - gy) * 0.14;
            glow.style.transform = `translate3d(${gx}px, ${gy}px, 0)`;
            if (active || Math.abs(mx - gx) > 1) {
              raf = requestAnimationFrame(tick);
            } else {
              raf = 0;
            }
          };
          const onMove = (ev: MouseEvent) => {
            mx = ev.clientX;
            my = ev.clientY;
            if (!active) {
              active = true;
              if (!raf) raf = requestAnimationFrame(tick);
            }
            const hot = (ev.target as Element | null)?.closest?.("a, button, [role='button']");
            glow.classList.toggle("glow-hot", !!hot);

            /* 5 — magnetic CTAs */
            document.querySelectorAll<HTMLElement>("a.btn-sheen, button.btn-sheen").forEach((el) => {
              const r = el.getBoundingClientRect();
              const cx = r.left + r.width / 2;
              const cy = r.top + r.height / 2;
              const dx = ev.clientX - cx;
              const dy = ev.clientY - cy;
              const dist = Math.hypot(dx, dy);
              const reach = Math.max(130, r.width);
              if (dist < reach) {
                el.style.transform = `translate(${(dx * 0.14).toFixed(1)}px, ${(dy * 0.2).toFixed(1)}px)`;
                el.style.setProperty("--mx", `${(ev.clientX - r.left).toFixed(0)}px`);
                el.style.setProperty("--my", `${(ev.clientY - r.top).toFixed(0)}px`);
              } else if (el.style.transform) {
                el.style.transform = "";
              }
            });

            /* 4 — tilt cards */
            document.querySelectorAll<HTMLElement>(".tilt-card").forEach((el) => {
              const r = el.getBoundingClientRect();
              if (
                ev.clientX < r.left - 80 || ev.clientX > r.right + 80 ||
                ev.clientY < r.top - 80 || ev.clientY > r.bottom + 80
              ) {
                if (el.style.transform) {
                  el.style.transform = "";
                  el.style.setProperty("--gx", "50%");
                  el.style.setProperty("--gy", "50%");
                }
                return;
              }
              const px = (ev.clientX - r.left) / r.width;
              const py = (ev.clientY - r.top) / r.height;
              const rx = (0.5 - py) * 7;
              const ry = (px - 0.5) * 9;
              el.style.transform = `perspective(900px) rotateX(${rx.toFixed(2)}deg) rotateY(${ry.toFixed(2)}deg) translateY(-3px)`;
              el.style.setProperty("--gx", `${(px * 100).toFixed(0)}%`);
              el.style.setProperty("--gy", `${(py * 100).toFixed(0)}%`);
            });
          };
          window.addEventListener("mousemove", onMove, { passive: true });
          raf = requestAnimationFrame(tick);

          /* ripple on CTA click */
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

          cleanupPointer = () => {
            window.removeEventListener("mousemove", onMove);
            window.removeEventListener("click", onClick);
            if (raf) cancelAnimationFrame(raf);
            glow.remove();
          };
        }

        /* ── 9. CountUp done-beat ───────────────────────────────────────── */
        const cio = new IntersectionObserver(
          (entries) => {
            for (const e of entries) {
              if (e.isIntersecting) {
                (e.target as HTMLElement).classList.add("count-live");
                cio.unobserve(e.target);
              }
            }
          },
          { threshold: 0.4 },
        );
        document.querySelectorAll<HTMLElement>("[data-countup], .tabular-nums").forEach((el) => {
          if (el.textContent && /\d/.test(el.textContent)) cio.observe(el);
        });

        return () => {
          window.clearTimeout(t1);
          window.clearTimeout(t2);
          io?.disconnect();
          mio.disconnect();
          cio.disconnect();
          window.removeEventListener("scroll", onScroll);
          if (scrollRaf) cancelAnimationFrame(scrollRaf);
          cleanupPointer?.();
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
