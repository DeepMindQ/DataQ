"use client";

import { useEffect, useState } from "react";

/* Consent-gated, privacy-friendly analytics loader (Top-20 #5 / #17).
   - Loads Plausible ONLY after the visitor chose "Accept analytics".
   - Nothing loads on "Essential only" — no requests, no storage beyond the
     consent record itself (dqs-cookie-consent, set by CookieConsent.tsx).
   - Env-driven: NEXT_PUBLIC_PLAUSIBLE_SRC (script origin, e.g. the CE-edition
     or cloud host) + NEXT_PUBLIC_PLAUSIBLE_DOMAIN (site identity). When the
     env is absent — e.g. before an account exists — NOTHING loads and the
     consent choice is simply stored for when it does. No fake requests. */

const CONSENT_KEY = "dqs-cookie-consent";
const CONSENT_EVENT = "dqs-consent-change";

declare global {
  interface Window {
    plausible?: (event: string, options?: { props?: Record<string, string> }) => void;
  }
}

/** Fire a custom event only when Plausible is actually active. */
export function trackEvent(event: string, props?: Record<string, string>) {
  try {
    window.plausible?.(event, props ? { props } : undefined);
  } catch {
    /* analytics must never break UX */
  }
}

export default function ConsentAnalytics() {
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    const src = process.env.NEXT_PUBLIC_PLAUSIBLE_SRC;
    const domain = process.env.NEXT_PUBLIC_PLAUSIBLE_DOMAIN;
    if (!src || !domain) return; // no account configured yet — stay inert

    const maybeLoad = (choice: string | null) => {
      if (choice !== "all") return;
      setLoaded((prev) => {
        if (prev) return prev;
        const s = document.createElement("script");
        s.defer = true;
        s.dataset.domain = domain;
        s.src = src;
        document.head.appendChild(s);
        return true;
      });
    };

    let stored: string | null = null;
    try {
      stored = window.localStorage.getItem(CONSENT_KEY);
    } catch {
      stored = null;
    }
    maybeLoad(stored);

    const onChange = (e: Event) => {
      const detail = (e as CustomEvent<string | null>).detail;
      maybeLoad(detail);
    };
    window.addEventListener(CONSENT_EVENT, onChange);
    return () => window.removeEventListener(CONSENT_EVENT, onChange);
  }, []);

  return null;
}
