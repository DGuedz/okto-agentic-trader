import { Terminal, Shield, Cpu } from "lucide-react";

export default function Hero() {
  return (
    <section className="container mx-auto px-6 py-20 md:py-32 grid md:grid-cols-2 gap-12 items-center">
      <div className="space-y-8">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-accent-amber-400/10 border border-accent-amber-400/20 text-accent-amber-400 text-xs font-mono">
          <span className="w-2 h-2 bg-accent-amber-400 rounded-full animate-pulse"></span>
          v1.0.0 STABLE | 🏆 BNB Chain Hackathon Edition
        </div>
        <h1 className="text-4xl md:text-6xl font-bold tracking-tight leading-tight">
          Okto — Sovereign <br/>
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-accent-amber-400 to-accent-amber-500">Agentic Trading</span> <br/>
          Infrastructure
        </h1>
        <p className="text-lg text-text-secondary max-w-xl">
          Headless, spec-driven, and auditable. Execute institutional strategies (Dark Pool, Sniping, Arbitrage) directly from your terminal. <br/>
          <span className="text-accent-neon-400 text-sm font-mono mt-2 block">Powered by BNB Chain & AI Agentic Logic.</span>
        </p>
        <div className="flex flex-wrap gap-4">
          <a href="https://github.com/DGuedz/okto-agentic-trader" target="_blank" rel="noopener noreferrer" className="px-6 py-3 bg-accent-amber-400 text-text-inverse font-bold rounded-full shadow-glowAmber hover:brightness-110 transition-all">
            Clone Repo
          </a>
          <a href="#" className="px-6 py-3 bg-white/5 border border-white/10 text-text-primary font-bold rounded-full hover:bg-white/10 transition-all">
            Read Manifesto
          </a>
        </div>
        <div className="flex items-center gap-6 text-xs text-text-muted font-mono pt-4">
          <span className="flex items-center gap-2"><Terminal size={14}/> Local-first</span>
          <span className="flex items-center gap-2"><Shield size={14}/> Keys stay local</span>
          <span className="flex items-center gap-2"><Cpu size={14}/> Deterministic</span>
        </div>
      </div>
      
      {/* Right side visual: Abstract Code/Infra */}
      <div className="relative group">
        {/* Background Glow - Intensified & Breathing */}
        <div className="absolute -inset-1 bg-gradient-to-r from-accent-amber-400 to-accent-neon-400 rounded-2xl blur-lg opacity-30 group-hover:opacity-50 transition-opacity duration-500 animate-pulseSlow"></div>
        
        <div className="relative bg-surface-panel border border-border-subtle rounded-2xl shadow-2xl overflow-hidden min-h-[500px]">
          {/* Cover Video Background - Full Visibility & Floating */}
          <div className="absolute inset-0 z-0 overflow-hidden">
             <video 
               autoPlay 
               loop 
               muted 
               playsInline
               poster="/assets/okto-cover-arquiteto-abissal.png"
               className="w-full h-full object-cover opacity-90 transition-all duration-1000 scale-105 group-hover:scale-110"
             >
               <source src="/assets/okto-hero-loop.mp4" type="video/mp4" />
               {/* Fallback to image if video fails or not supported */}
               <img 
                 src="/assets/okto-cover-arquiteto-abissal.png" 
                 alt="Arquiteto Abissal" 
                 className="w-full h-full object-cover"
               />
             </video>
             
             {/* Gradient Overlay for Text Readability Only */}
             <div className="absolute inset-0 bg-gradient-to-t from-bg-0 via-bg-0/90 to-transparent"></div>
          </div>

          {/* Terminal Content (Foreground) */}
          <div className="relative z-10 p-6 h-full flex flex-col">
            <div className="flex items-center gap-2 mb-4 border-b border-border-subtle pb-4">
              <div className="flex gap-1.5">
                <div className="w-3 h-3 rounded-full bg-red-500/20 border border-red-500/50"></div>
                <div className="w-3 h-3 rounded-full bg-yellow-500/20 border border-yellow-500/50"></div>
                <div className="w-3 h-3 rounded-full bg-green-500/20 border border-green-500/50"></div>
              </div>
              <div className="text-xs text-text-muted font-mono ml-2">okto-brain — python — 80x24</div>
            </div>
            <div className="font-mono text-xs space-y-1">
              <div className="text-accent-neon-400">$ okto start --mode=live</div>
              <div className="text-text-secondary">[SYSTEM] OKTO AGENTIC ASSISTANT: INITIALIZED</div>
              <div className="text-text-secondary">[SYSTEM] MODE: PRO TRADER (Aster & BNB Chain)</div>
              <div className="text-text-muted">--------------------------------------------------</div>
              <div className="text-text-primary">[ASTER] SCANNING ECOSYSTEM...</div>
              <div className="text-text-primary">[CAPITAL] INITIAL BALANCE LOCKED: $1,250.00</div>
              <div className="text-accent-amber-400">[SIGNAL] OPPORTUNITY DETECTED: ASTER/USDT</div>
              <div className="text-text-secondary">[EXEC] SIMULATING TX... GAS: 0.0004 BNB</div>
              <div className="text-accent-neon-400">[SUCCESS] TX CONFIRMED: 0x8a...4f2</div>
              <div className="text-text-secondary animate-pulse">_</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
