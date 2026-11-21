import Link from "next/link";
import { ArrowRight } from "lucide-react";
import Logo from "@/components/site/Logo";

/* Branded animated 404 (Wave 1 CHG-030 + Wave 2 CHG-162): float loop, choreography. */
export default function NotFound() {
  return (
    <section className="relative overflow-hidden grad-navy-field text-white">
      <div className="bg-field-drift absolute inset-0 dot-grid" aria-hidden="true" />
      <div className="absolute inset-0 grad-orange-glow" aria-hidden="true" />
      <div className="relative container-dq py-20 text-center">
        <Logo variant="reversed" height={30} className="mx-auto" />
        <p className="animate-float mt-8 font-display text-[72px] font-bold leading-none text-brand sm:text-[88px]">404</p>
        <h1 className="mt-4 text-display-3 text-white">This page drifted outside the grid.</h1>
        <p className="mx-auto mt-3 max-w-lg text-[14px] text-white/65">
          The URL may have moved in our relaunch. Everything is four clicks from home — start with
          the towers, the industries, or the evidence.
        </p>
        <div className="mt-8 flex flex-wrap justify-center gap-3">
          {[
            { label: "Home", url: "/" },
            { label: "Services", url: "/services/" },
            { label: "Industries", url: "/industries/" },
            { label: "Case Studies", url: "/case-studies/" },
            { label: "Contact", url: "/contact/" },
          ].map((l) => (
            <Link
              key={l.url}
              href={l.url}
              className="inline-flex items-center gap-2 rounded-[10px] border border-white/25 px-5 py-2.5 text-[13px] font-medium text-white/85 hover:border-brand-300 hover:text-brand-300"
            >
              {l.label} <ArrowRight className="h-3.5 w-3.5" />
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}
