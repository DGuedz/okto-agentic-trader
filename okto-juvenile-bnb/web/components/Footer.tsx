export default function Footer() {
  return (
    <footer className="border-t border-border-subtle bg-bg-1 mt-20">
      <div className="container mx-auto px-6 py-12">
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-8">
          <div>
            <h3 className="font-mono font-bold text-lg text-text-primary mb-2">OKTO_INFRA</h3>
            <p className="text-text-secondary text-sm max-w-md">
              Sovereign Agentic Trading Infrastructure.
              <br />
              Headless, spec-driven, and auditable by design.
            </p>
          </div>
          <div className="flex gap-8 text-sm text-text-muted">
            <a href="#" className="hover:text-accent-amber-400 transition-colors">Manifesto</a>
            <a href="#" className="hover:text-accent-amber-400 transition-colors">GitHub</a>
            <a href="#" className="hover:text-accent-amber-400 transition-colors">Docs</a>
          </div>
        </div>
        <div className="mt-12 pt-8 border-t border-border-subtle flex justify-between items-center text-xs text-text-muted font-mono">
          <p>Okto Agentic System © 2026</p>
          <div className="flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-accent-neon-400 animate-pulse"></span>
            SYSTEM: ONLINE
          </div>
        </div>
      </div>
    </footer>
  );
}
