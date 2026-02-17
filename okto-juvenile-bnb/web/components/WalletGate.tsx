 "use client";

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { ShieldAlert } from 'lucide-react';
import WalletConnect from './WalletConnect';

export default function WalletGate({ children }: { children: React.ReactNode }) {
  const [isAuthorized, setIsAuthorized] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const checkAuth = () => {
      const connected = localStorage.getItem('okto_wallet_connected') === 'true';
      setIsAuthorized(connected);
      setIsLoading(false);
    };

    // Initial check
    checkAuth();

    // Listen for changes
    window.addEventListener('wallet-connection-changed', checkAuth);
    return () => window.removeEventListener('wallet-connection-changed', checkAuth);
  }, []);

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-[#0B0E11]">
        <div className="w-8 h-8 border-2 border-[#F3BA2F] border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  if (!isAuthorized) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center bg-[#0B0E11] text-[#F3BA2F] font-mono p-4 text-center">
        <div className="w-16 h-16 mb-6 border border-[#F3BA2F] flex items-center justify-center animate-pulse">
          <ShieldAlert size={32} />
        </div>
        <h1 className="text-3xl font-bold mb-4">RESTRICTED ACCESS</h1>
        <p className="text-white/50 mb-8 max-w-md">
          Security Protocol Active. You must initialize a session to access this node's internal documentation and architecture.
        </p>
        
        <div className="flex flex-col items-center gap-4">
          <WalletConnect />
          <Link href="/" className="text-xs text-white/30 hover:text-white mt-4 underline">
            Return to Command Deck
          </Link>
        </div>
      </div>
    );
  }

  return <>{children}</>;
}
