# Liquity V2 (BOLD): Backing Mechanism Profile (Part I)

**Authors**: Research Challenge Team
**Date**: January 2026
**Series**: Liquity Research Series (Part I)

---

## 1. Executive Verdict

**Status:** 🟢 **Structurally Robust / Politically Resilient**

Liquity V2 represents the state-of-the-art in **Modular Solvency**. By abandoning the "Unified Debt" model of MakerDAO and V1, it eliminates cross-collateral contagion. The backing portfolio is user-defined, meaning the "Protocol" has no single solvency score; instead, each "Branch" (e.g., WETH, rETH) has its own independent integrity. However, the global liability (BOLD) is mathematically secured by the **Unbackedness Routing** algorithm, which acts as a "Self-Healing" immune system for the peg.

### The Solvency Lens

* **Kinetic Solvency (Physics)**: **Robust**. Algorithmic routing forces redemptions to target the riskiest debt first.
* **Static Solvency (Assets)**: **Variable**. Depends entirely on the specific Branch, but contagion is **firewalled**.

---

## 2. Backing Scorecard (Pillar I)

| Dimension | Score (0-10) | Status | Key Driver |
| :--- | :--- | :--- | :--- |
| **Asset Quality** | **N/A** | ⚪ **Modular** | Varies by branch. Protocol level score is undefined; Branch level scores are isolated. |
| **Custody Risk** | **10/10** | 🟢 **Trustless** | The Hub holds **zero collateral**. Assets are held in isolated, non-custodial Smart Contracts. |
| **Engine Speed** | **9/10** | 🟢 **Atomic** | 75% Yield Split ensures Deep Stability Pools. Flash Loan arb via Urgent Redemption Mode. |
| **Redemption LCR** | **10/10** | 🟢 **Perfect** | **Algorithmic Routing** guarantees instant exit into the most solvent/liquid assets. |

---

## 3. Evidence Classification

### 3.1 Verified Facts (Type A)

* **F1 (Isolation):** Code audit confirms `ActivePool` contracts are cryptographically distinct. A hack in rETH cannot drain WETH.
* **F2 (Yield):** 75% of borrower interest is mathematically routed to the local Stability Pool, maximizing kinetic reserves.

### 3.2 Risk Scenarios (Type D)

* **Scenario A (The LST Rug):** A specific LST (e.g., rETH) goes to zero.
  * *Result:* rETH Branch becomes insolvent.
  * *Defense:* **Granular Shutdown**. rETH branch freezes. WETH/wstETH branches remain 100% operational. BOLD peg holds via healthy branches.
* **Scenario B (Oracle Freeze):** Chainlink feed for WETH stops updating.
  * *Result:* Epistemic Insolvency.
  * *Defense:* `shutdown()` triggered by staleness check. **Urgent Redemption Mode** allows arbitrageurs to unwind debt with 0% fees, clearing the risk.

---

## 4. Conclusion

* **Is it backed?** Yes. By a federation of independent collateral pools.
* **Can you redeem it?** Yes. And the algorithm ensures you likely get the *best* collateral (healing the system) or the *most liquid* (in urgent mode).
* **Is it safe?** It offers the strongest **Contagion Resistance** in the market.

---

### Series Navigation

* **Part I: Backing Profile** (You are here)
* [Part II: Economic Sustainability Profile](./Liquity_V2_Economic_Resilience.md)
* [Part III: Decentralization Profile](./Liquity_V2_Decentralization_Analysis.md)

---

## References

<span id="ref-deep-dive"></span>Internal Research. (2026). *[Liquity V2 Backing Deep Dive](./Liquity_V2_Backing_DeepDive.md)*. Canonical Analysis.
