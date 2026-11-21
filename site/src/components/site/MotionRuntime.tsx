"use client";

import { useEffect } from "react";

/* ── MotionRuntime v2 (Wave 2) ──────────────────────────────────────
   ONE client component, mounted once in the root layout:
   1. Scroll choreography — observes sections / chart cards / [data-reveal]
      and toggles .is-inview (CSS drives all transitions).
   2. Cursor spotlight — a soft brand-glow that follows the pointer.
   3. Magnetic CTAs — .btn-sheen elements lean toward the cursor.
   All effects are pointer/reduced-motion aware and purely decorative. */
export default function MotionRuntime() {
  useEffect(() => {
    try {
      const reduced = window.matchMedia?.("(prefers-reduced-motion: reduce)").matches;
      const finePointer = window.matchMedia?.("(hover: hover) and (pointer: fine)").matches;

      /* 1 — scroll choreography */
      if (!reduced && "IntersectionObserver" in window) {
        const io = new IntersectionObserver(
          (entries) => {
            for (const e of entries) {
              if (e.isIntersecting) {
                (e.target as HTMLElement).classList.add("is-inview");
                io.unobserve(e.target);
              }
            }
          },
          { threshold: 0.05, rootMargin: "0px 0px -6% 0px" },
        );
        const observeAll = () => {
          document
            .querySelectorAll<HTMLElement>(
              "main section:not(.reveal):not([data-motion-done]), main [data-reveal]:not(.is-inview), main .dv-card:not(.is-inview), main figure.pi-figure:not(.is-inview)",
            )
            .forEach((el) => {
              el.setAttribute("data-motion-done", "1");
              io.observe(el);
            });
        };
        observeAll();
        const t = window.setTimeout(observeAll, 400);

        /* 2 — cursor spotlight + 3 — magnetic CTAs */
        if (finePointer) {
          const glow = document.createElement("div");
          glow.id = "dq-cursor-glow";
          document.body.appendChild(glow);
          let mx = -600, my = -600, gx = mx, gy = my;
          let raf = 0;
          const tick = () => {
            gx += (mx - gx) * 0.12;
            gy += (my - gy) * 0.12;
            glow.style.transform = `translate3d(${gx}px, ${gy}px, 0)`;
            glow.style.opacity = "1";
            raf = requestAnimationFrame(tick);
          };
          const onMove = (ev: MouseEvent) => {
            mx = ev.clientX;
            my = ev.clientY;
            glow.style.opacity = "1";
            /* magnetic pull on nearby CTAs */
            document.querySelectorAll<HTMLElement>("a.btn-sheen").forEach((el) => {
              const r = el.getBoundingClientRect();
              const cx = r.left + r.width / 2;
              const cy = r.top + r.height / 2;
              const dx = ev.clientX - cx;
              const dy = ev.clientY - cy;
              const dist = Math.hypot(dx, dy);
              if (dist < 130) {
                el.style.transform = `translate(${dx * 0.16}px, ${dy * 0.22}px)`;
              } else if (el.style.transform) {
                el.style.transform = "";
              }
            });
          };
          window.addEventListener("mousemove", onMove, { passive: true });
          raf = requestAnimationFrame(tick);
          return () => {
            window.removeEventListener("mousemove", onMove);
            cancelAnimationFrame(raf);
            glow.remove();
            window.clearTimeout(t);
            io.disconnect();
          };
        }
        return () => {
          window.clearTimeout(t);
          io.disconnect();
        };
      }
      return;
    } catch {
      /* motion is decorative — never block the page */
    }
  }, []);
  return null;
}
