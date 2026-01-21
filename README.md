# Stablecoin Research: Final Submission Portfolio

**Date**: January 2026
**Subject**: Stablecoin Research Challenge: Analysis, Design & Attack Modelling

---

## 📌 Challenge Alignment

This portfolio addresses **Option 2: Stablecoins** of the Research Challenge.

| Challenge Requirement | Submitted Module | Description |
| :--- | :--- | :--- |
| **2a. Analysis** | Comparative Analysis | Deep dive into Liquity (Decentralized) vs. Sky (Hybrid). |
| **2b. Design** | Protocol Design (Volatile & Non-Volatile) | Frameworks for both Risky (Crypto) and Risk-Free (Fiat) collateral. |
| **2c. Modelling** | Attack Simulation | "The Infinite Money Glitch": Modeling an Algorithmic De-Peg. |

---
> **Navigation note:**
This portfolio is organized in a GitBook-style structure, so the reader does not need to browse the underlying folder tree directly. All sections and artifacts are accessible from this index file, and you can navigate the full submission simply by following the embedded hyperlinks
>
## 📂 Submission Structure

This portfolio contains the final technical reports and design documents for stablecoin research.

### Part I: Protocol Analysis

#### 1. [Liquity V2 (BOLD)](Liquity-final/Liquity-Research.md)

An evaluation of "Pure Crypto" resilience, covering Federated Solvency, the Liquidation Waterfall, and User-Set Interest Rates.

#### 2. [Sky Ecosystem (USDS/DAI)](Sky-final/Sky-Research.md)

A structural analysis of the "Hybrid Shadow Banking" pivot, focusing on RWA dependency and governance concentration.

---

### Part II: Design Scenarios

#### 3. [Volatile Collateral Design](Design/Volatile.md)

A theoretical framework for crypto-backed stablecoins using senior–junior tranching to internalize volatility.

#### 4. [Non-Volatile Collateral Design](Design/Non-Volatile.md)

A theoretical framework for fiat-backed stablecoins using convex redemption curves to manage liquidity risk.

---

## Part III: Modelling

Quantitative analysis of attack economics using the DualTokenSim framework.

| Document | Description |
|:---------|:------------|
| [Modelling Index](Modelling/README.md) | Overview and navigation |
| [1. Foundations](Modelling/01_Foundations.md) | Attack Theory, Mechanism Design, and Profitability Hypothesis |
| [2. Market Simulations](Modelling/02_Market_Simulation.md) | Baseline Attacks, Liquidity Sensitivity, and Curve vs Uniswap |
| [3. Attack Analysis](Modelling/03_Attack_Analysis.md) | **"The Infinite Money Glitch"** - Trigger vs Capture Economics |
| [4. Conclusions](Modelling/04_Conclusion.md) | Unified Theory of Failure and Strategic Recommendations |

---
