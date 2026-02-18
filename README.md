# OKTO Agentic Trader

Home repository for the OKTO hackathon project.

This root repo contains multiple folders and working notes.  
The production-ready hackathon deliverable lives in:

- `okto-juvenile-bnb/`

## Quick Links

- Main project README: `okto-juvenile-bnb/README.md`
- Public repository: <https://github.com/DGuedz/okto-agentic-trader>
- Live demo: <https://okto-agentic-trader.vercel.app>
- On-chain proof (contract): <https://testnet.bscscan.com/address/0x2a7F7FF2eF8Cf6948D445310B5e09Be5774EFffC>
- On-chain proof (tx): <https://testnet.bscscan.com/tx/0xa59722a64950b6a97c7e986450876e8e1dca2b7063f468eed97510b343f0f5b1>

## Hackathon Submission Scope

For judges and reproducibility checks, use only:

1. `okto-juvenile-bnb/README.md`
2. `okto-juvenile-bnb/` source code
3. Public links above (demo + on-chain proof)

## Reproducibility (Fast Path)

```bash
git clone https://github.com/DGuedz/okto-agentic-trader.git
cd okto-agentic-trader/okto-juvenile-bnb
pip install -r requirements.txt
python3 ops/grid_live.py --auto-regime
```

## Security Note

No private credentials should be committed.  
Use local-only environment files (for example, `.secure_env/okto.env`) and keep them out of git.
