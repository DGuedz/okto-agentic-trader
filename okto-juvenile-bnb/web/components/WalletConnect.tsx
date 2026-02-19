 "use client";

import React, { useState, useEffect } from 'react';
import { Wallet, ChevronDown, CheckCircle, ExternalLink } from 'lucide-react';

export default function WalletConnect() {
  const [isConnecting, setIsConnecting] = useState(false);
  const [isConnected, setIsConnected] = useState(false);
  const [address, setAddress] = useState<string | null>(null);

  useEffect(() => {
    const connected = localStorage.getItem('okto_wallet_connected') === 'true';
    if (connected) {
      setIsConnected(true);
      setAddress('0x71C...9A2');
      if (!localStorage.getItem('okto_wallet_address')) {
        localStorage.setItem('okto_wallet_address', '0x71C7656EC7ab88b098defB751B7401B5f6d899A2');
      }
    }
  }, []);

  const handleConnect = () => {
    setIsConnecting(true);
    setTimeout(() => {
      localStorage.setItem('okto_wallet_connected', 'true');
      localStorage.setItem('okto_wallet_address', '0x71C7656EC7ab88b098defB751B7401B5f6d899A2');
      setIsConnected(true);
      setAddress('0x71C...9A2');
      setIsConnecting(false);
      window.dispatchEvent(new Event('wallet-connection-changed'));
    }, 1500);
  };

  const handleDisconnect = () => {
    localStorage.removeItem('okto_wallet_connected');
    localStorage.removeItem('okto_wallet_address');
    setIsConnected(false);
    setAddress(null);
    window.dispatchEvent(new Event('wallet-connection-changed'));
  };

  if (isConnected && address) {
    return (
      <div className="relative group">
        <button 
          className="flex items-center gap-2 bg-[#F3BA2F]/20 border border-[#F3BA2F] text-[#F3BA2F] px-4 py-2 rounded-sm font-mono text-xs uppercase tracking-widest hover:bg-[#F3BA2F]/30 transition-all"
        >
          <div className="w-2 h-2 bg-[#F3BA2F] rounded-full animate-pulse" />
          {address}
        </button>
        
        {/* Dropdown */}
        <div className="absolute right-0 mt-2 w-48 bg-[#0B0E11] border border-[#F3BA2F]/20 rounded-sm shadow-[0_0_20px_rgba(0,0,0,0.5)] opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none group-hover:pointer-events-auto z-50">
          <div className="p-3 border-b border-[#F3BA2F]/10 text-[10px] text-gray-500 font-mono uppercase tracking-wider">
            Connected to BNB Chain
          </div>
          <a 
            href="https://bscscan.com/address/0x71C7656EC7ab88b098defB751B7401B5f6d899A2" 
            target="_blank"
            rel="noopener noreferrer"
            className="w-full text-left px-4 py-3 hover:bg-white/5 text-xs text-gray-300 flex items-center gap-2 font-mono transition-colors"
          >
            <ExternalLink size={12} /> View on BscScan
          </a>
          <button 
            onClick={handleDisconnect}
            className="w-full text-left px-4 py-3 hover:bg-red-500/10 text-xs text-red-400 font-mono transition-colors border-t border-[#F3BA2F]/10"
          >
            Disconnect Session
          </button>
        </div>
      </div>
    );
  }

  return (
    <button
      onClick={handleConnect}
      disabled={isConnecting}
      className="border border-[#F3BA2F] text-[#F3BA2F] px-4 py-2 text-xs hover:bg-[#F3BA2F] hover:text-black transition-all uppercase tracking-widest font-bold shadow-[0_0_10px_rgba(243,186,47,0.2)] flex items-center gap-2 disabled:opacity-50 disabled:cursor-wait"
    >
      {isConnecting ? (
        <>
          <span className="w-3 h-3 border-2 border-[#F3BA2F] border-t-transparent rounded-full animate-spin" />
          INITIALIZING...
        </>
      ) : (
        <>
          Initialize_Session
        </>
      )}
    </button>
  );
}
