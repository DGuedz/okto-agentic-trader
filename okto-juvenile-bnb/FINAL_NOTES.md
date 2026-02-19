# FINAL_NOTES

## Project
- Name: `OKTO — Sovereign Agentic Trading Infrastructure`
- Track: `AI Agent | DeFi | BNB Chain`
- Status: `Submitted`
- Final web commit (submission state): `2fc8a80`
- Date (UTC): `2026-02-19`

## Submission Links
- Demo: `https://okto-agentic-trader.vercel.app`
- Repository: `https://github.com/DGuedz/okto-agentic-trader`

## On-Chain Proof
- Network: `BNB Smart Chain Testnet (ChainID 97)`
- Contract: `0x2a7F7FF2eF8Cf6948D445310B5e09Be5774EFffC`
  - BscScan: `https://testnet.bscscan.com/address/0x2a7F7FF2eF8Cf6948D445310B5e09Be5774EFffC`
- Tx Hash (commit proof): `0xa59722a64950b6a97c7e986450876e8e1dca2b7063f468eed97510b343f0f5b1`
  - BscScan: `https://testnet.bscscan.com/tx/0xa59722a64950b6a97c7e986450876e8e1dca2b7063f468eed97510b343f0f5b1`

## Repro (Short)
```bash
git clone https://github.com/DGuedz/okto-agentic-trader.git
cd okto-agentic-trader/okto-juvenile-bnb
python3 ops/grid_live.py --auto-regime
```

Web:
```bash
cd web
npm install
npm run build
```

## Product Coherence (Final)
- Global language switcher `EN/PT` implemented (stateful via localStorage).
- Messaging aligned to: `headless`, `policy-first`, `auditable`.
- "No profit promises" stance preserved in app copy.

## Security Hygiene (Final)
- `.env` and `.secure_env` are outside versioned files.
- `config/.env.example` contains placeholders only.
- Secret scan hook enabled (`scripts/secret_scan.sh`).
- Keys rotated previously (Binance, Aster, OKTO wallet path) and old credentials treated as compromised.

## Operational Freeze
- No non-critical changes after submission.
- Only emergency fixes allowed (build break, broken route, unavailable proof links).

## Notes for Judge Follow-up
- If requested, provide:
  - Submission screenshot
  - Live demo walkthrough video
  - Proof links above
  - Repro commands above
