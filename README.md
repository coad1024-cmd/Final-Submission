# Stablecoin Research: Final Submission Portfolio

**Date**: January 2026
**Subject**: Comparative Analysis of Decentralized & Hybrid Solvency Models

---

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
| [Theoretical Foundation](Modelling/01_Theory.md) | Death spiral mechanics and attacker economics |
| [Simulation Framework](Modelling/02_Framework.md) | DualTokenSim architecture and components |
| [Experimental Results](Modelling/03_Experiments.md) | Attack scenarios and profitability analysis |
| [Pool Size Sensitivity](Modelling/04_Pool_Sensitivity.md) | Liquidity depth as defense mechanism |
| [Curve vs Uniswap](Modelling/05_Curve_Comparison.md) | Impact of AMM bonding curve choice |
| [Hawkes Process Risk](Modelling/06_Hawkes_Comparison.md) | Impact of self-exciting market volatility |
| [Redemption Attack](Modelling/07_Redemption_Attack.md) | **"The Death Spiral"** - Exploiting solvency mechanism |
| [Robustness Design](Modelling/09_Robustness_Design.md) | **"The Defense"** - Exogenous Backing (ETH) simulation |
| [cadCAD Validation](Modelling/11_cadCAD_Validation.md) | **Independent Verification** of Death Spiral |
| [Conclusions](Modelling/10_Conclusions.md) | Key findings and design recommendations |

---

## 🏛️ Project Artifacts

- **[Executive Summary](Final_Deliverables/Stablecoin_Research_Executive_Summary.md)**: High-level findings for stakeholders.
- **[Technical Report](Final_Deliverables/Stablecoin_Technical_Report.md)**: Detailed engineering specifications and backing mechanisms.
- **[Research Paper](Final_Deliverables/Stablecoin_Research_Paper.md)**: Academic synthesis of findings.

---

© 2026 Research Challenge Team
