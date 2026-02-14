export default function Architecture() {
  return (
    <div className="container mx-auto px-6 py-20">
      <h1 className="text-4xl font-bold font-mono mb-8 text-accent-amber-400">System Architecture</h1>
      <div className="bg-surface-card border border-border-subtle rounded-xl p-8 mb-12">
        <p className="text-text-secondary mb-4">
          Okto follows a <strong>Headless, Spec-Driven</strong> architecture. The core logic resides in `brain.py`, which orchestrates modular tentacles based on the genesis configuration.
        </p>
        <div className="grid md:grid-cols-3 gap-8 mt-12">
            <div className="p-6 border border-border-default rounded-lg bg-bg-0">
                <h3 className="font-mono font-bold text-accent-neon-400 mb-4">1. Interface Layer</h3>
                <ul className="text-sm text-text-secondary space-y-2">
                    <li>• CLI / Terminal</li>
                    <li>• Config (okto.yaml)</li>
                    <li>• Env Variables</li>
                </ul>
            </div>
            <div className="p-6 border border-border-default rounded-lg bg-bg-0">
                <h3 className="font-mono font-bold text-accent-amber-400 mb-4">2. Control Layer (Brain)</h3>
                <ul className="text-sm text-text-secondary space-y-2">
                    <li>• Risk Engine</li>
                    <li>• Decision Core</li>
                    <li>• Scheduler</li>
                </ul>
            </div>
            <div className="p-6 border border-border-default rounded-lg bg-bg-0">
                <h3 className="font-mono font-bold text-accent-neon-400 mb-4">3. Value Layer</h3>
                <ul className="text-sm text-text-secondary space-y-2">
                    <li>• CEX Adapter (ccxt)</li>
                    <li>• DEX Adapter (web3)</li>
                    <li>• Blockchain RPC</li>
                </ul>
            </div>
        </div>
      </div>
    </div>
  );
}
