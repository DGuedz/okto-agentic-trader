export default function TerminalWidget() {
  return (
    <div className="grid md:grid-cols-2 bg-surface-panel min-h-[400px]">
      {/* Spec Preview */}
      <div className="border-r border-border-subtle p-6 font-mono text-sm">
        <div className="text-text-muted mb-4 uppercase tracking-widest text-xs">/config/okto.yaml</div>
        <pre className="text-text-secondary overflow-x-auto">
          <code>
            <span className="text-accent-amber-400">strategy:</span><br/>
            &nbsp;&nbsp;name: &quot;bnb_scalp_v1&quot;<br/>
            &nbsp;&nbsp;assets: [&quot;BNB/USDT&quot;]<br/>
            &nbsp;&nbsp;interval: &quot;1m&quot;<br/>
            <br/>
            <span className="text-accent-amber-400">risk_manager:</span><br/>
            &nbsp;&nbsp;max_drawdown: 5.0%<br/>
            &nbsp;&nbsp;stop_loss: 1.5%<br/>
            &nbsp;&nbsp;take_profit: 3.0%<br/>
            &nbsp;&nbsp;leverage: 5x<br/>
            <br/>
            <span className="text-accent-amber-400">modules:</span><br/>
            &nbsp;&nbsp;- &quot;anti_mev&quot;<br/>
            &nbsp;&nbsp;- &quot;capital_rotation&quot;<br/>
          </code>
        </pre>
      </div>

      {/* Live Telemetry */}
      <div className="p-6 font-mono text-sm bg-bg-0 relative overflow-hidden">
        <div className="text-text-muted mb-4 uppercase tracking-widest text-xs flex justify-between">
            <span>Terminal Telemetry</span>
            <span className="text-accent-neon-400">● LIVE</span>
        </div>
        <div className="space-y-3">
            <div className="flex gap-2">
                <span className="text-text-muted">10:42:01</span>
                <span className="text-state-info">[INFO]</span>
                <span className="text-text-secondary">Market scan complete. 12 pairs analyzed.</span>
            </div>
            <div className="flex gap-2">
                <span className="text-text-muted">10:42:05</span>
                <span className="text-state-warning">[WARN]</span>
                <span className="text-text-secondary">High slippage detected on POOL (1.2%). Vetoing trade.</span>
            </div>
            <div className="flex gap-2">
                <span className="text-text-muted">10:42:12</span>
                <span className="text-state-info">[INFO]</span>
                <span className="text-text-secondary">Capital Rotation: Checking High Water Mark...</span>
            </div>
            <div className="flex gap-2">
                <span className="text-text-muted">10:42:15</span>
                <span className="text-accent-neon-400">[EXEC]</span>
                <span className="text-text-primary">Scalp Entry Long BNB @ 620.50</span>
            </div>
             <div className="flex gap-2 opacity-50">
                <span className="text-text-muted">10:42:18</span>
                <span className="text-state-info">[INFO]</span>
                <span className="text-text-secondary">Monitoring position...</span>
            </div>
        </div>
        <div className="absolute bottom-6 right-6">
            <button className="px-4 py-2 bg-accent-amber-400 text-text-inverse font-bold text-xs rounded hover:brightness-110 transition-all shadow-glowAmber">
                RUN SIMULATION
            </button>
        </div>
      </div>
    </div>
  );
}
