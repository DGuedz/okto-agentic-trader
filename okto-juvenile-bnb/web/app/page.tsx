import Hero from "@/components/Hero";
import FeatureCard from "@/components/FeatureCard";
import MetricCard from "@/components/MetricCard";
import TerminalWidget from "@/components/TerminalWidget";

export default function Home() {
  return (
    <div className="flex flex-col gap-20 pb-20">
      <Hero />
      
      {/* WHY Section */}
      <section className="container mx-auto px-6 grid md:grid-cols-3 gap-8">
        <div className="p-6 border border-border-subtle rounded-xl bg-bg-1/50 backdrop-blur-sm">
          <h3 className="font-mono font-bold text-accent-amber-400 mb-2">Execution &gt; UI</h3>
          <p className="text-text-secondary text-sm">CLI-first automation. Higher throughput, zero clicks.</p>
        </div>
        <div className="p-6 border border-border-subtle rounded-xl bg-bg-1/50 backdrop-blur-sm">
          <h3 className="font-mono font-bold text-accent-amber-400 mb-2">Safety by Design</h3>
          <p className="text-text-secondary text-sm">Simulation mode, slippage guardrails, circuit breakers.</p>
        </div>
        <div className="p-6 border border-border-subtle rounded-xl bg-bg-1/50 backdrop-blur-sm">
          <h3 className="font-mono font-bold text-accent-amber-400 mb-2">Auditability</h3>
          <p className="text-text-secondary text-sm">Reproducible logs. Spec-driven decision trails.</p>
        </div>
      </section>

      {/* FEATURES Section */}
      <section className="container mx-auto px-6">
        <h2 className="text-2xl font-bold font-mono mb-8 text-text-primary">CORE MODULES</h2>
        <div className="grid md:grid-cols-3 gap-6">
          {[
            { title: "Spec-Driven Execution (SDD)", desc: "Configure strategy and risk via okto.yaml. No improvisation." },
            { title: "Transaction Simulation Mode", desc: "Simulate tx, measure cost and validate expected outcome before gas spend." },
            { title: "On-Chain Alpha Sniffer", desc: "Modular detection: liquidity, spreads, funding, flow analysis." },
            { title: "Anti-MEV Routing", desc: "Private relays + iceberg orders + intent protection." },
            { title: "Hybrid CEX/DEX Connectivity", desc: "Connect Binance liquidity and Uniswap innovation in one session." },
            { title: "Real-Time Terminal Telemetry", desc: "Live logs: mempool, gas, fills, PnL, risk vetoes." }
          ].map((f, i) => (
            <FeatureCard key={i} title={f.title} desc={f.desc} />
          ))}
        </div>
      </section>

      {/* METRICS Section */}
      <section className="container mx-auto px-6">
        <h2 className="text-2xl font-bold font-mono mb-8 text-text-primary">PERFORMANCE METRICS <span className="text-xs font-normal text-text-muted ml-2">(Sample / Simulated)</span></h2>
        <div className="grid md:grid-cols-4 gap-6">
           <MetricCard label="Fill Rate" value="92%" />
           <MetricCard label="Median Latency" value="180ms" />
           <MetricCard label="Slippage Saved" value="0.34%" />
           <MetricCard label="Risk Vetoes" value="17 blocked" />
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
        <h2 className="text-3xl md:text-4xl font-bold font-mono mb-8">Ready to deploy your agent?</h2>
        <div className="flex justify-center gap-6">
          <a href="https://github.com/DGuedz/okto-agentic-trader" target="_blank" rel="noopener noreferrer" className="px-8 py-3 bg-accent-amber-400 text-text-inverse font-bold rounded-full shadow-glowAmber hover:brightness-110 transition-all">Clone Repo</a>
          <a href="/architecture" className="px-8 py-3 bg-white/5 border border-white/10 text-text-primary font-bold rounded-full hover:bg-white/10 transition-all">View Architecture</a>
        </div>
      </section>
    </div>
  );
}
