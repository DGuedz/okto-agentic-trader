import React from 'react';
import { Shield, Lock, Activity, Zap, AlertTriangle, CheckCircle2 } from 'lucide-react';

export default function SafetyHUD() {
  return (
    <div className="w-full bg-surface-panel border border-border-subtle rounded-lg p-4 font-mono">
      <div className="flex justify-between items-center mb-4 border-b border-border-subtle pb-2">
        <h3 className="text-xs font-bold text-text-muted uppercase tracking-widest flex items-center gap-2">
          <Shield size={14} className="text-state-success" />
          Safety Rails Active
        </h3>
        <span className="text-[10px] bg-state-success/10 text-state-success px-2 py-0.5 rounded border border-state-success/20 animate-pulse">
          SYSTEM SECURE
        </span>
      </div>

      <div className="grid grid-cols-2 gap-3">
        {/* Module 1: Max Drawdown */}
        <div className="p-3 bg-bg-1 rounded border border-border-subtle relative overflow-hidden group">
          <div className="absolute top-0 right-0 p-1 opacity-20 group-hover:opacity-100 transition-opacity">
            <Lock size={12} className="text-text-secondary" />
          </div>
          <div className="text-[10px] text-text-muted uppercase mb-1">Max Drawdown</div>
          <div className="text-sm font-bold text-text-primary flex items-center gap-2">
            2.5% 
            <span className="text-[10px] text-state-success font-normal">/ Session</span>
          </div>
          <div className="w-full h-1 bg-bg-2 mt-2 rounded-full overflow-hidden">
            <div className="h-full bg-state-success w-[10%]" />
          </div>
        </div>

        {/* Module 2: Anti-Rug (Liquidity Lock) */}
        <div className="p-3 bg-bg-1 rounded border border-border-subtle relative overflow-hidden group">
          <div className="absolute top-0 right-0 p-1 opacity-20 group-hover:opacity-100 transition-opacity">
            <Activity size={12} className="text-text-secondary" />
          </div>
          <div className="text-[10px] text-text-muted uppercase mb-1">Liquidity Check</div>
          <div className="text-sm font-bold text-state-success flex items-center gap-2">
            <CheckCircle2 size={14} />
            VERIFIED
          </div>
          <div className="text-[10px] text-text-muted mt-1">Pool &gt; $500k Locked</div>
        </div>

        {/* Module 3: Gas Ceiling */}
        <div className="p-3 bg-bg-1 rounded border border-border-subtle relative overflow-hidden group">
          <div className="absolute top-0 right-0 p-1 opacity-20 group-hover:opacity-100 transition-opacity">
            <Zap size={12} className="text-text-secondary" />
          </div>
          <div className="text-[10px] text-text-muted uppercase mb-1">Gas Ceiling</div>
          <div className="text-sm font-bold text-text-primary flex items-center gap-2">
            5 Gwei
          </div>
          <div className="w-full h-1 bg-bg-2 mt-2 rounded-full overflow-hidden">
            <div className="h-full bg-blue-400 w-[40%]" />
          </div>
        </div>

        {/* Module 4: Slippage Protection */}
        <div className="p-3 bg-bg-1 rounded border border-border-subtle relative overflow-hidden group">
          <div className="absolute top-0 right-0 p-1 opacity-20 group-hover:opacity-100 transition-opacity">
            <AlertTriangle size={12} className="text-text-secondary" />
          </div>
          <div className="text-[10px] text-text-muted uppercase mb-1">Max Slippage</div>
          <div className="text-sm font-bold text-accent-amber-400 flex items-center gap-2">
            0.5%
            <span className="text-[10px] text-text-muted font-normal">Dynamic</span>
          </div>
          <div className="w-full h-1 bg-bg-2 mt-2 rounded-full overflow-hidden">
            <div className="h-full bg-accent-amber-400 w-[20%]" />
          </div>
        </div>
      </div>

      <div className="mt-3 pt-2 border-t border-border-subtle text-[10px] text-text-muted flex justify-between">
        <span>Last Audit: 12s ago</span>
        <span className="text-state-success">142 Checks Passed</span>
      </div>
    </div>
  );
}
