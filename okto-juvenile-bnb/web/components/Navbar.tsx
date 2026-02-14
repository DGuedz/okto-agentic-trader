import Link from "next/link";
import { Terminal } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="border-b border-white/5 bg-bg-0/60 backdrop-blur-xl sticky top-0 z-50 transition-all duration-300">
      <div className="container mx-auto px-6 h-20 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-4 group relative z-10">
          <div className="relative">
            <div className="absolute inset-0 bg-accent-amber-400/20 blur-xl rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-500 scale-125"></div>
            <img 
              src="/assets/okto-logo-final.png" 
              alt="OKTO Logo" 
              className="w-10 h-10 object-contain transition-all duration-500 ease-out opacity-90 group-hover:opacity-100 group-hover:scale-150 group-hover:rotate-6 relative z-10" 
            />
          </div>
          <span className="font-mono font-bold text-lg tracking-wider text-text-primary group-hover:text-accent-amber-400 transition-colors duration-300 group-hover:translate-x-3">
            OKTO<span className="text-white/20">_</span>INFRA
          </span>
        </Link>
        
        <div className="hidden md:flex items-center gap-10 text-xs font-mono uppercase tracking-widest text-text-secondary/80 absolute left-1/2 -translate-x-1/2">
          {['Architecture', 'Docs', 'Security', 'Live Demo'].map((item) => (
            <Link 
              key={item} 
              href={`/${item.toLowerCase().replace(' ', '')}`} 
              className="hover:text-accent-neon-400 transition-colors duration-300 relative group"
            >
              <span className="relative z-10">{item}</span>
              <span className="absolute -bottom-1 left-0 w-0 h-[1px] bg-accent-neon-400 transition-all duration-300 group-hover:w-full"></span>
            </Link>
          ))}
        </div>

        <div className="flex items-center gap-4 relative z-10">
          <a 
            href="https://github.com/DGuedz/okto-agentic-trader" 
            target="_blank" 
            rel="noopener noreferrer"
            className="hidden md:flex items-center gap-2 px-5 py-2.5 rounded-sm bg-accent-amber-400/90 hover:bg-accent-amber-400 text-bg-0 font-mono font-bold text-xs uppercase tracking-wider shadow-[0_0_20px_rgba(253,186,18,0.3)] hover:shadow-[0_0_30px_rgba(253,186,18,0.5)] hover:-translate-y-0.5 transition-all duration-300 border border-accent-amber-400"
          >
            <span>Clone Repo</span>
            <span className="text-[10px] opacity-60">↗</span>
          </a>
        </div>
      </div>
    </nav>
  );
}
