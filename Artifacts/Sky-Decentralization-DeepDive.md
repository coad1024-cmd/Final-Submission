# Sky Ecosystem (MakerDAO): Decentralization Deep Dive

**Date:** January 2026  
**Subject:** Sky Ecosystem (DAI/USDS)  
**Analysis Type:** Decentralization Stress Test (Framework v3.0)  
**Authors:** Research Challenge Team

---

## 1. Executive Summary

This report applies the **Stablecoin Decentralization Assessment Framework (v3.0)** to the Sky Ecosystem (formerly MakerDAO) ([Internal Research, 2026](#ref-decentralization-framework)). The analysis reveals a stark dichotomy: while the protocol has achieved impressive **Operational Decentralization** (diverse liquidators, robust oracles), it exhibits critical centralization in its **Governance** and **Collateral** layers.

**Final Composite Score:** **0.50 (Effectively Centralized)**

The protocol's decentralization is bounded by a **binding constraint**: extreme centralization in voting power (Gini > 0.98) and excessive single-counterparty exposure (Circle/Coinbase > 42%) cap the system's resilience score, regardless of its operational health.

![Sky Decentralization Radar Chart](../images/sky_decentralization_radar.png)

---

## 2. Methodology

We assess decentralization across four orthogonal dimensions, where the system is only as decentralized as its weakest link during stress:

$$ D = (G, C, O, E) $$

*   **Governance (G):** Distribution of political control.
*   **Collateral (C):** Independence of backing assets.
*   **Operational (O):** Resilience of execution infrastructure.
*   **Emergency (E):** Distribution of "God Mode" powers.

### Binding Constraint Rule
If any single dimension falls into the **RED (Centralized)** zone, the total score is capped at **0.50**, reflecting the reality that a chain with a broken link fails completely.

---

## 3. Pillar I: Governance (The "Plutocracy" Risk)

**Status:** 🔴 **Critical Centralization**

Governance is the ultimate root of trust. In Sky, this root has narrowed to a singular point of failure.

### Data Findings
*   **Token Distribution:** The Gini coefficient for MKR is **0.988**, indicating wealth inequality surpasses that of Bitcoin (0.88) and most nation-states ([Sky Protocol Mainnet, 2026](#ref-data-sky-vow)).
*   **Effective Control (Delegation):** While "token holding" is concentrated, "voting power" is even worse due to delegation.
    *   **Top 1 Delegate:** Controls **86.5%** of active voting weight (`0x1678...`).
    *   **Top 5 Delegates:** Control **99.2%** of voting weight.

### Implication
The "DAO" structure is effectively a **Sole Proprietorship**. A single delegate possesses the mathematical authority to:
1.  Pass any proposal unilaterally.
2.  Trigger Emergency Shutdown.
3.  Mint infinite MKR/DAI (via malformed executive spells, subject to GSM delay).

> **Stress Test Result:** In an adversarial governance scenario (e.g., the top delegate is coerced or compromised), the protocol has **zero on-chain defense**. The only protection is the GSM Pause Delay (~48 hours), which allows users to exit but guarantees protocol dissolution.

---

## 4. Pillar II: Collateral (The "Custodial" Risk)

**Status:** 🔴 **Critical Centralization**

Collateral decentralization evaluates whether the backing can be seized.

### Data Findings
*   **Asset HHI:** **0.23** (Green). The *types* of assets are well-distributed (Crypto, RWA, Stablecoins).
*   **Counterparty Exposure:**
    *   **USDC + Coinbase Prime:** $2.26B (**42.23%** of total backing).
    *   **RWA (Other):** ~$2.0B (**38%**).
    *   **Crypto Native (ETH/WBTC):** ~$1.55B (**29%**).

### Implication
The protocol violates the **Basel III Single-Counterparty Limit** (25%) ([Basel Committee, 2019](#ref-basel-framework)). With >40% of its balance sheet dependent on a single legal nexus (Circle/Coinbase), Sky imports the regulatory censorship set of the United States.

> **Stress Test Result (USDC Freeze):** If Circle blacklists the Sky operational vaults (e.g., PSM), **42% of the diverse backing becomes worthless instantly**.
> *   **Solvency Impact:** DAI drops to ~$0.58.
> *   **Market Impact:** Massive bank run; surplus buffer (if any) is instantly wiped out.
> *   **Survival Probability:** 0%.

---

## 5. Pillar III: Operational (The "Resilience" Layer)

**Status:** 🟢 **High Decentralization**

This is the system's strongest capability. The "Keepers" (liquidators) and Oracles operate in a competitive, permissionless market.

### Data Findings
*   **Keeper HHI:** **1136** (0.11).
*   **Market Structure:**
    *   **Top 1 Keeper:** 27% share.
    *   **Top 5 Keepers:** 60% share.
    *   **Unique Participants:** 24+ active independent addresses.
*   **Oracle Redundancy:** Chronicle medianizer aggregates >10 independent feeds.

### Implication
The execution layer is robust. Unlike the "cartel-like" governance, the machinery of the protocol (auctioning collateral, updating prices) is distributed. No single actor can halt the system's heartbeat.

> **Stress Test Result (Keeper Exit):** Even if the top 3 liquidators (47% share) withdraw during a crash, the HHI structure suggests the remaining 21 keepers have sufficient diversity to scale up. Latency would increase, but the **system would likely clear the bad debt** (albeit with higher slippage).

---

## 6. Pillar IV: Emergency (The "Nuclear" Option)

**Status:** 🟡 **Moderate Risk**

The **Emergency Shutdown Module (ESM)** is the fail-safe. It allows MKR holders to burn tokens to trigger a global settlement.

*   **Mechanism:** Decentralized (anyone with 50k MKR can trigger).
*   **Problem:** Due to wealth concentration (Pillar I), only the top Whales/Delegates can realistically trigger this. Use retail cannot "rage quit" the protocol; they must wait for a Whale to save them.

---

## 7. Synthesis & "The Centralization Paradox"

Sky Ecosystem presents a paradox common in mature DeFi:

1.  **Code Layer:** Decentralized, robust, permissionless (Green).
2.  **Trust Layer:** Centralized, custodial, plutocratic (Red).

The protocol is effectively a **centralized hedge fund** (administered by 1-5 delegates and backed by US Corporate debt/USDC) running on **decentralized rail infrastructure** (Ethereum + Keepers).

### Final Recommendation

To reclaim the "Decentralized" label, Sky must:
1.  **Cap USDC/Coinbase exposure** at 20% (diversify to other custodians or return to crypto-native assets).
2.  **Implement Voting Decay** to break the 86% delegate hegemony.
3.  **Harden the ESM** to allow smaller minority groups to trigger safety stops (e.g., lower threshold if price deviation > 5%).

---

### Appendix: Quantitative Scorecard

| Metric | Measured Value | Threshold | Score Impact |
|:---|:---|:---|:---|
| **MKR Gini** | 0.98 | > 0.85 | 🔴 **Cap at 0.50** |
| **Backing HHI** | 0.23 | < 0.25 | 🟢 +0.30 |
| **Counterparty** | 42.2% | > 40% | 🔴 **Cap at 0.50** |
| **Keeper HHI** | 0.11 | < 0.25 | 🟢 +0.25 |
| **Emergency** | Whale-Gated | - | 🟡 Neutral |

**Calculated D-Score:** 0.56  
**Final D-Score (Capped):** 0.50

---

## References

<span id="ref-decentralization-framework"></span>Internal Research. (2026). *[Stablecoin Decentralization Framework](./Stablecoin-Decentralization-Framework.md)*. Methodological Framework.

<span id="ref-data-sky-vow"></span>Sky Protocol Mainnet. (2026). *Vow Contract Balance Query*. Retrieved Jan 5, 2026 via `pipeline/scripts/data_fetchers/fetch_makerdao_data.py`. Contract: `0xA950524441892A31ebddF91d3cEEfa04Bf454466`.

<span id="ref-basel-framework"></span>Basel Committee on Banking Supervision. (2019). *[The Basel Framework: Liquidity Coverage Ratio](https://www.bis.org/basel_framework/standard/LCR.htm)*. Bank for International Settlements.
