# Attack Profitability Analysis

*A quantitative analysis of profitable de-pegging strategies against dual-token systems*

---

## Overview

This modelling study quantifies the economic feasibility of attacking algorithmic stablecoins. The analysis uses the DualTokenSim framework ([Calandra et al., 2024](https://ieeexplore.ieee.org/document/11114693)) to determine when de-peg attacks become profitable.

**Key Finding:** Algorithmic stablecoins backed by endogenous collateral are structurally exploitable. A sufficiently capitalized adversary can profitably attack these systems by combining a trigger mechanism (selling stablecoins) with a capture mechanism (shorting the collateral token).

---

## Contents

### [1. Theoretical Foundation](01_Theory.md)

- The Dual-Token Mechanism
- The Death Spiral
- The Attacker's Position

### [2. Simulation Framework](02_Framework.md)

- The Three-Pool Architecture  
- Simulation Parameters
- Core Components (Tokens, Pools, Arbitrage, Trading)

### [3. Experimental Results](03_Experiments.md)

- Visual Evidence
- Experiment 1: Raw Dump (Baseline)
- Experiment 2: Short + Dump (Soros Strategy)
- Experiment 3: Maximum Leverage
- Sensitivity Analysis

### [4. Pool Size Sensitivity](04_Pool_Sensitivity.md)

- Hypothesis: Liquidity as Defense
- Experimental Design
- Results

### [5. Conclusions](05_Conclusions.md)

- Key Findings
- Model Limitations
- Strategic Implications

---

## Quick Reference

| Experiment | Short Position | Net PnL | ROI |
|:-----------|---------------:|--------:|----:|
| Raw Dump | $0 | −$87M | — |
| Short + Dump | $300M | +$68M | 23% |
| Max Leverage | $1B | +$411M | 41% |

---

## References

- **IEEE Paper:** [Calandra et al., 2024](https://ieeexplore.ieee.org/document/11114693)
- **Original Simulator:** [DualTokenSim](https://github.com/FedericoCalandra/DualTokenSim)
- **Attack Fork:** [Research Repository](https://github.com/coad1024-cmd/Stablecoin_Research/tree/main/challenge-research-coad1024/Algo-Attack-Model)

---

<div align="center">

| [Previous] | Home | [Next] |
|:---|:---:|---:|
| [Non-Volatile Collateral Design](../Design/Non-Volatile.md) | [Table of Contents](../README.md) | — |

</div>
