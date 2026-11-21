"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Cookie } from "lucide-react";

const KEY = "dqs-cookie-consent";

export default function CookieConsent() {
  const [choice, setChoice] = useState<string | null>(null);

  useEffect(() => {
    // read stored consent (deferred to avoid cascading render on mount)
    const t = setTimeout(() => {
      try {
        setChoice(window.localStorage.getItem(KEY));
      } catch {
        setChoice(null);
      }
    }, 0);
    return () => clearTimeout(t);
  }, []);

  function decide(value: "all" | "essential") {
    try {
      window.localStorage.setItem(KEY, value);
    } catch {
      /* storage unavailable */
    }
    setChoice(value);
  }

  if (choice !== null) return null;

  return (
    <div
      role="dialog"
      aria-label="Cookie consent"
      className="fixed bottom-4 left-4 right-4 z-[60] mx-auto max-w-3xl rounded-2xl border border-navy-600 bg-navy-800 p-5 shadow-3"
    >
      <div className="flex items-start gap-3">
        <Cookie className="mt-0.5 h-5 w-5 shrink-0 text-brand-300" />
        <div className="flex-1">
          <p className="text-[13.5px] font-semibold text-white">Cookies, on your terms</p>
          <p className="mt-1 text-[12.5px] leading-relaxed text-white/65">
            We use essential cookies to run this site and — only with your consent — analytics to
            measure what works. GDPR &amp; CCPA aligned. See our{" "}
            <Link href="/cookie-policy/" className="underline hover:text-brand-300">
              Cookie Policy
            </Link>
            .
          </p>
          <div className="mt-3 flex flex-wrap gap-2">
            <button
              onClick={() => decide("all")}
              className="rounded-[10px] bg-brand px-4 py-2 text-[12.5px] font-semibold text-white hover:bg-brand-hover"
            >
              Accept analytics
            </button>
            <button
              onClick={() => decide("essential")}
              className="rounded-[10px] border border-white/25 px-4 py-2 text-[12.5px] font-medium text-white/85 hover:border-brand-300 hover:text-brand-300"
            >
              Essential only
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
