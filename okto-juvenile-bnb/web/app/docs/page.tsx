import { Terminal } from "lucide-react";

export default function Docs() {
  return (
    <div className="container mx-auto px-6 py-20">
      <h1 className="text-4xl font-bold font-mono mb-8 text-accent-amber-400">Documentation</h1>
      
      <div className="space-y-12">
        <section>
            <h2 className="text-2xl font-bold text-text-primary mb-4">Quickstart</h2>
            <div className="bg-surface-panel p-6 rounded-xl border border-border-subtle font-mono text-sm overflow-x-auto">
                <div className="flex gap-2 text-text-muted mb-4">
                    <Terminal size={16} />
                    <span>bash</span>
                </div>
                <div className="space-y-2 text-text-secondary">
                    <p><span className="text-accent-neon-400">$</span> git clone https://github.com/DGuedz/okto-agentic-trader</p>
                    <p><span className="text-accent-neon-400">$</span> cd okto-agentic-trader</p>
                    <p><span className="text-accent-neon-400">$</span> cp config/.env.example config/.env</p>
                    <p><span className="text-accent-neon-400">$</span> python3 main.py --mode=simulation</p>
                </div>
            </div>
        </section>

        <section>
            <h2 className="text-2xl font-bold text-text-primary mb-4">Configuration (okto.yaml)</h2>
            <p className="text-text-secondary mb-4">Define your agent's personality and risk limits.</p>
            <div className="bg-surface-panel p-6 rounded-xl border border-border-subtle font-mono text-sm overflow-x-auto text-text-secondary">
<pre>{`risk_manager:
  max_drawdown_per_day: 5.0%
  max_open_positions: 3
  stop_loss_default: 1.5%

strategies:
  - name: "aster_arb_v1"
    enabled: true
    interval: 60s
    markets: ["BNB/USDT", "ASTER/USDT"]
`}</pre>
            </div>
        </section>
      </div>
    </div>
  );
}
