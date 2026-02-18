import IntelClient from "@/components/IntelClient";
import HeadlessTopologySection from "@/components/HeadlessTopologySection";

export default function Home() {
  return (
    <main className="mx-auto max-w-6xl px-6 py-10 font-mono">
      <div className="mb-3 text-sm text-zinc-500">v1.0.0 · CLI-first · Explorer-first</div>
      <h1 className="my-3 text-4xl md:text-5xl">OKTO — Sovereign Agentic Trading Infrastructure</h1>
      <p className="max-w-4xl text-zinc-300">
        Headless execution layer for BNB Chain. Designed for terminal operators:
        spec-driven, auditable, and local-first.
      </p>

      <pre className="mt-5 rounded-xl border border-zinc-800 bg-white/5 p-4 text-sm text-zinc-200">
        {`$ git clone https://github.com/DGuedz/okto-agentic-trader
$ cd okto-agentic-trader/okto-juvenile-bnb
$ python3 ops/grid_live.py --auto-regime
[INFO] policy loaded
[INFO] simulation gate: enabled
[OK] evidence emitted`}
      </pre>

      <div className="mt-5 flex flex-wrap gap-3">
        <a
          href="https://github.com/DGuedz/okto-agentic-trader"
          className="rounded-full bg-amber-400 px-4 py-2 font-semibold text-black"
        >
          Clone Repo
        </a>
        <a href="/docs" className="rounded-full border border-white/20 px-4 py-2 text-white">
          Read Docs
        </a>
        <a href="/preview.html" className="rounded-full border border-white/20 px-4 py-2 text-white">
          View Demo
        </a>
      </div>

      <p className="mt-4 text-sm text-zinc-500">
        Evidence-linked. Explorer-first. No profit promises.
      </p>

      <HeadlessTopologySection />

      <div className="mt-10">
        <IntelClient />
      </div>
    </main>
  );
}
