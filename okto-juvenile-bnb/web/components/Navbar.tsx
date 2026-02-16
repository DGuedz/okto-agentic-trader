import Link from "next/link";
import WalletConnect from "@/components/WalletConnect";

export default function Navbar() {
  return (
    <nav className="border-b border-[#F3BA2F]/20 bg-[#0B0E11]/90 backdrop-blur-xl sticky top-0 z-50 font-mono">
      <div className="container mx-auto px-6 h-20 flex items-center justify-between">
        
        {/* LOGO: COMMAND HOSTNAME */}
        <Link href="/" className="flex items-center gap-3 group">
          <div className="w-8 h-8 bg-[#F3BA2F] rounded-sm shadow-[0_0_10px_#F3BA2F] flex items-center justify-center">
             <img src="/assets/okto-logo-final.png" alt="Okto" className="w-6 h-6 object-contain opacity-90" />
          </div>
          <span className="text-white text-xl font-bold tracking-tighter group-hover:text-[#F3BA2F] transition-colors">
            Okto
          </span>
        </Link>
        
        {/* NAV: COMMAND LINKS */}
        <div className="hidden md:flex gap-8 text-xs md:text-sm text-gray-400">
          <Link href="/docs" className="hover:text-[#F3BA2F] transition-colors flex items-center gap-1">
            <span className="text-[#F3BA2F]/50">[/]</span> DOCS
          </Link>
          <Link href="/architecture" className="hover:text-[#F3BA2F] transition-colors flex items-center gap-1">
            <span className="text-[#F3BA2F]/50">[/]</span> ARCHITECT_CHANNEL
          </Link>
          <Link href="/blog" className="hover:text-[#F3BA2F] transition-colors flex items-center gap-1">
            <span className="text-[#F3BA2F]/50">[/]</span> INTEL_BLOG
          </Link>
        </div>

        {/* STATUS DECK */}
        <div className="flex items-center gap-6">
          <div className="hidden lg:flex flex-col items-end text-[10px] text-[#F3BA2F]/70 font-bold leading-tight">
            <span>LATENCY: 14ms</span>
            <span>GAS: 0.05 GWEI</span>
          </div>
          <WalletConnect />
        </div>
      </div>
    </nav>
  );
}