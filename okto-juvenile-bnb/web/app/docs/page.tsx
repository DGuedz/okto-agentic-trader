import Link from "next/link";
import WalletGate from "@/components/WalletGate";

export default function DocsPage() {
  return (
    <WalletGate>
      <main className="container mx-auto px-6 py-20 max-w-5xl font-mono text-gray-400">
        
        <div className="grid md:grid-cols-4 gap-12">
          
          {/* SIDEBAR */}
          <aside className="hidden md:block col-span-1 space-y-8 sticky top-32 h-fit">
              <div>
                  <h3 className="text-white font-bold mb-4 uppercase text-xs tracking-widest border-b border-[#F3BA2F]/20 pb-2">Protocol</h3>
                  <ul className="space-y-3 text-sm">
                      <li className="text-[#F3BA2F]">Introduction</li>
                      <li className="hover:text-[#F3BA2F] cursor-pointer">Spec-Driven DevOps</li>
                      <li className="hover:text-[#F3BA2F] cursor-pointer">Safety Rails</li>
                  </ul>
              </div>
              <div>
                  <h3 className="text-white font-bold mb-4 uppercase text-xs tracking-widest border-b border-white/10 pb-2">Modules</h3>
                  <ul className="space-y-3 text-sm">
                      <li className="hover:text-[#F3BA2F] cursor-pointer">Aster Farmer</li>
                      <li className="hover:text-[#F3BA2F] cursor-pointer">Mind Shield</li>
                      <li className="hover:text-[#F3BA2F] cursor-pointer text-white/20 cursor-not-allowed">Dark Pool [RESTRICTED]</li>
                  </ul>
              </div>
          </aside>

          {/* CONTENT */}
          <div className="col-span-3 space-y-16">
              
              <section>
                  <div className="inline-block px-2 py-1 bg-[#F3BA2F]/10 text-[#F3BA2F] text-[10px] rounded mb-4">
                      PUBLIC CLEARANCE
                  </div>
                  <h1 className="text-4xl font-bold text-white mb-6">Introduction to OKTO</h1>
                  <p className="text-lg leading-relaxed mb-6">
                      OKTO is a <strong className="text-white">Headless Liquidity Node</strong> designed for the BNB Smart Chain. It allows developers to deploy institutional-grade trading strategies directly from their local environment, bypassing traditional web interfaces.
                  </p>
                  <div className="p-4 bg-white/5 border border-white/10 rounded text-sm">
                      <p className="text-[#F3BA2F]">⚠ WARNING:</p>
                      <p className="mt-1">
                          OKTO is not a "bot". It is an autonomous agent. Once initialized, it will execute logic defined in your genesis spec without human intervention.
                      </p>
                  </div>
              </section>

              <section>
                  <h2 className="text-2xl font-bold text-white mb-4">Spec-Driven DevOps (SDD)</h2>
                  <p className="mb-4">
                      The core philosophy of OKTO is that code should follow policy, not the other way around. All risk parameters are defined in a static YAML file.
                  </p>
                  <div className="bg-black/50 border border-white/10 rounded p-4 overflow-x-auto">
  <pre className="text-xs text-gray-300">
  <span className="text-[#F3BA2F]">risk_engine:</span>
    <span className="text-[#F3BA2F]">max_drawdown:</span> 15.0  <span className="text-gray-600"># Hard stop at 15% loss</span>
    <span className="text-[#F3BA2F]">max_leverage:</span> 3     <span className="text-gray-600"># Never exceed 3x</span>
    <span className="text-[#F3BA2F]">assets:</span>
      - BNB
      - ASTER
  </pre>
                  </div>
              </section>

              <section>
                  <h2 className="text-2xl font-bold text-white mb-4">Safety Rails</h2>
                  <p className="mb-4">
                      Before any transaction is broadcast to the mempool, it passes through a local simulation layer. If the simulation predicts a failure, slippage &gt; 1%, or high gas costs, the transaction is <strong className="text-red-400">aborted locally</strong>.
                  </p>
                  <ul className="list-disc pl-5 space-y-2">
                      <li><strong className="text-white">Gas Protection:</strong> Auto-abort if Gwei &gt; 50.</li>
                      <li><strong className="text-white">Slippage Guard:</strong> Revert if impact &gt; 0.5%.</li>
                      <li><strong className="text-white">MEV Cloak:</strong> [REDACTED - PROPRIETARY LOGIC]</li>
                  </ul>
              </section>

               <section>
                  <h2 className="text-2xl font-bold text-white mb-4">Mind Shield Protocol</h2>
                  <p className="mb-4">
                     OKTO implements a cognitive firewall to prevent LLM hallucinations from affecting financial logic. The "Mind Shield" validates all agent outputs against the <code className="text-[#F3BA2F]">genesis.yaml</code> constraints.
                  </p>
              </section>

          </div>

        </div>
      </main>
    </WalletGate>
  );
}
