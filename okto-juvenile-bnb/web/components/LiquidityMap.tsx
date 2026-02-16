import React from 'react';
import { Activity, Zap, Layers } from 'lucide-react';

export default function LiquidityMap() {
  return (
    <div className="w-full bg-surface-card border border-border-subtle rounded-lg p-4">
      <div className="flex justify-between items-center mb-6">
        <h3 className="text-sm font-bold text-text-primary flex items-center gap-2">
          <Activity size={16} className="text-accent-amber-400" />
          Liquidity Heatmap
        </h3>
        <div className="flex gap-2 text-xs">
          <span className="px-2 py-1 bg-bg-2 rounded border border-border-subtle text-text-secondary cursor-pointer hover:text-accent-amber-400">1H</span>
          <span className="px-2 py-1 bg-accent-amber-400/10 border border-accent-amber-400/20 text-accent-amber-400 rounded cursor-pointer">4H</span>
          <span className="px-2 py-1 bg-bg-2 rounded border border-border-subtle text-text-secondary cursor-pointer hover:text-accent-amber-400">1D</span>
        </div>
      </div>

      <div className="relative h-64 bg-bg-0 rounded border border-border-subtle overflow-hidden flex items-center justify-center">
        {/* Abstract Heatmap Visualization */}
        <div className="absolute inset-0 opacity-20 bg-[radial-gradient(circle_at_50%_50%,_rgba(243,186,47,0.4),transparent_70%)]" />
        
        <div className="grid grid-cols-12 gap-1 w-full h-full p-1">
          {Array.from({ length: 48 }).map((_, i) => {
            const intensity = Math.random();
            const color = intensity > 0.7 ? 'bg-accent-amber-400' : intensity > 0.4 ? 'bg-accent-amber-500' : 'bg-bg-2';
            const opacity = intensity > 0.7 ? 'opacity-80' : 'opacity-30';
            
            return (
              <div 
                key={i} 
                className={`${color} ${opacity} rounded-sm transition-all duration-1000 hover:opacity-100`}
                style={{ animationDelay: `${Math.random() * 2}s` }}
              />
            );
          })}
        </div>

        <div className="absolute bottom-4 left-4 text-xs font-mono space-y-1 bg-bg-1/90 p-2 rounded border border-border-subtle backdrop-blur-sm">
          <div className="flex items-center gap-2 text-text-secondary">
            <Zap size={12} className="text-accent-amber-400" />
            <span>High Volatility Zone</span>
          </div>
          <div className="flex items-center gap-2 text-text-secondary">
            <Layers size={12} className="text-blue-400" />
            <span>Deep Liquidity (630-640)</span>
          </div>
        </div>
      </div>
    </div>
  );
}
