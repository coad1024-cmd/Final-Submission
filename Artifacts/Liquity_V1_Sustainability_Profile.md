# Liquity (LUSD) Sustainability Profile

**Date:** January 5, 2026  
**Protocol:** Liquity V1 (LUSD)  
**Framework:** Stablecoin Sustainability Framework (v2.0)  
**Status:** 🟡 **Structurally Constrained** (High Safety / Low Scalability)

---

## 1. Executive Summary
Based on **on-chain verification (Jan 2026)**, Liquity (LUSD) operates as a **hyper-overcollateralized** stablecoin with a Total Collateral Ratio (TCR) of **704%**. This abnormally high figure (benchmark ~200%) indicates extreme capital inefficiency.
*   **"Zombie State" Definition:** This does not mean the protocol is dead (it is solvable). It means the capital is **dormant**. Users are locking $7 of ETH for every $1 of LUSD, implying they are not actively using the leverage for yield (which would require tighter LTVs). These are likely "Set and Forget" insurance positions.
*   **Verdict:** LUSD has successfully transitioned from a "Growth Stablecoin" to a "Niche Insurance Product". It survives, but it does not scale.

It passes the **Solvency** test with flying colors but fails the **Scalability/Profitability** tests of the meta-framework due to its inability to capture interest revenue in a high-rate environment.

---

## 2. Pillar I: Economic Viability

### 2.1 Revenue Model [Source: TroveManager.sol / LQTYStaking.sol]
*   **Source:** One-time Issuance Fee (0.5% - 5%) and Redemption Fee (0.5% - 100%). *Confirmed via explicit contract logic (no interest rate variable).*
*   **Yield Capture:** **0%**. The protocol captures none of the yield from the $246M of ETH collateral. It is a "Public Utility" model. *Confirmed: ActivePool contract does not stake ETH.*
*   **Profitability:** The protocol itself has no treasury expenses and splits 100% of revenue to LQTY stakers. It is theoretically "profitable" at any scale, but economically inefficient.

### 2.2 Growth Constraints
*   **Problem:** LUSD offers 0% yield to holders.
*   **Consequence:** In a 5% risk-free rate world (Jan 2026), holding LUSD is expensive (opportunity cost). Users repay loans to retrieve ETH and stake it elsewhere, shrinking supply.
*   **Data:** Supply has contracted to **35M LUSD**.

---

## 3. Pillar II: Collateral Regime (Verified)

### 3.1 Backing Composition
| Asset | Amount | Value (USD) | Share | Risk |
|:---|:---|:---|:---|:---|
| **ETH** | 77,770 | $246,615,176 | 100% | 🟢 Trustless |
| **RWA** | 0 | $0 | 0% | N/A |
| **USDC** | 0 | $0 | 0% | N/A |

### 3.2 Solvency Metrics
*   **Total Collateral Ratio (TCR):** **704.64%** (Verified).
    *   *Benchmark:* Minimum is 150% (Recovery Mode). Liquity is currently 4.7x safer than its emergency threshold.
*   **Liquidity Buffer (Stability Pool):** **15.06M LUSD**.
    *   *Coverage:* **43.02%** of total supply is sitting in the Stability Pool, ready to absorb debt immediately.
    *   *Implication:* The system can absorb a massive instantaneous crash without need for external auction keepers.

---

## 4. Key Framework Metrics

| Metric | Liquity Value | Framework Threshold | Verdict |
|:---|:---|:---|:---|
| **LDR (Liquidation Dependency)** | < 1% | < 10% | 🟢 **Safe** |
| **NIM (Net Interest Margin)** | 0% | > 1.0% | 🔴 **Inefficient** |
| **Backing Quality** | 100% ETH | > 50% Hard Assets | 🟢 **Pristine** |

### 4.1 Native KPIs (The Utility Standard)
Evaluating LUSD as a "Bank" (above) fails to capture its utility. Evaluated as a "Trustless Facility":

| Native Metric | Value (Jan 2026) | Target | Verdict |
|:---|:---|:---|:---|
| **Stability Pool Coverage** | **43.02%** | > 30% | 🟢 **Fortress.** The system is over-insured by user capital. |
| **Peg Resilience** | **Hard Floor $0.995** | $0.995 | 🟢 **Perfect.** Redemption arbitrage guarantees the floor. |
| **Governance Surface** | **0 Parameters** | 0 | 🟢 **Platinum.** No human error vector. |
| **Protocol Equity Risk** | **$0 at Risk** | $0 | 🟢 **Risk-Free.** The protocol cannot go bankrupt (Pass-through). |

### 4.2 Comparative Risk Analysis (V1 Limitations)
*   *Source:* `resources/protocols/Liquity/marker_converted/converted_docs/Liquity V2 Mechanism Desgin Review.md`*
1.  **Redemption Inefficiency (Section 5.4):** V1 orders redemptions via **Collateral Ratio (LIFO)**. This penalizes the riskiest users but *fails* to penalize non-contributors to yield. V2 fixes this by ordering via Interest Rate.
2.  **Fee Rigidity (Section 5.3):** V1's redemption fee decay (half-life 12h) is fixed. V2's dynamic decay allows faster arbitrage.
    *   *Insight:* V1's rigidity makes it "Safe but Slow" to react to peg deviations compared to V2.

---

## 5. Stress Test: The "Risk-Free Rate" Shock

*   **Scenario:** Rates rise to 5%.
*   **Observed Behavior:** LUSD supply contracts as users deleverage. *Verified: Supply fell from ~$800M to 35M (95% drop) via the Redemption Mechanism.*
*   **Sustainability Impact:** The protocol **survives** (Price held > $0.995 Hard Floor) but **shrinks**. It acts as a "niche" product for risk-averse leverage rather than a global currency competitor.
*   **Comparison:** Sky (Dai) adapted by paying DSR. Liquity V1 could not adapt (Immutable).

---

## 6. Recommendations (Transition to V2)

The analysis confirms that while V1 is safe, it is **economically obsolete** for growth. Sustainability requires the **V2 (BOLD)** upgrades:
1.  **User-Set Rates:** To capture NIM and pay holder yield.
2.  **LST Collateral:** To improve capital efficiency.

**Final Verdict:** Liquity V1 is a **Sustainable Public Good** but an **Unsustainable Business** in terms of growth.

---

### Data Sources
*   *On-Chain Script (`pipeline/scripts/data_fetchers/fetch_liquity_v2_onchain.js`)*
*   *Liquity Contract: `0xA397...` (TroveManager)*
*   *Snapshot Date: Jan 05, 2026*
