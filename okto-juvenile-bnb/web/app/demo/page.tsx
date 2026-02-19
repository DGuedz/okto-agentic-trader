import TerminalWidget from "@/components/TerminalWidget";
import BiText from "@/components/BiText";
import LText from "@/components/LText";

export default function Demo() {
  return (
    <div className="container mx-auto px-6 py-20">
      <h1 className="text-4xl font-bold font-mono mb-8 text-accent-amber-400"><LText en="Live Simulation" pt="Simulacao ao vivo" /></h1>
      <BiText
        className="text-text-secondary mb-8 space-y-1"
        en="This demo visualizes the decision-making process of the Okto brain in real-time."
        pt="Esta demo mostra o processo de decision-making do Okto brain em tempo real."
      />
      
      <div className="bg-bg-1 border border-border-subtle rounded-2xl p-1 overflow-hidden shadow-2xl h-[600px]">
        <TerminalWidget />
      </div>
      
      <div className="mt-12 text-center">
        <p className="text-text-muted text-sm font-mono mb-4"><LText en="Want to run this on your own data?" pt="Quer rodar com seus dados?" /></p>
        <a href="https://github.com/DGuedz/okto-agentic-trader" className="px-6 py-3 bg-accent-amber-400 text-text-inverse font-bold rounded-full shadow-glowAmber hover:brightness-110 transition-all">
            <LText en="Deploy Your Own Agent" pt="Fazer Deploy do seu Agent" />
        </a>
      </div>
    </div>
  );
}
