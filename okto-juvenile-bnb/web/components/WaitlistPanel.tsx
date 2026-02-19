"use client";

import { useEffect, useMemo, useState } from "react";
import { useLanguage } from "@/components/LanguageProvider";

type WaitlistEntry = {
  id: string;
  method: "wallet" | "email";
  spot: number;
  email?: string;
  wallet?: string;
  timestamp: string;
};

const WAITLIST_ENTRY_KEY = "okto_waitlist_entry";
const WAITLIST_COUNT_KEY = "okto_waitlist_count";
const WALLET_CONNECTED_KEY = "okto_wallet_connected";
const WALLET_ADDRESS_KEY = "okto_wallet_address";
const MAX_PRIORITY = 100;

function readCount(): number {
  const raw = localStorage.getItem(WAITLIST_COUNT_KEY);
  const parsed = raw ? Number(raw) : 0;
  if (!Number.isFinite(parsed) || parsed < 0) return 0;
  return Math.floor(parsed);
}

function reserveSpot(method: "wallet" | "email", payload: { email?: string; wallet?: string }): WaitlistEntry | null {
  const existingRaw = localStorage.getItem(WAITLIST_ENTRY_KEY);
  if (existingRaw) {
    try {
      return JSON.parse(existingRaw) as WaitlistEntry;
    } catch {
      localStorage.removeItem(WAITLIST_ENTRY_KEY);
    }
  }

  const count = readCount();
  if (count >= MAX_PRIORITY) return null;

  const entry: WaitlistEntry = {
    id: `okto-${Date.now()}`,
    method,
    spot: count + 1,
    email: payload.email,
    wallet: payload.wallet,
    timestamp: new Date().toISOString(),
  };

  localStorage.setItem(WAITLIST_COUNT_KEY, String(entry.spot));
  localStorage.setItem(WAITLIST_ENTRY_KEY, JSON.stringify(entry));
  return entry;
}

export default function WaitlistPanel() {
  const { language } = useLanguage();
  const [email, setEmail] = useState("");
  const [entry, setEntry] = useState<WaitlistEntry | null>(null);
  const [count, setCount] = useState(0);
  const [message, setMessage] = useState<string>("");

  useEffect(() => {
    const existingRaw = localStorage.getItem(WAITLIST_ENTRY_KEY);
    if (existingRaw) {
      try {
        setEntry(JSON.parse(existingRaw) as WaitlistEntry);
      } catch {
        localStorage.removeItem(WAITLIST_ENTRY_KEY);
      }
    }

    setCount(readCount());

    const walletConnected = localStorage.getItem(WALLET_CONNECTED_KEY) === "true";
    if (!existingRaw && walletConnected) {
      const wallet = localStorage.getItem(WALLET_ADDRESS_KEY) || "wallet-session";
      const reserved = reserveSpot("wallet", { wallet });
      if (reserved) {
        setEntry(reserved);
        setCount(reserved.spot);
        setMessage(language === "pt" ? "Vaga prioritaria reservada via wallet connection." : "Priority slot reserved via wallet connection.");
      } else {
        setMessage(language === "pt" ? "Lista prioritaria cheia. Voce entrou em standby." : "Priority list is full. You are on standby.");
      }
    }

    const onWalletChange = () => {
      if (localStorage.getItem(WALLET_CONNECTED_KEY) !== "true") return;
      if (localStorage.getItem(WAITLIST_ENTRY_KEY)) return;
      const wallet = localStorage.getItem(WALLET_ADDRESS_KEY) || "wallet-session";
      const reserved = reserveSpot("wallet", { wallet });
      if (reserved) {
        setEntry(reserved);
        setCount(reserved.spot);
        setMessage(language === "pt" ? "Vaga prioritaria reservada via wallet connection." : "Priority slot reserved via wallet connection.");
      }
    };

    window.addEventListener("wallet-connection-changed", onWalletChange);
    return () => window.removeEventListener("wallet-connection-changed", onWalletChange);
  }, []);

  const remaining = useMemo(() => Math.max(0, MAX_PRIORITY - count), [count]);

  function handleEmailSubmit(e: React.FormEvent) {
    e.preventDefault();
    const cleaned = email.trim().toLowerCase();
    const valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(cleaned);
    if (!valid) {
      setMessage(language === "pt" ? "Formato de email invalido. Use um endereco valido." : "Invalid email format. Use a valid address.");
      return;
    }
    const reserved = reserveSpot("email", { email: cleaned });
    if (!reserved) {
      setMessage(language === "pt" ? "Lista prioritaria cheia. Voce entrou em standby." : "Priority list is full. You are on standby.");
      return;
    }
    setEntry(reserved);
    setCount(reserved.spot);
    setMessage(language === "pt" ? "Vaga prioritaria reservada via email." : "Priority slot reserved via email.");
  }

  return (
    <section className="mt-8 rounded-2xl border border-zinc-800 bg-zinc-950/40 p-5">
      <div className="text-xs uppercase tracking-widest text-zinc-500">{language === "pt" ? "Lista de espera" : "Waitlist"}</div>
      <h2 className="mt-2 text-xl text-zinc-100">
        {language === "pt" ? "Acesso antecipado para os primeiros 100" : "First 100 Early Access"}
      </h2>
      <p className="mt-2 text-sm text-zinc-400">
        {language === "pt"
          ? "Conecte wallet ou envie email para reservar prioridade nesta versao de hackathon."
          : "Connect wallet or submit email to reserve priority access in this hackathon version."}
      </p>

      {entry ? (
        <div className="mt-4 rounded-xl border border-emerald-500/40 bg-emerald-500/10 p-4 text-sm text-emerald-300">
          {language === "pt" ? `Reservado: Posicao #${entry.spot}` : `Reserved: Spot #${entry.spot}`}
          <br />
          {language === "pt" ? "Metodo" : "Method"}: {entry.method === "wallet" ? "Wallet" : "Email"}
        </div>
      ) : (
        <form onSubmit={handleEmailSubmit} className="mt-4 flex flex-col gap-3 md:flex-row md:items-center">
          <input
            type="email"
            value={email}
            onChange={(ev) => setEmail(ev.target.value)}
            placeholder="email@domain.com"
            className="w-full rounded-xl border border-zinc-700 bg-black/40 px-4 py-2 text-zinc-200 outline-none focus:border-amber-400 md:max-w-xs"
          />
          <button
            type="submit"
            className="rounded-xl bg-amber-400 px-4 py-2 font-semibold text-black hover:brightness-110"
          >
            {language === "pt" ? "Entrar na lista" : "Join Waitlist"}
          </button>
        </form>
      )}

      <div className="mt-3 text-xs text-zinc-500">
        {language === "pt" ? `Vagas prioritarias restantes: ${remaining}` : `Remaining priority slots: ${remaining}`}
      </div>
      {message ? <div className="mt-2 text-xs text-zinc-400">{message}</div> : null}
    </section>
  );
}
