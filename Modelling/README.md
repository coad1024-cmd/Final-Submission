# Quantitative Risk & Attack Analysis

*A quantitative analysis of profitable de-pegging strategies against dual-token systems*

---

## Overview

This modelling study quantifies the economic feasibility of attacking algorithmic stablecoins. The analysis uses the DualTokenSim framework to determine when de-peg attacks become profitable.

**Key Finding:** Algorithmic stablecoins backed by endogenous collateral are structurally exploitable. A sufficiently capitalized adversary can profitably attack these systems by combining a trigger mechanism (selling stablecoins) with a capture mechanism (shorting the collateral token).

---

## Research Stack

### [1. Foundations & Methodology](01_Foundations.md)

* The Dual-Token Mechanism & Death Spiral Theory
* Simulation Framework & Architecture
* The Profitability Hypothesis (Trigger Cost vs Short Profit)

### [2. Market Simulations](02_Market_Simulation.md)

* Baseline Attack Experiments
* Liquidity Sensitivity (The "Paradox")
* Curve vs Uniswap
* Gaussian vs Hawkes (Fat Tails)

### [3. Attack Analysis](03_Attack_Analysis.md)

* Attack Economics (Trigger vs Capture)
* The "Infinite Money Glitch" (Redemption Attack)
* Profitability Heatmaps

### [4. Conclusions](04_Conclusion.md)

* Unified Theory of Failure
* Strategic Recommendations

---

<div align="center">

| [Previous] | Home | [Next] |
|:---|:---:|---:|
| [Non-Volatile Design](../Design/Non-Volatile.md) | [Table of Contents](../README.md) | [1. Foundations →](01_Foundations.md) |

</div>
