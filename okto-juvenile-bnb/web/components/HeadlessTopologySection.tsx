import React from "react";
import TentacleSvg from "@/components/TentacleSvg";

const CARD_BASE =
  "rounded-2xl border border-white/10 bg-[rgba(15,18,24,0.55)] backdrop-blur-[12px] shadow-[0_10px_40px_rgba(0,0,0,0.6)] p-6";

function TopologyCard({
  title,
  color,
  text,
  icon,
}: {
  title: string;
  color: string;
  text: string;
  icon: string;
}) {
  return (
    <div className={CARD_BASE}>
      <div className="mb-3 flex items-center gap-3">
        <span className="text-lg" aria-hidden="true">
          {icon}
        </span>
        <h3 className="text-3xl font-semibold tracking-tight" style={{ color }}>
          {title}
        </h3>
      </div>
      <p className="font-mono text-lg leading-relaxed text-zinc-300">{text}</p>
    </div>
  );
}

export default function HeadlessTopologySection() {
  return (
    <section className="relative mt-16 w-full">
      <header className="mb-10 text-center">
        <h2 className="text-5xl font-semibold tracking-tight text-zinc-100 md:text-6xl">
          The <span className="text-amber-300">Headless</span> Topology
        </h2>
      </header>

      <div className="relative min-h-[680px] rounded-3xl border border-white/5 bg-[radial-gradient(circle_at_50%_50%,rgba(246,195,86,0.08),transparent_45%),radial-gradient(circle_at_80%_20%,rgba(73,226,161,0.08),transparent_40%),#070A0D] p-6 md:p-10">
        <div className="hidden md:block">
          <TentacleSvg
            paths={[
              {
                d: "M 600 350 C 490 320, 410 260, 350 190",
                gradientId: "tentacle-amber",
                glow: "rgba(246,195,86,0.28)",
              },
              {
                d: "M 600 350 C 480 390, 400 470, 320 520",
                gradientId: "tentacle-blue",
                glow: "rgba(74,163,255,0.28)",
              },
              {
                d: "M 600 350 C 710 320, 800 260, 860 190",
                gradientId: "tentacle-green",
                glow: "rgba(73,226,161,0.28)",
              },
              {
                d: "M 600 350 C 720 390, 810 470, 880 520",
                gradientId: "tentacle-purple",
                glow: "rgba(181,123,255,0.28)",
              },
            ]}
          />
        </div>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-3 md:items-center">
          <div className="space-y-6">
            <TopologyCard
              title="Genesis Spec"
              color="#F6C356"
              icon="</>"
              text="Spec defines the laws. No UI drift. Pure intent."
            />
            <TopologyCard
              title="Market Data"
              color="#4AA3FF"
              icon="⚡"
              text="Evidence-sourced signals from BNB Chain RPC."
            />
          </div>

          <div className="flex justify-center py-4">
            <div className="relative flex h-[300px] w-[300px] items-center justify-center rounded-full border-[3px] border-amber-300 bg-[#0B0F14] shadow-[0_0_40px_rgba(246,195,86,0.22)] md:h-[360px] md:w-[360px]">
              <div className="absolute -top-3 h-6 w-6 rounded-full bg-blue-500 shadow-[0_0_20px_rgba(74,163,255,0.9)]" />
              <div className="absolute -bottom-3 h-6 w-6 rounded-full bg-green-400 shadow-[0_0_20px_rgba(73,226,161,0.9)]" />
              <div className="text-center">
                <div className="mb-3 text-4xl" aria-hidden="true">
                  🐙
                </div>
                <div className="text-5xl font-semibold tracking-[0.12em] text-zinc-100">OKTO NODE</div>
                <div className="mx-auto mt-4 inline-flex rounded-full border border-white/10 bg-amber-300/15 px-4 py-2 text-xl font-medium tracking-widest text-amber-300">
                  v1.1 STABLE
                </div>
              </div>
            </div>
          </div>

          <div className="space-y-6">
            <TopologyCard
              title="Intel Layer"
              color="#49E2A1"
              icon="✹"
              text="Evidence-linked events. Generates policy-ready diffs."
            />
            <TopologyCard
              title="Execution"
              color="#B57BFF"
              icon="↯"
              text="Guardrailed actions with audit receipts and MEV-protected execution."
            />
          </div>
        </div>
      </div>

      <p className="mt-4 text-center text-sm text-zinc-500">
        Evidence-linked only. No profit promises.
      </p>
    </section>
  );
}
