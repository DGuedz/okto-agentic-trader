import WalletGate from "@/components/WalletGate";
import BiText from "@/components/BiText";
import LText from "@/components/LText";

export default function BlogPage() {
  return (
    <WalletGate>
      <main className="container mx-auto px-6 py-20 max-w-4xl">
        <article className="prose prose-invert prose-green max-w-none">
          
          <header className="mb-12 border-b border-white/10 pb-10">
            <div className="flex items-center gap-2 mb-6">
              <span className="px-2 py-0.5 bg-accent-neon-400/10 border border-accent-neon-400/20 text-accent-neon-400 text-xs rounded uppercase tracking-wider font-mono">Intel</span>
              <span className="text-white/30 text-xs">•</span>
              <span className="text-white/50 text-xs uppercase tracking-wider font-mono">February 19, 2026</span>
            </div>
            <h1 className="text-4xl md:text-5xl font-bold mb-6 tracking-tight leading-tight">
              The AI Agent Economy: <br/>
              <span className="text-[#F3BA2F] drop-shadow-[0_0_10px_rgba(243,186,47,0.5)]">Monetizing Autonomous Intelligence</span>
            </h1>
            <p className="mb-4 text-sm text-white/60">
              <LText en="Core technical terms are preserved in English." pt="Os termos tecnicos principais permanecem em ingles." />
            </p>
            <div className="flex items-center gap-4">
              <div>
                <div className="text-white font-bold text-sm">Double Green</div>
                <div className="text-white/40 text-xs">Dev & Founder, OKTO | Black Mindz Labs</div>
              </div>
            </div>
          </header>

          <div className="space-y-8 text-lg text-gray-400 leading-relaxed">
              
              <div className="mb-12 border-b border-white/10 pb-8">
                  <span className="px-2 py-0.5 bg-[#F3BA2F]/10 border border-[#F3BA2F]/20 text-[#F3BA2F] text-xs rounded uppercase tracking-wider font-mono mb-4 inline-block">Previous Post</span>
                  <h2 className="text-2xl font-bold text-white mb-2">The Interface is the Enemy</h2>
                  <p className="text-sm text-gray-500 mb-4">February 16, 2026</p>
                  <p className="mb-4">
                      While your browser struggles to render a &quot;Swap&quot; button, a headless script has already won. In the Dark Forest of DeFi, the UI is a liability.
                  </p>
                  <BiText
                    className="italic text-white/60 mb-4"
                    en='"The greatest lie told to retail traders is that you need a website to transact."'
                    pt='"A maior mentira contada aos traders de varejo é que você precisa de um site para transacionar."'
                  />
                  <p className="text-sm text-gray-500">
                      Read the full manifesto in our archives.
                  </p>
              </div>

              <BiText
                className="font-bold text-white text-xl"
                en="The game has changed. BNB Chain has officially deployed the ERC-8004 infrastructure, laying the foundation for the Trustless Agent Economy."
                pt="O jogo mudou. A BNB Chain implantou oficialmente a infraestrutura ERC-8004, estabelecendo a base para a Trustless Agent Economy."
              />

              <p>
                  This is not just another protocol update. This is the birth of a new asset class: <strong>Verifiable Autonomous Agents</strong>. Until now, bots were just scripts running in the dark. Now, they are on-chain entities with Identity (Passport) and Reputation (Credit Score).
              </p>

              <h2 className="text-2xl font-bold text-white mt-12 mb-4 border-l-4 border-[#F3BA2F] pl-4">The Cash Flow Mechanism</h2>
              <BiText
                en="How do you monetize this? By deploying an agent that builds trust. In the AI Agent Economy, 'Reputation' is the new liquidity. Agents with high on-chain reputation scores (proven via the Registry) will get priority access to:"
                pt="Como voce monetiza isso? Implantando um agente que constroi confianca. Na AI Agent Economy, 'Reputacao' e a nova liquidez. Agentes com alta reputacao on-chain (provada via Registry) terao acesso prioritario a:"
              />
              <ul className="list-disc pl-5 space-y-2 text-base">
                  <li><strong>Capital Allocation:</strong> DAOs and vaults delegating funds to proven agents.</li>
                  <li><strong>Exclusive Arbitrage:</strong> Routing priority in MEV-protected pools.</li>
                  <li><strong>Service Fees:</strong> Other contracts paying your agent for data or execution.</li>
              </ul>

              <h2 className="text-2xl font-bold text-white mt-12 mb-4 border-l-4 border-[#F3BA2F] pl-4">OKTO: Your Gateway</h2>
              <p>
                  This is where <strong>OKTO</strong> comes in. We didn&apos;t just build a trading bot; we built a <strong>Headless Liquidity Node</strong> compliant with these new standards. OKTO is designed to be the &quot;body&quot; that your strategy inhabits on-chain.
              </p>
              <BiText
                en="OKTO abstracts the complexity of ERC-8004. It handles the identity registration, the reputation proofing, and the execution logic. You remain the Sovereign Operator."
                pt="OKTO abstrai a complexidade do ERC-8004. Ele lida com o registro de identidade, a prova de reputacao e a logica de execucao. Voce permanece o Operador Soberano."
              />

              <h2 className="text-2xl font-bold text-white mt-12 mb-4 border-l-4 border-[#F3BA2F] pl-4">The Inner Circle (Mentorship)</h2>
              <p>
                  Information without execution is just noise. To truly leverage this &quot;Privileged Information,&quot; you need guidance.
              </p>
              <BiText
                className="p-4 bg-white/5 border-l-2 border-accent-neon-400 italic text-white"
                en="Our Mentorship Program is the 'Software Upgrade' for your brain. We don't just give you the code; we teach you how to configure the Genesis Spec to align with institutional flows."
                pt="Nosso Programa de Mentoria e o 'Software Upgrade' para o seu cerebro. Nao te damos apenas o codigo; ensinamos como configurar a Genesis Spec para alinhar com fluxos institucionais."
              />
              <p>
                  This product is exclusive. It is for those who want to stop being &quot;Users&quot; and start being &quot;Architects&quot; of the flow. We deep dive into the <strong>Okto Core</strong>, the <strong>Regime Engine</strong>, and the <strong>Safety Rails</strong> that keep execution disciplined and auditable.
              </p>

              <h2 className="text-2xl font-bold text-white mt-12 mb-4 border-l-4 border-[#F3BA2F] pl-4">Conclusion</h2>
              <BiText
                en="The infrastructure is live. The opportunity is raw. OKTO is the tool. The Mentorship is the manual. The cash flow awaits those who verify."
                pt="A infraestrutura esta no ar. A oportunidade e bruta. OKTO e a ferramenta. A Mentoria e o manual. O cash flow aguarda aqueles que verificam."
              />

              <div className="flex flex-wrap gap-2 mt-8 font-mono">
                  {['#ERC8004', '#AIAgentEconomy', '#BNBChain', '#Mentorship', '#CashFlow', '#Okto'].map((tag) => (
                    <span key={tag} className="px-2 py-1 bg-white/5 text-xs text-white/50 rounded hover:text-[#F3BA2F] transition-colors cursor-pointer">{tag}</span>
                  ))}
              </div>
          </div>

        </article>
      </main>
    </WalletGate>
  );
}
