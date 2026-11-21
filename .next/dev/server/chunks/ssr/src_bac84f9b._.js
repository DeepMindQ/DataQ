module.exports = [
"[project]/src/lib/seeded.ts [app-ssr] (ecmascript)", ((__turbopack_context__) => {
"use strict";

/* Deterministic seeded RNG — server-safe (no "use client"), shared by
   DataVisuals and PageAugment so page-seeded telemetry is stable across
   server render and client hydration. */ __turbopack_context__.s([
    "hashStr",
    ()=>hashStr,
    "mulberry32",
    ()=>mulberry32
]);
function hashStr(s) {
    let h = 2166136261;
    for(let i = 0; i < s.length; i++){
        h ^= s.charCodeAt(i);
        h = Math.imul(h, 16777619);
    }
    return h >>> 0;
}
function mulberry32(seed) {
    let a = seed;
    return ()=>{
        a |= 0;
        a = a + 0x6d2b79f5 | 0;
        let t = Math.imul(a ^ a >>> 15, 1 | a);
        t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
        return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
}
}),
"[project]/src/components/site/DataVisuals.tsx [app-ssr] (ecmascript) <locals>", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "ArchitectureFlow",
    ()=>ArchitectureFlow,
    "BRAND",
    ()=>BRAND,
    "BRAND_SOFT",
    ()=>BRAND_SOFT,
    "BarChart",
    ()=>BarChart,
    "Donut",
    ()=>Donut,
    "Funnel",
    ()=>Funnel,
    "Gauge",
    ()=>Gauge,
    "Heatmap",
    ()=>Heatmap,
    "LineArea",
    ()=>LineArea,
    "NAVY",
    ()=>NAVY,
    "NetworkGraph",
    ()=>NetworkGraph,
    "Radar",
    ()=>Radar,
    "Sparkline",
    ()=>Sparkline,
    "WorldPins",
    ()=>WorldPins
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/node_modules/next/dist/server/route-modules/app-page/vendored/ssr/react-jsx-dev-runtime.js [app-ssr] (ecmascript)");
/* ── DataQ Soft data-visualization library (Wave 2, CHG-178/223 + output graphs)
   Pure SVG, brand-token colored, scroll-triggered draw animations, deterministic
   props (all data computed server-side → hydration-safe). Reduced motion: the
   globals.css kill switch drops every transition to instant.                 */ var __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$Motion$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/src/components/site/Motion.tsx [app-ssr] (ecmascript)");
var __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$lib$2f$seeded$2e$ts__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/src/lib/seeded.ts [app-ssr] (ecmascript)");
"use client";
;
;
;
const BRAND = "#FE5722";
const BRAND_SOFT = "#FE9C77";
const NAVY = "#18142D";
const NAVY_SOFT = "#3A3358";
;
/* ── shared frame ─────────────────────────────────────────────────────── */ function Frame({ title, caption, dark, children }) {
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("figure", {
        className: `overflow-hidden rounded-2xl border shadow-2 ${dark ? "border-white/10 bg-white/[0.05] backdrop-blur" : "border-line bg-white"}`,
        children: [
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("figcaption", {
                className: `flex flex-wrap items-center justify-between gap-2 border-b px-5 py-3.5 ${dark ? "border-white/10" : "border-line bg-mist/70"}`,
                children: [
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                        className: `text-[13px] font-semibold ${dark ? "text-white" : "text-navy-800"}`,
                        children: title
                    }, void 0, false, {
                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                        lineNumber: 39,
                        columnNumber: 9
                    }, this),
                    caption && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                        className: `text-[10.5px] font-medium uppercase tracking-[0.14em] ${dark ? "text-brand-300" : "text-brand-deep"}`,
                        children: caption
                    }, void 0, false, {
                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                        lineNumber: 41,
                        columnNumber: 11
                    }, this)
                ]
            }, void 0, true, {
                fileName: "[project]/src/components/site/DataVisuals.tsx",
                lineNumber: 34,
                columnNumber: 7
            }, this),
            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                className: "px-5 py-5",
                children: children
            }, void 0, false, {
                fileName: "[project]/src/components/site/DataVisuals.tsx",
                lineNumber: 46,
                columnNumber: 7
            }, this)
        ]
    }, void 0, true, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 29,
        columnNumber: 5
    }, this);
}
function BarChart({ title, labels, series, unit = "", caption, dark, height = 210 }) {
    const { ref, inView } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$Motion$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useInView"])(0.3);
    const max = Math.max(...series.flatMap((s)=>values1(s.values))) * 1.15 || 1;
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        ref: ref,
        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])(Frame, {
            title: title,
            caption: caption,
            dark: dark,
            children: [
                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                    style: {
                        height
                    },
                    className: "flex items-end",
                    children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        className: "flex h-full flex-1 flex-col",
                        children: [
                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                className: "flex h-full items-end gap-1",
                                children: labels.map((lb, gi)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                        className: "flex h-full flex-1 items-end justify-center gap-1.5",
                                        children: series.map((s, si)=>{
                                            const v = s.values[gi] ?? 0;
                                            const h = Math.max(2, v / max * 100);
                                            return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                                className: "relative flex h-full flex-1 max-w-[46px] flex-col justify-end",
                                                children: [
                                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                                        className: `absolute -top-5 w-full text-center text-[10.5px] font-semibold tabular-nums ${dark ? "text-white/80" : "text-navy-800"}`,
                                                        style: {
                                                            opacity: inView ? 1 : 0,
                                                            transition: "opacity 500ms ease " + (si * 90 + gi * 90 + 350) + "ms"
                                                        },
                                                        children: [
                                                            v.toLocaleString("en-US"),
                                                            unit
                                                        ]
                                                    }, void 0, true, {
                                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                                        lineNumber: 83,
                                                        columnNumber: 25
                                                    }, this),
                                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                                        className: "w-full rounded-t-[5px]",
                                                        style: {
                                                            height: `${h}%`,
                                                            background: s.color ?? (si === 0 ? NAVY : BRAND),
                                                            opacity: si === 0 && series.length > 1 ? 0.55 : 1,
                                                            transform: inView ? "scaleY(1)" : "scaleY(0)",
                                                            transformOrigin: "bottom",
                                                            transition: `transform 800ms cubic-bezier(.22,1,.36,1) ${si * 90 + gi * 90}ms`
                                                        }
                                                    }, void 0, false, {
                                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                                        lineNumber: 93,
                                                        columnNumber: 25
                                                    }, this)
                                                ]
                                            }, si, true, {
                                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                                lineNumber: 82,
                                                columnNumber: 23
                                            }, this);
                                        })
                                    }, lb, false, {
                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                        lineNumber: 77,
                                        columnNumber: 17
                                    }, this))
                            }, void 0, false, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 75,
                                columnNumber: 13
                            }, this),
                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                className: `mt-2.5 flex gap-1 border-t pt-2 ${dark ? "border-white/10" : "border-line"}`,
                                children: labels.map((lb)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                        className: `flex-1 text-center text-[10px] font-medium leading-tight ${dark ? "text-white/55" : "text-slate-body/70"}`,
                                        children: lb
                                    }, lb, false, {
                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                        lineNumber: 112,
                                        columnNumber: 17
                                    }, this))
                            }, void 0, false, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 110,
                                columnNumber: 13
                            }, this)
                        ]
                    }, void 0, true, {
                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                        lineNumber: 74,
                        columnNumber: 11
                    }, this)
                }, void 0, false, {
                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                    lineNumber: 73,
                    columnNumber: 9
                }, this),
                series.length > 1 && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                    className: "mt-3 flex flex-wrap gap-4",
                    children: series.map((s, si)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                            className: `flex items-center gap-1.5 text-[11px] ${dark ? "text-white/65" : "text-slate-body/75"}`,
                            children: [
                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                    "aria-hidden": "true",
                                    className: "h-2 w-2 rounded-[3px]",
                                    style: {
                                        background: s.color ?? (si === 0 ? NAVY : BRAND)
                                    }
                                }, void 0, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 126,
                                    columnNumber: 17
                                }, this),
                                s.name
                            ]
                        }, s.name, true, {
                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                            lineNumber: 125,
                            columnNumber: 15
                        }, this))
                }, void 0, false, {
                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                    lineNumber: 123,
                    columnNumber: 11
                }, this)
            ]
        }, void 0, true, {
            fileName: "[project]/src/components/site/DataVisuals.tsx",
            lineNumber: 72,
            columnNumber: 7
        }, this)
    }, void 0, false, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 71,
        columnNumber: 5
    }, this);
}
const values1 = (a)=>a.length ? a : [
        0
    ];
function LineArea({ title, labels, series, unit = "", caption, dark, height = 210 }) {
    const { ref, inView } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$Motion$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useInView"])(0.3);
    const W = 560;
    const H = height;
    const pad = {
        l: 34,
        r: 12,
        t: 14,
        b: 26
    };
    const all = series.flatMap((s)=>s.values);
    const min = Math.min(0, ...all);
    const max = Math.max(...all) * 1.1 || 1;
    const x = (i, n)=>pad.l + i * (W - pad.l - pad.r) / Math.max(1, n - 1);
    const y = (v)=>pad.t + (1 - (v - min) / (max - min || 1)) * (H - pad.t - pad.b);
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        ref: ref,
        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])(Frame, {
            title: title,
            caption: caption,
            dark: dark,
            children: [
                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("svg", {
                    viewBox: `0 0 ${W} ${H}`,
                    className: "w-full",
                    role: "img",
                    "aria-label": title,
                    children: [
                        [
                            0,
                            0.5,
                            1
                        ].map((g)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("line", {
                                x1: pad.l,
                                x2: W - pad.r,
                                y1: pad.t + g * (H - pad.t - pad.b),
                                y2: pad.t + g * (H - pad.t - pad.b),
                                stroke: dark ? "rgba(255,255,255,.12)" : "#E7E3F0",
                                strokeWidth: "1"
                            }, g, false, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 169,
                                columnNumber: 13
                            }, this)),
                        series.map((s, si)=>{
                            const pts = s.values.map((v, i)=>`${x(i, s.values.length)},${y(v)}`).join(" ");
                            const line = `M${pts}`;
                            const area = `${line} L${x(s.values.length - 1, s.values.length)},${H - pad.b} L${x(0, s.values.length)},${H - pad.b} Z`;
                            const color = s.color ?? (si === 0 ? BRAND : NAVY_SOFT);
                            return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("g", {
                                children: [
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("path", {
                                        d: area,
                                        fill: color,
                                        opacity: inView ? 0.14 : 0,
                                        style: {
                                            transition: "opacity 900ms ease 500ms"
                                        }
                                    }, void 0, false, {
                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                        lineNumber: 186,
                                        columnNumber: 17
                                    }, this),
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("path", {
                                        d: line,
                                        fill: "none",
                                        stroke: color,
                                        strokeWidth: "2.5",
                                        strokeLinecap: "round",
                                        strokeLinejoin: "round",
                                        pathLength: 1,
                                        strokeDasharray: 1,
                                        strokeDashoffset: inView ? 0 : 1,
                                        style: {
                                            transition: `stroke-dashoffset 1300ms cubic-bezier(.4,0,.2,1) ${si * 180}ms`
                                        }
                                    }, void 0, false, {
                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                        lineNumber: 187,
                                        columnNumber: 17
                                    }, this),
                                    s.values.map((v, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("circle", {
                                            cx: x(i, s.values.length),
                                            cy: y(v),
                                            r: 2.6,
                                            fill: dark ? "#fff" : "#fff",
                                            stroke: color,
                                            strokeWidth: "1.6",
                                            opacity: inView ? 1 : 0,
                                            style: {
                                                transition: `opacity 300ms ease ${700 + i * 60 + si * 180}ms`
                                            }
                                        }, i, false, {
                                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                                            lineNumber: 200,
                                            columnNumber: 19
                                        }, this))
                                ]
                            }, si, true, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 185,
                                columnNumber: 15
                            }, this);
                        }),
                        labels.map((lb, i)=>i % Math.ceil(labels.length / 7) === 0 || i === labels.length - 1 ? /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("text", {
                                x: x(i, labels.length),
                                y: H - 8,
                                textAnchor: "middle",
                                fontSize: "9.5",
                                fill: dark ? "rgba(255,255,255,.5)" : "#6B6580",
                                children: lb
                            }, i, false, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 217,
                                columnNumber: 15
                            }, this) : null),
                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("text", {
                            x: pad.l - 6,
                            y: pad.t + 4,
                            textAnchor: "end",
                            fontSize: "9",
                            fill: dark ? "rgba(255,255,255,.5)" : "#6B6580",
                            children: [
                                Math.round(max).toLocaleString("en-US"),
                                unit
                            ]
                        }, void 0, true, {
                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                            lineNumber: 222,
                            columnNumber: 11
                        }, this)
                    ]
                }, void 0, true, {
                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                    lineNumber: 167,
                    columnNumber: 9
                }, this),
                series.length > 1 && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                    className: "mt-1 flex flex-wrap gap-4",
                    children: series.map((s, si)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                            className: `flex items-center gap-1.5 text-[11px] ${dark ? "text-white/65" : "text-slate-body/75"}`,
                            children: [
                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                    "aria-hidden": "true",
                                    className: "h-[3px] w-4 rounded-full",
                                    style: {
                                        background: s.color ?? (si === 0 ? BRAND : NAVY_SOFT)
                                    }
                                }, void 0, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 231,
                                    columnNumber: 17
                                }, this),
                                s.name
                            ]
                        }, s.name, true, {
                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                            lineNumber: 230,
                            columnNumber: 15
                        }, this))
                }, void 0, false, {
                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                    lineNumber: 228,
                    columnNumber: 11
                }, this)
            ]
        }, void 0, true, {
            fileName: "[project]/src/components/site/DataVisuals.tsx",
            lineNumber: 166,
            columnNumber: 7
        }, this)
    }, void 0, false, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 165,
        columnNumber: 5
    }, this);
}
function Donut({ title, segments, caption, dark, center }) {
    const { ref, inView } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$Motion$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useInView"])(0.35);
    const total = segments.reduce((a, s)=>a + s.value, 0) || 1;
    const C = 2 * Math.PI * 40;
    let acc = 0;
    const palette = [
        BRAND,
        NAVY,
        BRAND_SOFT,
        NAVY_SOFT,
        "#8A82A6"
    ];
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        ref: ref,
        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])(Frame, {
            title: title,
            caption: caption,
            dark: dark,
            children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                className: "flex flex-col items-center gap-5 sm:flex-row",
                children: [
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("svg", {
                        viewBox: "0 0 110 110",
                        className: "h-[132px] w-[132px] shrink-0 -rotate-90",
                        role: "img",
                        "aria-label": title,
                        children: [
                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("circle", {
                                cx: "55",
                                cy: "55",
                                r: "40",
                                fill: "none",
                                stroke: dark ? "rgba(255,255,255,.1)" : "#EEEAF5",
                                strokeWidth: "13"
                            }, void 0, false, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 265,
                                columnNumber: 13
                            }, this),
                            segments.map((s, i)=>{
                                const frac = s.value / total;
                                const dash = `${inView ? frac * C : 0} ${C}`;
                                const off = -acc * C;
                                acc += frac;
                                return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("circle", {
                                    cx: "55",
                                    cy: "55",
                                    r: "40",
                                    fill: "none",
                                    stroke: s.color ?? palette[i % palette.length],
                                    strokeWidth: "13",
                                    strokeDasharray: dash,
                                    strokeDashoffset: off,
                                    style: {
                                        transition: `stroke-dasharray 1000ms cubic-bezier(.22,1,.36,1) ${i * 160}ms`
                                    }
                                }, i, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 272,
                                    columnNumber: 17
                                }, this);
                            })
                        ]
                    }, void 0, true, {
                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                        lineNumber: 264,
                        columnNumber: 11
                    }, this),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        className: "w-full space-y-2",
                        children: [
                            center && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("p", {
                                className: `text-[20px] font-bold tabular-nums ${dark ? "text-white" : "text-navy-800"}`,
                                children: center
                            }, void 0, false, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 289,
                                columnNumber: 15
                            }, this),
                            segments.map((s, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                    className: "flex items-center justify-between gap-3 text-[12px]",
                                    children: [
                                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                            className: `flex items-center gap-2 ${dark ? "text-white/75" : "text-slate-body/85"}`,
                                            children: [
                                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                                    "aria-hidden": "true",
                                                    className: "h-2.5 w-2.5 rounded-full",
                                                    style: {
                                                        background: s.color ?? palette[i % palette.length]
                                                    }
                                                }, void 0, false, {
                                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                                    lineNumber: 294,
                                                    columnNumber: 19
                                                }, this),
                                                s.name
                                            ]
                                        }, void 0, true, {
                                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                                            lineNumber: 293,
                                            columnNumber: 17
                                        }, this),
                                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                            className: `font-semibold tabular-nums ${dark ? "text-white/90" : "text-navy-800"}`,
                                            children: [
                                                Math.round(s.value / total * 100),
                                                "%"
                                            ]
                                        }, void 0, true, {
                                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                                            lineNumber: 297,
                                            columnNumber: 17
                                        }, this)
                                    ]
                                }, s.name, true, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 292,
                                    columnNumber: 15
                                }, this))
                        ]
                    }, void 0, true, {
                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                        lineNumber: 287,
                        columnNumber: 11
                    }, this)
                ]
            }, void 0, true, {
                fileName: "[project]/src/components/site/DataVisuals.tsx",
                lineNumber: 263,
                columnNumber: 9
            }, this)
        }, void 0, false, {
            fileName: "[project]/src/components/site/DataVisuals.tsx",
            lineNumber: 262,
            columnNumber: 7
        }, this)
    }, void 0, false, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 261,
        columnNumber: 5
    }, this);
}
function Radar({ title, axes, series, caption, dark }) {
    const { ref, inView } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$Motion$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useInView"])(0.3);
    const N = axes.length;
    const R = 78;
    const c = 110;
    const pt = (i, v)=>{
        const a = Math.PI * 2 * i / N - Math.PI / 2;
        return [
            c + Math.cos(a) * R * (v / 100),
            c + Math.sin(a) * R * (v / 100)
        ];
    };
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        ref: ref,
        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])(Frame, {
            title: title,
            caption: caption,
            dark: dark,
            children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                className: "flex flex-col items-center gap-4 sm:flex-row sm:items-start",
                children: [
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("svg", {
                        viewBox: "0 0 220 220",
                        className: "h-[200px] w-[200px] shrink-0",
                        role: "img",
                        "aria-label": title,
                        children: [
                            [
                                25,
                                50,
                                75,
                                100
                            ].map((g)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("polygon", {
                                    points: axes.map((_, i)=>pt(i, g).join(",")).join(" "),
                                    fill: "none",
                                    stroke: dark ? "rgba(255,255,255,.1)" : "#E7E3F0",
                                    strokeWidth: "1"
                                }, g, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 336,
                                    columnNumber: 15
                                }, this)),
                            axes.map((_, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("line", {
                                    x1: c,
                                    y1: c,
                                    x2: pt(i, 100)[0],
                                    y2: pt(i, 100)[1],
                                    stroke: dark ? "rgba(255,255,255,.1)" : "#E7E3F0"
                                }, i, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 345,
                                    columnNumber: 15
                                }, this)),
                            series.map((s, si)=>{
                                const pts = s.values.map((v, i)=>pt(i, v).join(",")).join(" ");
                                return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("polygon", {
                                    points: pts,
                                    fill: (s.color ?? (si === 0 ? BRAND : NAVY)) + "33",
                                    stroke: s.color ?? (si === 0 ? BRAND : NAVY),
                                    strokeWidth: "2",
                                    style: {
                                        transformOrigin: "110px 110px",
                                        transform: inView ? "scale(1)" : "scale(0.05)",
                                        opacity: inView ? 1 : 0,
                                        transition: `transform 900ms cubic-bezier(.22,1,.36,1) ${si * 150}ms, opacity 500ms ease ${si * 150}ms`
                                    }
                                }, si, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 350,
                                    columnNumber: 17
                                }, this);
                            }),
                            axes.map((a, i)=>{
                                const [px, py] = pt(i, 118);
                                return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("text", {
                                    x: px,
                                    y: py,
                                    textAnchor: "middle",
                                    dominantBaseline: "middle",
                                    fontSize: "8.5",
                                    fill: dark ? "rgba(255,255,255,.6)" : "#6B6580",
                                    children: a
                                }, a, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 368,
                                    columnNumber: 17
                                }, this);
                            })
                        ]
                    }, void 0, true, {
                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                        lineNumber: 334,
                        columnNumber: 11
                    }, this),
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        className: "space-y-2.5",
                        children: series.map((s, si)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                children: [
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                        className: `flex items-center gap-2 text-[12px] font-semibold ${dark ? "text-white" : "text-navy-800"}`,
                                        children: [
                                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                                "aria-hidden": "true",
                                                className: "h-2.5 w-2.5 rounded-full",
                                                style: {
                                                    background: s.color ?? (si === 0 ? BRAND : NAVY)
                                                }
                                            }, void 0, false, {
                                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                                lineNumber: 378,
                                                columnNumber: 19
                                            }, this),
                                            s.name
                                        ]
                                    }, void 0, true, {
                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                        lineNumber: 377,
                                        columnNumber: 17
                                    }, this),
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("p", {
                                        className: `mt-0.5 text-[11px] tabular-nums ${dark ? "text-white/60" : "text-slate-body/70"}`,
                                        children: axes.map((a, i)=>`${a.split(" ")[0]} ${Math.round(s.values[i])}`).join(" · ")
                                    }, void 0, false, {
                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                        lineNumber: 381,
                                        columnNumber: 17
                                    }, this)
                                ]
                            }, s.name, true, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 376,
                                columnNumber: 15
                            }, this))
                    }, void 0, false, {
                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                        lineNumber: 374,
                        columnNumber: 11
                    }, this)
                ]
            }, void 0, true, {
                fileName: "[project]/src/components/site/DataVisuals.tsx",
                lineNumber: 333,
                columnNumber: 9
            }, this)
        }, void 0, false, {
            fileName: "[project]/src/components/site/DataVisuals.tsx",
            lineNumber: 332,
            columnNumber: 7
        }, this)
    }, void 0, false, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 331,
        columnNumber: 5
    }, this);
}
function Funnel({ title, stages, caption, dark }) {
    const { ref, inView } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$Motion$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useInView"])(0.3);
    const max = Math.max(...stages.map((s)=>s.value)) || 1;
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        ref: ref,
        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])(Frame, {
            title: title,
            caption: caption,
            dark: dark,
            children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                className: "space-y-2.5",
                children: stages.map((s, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        className: "flex items-center gap-3",
                        children: [
                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                className: `w-28 shrink-0 text-right text-[11.5px] font-medium leading-tight ${dark ? "text-white/70" : "text-slate-body/80"}`,
                                children: s.name
                            }, void 0, false, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 412,
                                columnNumber: 15
                            }, this),
                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                className: `relative h-7 flex-1 overflow-hidden rounded-md ${dark ? "bg-white/5" : "bg-mist"}`,
                                children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                    className: "flex h-full items-center justify-end rounded-md pr-2.5",
                                    style: {
                                        width: inView ? `${Math.max(14, s.value / max * 100)}%` : "4%",
                                        background: `linear-gradient(90deg, ${BRAND}, ${BRAND_SOFT})`,
                                        opacity: 1 - i * 0.14,
                                        transition: `width 900ms cubic-bezier(.22,1,.36,1) ${i * 120}ms`
                                    },
                                    children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                        className: "text-[11px] font-bold tabular-nums text-white",
                                        children: s.value.toLocaleString("en-US")
                                    }, void 0, false, {
                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                        lineNumber: 425,
                                        columnNumber: 19
                                    }, this)
                                }, void 0, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 416,
                                    columnNumber: 17
                                }, this)
                            }, void 0, false, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 415,
                                columnNumber: 15
                            }, this)
                        ]
                    }, s.name, true, {
                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                        lineNumber: 411,
                        columnNumber: 13
                    }, this))
            }, void 0, false, {
                fileName: "[project]/src/components/site/DataVisuals.tsx",
                lineNumber: 409,
                columnNumber: 9
            }, this)
        }, void 0, false, {
            fileName: "[project]/src/components/site/DataVisuals.tsx",
            lineNumber: 408,
            columnNumber: 7
        }, this)
    }, void 0, false, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 407,
        columnNumber: 5
    }, this);
}
function NetworkGraph({ title, nodes, links, caption, dark, height = 230 }) {
    const { ref, inView } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$Motion$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useInView"])(0.3);
    const W = 560;
    const H = height;
    const px = (n)=>24 + n.x * (W - 48);
    const py = (n)=>20 + n.y * (H - 40);
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        ref: ref,
        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])(Frame, {
            title: title,
            caption: caption,
            dark: dark,
            children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("svg", {
                viewBox: `0 0 ${W} ${H}`,
                className: "w-full",
                role: "img",
                "aria-label": title,
                children: [
                    links.map(([a, b], i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("line", {
                            x1: px(nodes[a]),
                            y1: py(nodes[a]),
                            x2: px(nodes[b]),
                            y2: py(nodes[b]),
                            stroke: dark ? "rgba(254,87,34,.5)" : "rgba(254,87,34,.45)",
                            strokeWidth: "1.4",
                            pathLength: 1,
                            strokeDasharray: 1,
                            strokeDashoffset: inView ? 0 : 1,
                            style: {
                                transition: `stroke-dashoffset 800ms ease ${i * 70 + 200}ms`
                            }
                        }, i, false, {
                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                            lineNumber: 461,
                            columnNumber: 13
                        }, this)),
                    nodes.map((n, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("g", {
                            style: {
                                opacity: inView ? 1 : 0,
                                transition: `opacity 400ms ease ${i * 45}ms`
                            },
                            children: [
                                n.hub && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("circle", {
                                    cx: px(n),
                                    cy: py(n),
                                    r: 13,
                                    fill: "none",
                                    stroke: BRAND,
                                    strokeWidth: "1.4",
                                    opacity: inView ? 0.5 : 0,
                                    style: {
                                        transition: "opacity 800ms ease 900ms"
                                    }
                                }, void 0, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 478,
                                    columnNumber: 17
                                }, this),
                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("circle", {
                                    cx: px(n),
                                    cy: py(n),
                                    r: n.hub ? 8 : 4.5,
                                    fill: n.hub ? BRAND : NAVY,
                                    stroke: dark ? "#fff" : "#fff",
                                    strokeWidth: n.hub ? 2 : 1
                                }, void 0, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 489,
                                    columnNumber: 15
                                }, this),
                                /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("text", {
                                    x: px(n),
                                    y: py(n) - 11,
                                    textAnchor: "middle",
                                    fontSize: "9",
                                    fontWeight: "600",
                                    fill: dark ? "rgba(255,255,255,.85)" : NAVY,
                                    children: n.id
                                }, void 0, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 490,
                                    columnNumber: 15
                                }, this)
                            ]
                        }, n.id, true, {
                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                            lineNumber: 476,
                            columnNumber: 13
                        }, this))
                ]
            }, void 0, true, {
                fileName: "[project]/src/components/site/DataVisuals.tsx",
                lineNumber: 459,
                columnNumber: 9
            }, this)
        }, void 0, false, {
            fileName: "[project]/src/components/site/DataVisuals.tsx",
            lineNumber: 458,
            columnNumber: 7
        }, this)
    }, void 0, false, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 457,
        columnNumber: 5
    }, this);
}
function Heatmap({ title, rows, cols, matrix, caption, dark, unit = "" }) {
    const { ref, inView } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$Motion$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useInView"])(0.3);
    const max = Math.max(...matrix.flat()) || 1;
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        ref: ref,
        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])(Frame, {
            title: title,
            caption: caption,
            dark: dark,
            children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                className: "overflow-x-auto",
                children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("table", {
                    className: "w-full min-w-[420px] border-separate border-spacing-[3px] text-[10.5px]",
                    children: [
                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("thead", {
                            children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("tr", {
                                children: [
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("th", {
                                        "aria-hidden": "true"
                                    }, void 0, false, {
                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                        lineNumber: 527,
                                        columnNumber: 17
                                    }, this),
                                    cols.map((c)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("th", {
                                            className: `px-1 pb-1 font-semibold ${dark ? "text-white/60" : "text-slate-body/70"}`,
                                            children: c
                                        }, c, false, {
                                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                                            lineNumber: 529,
                                            columnNumber: 19
                                        }, this))
                                ]
                            }, void 0, true, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 526,
                                columnNumber: 15
                            }, this)
                        }, void 0, false, {
                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                            lineNumber: 525,
                            columnNumber: 13
                        }, this),
                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("tbody", {
                            children: rows.map((r, ri)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("tr", {
                                    children: [
                                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("td", {
                                            className: `pr-2 text-right font-medium ${dark ? "text-white/70" : "text-slate-body/80"}`,
                                            children: r
                                        }, void 0, false, {
                                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                                            lineNumber: 538,
                                            columnNumber: 19
                                        }, this),
                                        matrix[ri].map((v, ci)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("td", {
                                                className: "rounded-[4px] text-center font-semibold tabular-nums text-white",
                                                style: {
                                                    background: `rgba(254, 87, 34, ${0.12 + 0.78 * (v / max)})`,
                                                    color: v / max > 0.55 || v / max < 0.2 ? dark ? "#fff" : NAVY : "#fff",
                                                    opacity: inView ? 1 : 0,
                                                    transform: inView ? "scale(1)" : "scale(.6)",
                                                    transition: `opacity 500ms ease ${(ri * cols.length + ci) * 35}ms, transform 500ms ease ${(ri * cols.length + ci) * 35}ms`
                                                },
                                                children: [
                                                    v.toLocaleString("en-US"),
                                                    unit
                                                ]
                                            }, ci, true, {
                                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                                lineNumber: 540,
                                                columnNumber: 21
                                            }, this))
                                    ]
                                }, r, true, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 537,
                                    columnNumber: 17
                                }, this))
                        }, void 0, false, {
                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                            lineNumber: 535,
                            columnNumber: 13
                        }, this)
                    ]
                }, void 0, true, {
                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                    lineNumber: 524,
                    columnNumber: 11
                }, this)
            }, void 0, false, {
                fileName: "[project]/src/components/site/DataVisuals.tsx",
                lineNumber: 523,
                columnNumber: 9
            }, this)
        }, void 0, false, {
            fileName: "[project]/src/components/site/DataVisuals.tsx",
            lineNumber: 522,
            columnNumber: 7
        }, this)
    }, void 0, false, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 521,
        columnNumber: 5
    }, this);
}
function Gauge({ title, value, max = 100, unit = "%", caption, dark }) {
    const { ref, inView } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$Motion$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useInView"])(0.4);
    const frac = Math.min(1, value / max);
    const C = Math.PI * 42;
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        ref: ref,
        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])(Frame, {
            title: title,
            caption: caption,
            dark: dark,
            children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                className: "flex flex-col items-center",
                children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("svg", {
                    viewBox: "0 0 110 66",
                    className: "w-[190px]",
                    role: "img",
                    "aria-label": title,
                    children: [
                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("path", {
                            d: "M 13 58 A 42 42 0 0 1 97 58",
                            fill: "none",
                            stroke: dark ? "rgba(255,255,255,.12)" : "#EEEAF5",
                            strokeWidth: "11",
                            strokeLinecap: "round"
                        }, void 0, false, {
                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                            lineNumber: 582,
                            columnNumber: 13
                        }, this),
                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("path", {
                            d: "M 13 58 A 42 42 0 0 1 97 58",
                            fill: "none",
                            stroke: BRAND,
                            strokeWidth: "11",
                            strokeLinecap: "round",
                            pathLength: 1,
                            strokeDasharray: 1,
                            strokeDashoffset: inView ? 1 - frac : 1,
                            style: {
                                transition: "stroke-dashoffset 1200ms cubic-bezier(.22,1,.36,1)"
                            }
                        }, void 0, false, {
                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                            lineNumber: 583,
                            columnNumber: 13
                        }, this),
                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("text", {
                            x: "55",
                            y: "52",
                            textAnchor: "middle",
                            fontSize: "15",
                            fontWeight: "700",
                            fill: dark ? "#fff" : NAVY,
                            className: "tabular-nums",
                            children: [
                                value.toLocaleString("en-US"),
                                unit
                            ]
                        }, void 0, true, {
                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                            lineNumber: 594,
                            columnNumber: 13
                        }, this)
                    ]
                }, void 0, true, {
                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                    lineNumber: 581,
                    columnNumber: 11
                }, this)
            }, void 0, false, {
                fileName: "[project]/src/components/site/DataVisuals.tsx",
                lineNumber: 580,
                columnNumber: 9
            }, this)
        }, void 0, false, {
            fileName: "[project]/src/components/site/DataVisuals.tsx",
            lineNumber: 579,
            columnNumber: 7
        }, this)
    }, void 0, false, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 578,
        columnNumber: 5
    }, this);
}
function Sparkline({ data, dark, className = "" }) {
    const W = 120;
    const H = 34;
    const min = Math.min(...data);
    const max = Math.max(...data);
    const pts = data.map((v, i)=>`${i * W / (data.length - 1)},${H - 4 - (v - min) / (max - min || 1) * (H - 8)}`).join(" ");
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("svg", {
        viewBox: `0 0 ${W} ${H}`,
        className: `w-[110px] ${className}`,
        "aria-hidden": "true",
        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("polyline", {
            points: pts,
            fill: "none",
            stroke: BRAND,
            strokeWidth: "2",
            strokeLinecap: "round",
            strokeLinejoin: "round",
            pathLength: 1,
            strokeDasharray: 1,
            strokeDashoffset: 0
        }, void 0, false, {
            fileName: "[project]/src/components/site/DataVisuals.tsx",
            lineNumber: 616,
            columnNumber: 7
        }, this)
    }, void 0, false, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 615,
        columnNumber: 5
    }, this);
}
function ArchitectureFlow({ title, layers, caption, dark }) {
    const { ref, inView } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$Motion$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useInView"])(0.22);
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        ref: ref,
        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])(Frame, {
            title: title,
            caption: caption,
            dark: dark,
            children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                className: "relative",
                children: layers.map((l, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                        className: "relative",
                        children: [
                            i > 0 && /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                "aria-hidden": "true",
                                className: "flex justify-center py-1",
                                children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("svg", {
                                    width: "26",
                                    height: "18",
                                    viewBox: "0 0 26 18",
                                    children: [
                                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("line", {
                                            x1: "13",
                                            y1: "0",
                                            x2: "13",
                                            y2: "14",
                                            stroke: BRAND,
                                            strokeWidth: "2",
                                            pathLength: 1,
                                            strokeDasharray: 1,
                                            strokeDashoffset: inView ? 0 : 1,
                                            style: {
                                                transition: `stroke-dashoffset 350ms ease ${i * 220 - 110}ms`
                                            }
                                        }, void 0, false, {
                                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                                            lineNumber: 652,
                                            columnNumber: 21
                                        }, this),
                                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("path", {
                                            d: "M 8 12 L 13 17 L 18 12",
                                            fill: "none",
                                            stroke: BRAND,
                                            strokeWidth: "2",
                                            style: {
                                                opacity: inView ? 1 : 0,
                                                transition: `opacity 300ms ease ${i * 220}ms`
                                            }
                                        }, void 0, false, {
                                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                                            lineNumber: 664,
                                            columnNumber: 21
                                        }, this)
                                    ]
                                }, void 0, true, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 651,
                                    columnNumber: 19
                                }, this)
                            }, void 0, false, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 650,
                                columnNumber: 17
                            }, this),
                            /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                className: `rounded-xl border px-4 py-3 ${dark ? "border-white/12 bg-white/[0.06]" : "border-line bg-mist/60"}`,
                                style: {
                                    opacity: inView ? 1 : 0,
                                    transform: inView ? "translateY(0)" : "translateY(14px)",
                                    transition: `opacity 600ms ease ${i * 220}ms, transform 600ms cubic-bezier(.22,1,.36,1) ${i * 220}ms`
                                },
                                children: [
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("p", {
                                        className: `text-[11px] font-bold uppercase tracking-[0.14em] ${dark ? "text-brand-300" : "text-brand-deep"}`,
                                        children: l.name
                                    }, void 0, false, {
                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                        lineNumber: 678,
                                        columnNumber: 17
                                    }, this),
                                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                                        className: "mt-2 flex flex-wrap gap-1.5",
                                        children: l.nodes.map((n)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                                                className: `rounded-md px-2 py-1 text-[11px] font-medium ${dark ? "bg-white/10 text-white/85" : "bg-white text-navy-800 border border-line"}`,
                                                children: n
                                            }, n, false, {
                                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                                lineNumber: 681,
                                                columnNumber: 21
                                            }, this))
                                    }, void 0, false, {
                                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                                        lineNumber: 679,
                                        columnNumber: 17
                                    }, this)
                                ]
                            }, void 0, true, {
                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                lineNumber: 668,
                                columnNumber: 15
                            }, this)
                        ]
                    }, l.name, true, {
                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                        lineNumber: 648,
                        columnNumber: 13
                    }, this))
            }, void 0, false, {
                fileName: "[project]/src/components/site/DataVisuals.tsx",
                lineNumber: 646,
                columnNumber: 9
            }, this)
        }, void 0, false, {
            fileName: "[project]/src/components/site/DataVisuals.tsx",
            lineNumber: 645,
            columnNumber: 7
        }, this)
    }, void 0, false, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 644,
        columnNumber: 5
    }, this);
}
function WorldPins({ title, pins, caption, dark }) {
    const { ref, inView } = (0, __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$Motion$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["useInView"])(0.3);
    const dots = [];
    const rng = (0, __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$lib$2f$seeded$2e$ts__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["mulberry32"])(7);
    for(let i = 0; i < 420; i++)dots.push({
        x: rng(),
        y: 0.12 + rng() * 0.72
    });
    return /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
        ref: ref,
        children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])(Frame, {
            title: title,
            caption: caption,
            dark: dark,
            children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("div", {
                className: "relative overflow-hidden rounded-xl",
                style: {
                    aspectRatio: "2.1 / 1"
                },
                children: [
                    /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("svg", {
                        viewBox: "0 0 100 48",
                        className: "absolute inset-0 h-full w-full",
                        "aria-hidden": "true",
                        children: [
                            dots.map((d, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("circle", {
                                    cx: d.x * 100,
                                    cy: d.y * 48,
                                    r: "0.45",
                                    fill: dark ? "rgba(255,255,255,.28)" : "rgba(24,20,45,.22)"
                                }, i, false, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 719,
                                    columnNumber: 15
                                }, this)),
                            pins.map((p, i)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("g", {
                                    style: {
                                        opacity: inView ? 1 : 0,
                                        transition: `opacity 500ms ease ${400 + i * 220}ms`
                                    },
                                    children: [
                                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("circle", {
                                            cx: p.x * 100,
                                            cy: p.y * 48,
                                            r: "1.9",
                                            fill: BRAND
                                        }, void 0, false, {
                                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                                            lineNumber: 723,
                                            columnNumber: 17
                                        }, this),
                                        /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("circle", {
                                            cx: p.x * 100,
                                            cy: p.y * 48,
                                            r: "3.4",
                                            fill: "none",
                                            stroke: BRAND,
                                            strokeWidth: "0.5",
                                            opacity: "0.6",
                                            children: /*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("animate", {
                                                attributeName: "r",
                                                values: "2.4;4.4;2.4",
                                                dur: "2.6s",
                                                begin: `${i * 0.5}s`,
                                                repeatCount: "indefinite"
                                            }, void 0, false, {
                                                fileName: "[project]/src/components/site/DataVisuals.tsx",
                                                lineNumber: 725,
                                                columnNumber: 19
                                            }, this)
                                        }, void 0, false, {
                                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                                            lineNumber: 724,
                                            columnNumber: 17
                                        }, this)
                                    ]
                                }, p.id, true, {
                                    fileName: "[project]/src/components/site/DataVisuals.tsx",
                                    lineNumber: 722,
                                    columnNumber: 15
                                }, this))
                        ]
                    }, void 0, true, {
                        fileName: "[project]/src/components/site/DataVisuals.tsx",
                        lineNumber: 717,
                        columnNumber: 11
                    }, this),
                    pins.map((p)=>/*#__PURE__*/ (0, __TURBOPACK__imported__module__$5b$project$5d2f$node_modules$2f$next$2f$dist$2f$server$2f$route$2d$modules$2f$app$2d$page$2f$vendored$2f$ssr$2f$react$2d$jsx$2d$dev$2d$runtime$2e$js__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["jsxDEV"])("span", {
                            className: "absolute -translate-x-1/2 whitespace-nowrap rounded-md px-1.5 py-0.5 text-[10px] font-semibold",
                            style: {
                                left: `${p.x * 100}%`,
                                top: `calc(${p.y * 100}% - 24px)`,
                                background: dark ? "rgba(24,20,45,.85)" : "rgba(24,20,45,.85)",
                                color: "#fff"
                            },
                            children: p.id
                        }, p.id, false, {
                            fileName: "[project]/src/components/site/DataVisuals.tsx",
                            lineNumber: 731,
                            columnNumber: 13
                        }, this))
                ]
            }, void 0, true, {
                fileName: "[project]/src/components/site/DataVisuals.tsx",
                lineNumber: 716,
                columnNumber: 9
            }, this)
        }, void 0, false, {
            fileName: "[project]/src/components/site/DataVisuals.tsx",
            lineNumber: 715,
            columnNumber: 7
        }, this)
    }, void 0, false, {
        fileName: "[project]/src/components/site/DataVisuals.tsx",
        lineNumber: 714,
        columnNumber: 5
    }, this);
}
}),
"[project]/src/components/site/DataVisuals.tsx [app-ssr] (ecmascript)", ((__turbopack_context__) => {
"use strict";

__turbopack_context__.s([
    "ArchitectureFlow",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["ArchitectureFlow"],
    "BRAND",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["BRAND"],
    "BRAND_SOFT",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["BRAND_SOFT"],
    "BarChart",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["BarChart"],
    "Donut",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["Donut"],
    "Funnel",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["Funnel"],
    "Gauge",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["Gauge"],
    "Heatmap",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["Heatmap"],
    "LineArea",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["LineArea"],
    "NAVY",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["NAVY"],
    "NetworkGraph",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["NetworkGraph"],
    "Radar",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["Radar"],
    "Sparkline",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["Sparkline"],
    "WorldPins",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__["WorldPins"],
    "hashStr",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$lib$2f$seeded$2e$ts__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["hashStr"],
    "mulberry32",
    ()=>__TURBOPACK__imported__module__$5b$project$5d2f$src$2f$lib$2f$seeded$2e$ts__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__["mulberry32"]
]);
var __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$components$2f$site$2f$DataVisuals$2e$tsx__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__$3c$locals$3e$__ = __turbopack_context__.i("[project]/src/components/site/DataVisuals.tsx [app-ssr] (ecmascript) <locals>");
var __TURBOPACK__imported__module__$5b$project$5d2f$src$2f$lib$2f$seeded$2e$ts__$5b$app$2d$ssr$5d$__$28$ecmascript$29$__ = __turbopack_context__.i("[project]/src/lib/seeded.ts [app-ssr] (ecmascript)");
}),
];

//# sourceMappingURL=src_bac84f9b._.js.map