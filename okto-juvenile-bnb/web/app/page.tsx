export default function Home() {
  return (
    <main style={{ padding: 32, fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" }}>
      <div style={{ opacity: 0.7, marginBottom: 12 }}>v1.0.0 • CLI-first</div>
      <h1 style={{ fontSize: 48, margin: "12px 0" }}>OKTO — Sovereign Agentic Trading Infrastructure</h1>
      <p style={{ maxWidth: 820, opacity: 0.85, lineHeight: 1.6 }}>
        Headless execution layer for BNB Chain. Designed for terminal operators: spec-driven, auditable, and local-first.
      </p>
      <pre style={{ marginTop: 20, padding: 16, borderRadius: 12, background: "rgba(255,255,255,0.05)" }}>
        {`$ git clone https://github.com/DGuedz/okto-agentic-trader
$ cd okto && python -m okto --mode live
[SIGNAL] opportunity detected...
[OK] tx simulated -> verified
[OK] tx confirmed -> 0x...`}
      </pre>
      <div style={{ marginTop: 20, display: "flex", gap: 12, flexWrap: "wrap" }}>
        <a href="https://github.com/DGuedz/okto-agentic-trader" style={{ padding: "10px 14px", borderRadius: 999, background: "#fbbf24", color: "#000", fontWeight: 700, textDecoration: "none" }}>
          Clone Repo
        </a>
        <a href="/docs" style={{ padding: "10px 14px", borderRadius: 999, border: "1px solid rgba(255,255,255,0.15)", color: "#fff", textDecoration: "none" }}>
          Read Docs
        </a>
        <a href="/preview.html" style={{ padding: "10px 14px", borderRadius: 999, border: "1px solid rgba(255,255,255,0.15)", color: "#fff", textDecoration: "none" }}>
          View Demo
        </a>
      </div>
      <p style={{ marginTop: 18, opacity: 0.7 }}>Note: OKTO is not a UI product. The interface is the terminal.</p>
    </main>
  );
}
