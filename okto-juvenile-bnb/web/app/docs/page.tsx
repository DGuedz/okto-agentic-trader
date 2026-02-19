import Link from "next/link";
import WalletGate from "@/components/WalletGate";
import BiText from "@/components/BiText";

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
                      <li><Link href="#intro" className="hover:text-[#F3BA2F] transition-colors">Introduction</Link></li>
                      <li><Link href="#sdd" className="hover:text-[#F3BA2F] transition-colors">Spec-Driven DevOps</Link></li>
                      <li><Link href="#safety" className="hover:text-[#F3BA2F] transition-colors">Safety Rails</Link></li>
                      <li><Link href="#usage" className="hover:text-[#F3BA2F] transition-colors">Protocol Usage</Link></li>
                  </ul>
              </div>
              <div>
                  <h3 className="text-white font-bold mb-4 uppercase text-xs tracking-widest border-b border-white/10 pb-2">License</h3>
                  <ul className="space-y-3 text-sm">
                      <li><Link href="#license" className="hover:text-[#F3BA2F] transition-colors">CC BY 4.0</Link></li>
                      <li><Link href="#attribution" className="hover:text-[#F3BA2F] transition-colors">Attribution</Link></li>
                      <li><Link href="#faq" className="hover:text-[#F3BA2F] transition-colors">FAQ</Link></li>
                      <li><Link href="#third-party" className="hover:text-[#F3BA2F] transition-colors">Third-Party Notice</Link></li>
                  </ul>
              </div>
              <div>
                  <h3 className="text-white font-bold mb-4 uppercase text-xs tracking-widest border-b border-white/10 pb-2">Modules</h3>
                  <ul className="space-y-3 text-sm">
                      <li className="text-white/60">Aster Farmer</li>
                      <li className="text-white/60">Mind Shield</li>
                      <li className="text-white/20">Dark Pool [RESTRICTED]</li>
                  </ul>
              </div>
          </aside>

          {/* CONTENT */}
          <div className="col-span-3 space-y-16">
              
              <section id="intro">
                  <div className="inline-block px-2 py-1 bg-[#F3BA2F]/10 text-[#F3BA2F] text-[10px] rounded mb-4">
                      PUBLIC CLEARANCE
                  </div>
                  <div className="mb-4 text-xs text-gray-500">
                    EN/PT enabled. Technical terms remain in English for operational consistency.
                  </div>
                  <h1 className="text-4xl font-bold text-white mb-6">Introduction to OKTO</h1>
                  <BiText
                    className="text-lg leading-relaxed mb-6 space-y-2"
                    en="OKTO is a Headless Liquidity Node designed for BNB Smart Chain. It enables institutional-grade execution directly from local environment, without dependency on traditional web interfaces."
                    pt="OKTO e um Headless Liquidity Node para BNB Smart Chain. Ele permite execution de nivel institucional direto do ambiente local, sem dependencia de web interfaces tradicionais."
                  />
                  <div className="p-4 bg-white/5 border border-white/10 rounded text-sm">
                      <p className="text-[#F3BA2F]">⚠ WARNING:</p>
                      <BiText
                        className="mt-1 space-y-1"
                        en='OKTO is not a "bot". It is an autonomous agent. Once initialized, it executes logic defined in your genesis spec.'
                        pt='OKTO nao e "bot". E um autonomous agent. Depois de inicializado, executa a logic definida na sua genesis spec.'
                      />
                  </div>
              </section>

              <section id="sdd">
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

              <section id="safety">
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

               <section id="mind-shield">
                  <h2 className="text-2xl font-bold text-white mb-4">Mind Shield Protocol</h2>
                  <p className="mb-4">
                     OKTO implements a cognitive firewall to prevent LLM hallucinations from affecting financial logic. The &quot;Mind Shield&quot; validates all agent outputs against the <code className="text-[#F3BA2F]">genesis.yaml</code> constraints.
                  </p>
              </section>

              <section id="usage">
                  <h2 className="text-2xl font-bold text-white mb-4">Protocol Usage</h2>
                  <BiText
                    className="mb-4 space-y-1"
                    en="This protocol is operated via terminal. The interface is CLI-first and flow is deterministic, with local simulation before any on-chain submission."
                    pt="Este protocolo opera via terminal. A interface e CLI-first e o fluxo e deterministico, com simulation local antes de qualquer envio on-chain."
                  />
                  <div className="bg-black/50 border border-white/10 rounded p-4 overflow-x-auto mb-6">
                    <pre className="text-xs text-gray-300">
{`$ git clone https://github.com/DGuedz/okto-agentic-trader
$ cd okto && python -m okto --mode live
[SIGNAL] opportunity detected...
[OK] tx simulated -> verified
[OK] tx confirmed -> 0x...`}
                    </pre>
                  </div>
                  <ul className="list-disc pl-5 space-y-2">
                      <li><strong className="text-white">Configuration:</strong> define parameters in <code className="text-[#F3BA2F]">genesis.yaml</code> and load keys via environment variables.</li>
                      <li><strong className="text-white">Security:</strong> signing occurs only in the local backend. Private keys are never logged, persisted, or exposed to the frontend.</li>
                      <li><strong className="text-white">Simulation:</strong> every execution is validated locally with checks for slippage, cost, and sequence.</li>
                      <li><strong className="text-white">Settlement:</strong> finalize only after verifiable on-chain confirmation.</li>
                  </ul>
              </section>

              <section id="license">
                  <h2 className="text-2xl font-bold text-white mb-4">Creative Commons — CC BY 4.0</h2>
                  <BiText
                    className="mb-4 space-y-1"
                    en="The public content of OKTO (site, docs, texts and visual materials) is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)."
                    pt="O conteudo publico do OKTO (site, docs, textos e materiais visuais) esta licenciado em Creative Commons Attribution 4.0 International (CC BY 4.0)."
                  />
                  <BiText
                    className="mb-4 space-y-1"
                    en="You may copy, redistribute, remix and adapt, including commercial use, as long as proper attribution is preserved."
                    pt="Voce pode copiar, redistribuir, remixar e adaptar, inclusive para uso comercial, desde que a atribuicao correta seja mantida."
                  />
                  <div className="grid md:grid-cols-2 gap-6">
                      <div className="bg-white/5 border border-white/10 rounded p-4">
                          <h3 className="text-white font-bold mb-2 text-sm uppercase tracking-widest">Covered by CC BY 4.0</h3>
                          <ul className="list-disc pl-5 space-y-1 text-sm">
                              <li>Documentation and institutional pages.</li>
                              <li>Editorial content, manifestos, and tutorials.</li>
                              <li>Original visual materials and project screenshots.</li>
                              <li>Presentation content and pitch decks.</li>
                          </ul>
                      </div>
                      <div className="bg-white/5 border border-white/10 rounded p-4">
                          <h3 className="text-white font-bold mb-2 text-sm uppercase tracking-widest">Exceptions</h3>
                          <ul className="list-disc pl-5 space-y-1 text-sm">
                              <li>Software source code.</li>
                              <li>Third-party trademarks and logos.</li>
                              <li>Content with a different explicit license.</li>
                          </ul>
                      </div>
                  </div>
                  <p className="text-xs text-gray-500 mt-4">
                      Golden Rule: Creative Commons is for content, not for software.
                  </p>
              </section>

              <section id="attribution">
                  <h2 className="text-2xl font-bold text-white mb-4">Official Attribution</h2>
                  <p className="mb-4">
                      To reuse any part of OKTO content, use the full attribution below.
                  </p>
                  <div className="bg-black/50 border border-white/10 rounded p-4 text-sm space-y-1">
                      <div><span className="text-white">Title:</span> OKTO — Sovereign Agentic Trading Infrastructure</div>
                      <div><span className="text-white">Author:</span> DGuedz / Double Green</div>
                      <div><span className="text-white">Year:</span> 2026</div>
                      <div><span className="text-white">Source:</span> https://okto-agentic-trader.vercel.app</div>
                      <div><span className="text-white">Profile:</span> https://x.com/dg_doublegreen</div>
                      <div><span className="text-white">License:</span> https://creativecommons.org/licenses/by/4.0/</div>
                  </div>
                  <div className="mt-6 space-y-2 text-sm">
                      <p className="text-white">Short text (1 line):</p>
                      <p>OKTO — Sovereign Agentic Trading Infrastructure © 2026 (DGuedz / Double Green) — CC BY 4.0.</p>
                      <p className="text-white">Short text with links:</p>
                      <p>
                        OKTO — Sovereign Agentic Trading Infrastructure © 2026 (DGuedz / Double Green) — Licensed under CC BY 4.0.
                      </p>
                  </div>
              </section>

              <section id="faq">
                  <h2 className="text-2xl font-bold text-white mb-4">FAQ</h2>
                  <div className="space-y-4">
                      <div>
                          <p className="text-white font-bold">Can I use it commercially?</p>
                          <p>Yes. CC BY 4.0 allows commercial use with proper attribution. / Sim. CC BY 4.0 permite uso comercial com atribuicao correta.</p>
                      </div>
                      <div>
                          <p className="text-white font-bold">Can I remix and create derivatives?</p>
                          <p>Yes. CC BY 4.0 allows adaptation and derivatives. / Sim. CC BY 4.0 permite adaptacao e derivados.</p>
                      </div>
                      <div>
                          <p className="text-white font-bold">Do I need to license my derivative under CC BY too?</p>
                          <p>No. CC BY is not copyleft. It only requires credit.</p>
                      </div>
                      <div>
                          <p className="text-white font-bold">What about OKTO code?</p>
                          <p>Software should use a software license (MIT/Apache-2.0). CC is not recommended for code.</p>
                      </div>
                      <div>
                          <p className="text-white font-bold">What if I don&#39;t want commercial use?</p>
                          <p>That would be CC BY-NC, but it reduces adoption and compatibility. For hackathons, CC BY is the standard.</p>
                      </div>
                  </div>
              </section>

              <section id="third-party">
                  <h2 className="text-2xl font-bold text-white mb-4">Third-Party Notice</h2>
                  <p className="mb-4">
                      Some materials may contain third-party trademarks, logos, or references. These items remain under the rights of their respective owners. Where applicable, OKTO indicates sources or maintains original copyright notices.
                  </p>
                  <div className="bg-white/5 border border-white/10 rounded p-4 text-sm">
                      <p className="text-white">Official Declaration:</p>
                      <p>OKTO — Sovereign Agentic Trading Infrastructure © 2026 (DGuedz / Double Green)</p>
                      <p>Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)</p>
                      <p>License: https://creativecommons.org/licenses/by/4.0/</p>
                      <p>Source: https://okto-agentic-trader.vercel.app</p>
                  </div>
              </section>

          </div>

        </div>
      </main>
    </WalletGate>
  );
}
