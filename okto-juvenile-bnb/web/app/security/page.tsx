import { Shield } from "lucide-react";

export default function Security() {
  return (
    <div className="container mx-auto px-6 py-20">
      <h1 className="text-4xl font-bold font-mono mb-8 text-accent-amber-400 flex items-center gap-4">
        <Shield className="w-10 h-10" />
        Security Model
      </h1>
      
      <div className="grid md:grid-cols-2 gap-8">
        <div className="bg-surface-card border border-border-subtle p-8 rounded-xl">
            <h3 className="text-xl font-bold text-text-primary mb-4">Local-First Keys</h3>
            <p className="text-text-secondary">
                Okto never transmits your private keys. They are loaded from your local `.env` file directly into the process memory and cleared upon termination. We recommend using a hardware wallet for signing if possible (future feature).
            </p>
        </div>
        <div className="bg-surface-card border border-border-subtle p-8 rounded-xl">
            <h3 className="text-xl font-bold text-text-primary mb-4">Anti-MEV Architecture</h3>
            <p className="text-text-secondary">
                By default, Okto routes DEX transactions through private RPC relays (Flashbots/Eden) to prevent sandwich attacks. Large orders are split (Iceberg) to minimize market impact.
            </p>
        </div>
        <div className="bg-surface-card border border-border-subtle p-8 rounded-xl">
            <h3 className="text-xl font-bold text-text-primary mb-4">Simulation Mode</h3>
            <p className="text-text-secondary">
                Every transaction is simulated against a local fork or mainnet simulation before broadcasting. If the simulation predicts failure or slippage &gt; 1%, the brain vetoes the execution.
            </p>

        </div>
        <div className="bg-surface-card border border-border-subtle p-8 rounded-xl">
            <h3 className="text-xl font-bold text-text-primary mb-4">Circuit Breakers</h3>
            <p className="text-text-secondary">
                Hard-coded stop limits. If the portfolio value drops by X% within Y minutes, the agent automatically halts all trading and cancels open orders.
            </p>
        </div>
      </div>
    </div>
  );
}
