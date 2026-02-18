# OKTO — Sovereign Agentic Trading Infrastructure
### Autonomous DeFi Execution Environment for BNB Chain

<div align="center">
  <img src="web/public/assets/okto-logo-terminal-operator.png" alt="OKTO Logo" width="120" />
  <br />
  <br />
  <a href="https://okto-agentic-trader.vercel.app">
    <img src="https://img.shields.io/badge/LIVE_DEMO-Click_Here-33FF99?style=for-the-badge&logo=vercel&logoColor=black" alt="Live Demo" />
  </a>
  <a href="https://testnet.bscscan.com/address/0x2a7F7FF2eF8Cf6948D445310B5e09Be5774EFffC">
    <img src="https://img.shields.io/badge/On--Chain_Proof-Verified-F3BA2F?style=for-the-badge&logo=binance&logoColor=black" alt="On-Chain Proof" />
  </a>
</div>

**Status:** LIVE | **Category:** AI Agent / DeFi | **License:** MIT

Okto is a "headless" AI agent designed for High-Frequency Trading (HFT) and Dark Pool routing on the **BNB Chain**.

It solves the "PvP execution" problem in DeFi by enabling institutional-grade strategies (Iceberg Orders, Volatility Scalping, and Sentiment Analysis) through a terminal-first autonomous agent.

---

## HACKATHON SUBMISSION (JUDGES START HERE)

**Event:** Good Vibes Only: OpenClaw Edition (BNB Chain)
**Track:** Agent (AI Agent × Onchain Actions)

### 1. On-Chain Proof (Required)
We have deployed a Proof-of-Execution contract to **BNB Smart Chain Testnet** to log agent actions immutably.

| Asset | Value | Link |
| :--- | :--- | :--- |
| **Contract** | `OktoProof` | [View on BscScan](https://testnet.bscscan.com/address/0x2a7F7FF2eF8Cf6948D445310B5e09Be5774EFffC) |
| **Transaction** | `Commit Hash` | [View Transaction](https://testnet.bscscan.com/tx/0xa59722a64950b6a97c7e986450876e8e1dca2b7063f468eed97510b343f0f5b1) |
| **Network** | BSC Testnet (97) | - |

### 2. Reproducibility & Demo
*   **Live App:** [https://okto-agentic-trader.vercel.app](https://okto-agentic-trader.vercel.app) (Command Deck UI)
*   **GitHub Repo:** [https://github.com/DGuedz/okto-agentic-trader](https://github.com/DGuedz/okto-agentic-trader) (Public)
*   **Video Demo:** [Watch on YouTube](https://youtu.be/zCZ38Joy97U)

### 3. AI Implementation
Okto uses a **Headless Spec-Driven Design** where the "Brain" (Python) uses:
*   **Regime Detection:** ML-lite logic (OBI + RSI + ATR) to classify market states (Bull/Bear/Range).
*   **Confluence Engine:** Multi-vector decision making before any on-chain action.

---

## CORE FEATURES (HFT ENGINE)

**Autonomous Execution:** No manual clicks. You define the strategy; the agent executes 24/7.

**Dark Pool Logic:** Splits large orders into micro-chunks to hide intent from predatory MEV bots.

**Smart Grid:** Instead of market buying, Okto places **Limit Orders (Maker)** at calculated support levels (Order Book Imbalance Walls), reducing fees and improving entry prices.

**Sentiment Analysis Engine:** Analyzes on-chain volume variance and funding rates to predict short-term volatility.

---

---

## TECH STACK

- **AI/Logic:** Python 3.14 (AsyncIO, Pandas, NumPy)
- **Blockchain:** Hardhat, Web3.py, BNB Chain
- **Interface:** Command Line Priority (Terminal) + Next.js Dashboard (Monitoring)

---

## INSTALLATION & REPRODUCTION

### Prerequisites
*   Python 3.10+
*   Node.js 18+
*   Binance Testnet API Keys (for Live Mode)

### 1. Agent Core (Python)
The brain of the operation. Handles execution logic and strategy.

```bash
# Clone the repository
git clone https://github.com/DGuedz/okto-agentic-trader.git
cd okto-agentic-trader

# Install Dependencies
pip install -r requirements.txt

# Run the Autonomous Agent (Simulation Mode)
python3 ops/grid_live.py --auto-regime
```

### 2. Command Deck UI (Next.js)
The visual interface for monitoring the agent's performance.

```bash
cd web

# Install UI Dependencies
npm install

# Start Development Server
npm run dev
# Access at http://localhost:3000
```

## UI/UX DESIGN SYSTEM (BNB CHAIN)

Okto follows the **BNB Chain Design Guidelines** for professional dApp interfaces.

- **Primary Color:** `#F3BA2F` (BNB Yellow)
- **Background:** `#0B0E11` (Deep Space / Binance Dark)
- **Typography:** `Inter` / `JetBrains Mono`
- **Components:** 
  - `OrderBook`: Real-time depth visualization.
  - `LiquidityMap`: On-chain flow analysis.
  - `WalletConnect`: Secure Web3 auth (Wagmi + Viem).

> **Note:** The UI uses Tailwind CSS for styling, adhering to the "Headless" aesthetic while maintaining brand consistency with the BSC ecosystem.

---

## HACKATHON TRACKS & TAGS

- **BNB Chain:** Native support for BSC execution.
- **AI Agent:** Fully autonomous decision-making engine.
- **DeFi:** Bridges CEX liquidity with On-Chain logic.
- **Moltbot / Platform Tech:** Modular "Tentacle" architecture for plug-and-play strategies.

---

## ✅ PROOF-OF-EXECUTION (ON-CHAIN VERIFICATION)

Required for **BNB Chain Good Vibes Only: OpenClaw Edition** hackathon submission.

| Metric | Value |
| :--- | :--- |
| **Network** | BNB Smart Chain Testnet (ChainID: 97) |
| **Contract (OktoProof)** | [`0x2a7F7FF2eF8Cf6948D445310B5e09Be5774EFffC`](https://testnet.bscscan.com/address/0x2a7F7FF2eF8Cf6948D445310B5e09Be5774EFffC) |
| **Tx Hash (Commit)** | [`0xa59722a64950b6a97c7e986450876e8e1dca2b7063f468eed97510b343f0f5b1`](https://testnet.bscscan.com/tx/0xa59722a64950b6a97c7e986450876e8e1dca2b7063f468eed97510b343f0f5b1) |
| **Run ID** | `0xa303ece179351865be958c0b86c6300c2c5c53209fc96599fde9e903c80c1c12` |
| **Report Hash** | `0x9f4a01d29f2c1b2180dcdd343c1aa4990fc9e19697df8f8e9b42990800624467` |
| **Tag** | `BINANCE->ASTER:dryrun:v1` |

> **Note:** The `OktoProof` contract logs execution metadata on-chain to ensure auditability and immutability of agent actions.

---

## LICENSE

MIT License. Built for the **BNB Chain OpenClaw Hackathon 2026**.
