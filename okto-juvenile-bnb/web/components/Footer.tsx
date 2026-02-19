"use client";

import BiText from "@/components/BiText";
import LText from "@/components/LText";

export default function Footer() {
  return (
    <footer className="border-t border-border-subtle bg-bg-1 mt-20">
      <div className="container mx-auto px-6 py-12">
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-8">
          <div>
            <h3 className="font-mono font-bold text-lg text-text-primary mb-2">OKTO_INFRA</h3>
            <BiText
              className="text-text-secondary text-sm max-w-md"
              en="Sovereign Agentic Trading Infrastructure. Headless, spec-driven, and auditable by design."
              pt="Infraestrutura Agentic Trading soberana. Headless, guiada por spec e auditavel por design."
            />
            <div className="text-accent-amber-400 text-xs mt-2 block">
              <LText en="Built for BNB Chain OpenClaw Hackathon 2026." pt="Construido para o BNB Chain OpenClaw Hackathon 2026." />
            </div>
          </div>
          <div className="flex flex-wrap gap-6 text-sm text-text-muted">
            <a href="/docs#usage" className="hover:text-accent-amber-400 transition-colors"><LText en="Use Protocol" pt="Uso do Protocol" /></a>
            <a href="/docs#license" className="hover:text-accent-amber-400 transition-colors"><LText en="License" pt="Licenca" /></a>
            <a href="/architecture" className="hover:text-accent-amber-400 transition-colors"><LText en="Architecture" pt="Arquitetura" /></a>
            <a href="/blog" className="hover:text-accent-amber-400 transition-colors"><LText en="Manifesto" pt="Manifesto" /></a>
            <a href="/demo" className="hover:text-accent-amber-400 transition-colors"><LText en="Demo" pt="Demo" /></a>
            <a href="https://github.com/DGuedz/okto-agentic-trader" className="hover:text-accent-amber-400 transition-colors">GitHub</a>
          </div>
        </div>
        <div className="mt-12 pt-8 border-t border-border-subtle flex flex-col md:flex-row justify-between items-start md:items-center gap-6 text-xs text-text-muted font-mono">
          <div className="space-y-2">
            <p>OKTO — Sovereign Agentic Trading Infrastructure © 2026 (DGuedz / Double Green)</p>
            <p>
              <a href="https://okto-agentic-trader.vercel.app" className="hover:text-accent-amber-400 transition-colors">Source</a>
              <span className="mx-2">•</span>
              <a href="https://x.com/dg_doublegreen" className="hover:text-accent-amber-400 transition-colors">Creator</a>
              <span className="mx-2">•</span>
              <a href="https://creativecommons.org/licenses/by/4.0/" className="hover:text-accent-amber-400 transition-colors">CC BY 4.0</a>
            </p>
          </div>
          <div className="flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-accent-neon-400 animate-pulse"></span>
            <LText en="SYSTEM: ONLINE" pt="SISTEMA: ONLINE" />
          </div>
        </div>
      </div>
    </footer>
  );
}
