import { Shield } from "lucide-react";
import BiText from "@/components/BiText";

export default function Security() {
  return (
    <div className="container mx-auto px-6 py-20">
      <h1 className="text-4xl font-bold font-mono mb-8 text-accent-amber-400 flex items-center gap-4">
        <Shield className="w-10 h-10" />
        Security Model / Modelo de seguranca
      </h1>
      
      <div className="grid md:grid-cols-2 gap-8">
        <div className="bg-surface-card border border-border-subtle p-8 rounded-xl">
            <h3 className="text-xl font-bold text-text-primary mb-4">Local-First Keys / Chaves Local-First</h3>
            <BiText
              className="text-text-secondary space-y-2"
              en="Okto never transmits your private keys. They are loaded from your local `.env` file directly into the process memory and cleared upon termination."
              pt="Okto nunca transmite suas private keys. Elas sao carregadas do seu `.env` local para process memory e limpas no encerramento."
            />
        </div>
        <div className="bg-surface-card border border-border-subtle p-8 rounded-xl">
            <h3 className="text-xl font-bold text-text-primary mb-4">Anti-MEV Architecture / Arquitetura Anti-MEV</h3>
            <BiText
              className="text-text-secondary space-y-2"
              en="By default, Okto routes DEX transactions through private RPC relays to reduce sandwich attack exposure."
              pt="Por padrao, o Okto envia transacoes DEX por private RPC relays para reduzir exposicao a sandwich attacks."
            />
        </div>
        <div className="bg-surface-card border border-border-subtle p-8 rounded-xl">
            <h3 className="text-xl font-bold text-text-primary mb-4">Simulation Mode / Modo de simulacao</h3>
            <BiText
              className="text-text-secondary space-y-2"
              en="Every transaction is simulated before broadcasting. If failure or excessive slippage is predicted, execution is vetoed."
              pt="Toda transacao passa por simulation antes do broadcast. Se houver previsao de falha ou slippage excessivo, a execution e vetada."
            />

        </div>
        <div className="bg-surface-card border border-border-subtle p-8 rounded-xl">
            <h3 className="text-xl font-bold text-text-primary mb-4">Circuit Breakers / Disjuntores de risco</h3>
            <BiText
              className="text-text-secondary space-y-2"
              en="Hard-coded stop limits can halt trading and cancel open orders when risk thresholds are reached."
              pt="Limites hard-coded de stop podem pausar trading e cancelar open orders quando os thresholds de risco sao atingidos."
            />
        </div>
      </div>
    </div>
  );
}
