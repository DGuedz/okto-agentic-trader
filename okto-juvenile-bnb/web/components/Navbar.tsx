"use client";

import Link from "next/link";
import WalletConnect from "@/components/WalletConnect";
import LText from "@/components/LText";
import { useLanguage } from "@/components/LanguageProvider";

export default function Navbar() {
  const { language, setLanguage } = useLanguage();

  return (
    <nav className="border-b border-[#F3BA2F]/20 bg-[#0B0E11]/90 backdrop-blur-xl sticky top-0 z-50 font-mono">
      <div className="container mx-auto px-6 h-20 flex items-center justify-between">
        
        {/* LOGO: COMMAND HOSTNAME */}
        <Link href="/" className="flex items-center gap-3 group">
          <div className="w-10 h-10 bg-[#F3BA2F] rounded shadow-[0_0_20px_rgba(243,186,47,0.4)] flex items-center justify-center group-hover:shadow-[0_0_30px_rgba(243,186,47,0.6)] transition-all duration-300">
             <img src="/assets/okto-logo-final.png" alt="Okto" className="w-7 h-7 object-contain" />
          </div>
          <span className="text-white text-2xl font-bold tracking-tighter group-hover:text-[#F3BA2F] transition-colors">
            Okto
          </span>
        </Link>
        
        {/* NAV: COMMAND LINKS */}
        <div className="hidden md:flex gap-8 text-xs md:text-sm text-gray-400">
          <Link href="/demo" className="hover:text-[#F3BA2F] transition-colors flex items-center gap-1">
            <span className="text-[#F3BA2F]/50">[/]</span> <LText en="TERMINAL" pt="TERMINAL" />
          </Link>
          <Link href="/docs" className="hover:text-[#F3BA2F] transition-colors flex items-center gap-1">
            <span className="text-[#F3BA2F]/50">[/]</span> <LText en="DOCS" pt="DOCUMENTACAO" />
          </Link>
          <Link href="/architecture" className="hover:text-[#F3BA2F] transition-colors flex items-center gap-1">
            <span className="text-[#F3BA2F]/50">[/]</span> <LText en="ARCHITECT_CHANNEL" pt="ARQUITETURA" />
          </Link>
          <Link href="/blog" className="hover:text-[#F3BA2F] transition-colors flex items-center gap-1">
            <span className="text-[#F3BA2F]/50">[/]</span> <LText en="INTEL_BLOG" pt="BLOG" />
          </Link>
        </div>

        {/* STATUS DECK */}
        <div className="flex items-center gap-6">
          <div className="hidden lg:flex flex-col items-end text-[10px] text-[#F3BA2F]/70 font-bold leading-tight">
            <span>LATENCY: 14ms</span>
            <span>GAS: 0.05 GWEI</span>
          </div>
          <div className="hidden md:flex items-center rounded-sm border border-[#F3BA2F]/40 overflow-hidden text-[10px]">
            <button
              onClick={() => setLanguage("en")}
              className={`px-2 py-1 transition-colors ${language === "en" ? "bg-[#F3BA2F] text-black" : "text-[#F3BA2F]"}`}
              aria-label="Switch language to English"
            >
              EN
            </button>
            <button
              onClick={() => setLanguage("pt")}
              className={`px-2 py-1 transition-colors ${language === "pt" ? "bg-[#F3BA2F] text-black" : "text-[#F3BA2F]"}`}
              aria-label="Mudar idioma para Portugues"
            >
              PT
            </button>
          </div>
          <WalletConnect />
        </div>
      </div>
    </nav>
  );
}
