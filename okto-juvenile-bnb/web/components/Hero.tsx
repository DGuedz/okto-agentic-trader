 "use client";

import { Terminal, Shield, Cpu, Copy, Check } from "lucide-react";
import { useState } from "react";

export default function Hero() {
  const [copied, setCopied] = useState(false);

  const copyCommand = () => {
    navigator.clipboard.writeText("git clone https://github.com/DGuedz/okto-agentic-trader.git && cd okto && ./install.sh");
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <section className="container mx-auto px-6 py-20 md:py-32 grid md:grid-cols-2 gap-12 items-center">
      <div className="space-y-8">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#F3BA2F]/10 border border-[#F3BA2F]/20 text-[#F3BA2F] text-xs font-mono">
          <span className="w-2 h-2 bg-[#F3BA2F] rounded-full animate-pulse"></span>
          v1.1 STABLE | 🏆 BNB Chain Hackathon Edition
        </div>
        <h1 className="text-4xl md:text-6xl font-bold tracking-tight leading-tight">
          Turn your IDE into a <br/>
          <span className="text-[#F3BA2F] drop-shadow-[0_0_10px_rgba(243,186,47,0.5)]">Liquidity Node</span>.
        </h1>
        <p className="text-lg text-text-secondary max-w-xl">
          While you code, OKTO executes policy-approved actions. The first Headless Liquidity Protocol designed for the AI-Augmented Developer. <br/>
          <span className="text-[#F3BA2F] text-sm font-mono mt-2 block">Powered by BNB Chain & AI Agentic Logic.</span>
        </p>
        <div className="flex flex-wrap gap-4">
          <button 
            onClick={copyCommand}
            className={`px-6 py-3 font-bold rounded-sm shadow-[0_0_20px_rgba(243,186,47,0.4)] hover:brightness-110 transition-all uppercase tracking-wider flex items-center gap-2 min-w-[200px] justify-center ${
              copied ? "bg-green-500 text-black" : "bg-[#F3BA2F] text-[#0B0E11]"
            }`}
          >
            {copied ? (
              <>
                <Check size={18} />
                CMD COPIED
              </>
            ) : (
              <>
                <Copy size={18} />
                Deploy Node
              </>
            )}
          </button>
          <a href="https://bscscan.com/address/0x71C7656EC7ab88b098defB751B7401B5f6d899A2" target="_blank" rel="noopener noreferrer" className="px-6 py-3 bg-white/5 border border-white/10 text-text-primary font-bold rounded-sm hover:bg-white/10 transition-all uppercase tracking-wider text-sm flex items-center gap-2">
            View on BscScan
            <ExternalLinkIcon />
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
        <div className="absolute -inset-1 bg-gradient-to-r from-[#F3BA2F] to-[#F3BA2F] rounded-2xl blur-lg opacity-20 group-hover:opacity-40 transition-opacity duration-500 animate-pulseSlow"></div>
        
        <div className="relative bg-[#0B0E11] border border-[#F3BA2F]/20 rounded-lg shadow-2xl overflow-hidden min-h-[500px]">
          {/* Cover Video Background - Full Visibility & Floating */}
          <div className="absolute inset-0 z-0 overflow-hidden">
             <video 
               autoPlay 
               loop 
               muted 
               playsInline
               poster="/assets/okto-cover-arquiteto-abissal.png"
               className="w-full h-full object-cover opacity-90 transition-all duration-1000 scale-105 group-hover:scale-110 grayscale brightness-75 contrast-125"
             >
               <source src="/assets/okto-hero-loop.mp4" type="video/mp4" />
               {/* Fallback to image if video fails or not supported */}
               <img 
                 src="/assets/okto-cover-arquiteto-abissal.png" 
                 alt="Arquiteto Abissal" 
                 className="w-full h-full object-cover grayscale"
               />
             </video>
             
             {/* Gradient Overlay for Text Readability Only */}
             <div className="absolute inset-0 bg-gradient-to-t from-[#0B0E11] via-[#0B0E11]/90 to-transparent"></div>
          </div>

          {/* Terminal Content (Foreground) */}
          <div className="relative z-10 p-6 h-full flex flex-col font-mono">
            <div className="flex items-center gap-2 mb-4 border-b border-white/10 pb-4">
              <div className="flex gap-1.5">
                <div className="w-3 h-3 rounded-full bg-red-500/50"></div>
                <div className="w-3 h-3 rounded-full bg-yellow-500/50"></div>
                <div className="w-3 h-3 rounded-full bg-green-500/50"></div>
              </div>
              <div className="text-xs text-white/30 ml-2">okto-node — -zsh — 80x24</div>
            </div>
            <div className="text-xs space-y-1">
              <div className="text-[#F3BA2F]">$ okto start --mode=liquidity_node</div>
              <div className="text-white/50">[SYSTEM] OKTO HEADLESS NODE: INITIALIZED</div>
              <div className="text-white/50">[SYSTEM] MODE: POLICY-DRIVEN EXECUTION (Aster & BNB Chain)</div>
              <div className="text-white/30">--------------------------------------------------</div>
              <div className="text-white">[ASTER] SCANNING CONNECTORS...</div>
              <div className="text-white">[CAPITAL] IDLE ASSETS DETECTED: 5.4 BNB</div>
              <div className="text-yellow-400">[SIGNAL] POLICY-COMPATIBLE ACTION DETECTED</div>
              <div className="text-white/50">[EXEC] SIMULATING DEPOSIT... GAS: 0.0004 BNB</div>
              <div className="text-[#F3BA2F]">[SUCCESS] ACTION RECEIPT LOGGED: 0x8a...4f2</div>
              <div className="text-white/50 animate-pulse">_</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function ExternalLinkIcon() {
  return (
    <svg className="w-3 h-3 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
  );
}
