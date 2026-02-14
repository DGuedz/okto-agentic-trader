# OKTO AGENTIC ASSISTANT
### Autonomous DeFi Execution Environment for BNB Chain

**Status:** LIVE | **Category:** AI Agent / DeFi | **License:** MIT

Okto is an autonomous High-Frequency Trading (HFT) agent designed to bridge the gap between institutional strategies and Decentralized Finance (DeFi) on the **BNB Chain**.

It operates as a **"Headless" execution layer**, enabling institutional-grade strategies like **Dark Pool routing** (Iceberg Orders), **Volatility Scalping** (RSI + Bollinger + ATR), and **Institutional Sentiment Analysis** (VWAP + Funding Rate).

---

## 🚀 CORE FEATURES (HFT ENGINE)

### 1. 🧠 Autonomous Trading Brain (RSI + Bollinger + Delta)
Okto doesn't just guess. It uses a **"Confluence Supreme"** logic engine that only executes when multiple on-chain vectors align:
- **Price Action:** RSI Oversold/Overbought (<30/>70) + Bollinger Band touches.
- **Volume Delta:** Confirms aggression (Buyers vs Sellers) before entering.
- **Volatility (ATR):** Dynamically adjusts Stop Loss and Take Profit targets based on market noise.

### 2. 🛡️ Smart Grid & Dark Pool Execution
- **Dark Pool Logic:** Splits large orders into micro-chunks to hide intent from predatory MEV bots.
- **Smart Grid:** Instead of market buying, Okto places **Limit Orders (Maker)** at calculated support levels (Order Book Imbalance Walls), reducing fees and improving entry prices.

### 3. 🧭 Institutional Compass (On-Chain Sentiment)
- **VWAP Trend:** Tracks if the "smart money" is buying or selling.
- **Funding Rate Monitor:** Detects over-leveraged markets to anticipate squeezes.
- **OBI (Order Book Imbalance):** Reads the depth of the book to predict short-term price walls.

---

## 🛠️ TECH STACK

- **Language:** Python 3.14 (Core Logic)
- **Blockchain:** BNB Chain (BSC)
- **Connectivity:** CCXT (CEX), Web3.py (On-Chain)
- **Analysis:** Pandas, NumPy (Financial Data Processing)
- **Security:** Local Environment Execution (Non-Custodial Logic)

---

## 📦 INSTALLATION & USAGE

```bash
# Clone the repository
git clone https://github.com/okto-agent/okto-juvenile-bnb.git
cd okto-juvenile-bnb

# Install Dependencies
pip install -r requirements.txt

# Run the Autonomous Agent
python3 main.py
```

---

## 🏆 HACKATHON TRACKS & TAGS

- **BNB Chain:** Native support for BSC execution.
- **AI Agent:** Fully autonomous decision-making engine.
- **DeFi:** Bridges CEX liquidity with On-Chain logic.
- **Moltbot / Platform Tech:** Modular "Tentacle" architecture for plug-and-play strategies.

---

## 📄 LICENSE

MIT License. Built for the **BNB Chain OpenClaw Hackathon 2026**.
