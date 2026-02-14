import TerminalWidget from "@/components/TerminalWidget";

export default function Demo() {
  return (
    <div className="container mx-auto px-6 py-20">
      <h1 className="text-4xl font-bold font-mono mb-8 text-accent-amber-400">Live Simulation</h1>
      <p className="text-text-secondary mb-8">
        This demo visualizes the decision-making process of the Okto brain in real-time.
      </p>
      
      <div className="bg-bg-1 border border-border-subtle rounded-2xl p-1 overflow-hidden shadow-2xl h-[600px]">
        <TerminalWidget />
      </div>
      
      <div className="mt-12 text-center">
        <p className="text-text-muted text-sm font-mono mb-4">Want to run this on your own data?</p>
        <a href="https://github.com/DGuedz/okto-agentic-trader" className="px-6 py-3 bg-accent-amber-400 text-text-inverse font-bold rounded-full shadow-glowAmber hover:brightness-110 transition-all">
            Deploy Your Own Agent
        </a>
      </div>
    </div>
  );
}
