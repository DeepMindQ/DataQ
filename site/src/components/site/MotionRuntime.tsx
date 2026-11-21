"use client";

import { useEffect } from "react";

/* ── MotionRuntime (Wave 2) ─────────────────────────────────────────
   ONE client component, mounted once in the root layout.
   Observes sections, chart cards and explicit [data-reveal] markers
   across the whole server-rendered site and toggles .is-inview so CSS
   drives all scroll choreography. No per-page JavaScript needed. */
export default function MotionRuntime() {
  useEffect(() => {
    try {
      if (window.matchMedia?.("(prefers-reduced-motion: reduce)").matches) return;
      if (!("IntersectionObserver" in window)) return;

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
      // late-mounted sections (e.g. after route transitions with prefetch)
      const t = window.setTimeout(observeAll, 400);
      return () => {
        window.clearTimeout(t);
        io.disconnect();
      };
    } catch {
      /* motion is decorative — never block the page */
    }
  }, []);
  return null;
}
