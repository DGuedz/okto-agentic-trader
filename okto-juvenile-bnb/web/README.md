# OKTO — Sovereign Agentic Trading Infrastructure

<div align="center">
  <img src="assets/okto-logo-terminal-operator.png" alt="OKTO Logo - Terminal Operator Style" width="120" />
  <br />
  <br />
  <a href="https://okto-agent.com">
    <img src="https://img.shields.io/badge/Status-Live_Simulation-33FF99?style=for-the-badge&logo=statuspage&logoColor=black" alt="Status" />
  </a>
  <a href="https://github.com/DGuedz/okto-agentic-trader/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-FDBA12?style=for-the-badge" alt="License" />
  </a>
  <a href="https://nextjs.org">
    <img src="https://img.shields.io/badge/Built_With-Next.js_14-000000?style=for-the-badge&logo=next.js" alt="Next.js" />
  </a>
</div>

<br />

![Arquiteto Abissal - Cover](assets/okto-cover-arquiteto-abissal.png)
> *A hyper-realistic biomechanical octopus floating in a dark digital void... The predator of the mempool.*

---

## 💀 The Manifesto

**We do not trust. We verify.**

OKTO is not a "trading bot". It is a **Sovereign Agentic Infrastructure** designed for the dark forest of DeFi. It exists to execute intent with **institutional precision** and **predatory speed**.

*   **Headless First:** The UI is just a viewer. The brain is a CLI.
*   **Spec-Driven:** Logic is defined in YAML. Deterministic execution.
*   **Anti-MEV:** Private relays and iceberg orders by default.
*   **Local Sovereignty:** Your keys never leave your machine.

---

## ⚡ Key Capabilities

| Feature | Description |
| :--- | :--- |
| **Biomechanical Execution** | Automated intent execution with sub-second latency. |
| **Spec-Driven Design (SDD)** | Define risk, strategies, and constraints in `okto.yaml`. |
| **Simulation Mode** | Replay historical data against your spec before risking capital. |
| **Anti-MEV Routing** | Flashbots-compatible private transaction submission. |
| **Audit Trail** | Immutable logs of every decision, veto, and execution. |

---

## 🚀 Quickstart

Clone the repo and deploy the infrastructure.

```bash
# 1. Clone the repository
git clone https://github.com/DGuedz/okto-agentic-trader.git
cd okto-agentic-trader

# 2. Install dependencies
pnpm install

# 3. Configure your spec
cp .env.example .env
cp okto.yaml.example okto.yaml

# 4. Run simulation
pnpm dev --mode=simulation
```

## 🏗 Architecture

```mermaid
graph TD
    A[User Spec (YAML)] -->|Validates| B(Risk Engine)
    B -->|Approved| C{Strategy Core}
    C -->|Signal| D[Execution Agent]
    D -->|Private TX| E((Mempool / Flashbots))
    D -->|Logs| F[Audit Database]
    G[Web Interface] -.->|Reads| F
```

## 🛡 Security & Risk

*   **Circuit Breaker:** Auto-shutdown on `max_drawdown` hit.
*   **Key Management:** Keys loaded via KMS or encrypted env vars only.
*   **Veto Power:** Risk engine can veto any trade regardless of strategy signal.

---

<div align="center">
  <sub>Built for the BNB Chain Hackathon 'Good Vibes Only' (ironically).</sub>
  <br />
  <sub>OKTO © 2026. Code is Law.</sub>
</div>
