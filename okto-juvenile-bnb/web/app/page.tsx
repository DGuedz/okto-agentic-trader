import Hero from "@/components/Hero";
import FeatureCard from "@/components/FeatureCard";
import MetricCard from "@/components/MetricCard";
import TerminalWidget from "@/components/TerminalWidget";

export default function Home() {
  return (
    <div className="flex flex-col gap-20 pb-20">
      <Hero />
      
      {/* THE PROBLEM Section (Idle Capital) */}
      <section className="container mx-auto px-6 grid md:grid-cols-3 gap-8">
        <div className="p-6 border border-border-subtle rounded-xl bg-bg-1/50 backdrop-blur-sm">
          <h3 className="font-mono font-bold text-[#F3BA2F] mb-2">{'>'} Idle Capital = Waste</h3>
          <p className="text-text-secondary text-sm">Your dev wallet sits dormant. Okto puts it to work.</p>
        </div>
        <div className="p-6 border border-border-subtle rounded-xl bg-bg-1/50 backdrop-blur-sm">
          <h3 className="font-mono font-bold text-[#F3BA2F] mb-2">{'>'} Headless Liquidity</h3>
          <p className="text-text-secondary text-sm">No UI. No dashboards. Just pure yield in your terminal.</p>
        </div>
        <div className="p-6 border border-border-subtle rounded-xl bg-bg-1/50 backdrop-blur-sm">
          <h3 className="font-mono font-bold text-[#F3BA2F] mb-2">{'>'} Code-to-Yield</h3>
          <p className="text-text-secondary text-sm">You code. Okto farms. Automatic profit bridging to Aster DEX.</p>
        </div>
      </section>

      {/* CORE INFRASTRUCTURE Section */}
      <section className="container mx-auto px-6">
        <h2 className="text-2xl font-bold font-mono mb-8 text-text-primary">INFRASTRUCTURE MODULES</h2>
        <div className="grid md:grid-cols-3 gap-6">
          {[
            { title: "Spec-Driven DevOps (SDD)", desc: "Define risk limits in `genesis.yaml`. Okto obeys strictly." },
            { title: "Safety Rails (Anti-MEV)", desc: "Simulates every tx locally. Blocks gas spikes and slippage." },
            { title: "Aster Tentacle (Yield)", desc: "Auto-harvests yields from Aster Perpetual Vaults on BNB Chain." },
            { title: "Mind Shield (Security)", desc: "Cognitive firewall preventing prompt injection & key leakage." },
            { title: "Silent Fortress", desc: "Zero-leakage logs. Your keys never leave your local env." },
            { title: "Real-Time Telemetry", desc: "Live terminal feed: Gas, Yield, PnL, Bridge Status." }
          ].map((f, i) => (
            <FeatureCard key={i} title={f.title} desc={f.desc} />
          ))}
        </div>
      </section>

      {/* LIVE METRICS Section */}
      <section className="container mx-auto px-6">
        <h2 className="text-2xl font-bold font-mono mb-8 text-text-primary">LIVE NODE STATUS <span className="text-xs font-normal text-text-muted ml-2">(Simulated Demo)</span></h2>
        <div className="grid md:grid-cols-4 gap-6">
           <MetricCard label="Yield Farmed" value="0.05 ASTER" />
           <MetricCard label="Gas Efficiency" value="0.05 Gwei" />
           <MetricCard label="Uptime" value="99.9%" />
           <MetricCard label="Security Checks" value="142 Passed" />
        </div>
      </section>

      {/* DEMO Section */}
      <section className="container mx-auto px-6">
        <div className="bg-bg-1 border border-border-subtle rounded-2xl p-1 overflow-hidden shadow-2xl">
            <TerminalWidget />
        </div>
      </section>

      {/* FINAL CTA */}
      <section className="container mx-auto px-6 py-20 text-center">
        <h2 className="text-3xl md:text-4xl font-bold font-mono mb-8">Turn your IDE into a Liquidity Node.</h2>
        <div className="flex justify-center gap-6">
          <a href="https://github.com/DGuedz/okto-agentic-trader" target="_blank" rel="noopener noreferrer" className="px-8 py-3 bg-[#F3BA2F] text-[#0B0E11] font-bold rounded-sm shadow-[0_0_20px_rgba(243,186,47,0.4)] hover:brightness-110 transition-all uppercase tracking-wider">Deploy Node</a>
          <a href="/docs" className="px-8 py-3 bg-white/5 border border-white/10 text-text-primary font-bold rounded-sm hover:bg-white/10 transition-all uppercase tracking-wider text-sm">Read Specs</a>
        </div>
      </section>
    </div>
  );
}
