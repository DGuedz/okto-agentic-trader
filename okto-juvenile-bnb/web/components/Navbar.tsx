import Link from "next/link";
import { Terminal } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="border-b border-border-subtle bg-bg-1/80 backdrop-blur-md sticky top-0 z-50">
      <div className="container mx-auto px-6 h-16 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2 group">
          <div className="p-2 bg-accent-amber-400/10 rounded-md border border-accent-amber-400/20 group-hover:border-accent-amber-400/50 transition-colors">
            <Terminal className="w-5 h-5 text-accent-amber-400" />
          </div>
          <span className="font-mono font-bold text-lg tracking-tight">OKTO_INFRA</span>
        </Link>
        
        <div className="hidden md:flex items-center gap-8 text-sm font-medium text-text-secondary">
          <Link href="/architecture" className="hover:text-text-primary transition-colors">Architecture</Link>
          <Link href="/docs" className="hover:text-text-primary transition-colors">Docs</Link>
          <Link href="/security" className="hover:text-text-primary transition-colors">Security</Link>
          <Link href="/demo" className="hover:text-text-primary transition-colors">Live Demo</Link>
        </div>

        <div className="flex items-center gap-4">
          <a 
            href="https://github.com/DGuedz/okto-agentic-trader" 
            target="_blank" 
            rel="noopener noreferrer"
            className="hidden md:flex items-center gap-2 px-4 py-2 rounded-full bg-accent-amber-400 text-text-inverse font-bold text-sm shadow-glowAmber hover:brightness-110 transition-all"
          >
            Clone Repo
          </a>
        </div>
      </div>
    </nav>
  );
}
