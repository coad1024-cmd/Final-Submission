# Terra (UST): Backing Mechanism Profile (Pillar I)

**Authors**: Research Challenge Team
**Date**: January 2026
**Series**: Terra Research Series (Part I)
**Framework**: [General Backing Framework](./general_backing_framework.md)

---

## 1. Executive Verdict

**Status:** 🔴 **FAILED (Algorithmic / Unbacked)**

Terra (UST) represents the archetype of **Endogenous Backing**. While it claimed to be "backed" by LUNA, the framework classifies this as a **"Red Flag" (Type C: The Chimera)**. The system relies on the **Absorption Assumption**: that LUNA liquidity will always be sufficient to absorb UST exits. Because LUNA's value is derived from the success of UST, this circular dependency creates a "Death Spiral" condition where the collateral value evaporates exactly when it is needed most ([Klages-Mundt & Minca, 2022](#ref-klages)).

### The Solvency Lens

* **Kinetic Solvency (Physics):** **Deterministic**. The system functioned exactly as coded (CPMM logic), but the economic physics were flawed ([Calandra et al., 2023](#ref-calandra)).
* **Static Solvency (Assets):** **Zero**. LUNA is not an external asset; it is a claim on the system's future growth (Seigniorage Shares).

---

## 2. Backing Scorecard (Pillar I)

| Dimension | Score (0-10) | Status | Key Driver |
| :--- | :--- | :--- | :--- |
| **Asset Quality** | **0/10** | 🔴 **Endogenous** | **LUNA Token.** Correlated asset. Framework Rule: "If your stablecoin needs GovTokens to stay solvent, it's already dead." |
| **Custody Risk** | **10/10** | 🟢 **Trustless** | **Smart Contract.** No admin keys. No upgradeability (except via Gov vote). Code is Law. |
| **Engine Speed** | **6/10** | 🟡 **Latent** | **Algorithmic Swap.** Fast execution, but limited by **Oracle Latency** (30s) and **Liquidity Recovery** decay. |
| **Redemption LCR** | **0/10** | 🔴 **Fiction** | **Virtual Pools.** There were no assets in the pool, only mathematical variables (`TerraPoolDelta`). |

---

## 3. Evidence Classification

### 3.1 Verified Facts (Type A)

* **F1 (Virtual Liquidity):** The `x/market` module did not hold reserves. It used variables (`BasePool`) to simulate market depth ([Internal Research, 2026](#ref-terra-analysis)).
* **F2 (Endogenous Collateral):** UST was redeemable only for LUNA, an asset printed by the protocol itself.
* **F3 (Oracle Latency):** The price feed had a ~30-second delay (`VotePeriod` = 5 blocks), creating a front-running vector during crashes.

### 3.2 Risk Scenarios (Type D)

* **Scenario A (The Death Spiral):** Confidence Crisis triggers UST sell-off.
  * *Mechanism:* System mints hyper-inflationary LUNA to honor redemptions.
  * *Result:* LUNA supply explodes to infinity -> Price goes to zero -> UST becomes unbacked.
* **Scenario B (Oracle Attack):** Price drops faster than Oracle update.
  * *Mechanism:* Attackers redeem UST at old (high) LUNA price.
  * *Result:* Value extraction accelerates insolvency.

---

## 4. Conclusion

* **Is it backed?** No. It is an algorithmic credit facility backed by future growth expectations.
* **Can you redeem it?** Yes, until the equity (LUNA) becomes worthless.
* **Is it safe?** No. It violates the fundamental rule of backing: **Collateral must be uncorrelated with the liability.**

---

### Series Navigation

* **Part I: Backing Profile** (You are here)
* [Part II: Backing Deep Dive](./Terra_Backing_DeepDive.md)
* [Part III: Sustainability Profile](./Terra_Sustainability_Profile.md) (Pending)
* [Part IV: Decentralization Profile](./Terra_Decentralization_Profile.md) (Pending)

---

## References

<span id="ref-backup-framework"></span>Internal Research. (2026). *[General Backing Framework](./general_backing_framework.md)*. Canonical Methodology.

<span id="ref-terra-analysis"></span>Internal Research. (2026). *[Terra Protocol Architecture Analysis](./Article_Backing.md)*. Source Code Audit.

<span id="ref-klages"></span>Klages-Mundt, A., & Minca, A. (2022). *[While Stability Lasts: A Stochastic Model of Non-Custodial Stablecoins](https://arxiv.org/abs/2004.01304)*. Cornell University.

<span id="ref-calandra"></span>Calandra, F., Rossi, F., Fabris, F., & Bernardo, M. (2023). *[Algorithmic Stablecoins: A Simulator for the Dual-Token Model](https://ieeexplore.ieee.org/document/11114693)*. University of Urbino.
