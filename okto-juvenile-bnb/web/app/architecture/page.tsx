import Link from "next/link";
import WalletGate from "@/components/WalletGate";

export default function ArchitecturePage() {
  return (
    <WalletGate>
      <main className="container mx-auto px-6 py-20 max-w-6xl font-mono text-gray-400">
        
        {/* HEADER */}
        <header className="mb-16 border-b border-[#F3BA2F]/20 pb-8">
          <div className="flex items-center gap-2 text-xs text-[#F3BA2F]/70 mb-2 tracking-widest uppercase">
            <span>System Architecture</span>
            <span>::</span>
            <span>v1.1</span>
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
            The <span className="text-[#F3BA2F]">Headless</span> Blueprint
          </h1>
          <p className="max-w-2xl text-lg text-gray-500">
            Okto is not a dApp. It is a sovereign execution node. Below is the unclassified structural diagram of the system.
          </p>
        </header>

        {/* DIAGRAM SECTION */}
        <section className="grid md:grid-cols-12 gap-8 mb-20">
          
          {/* LEFT COLUMN: CONTEXT */}
          <div className="md:col-span-4 space-y-8">
              <div className="p-6 border border-[#F3BA2F]/20 rounded bg-[#F3BA2F]/5">
                <h3 className="text-[#F3BA2F] font-bold mb-2 flex items-center gap-2">
                    <span className="w-2 h-2 bg-[#F3BA2F] rounded-full animate-pulse"></span>
                    Local-First
                </h3>
                <p className="text-sm leading-relaxed">
                    Logic runs on your hardware. Keys never leave your machine. No backend servers, no centralized APIs.
                </p>
              </div>
              
              <div className="p-6 border border-white/10 rounded bg-white/5">
                <h3 className="text-white font-bold mb-2">Spec-Driven (SDD)</h3>
                <p className="text-sm leading-relaxed">
                    Behavior is defined in <code className="text-[#F3BA2F]">genesis.yaml</code>. The code obeys the spec, preventing drift and unauthorized execution.
                </p>
              </div>
          </div>

          {/* RIGHT COLUMN: LAYERS */}
          <div className="md:col-span-8 space-y-4">
              
              {/* LAYER 1 */}
              <div className="relative p-6 border border-white/10 rounded-lg hover:border-[#F3BA2F]/50 transition-colors group">
                <div className="absolute top-0 right-0 p-2 text-[10px] text-gray-600 uppercase">Layer 01</div>
                <h4 className="text-xl font-bold text-white mb-2 group-hover:text-[#F3BA2F] transition-colors">Interface Layer</h4>
                <div className="grid grid-cols-3 gap-4 text-xs">
                    <div className="bg-black/40 p-3 rounded border border-white/5 text-center">CLI Terminal</div>
                    <div className="bg-black/40 p-3 rounded border border-white/5 text-center">Config (YAML)</div>
                    <div className="bg-black/40 p-3 rounded border border-white/5 text-center">Env Variables</div>
                </div>
              </div>

              {/* ARROW */}
              <div className="flex justify-center text-[#F3BA2F]/30">↓</div>

              {/* LAYER 2 */}
              <div className="relative p-6 border border-[#F3BA2F]/30 rounded-lg bg-[#F3BA2F]/5 hover:border-[#F3BA2F] transition-colors group">
                <div className="absolute top-0 right-0 p-2 text-[10px] text-[#F3BA2F]/70 uppercase">Layer 02 (Core)</div>
                <h4 className="text-xl font-bold text-white mb-2 group-hover:text-[#F3BA2F] transition-colors">Brain & Control</h4>
                <div className="grid grid-cols-3 gap-4 text-xs">
                    <div className="bg-black/40 p-3 rounded border border-[#F3BA2F]/20 text-center text-[#F3BA2F]">Safety Rails</div>
                    <div className="bg-black/40 p-3 rounded border border-[#F3BA2F]/20 text-center text-white">Decision Engine</div>
                    <div className="bg-black/40 p-3 rounded border border-[#F3BA2F]/20 text-center text-white">Mind Shield</div>
                </div>
              </div>

              {/* ARROW */}
              <div className="flex justify-center text-[#F3BA2F]/30">↓</div>

              {/* LAYER 3 */}
              <div className="relative p-6 border border-white/10 rounded-lg hover:border-[#F3BA2F]/50 transition-colors group">
                <div className="absolute top-0 right-0 p-2 text-[10px] text-gray-600 uppercase">Layer 03</div>
                <h4 className="text-xl font-bold text-white mb-2 group-hover:text-[#F3BA2F] transition-colors">Value Layer</h4>
                <div className="grid grid-cols-3 gap-4 text-xs">
                    <div className="bg-black/40 p-3 rounded border border-white/5 text-center">BNB Chain RPC</div>
                    <div className="bg-black/40 p-3 rounded border border-white/5 text-center">Aster Vaults</div>
                    <div className="bg-black/40 p-3 rounded border border-white/5 text-center">DEX Router</div>
                </div>
              </div>

          </div>
        </section>

        <footer className="text-center text-xs text-gray-600 border-t border-white/5 pt-8">
          <p>UNCLASSIFIED ARCHITECTURE DIAGRAM • OKTO PROTOCOL</p>
        </footer>

      </main>
    </WalletGate>
  );
}
