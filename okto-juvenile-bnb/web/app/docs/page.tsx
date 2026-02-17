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
                  <h1 className="text-4xl font-bold text-white mb-6">Introduction to OKTO</h1>
                  <p className="text-lg leading-relaxed mb-6">
                      OKTO is a <strong className="text-white">Headless Liquidity Node</strong> designed for the BNB Smart Chain. It allows developers to deploy institutional-grade trading strategies directly from their local environment, bypassing traditional web interfaces.
                  </p>
                  <div className="p-4 bg-white/5 border border-white/10 rounded text-sm">
                      <p className="text-[#F3BA2F]">⚠ WARNING:</p>
                      <p className="mt-1">
                          OKTO is not a &quot;bot&quot;. It is an autonomous agent. Once initialized, it will execute logic defined in your genesis spec without human intervention.
                      </p>
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
                  <p className="mb-4">
                      Este protocolo é operado via terminal. A interface é o CLI e o fluxo é determinístico, com simulação local antes de qualquer envio on-chain.
                  </p>
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
                      <li><strong className="text-white">Configuração:</strong> defina parâmetros no <code className="text-[#F3BA2F]">genesis.yaml</code> e carregue chaves por variáveis de ambiente.</li>
                      <li><strong className="text-white">Segurança:</strong> assinatura ocorre somente no backend local. Chaves privadas nunca são logadas, persistidas ou expostas no frontend.</li>
                      <li><strong className="text-white">Simulação:</strong> toda execução é validada localmente com verificação de slippage, custo e sequência.</li>
                      <li><strong className="text-white">Liquidação:</strong> finalize somente após confirmação on-chain verificável.</li>
                  </ul>
              </section>

              <section id="license">
                  <h2 className="text-2xl font-bold text-white mb-4">Creative Commons — CC BY 4.0</h2>
                  <p className="mb-4">
                      O conteúdo público do projeto OKTO — Sovereign Agentic Trading Infrastructure (site, documentação, textos e materiais visuais autorais) é licenciado sob Creative Commons Attribution 4.0 International (CC BY 4.0).
                  </p>
                  <p className="mb-4">
                      Esta licença permite copiar, redistribuir, remixar, adaptar e criar derivados, inclusive para uso comercial, desde que haja atribuição correta ao autor e à fonte.
                  </p>
                  <div className="grid md:grid-cols-2 gap-6">
                      <div className="bg-white/5 border border-white/10 rounded p-4">
                          <h3 className="text-white font-bold mb-2 text-sm uppercase tracking-widest">Coberto por CC BY 4.0</h3>
                          <ul className="list-disc pl-5 space-y-1 text-sm">
                              <li>Documentação e páginas institucionais.</li>
                              <li>Conteúdo editorial, manifestos e tutoriais.</li>
                              <li>Materiais visuais autorais e screenshots do projeto.</li>
                              <li>Conteúdo de apresentação e pitch.</li>
                          </ul>
                      </div>
                      <div className="bg-white/5 border border-white/10 rounded p-4">
                          <h3 className="text-white font-bold mb-2 text-sm uppercase tracking-widest">Exceções</h3>
                          <ul className="list-disc pl-5 space-y-1 text-sm">
                              <li>Código-fonte do software.</li>
                              <li>Marcas e logotipos de terceiros.</li>
                              <li>Conteúdo com licença explícita diferente.</li>
                          </ul>
                      </div>
                  </div>
                  <p className="text-xs text-gray-500 mt-4">
                      Regra de ouro: Creative Commons é para conteúdo, não para software.
                  </p>
              </section>

              <section id="attribution">
                  <h2 className="text-2xl font-bold text-white mb-4">Atribuição Oficial</h2>
                  <p className="mb-4">
                      Para reutilizar qualquer parte do conteúdo do OKTO, use a atribuição completa abaixo.
                  </p>
                  <div className="bg-black/50 border border-white/10 rounded p-4 text-sm space-y-1">
                      <div><span className="text-white">Título:</span> OKTO — Sovereign Agentic Trading Infrastructure</div>
                      <div><span className="text-white">Autor:</span> DGuedz / Double Green</div>
                      <div><span className="text-white">Ano:</span> 2026</div>
                      <div><span className="text-white">Fonte:</span> https://okto-agentic-trader.vercel.app</div>
                      <div><span className="text-white">Perfil:</span> https://x.com/dg_doublegreen</div>
                      <div><span className="text-white">Licença:</span> https://creativecommons.org/licenses/by/4.0/</div>
                  </div>
                  <div className="mt-6 space-y-2 text-sm">
                      <p className="text-white">Texto curto (1 linha):</p>
                      <p>OKTO — Sovereign Agentic Trading Infrastructure © 2026 (DGuedz / Double Green) — CC BY 4.0.</p>
                      <p className="text-white">Texto curto com links:</p>
                      <p>
                        OKTO — Sovereign Agentic Trading Infrastructure © 2026 (DGuedz / Double Green) — Licensed under CC BY 4.0.
                      </p>
                  </div>
              </section>

              <section id="faq">
                  <h2 className="text-2xl font-bold text-white mb-4">FAQ</h2>
                  <div className="space-y-4">
                      <div>
                          <p className="text-white font-bold">Posso usar comercialmente?</p>
                          <p>Sim. CC BY 4.0 permite uso comercial desde que haja atribuição correta.</p>
                      </div>
                      <div>
                          <p className="text-white font-bold">Posso remixar e criar derivados?</p>
                          <p>Sim. CC BY 4.0 permite adaptação e derivados.</p>
                      </div>
                      <div>
                          <p className="text-white font-bold">Preciso licenciar meu derivado também em CC BY?</p>
                          <p>Não. CC BY não é copyleft. Só exige crédito.</p>
                      </div>
                      <div>
                          <p className="text-white font-bold">E o código do OKTO?</p>
                          <p>Software deve usar licença de software (MIT/Apache-2.0). CC não é recomendado para código.</p>
                      </div>
                      <div>
                          <p className="text-white font-bold">E se eu não quiser uso comercial?</p>
                          <p>Seria CC BY-NC, mas reduz adoção e compatibilidade. Para hackathons, CC BY é o padrão.</p>
                      </div>
                  </div>
              </section>

              <section id="third-party">
                  <h2 className="text-2xl font-bold text-white mb-4">Aviso de Terceiros</h2>
                  <p className="mb-4">
                      Alguns materiais podem conter marcas, logos ou referências de terceiros. Esses itens permanecem sob os direitos de seus respectivos proprietários. Onde aplicável, o OKTO indica fontes ou mantém avisos de copyright originais.
                  </p>
                  <div className="bg-white/5 border border-white/10 rounded p-4 text-sm">
                      <p className="text-white">Declaração oficial:</p>
                      <p>OKTO — Sovereign Agentic Trading Infrastructure © 2026 (DGuedz / Double Green)</p>
                      <p>Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)</p>
                      <p>Licença: https://creativecommons.org/licenses/by/4.0/</p>
                      <p>Fonte: https://okto-agentic-trader.vercel.app</p>
                  </div>
              </section>

          </div>

        </div>
      </main>
    </WalletGate>
  );
}
