# Liquity V2 (BOLD): The Architecture of Kinetic Solvency & Sovereign Resilience

**Date**: January 2026
**Subject**: Canonical Research Synthesis
**Framework Alignment**: [Sustainability v1.0](../../01_frameworks/Stablecoin-Sustainability-Framework.md), [Decentralization v3.0](../../01_frameworks/Stablecoin-Decentralization-Framework.md)
**Authors**: Research Challenge Team

---

## Executive Summary

Liquity V1 (LUSD) established the benchmark for "Static Solvency"—an immutable, trustless stablecoin backed 100% by Ether. While secure, it proved economically fragile in the post-ZIRP environment and scalable only as far as ETH leverage demand allowed. Liquity V2 (BOLD) represents a paradigm shift to **"Kinetic Solvency"** ([Liquity V2 Docs](#ref-liquity-v2-docs)). It acknowledges that absolute stability in a multi-collateral world cannot be achieved through static backing alone. Instead, it relies on a dynamic, self-healing mechanism where the system's solvency is maintained by the continuous "motion" of redemptions targeting the riskiest liabilities.

This report synthesizes three core dimensions of the V2 architecture:

1. **Backing Mechanism ("The Physics")**: The "Federated" Hub-and-Spoke model and Unbackedness Routing.
2. **Economic Sustainability ("The Economics")**: The "User-Set Rate" mechanism analyzed via the *Sustainability Triangle*.
3. **Decentralization ("The Sovereignty")**: The "Pragmatic Sovereignty" trade-off analyzed via the *G-C-O-E Framework*.

---

## Part I: Kinetic Solvency (The Backing Mechanism)

### 1.1 The Architecture: Federated Hub-and-Spoke

![Hub and Spoke Architecture Diagram](v2_hub_spoke_architecture.png)

<small>*Fig 1.1: The Federated Solvency Architecture. The Central Hub manages the global BOLD liability and routes redemptions, while isolated "Spokes" (Branches) hold the actual collateral assets (WETH, rETH) in compartmentalized silos. This ensures that risk does not spill over between different collateral types.*</small>

**The "Why" Analysis:**
In a standard Unified Debt Model (e.g., MakerDAO, Aave), solvency is global. All assets back all debt. This creates a "Lowest Common Denominator" problem: if one asset (e.g., a bridge-wrapped token) fails, the entire solvency pool is contaminated ([Internal Research, 2026](#ref-internal-backing)).

* **V1 Approach:** Avoid the problem by only accepting ETH. (Tradeoff: Zero Scalability).
* **V2 Approach:** Accept many assets, but **strictly isolate** their risk. This is the **Federated** model.

**The "How" Analysis (Hub vs Spoke):**
The system is bifurcated into a lightweight logic layer and a heavy asset layer.

* **The Hub (CollateralRegistry):** This contract acts as the system's "Solvency CPU." Crucially, it **holds no collateral**. Its sole purpose is to track the "Unbackedness" of each branch. It manages the global liability token (BOLD) but delegates asset management to the branches.
* **The Spokes (Branches):** Each collateral type (WETH, rETH, wstETH) exists in a fully self-contained market. A branch contains its own `TroveManager`, `ActivePool`, `StabilityPool`, and `DefaultPool`.

### 1.2 The Innovation: Algorithmic Unbackedness Routing

![Redemption Routing Engine](redemption_routing_engine.png)

<small>*Fig 1.2: Redemption Routing Engine. The protocol dynamically routes redemptions based on branch health metrics, prioritizing undercollateralized branches to automatically excise systemic risk.*</small>

**The Design Necessity:**
Since collateral is fractured across isolated pools, there is no single "pot" to redeem against. If a user redeems BOLD, *which* collateral should they get? Randomness is inefficient. Pro-rata is unfair to safe branches.
**The Solution:** Route redemptions to the "sickest" branches first. This acts as an automated immune system.

**The Mechanism (Unbackedness Formula):**
For every branch $i$, we calculate "Unbackedness" ($U$) using the formula:
$$U_i = \max(0, \text{Debt}_i - \text{StabilityPool}_i)$$

This formula mathematically isolates "Exposed Debt." If a branch has a deep Stability Pool, $U=0$. If the SP is empty, $U > 0$.

**The Routing Logic:**
When a redemption occurs, the Hub calculates the share ($R_i$) for each branch:
$$R_i = \frac{U_i}{\sum U_j} \cdot R_{total}$$

**Routing Logic Pseudocode:**
To clarify the exact mechanism of *Algorithmic Unbackedness Routing*:

```
FUNCTION RouteRedemption(BOLD_Amount)
    
    // Step 1: Calculate Unbackedness for all branches
    FOR EACH branch IN system.branches DO
        U[branch] ← MAX(0, branch.total_debt - branch.stability_pool_balance)
    END FOR
    
    // Step 2: Route based on system health
    IF SUM(U) > 0 THEN
        // High Risk Mode: Route to unhealthy branches proportionally
        RETURN WeightedSplit(U, BOLD_Amount)
    ELSE
        // Healthy Mode: Route to lowest interest rate Troves first
        RETURN RouteByInterestRate(BOLD_Amount)
    END IF
    
END FUNCTION
```

**Advantage & Tradeoff:**

The core advantage of Algorithmic Routing is that it weaponizes the "Run on the Bank," transforming typically destructive capital flight into a constructive "System Cleanup." By automatically channeling redemptions toward the weakest branches, the protocol utilizes market exit pressure to excise bad debt without human intervention, effectively acting as a self-healing immune system. The unavoidable cost of this resilience is **Redemption Uncertainty**. Unlike simple mono-collateral models, an arbitrageur redeeming BOLD cannot know *ex-ante* the precise mix of assets they will receive. This introduces epistemic friction for the redeemer—a calculated tax paid to ensure the system survives local asset failures.

### 1.3 The Defense: The Liquidation Waterfall

![Liquidation Waterfall Diagram](detailed-liquidation-waterfall.png)

<small>*Fig 1.3: The Liquidity Defense Waterfall. Solvency is maintained through a three-stage defense: (1) Atomic Offset via the Stability Pool (The "Wall"), (2) Debt Redistribution (The "Spread"), and (3) Critical Collateral Ratio (System Defense). This multi-layered approach removes dependency on external auction markets during crises.*</small>

**Key Metrics & The Liquidation Waterfall:**

In Liquity V2, solvency is governed by three **branch-specific** economic tripwires. Each collateral type (WETH, rETH, etc.) maintains independent thresholds, enabling the "Bulkhead" architecture that isolates risk.

| Metric | Level | Definition | Trigger |
| --- | --- | --- | --- |
| **ICR** | Individual | `(Collateral Value) / (Debt in BOLD)` — A Trove's health score | If `ICR < MCR` → Trove enters Waterfall |
| **MCR** | Branch | Minimum Collateral Ratio (e.g., 110% for WETH, 120% for volatile LSTs) | Activates Layer 1 or Layer 2 |
| **CCR** | Systemic | Critical Collateral Ratio (e.g., 150%) — Branch safety limit | If `TCR < CCR` → Recovery Mode |

**The Three-Layer Defense:**

1. **Layer 1: Stability Pool** — When `ICR < MCR`, debt is instantly burned against the branch's Stability Pool; collateral is distributed to depositors at a profit (MCR > 100% = discount).

2. **Layer 2: Redistribution** — If the Stability Pool is exhausted, remaining debt/collateral is redistributed pro-rata to all active Troves in that branch. Recipients gain collateral value exceeding the debt absorbed.

3. **Layer 3: Recovery Mode** — If a branch's `TCR < CCR`, the protocol enters a defensive state: (a) Troves with `ICR < CCR` become liquidatable even if above MCR, (b) new BOLD minting is restricted to prevent further TCR decline.

**V1 vs V2 Comparison:**

| Feature | V1 (LUSD) | V2 (BOLD) |
| --- | --- | --- |
| Recovery Trigger | System-wide (150%) | Branch-specific |
| Stability Pool Yield | Liquidations only | Liquidations + Aggregated Interest |
| Contagion Risk | Global | Isolated per branch |

**Key Insight:** The Waterfall ensures BOLD is **path-independent**—the protocol deleverages via a pre-defined algorithmic sequence regardless of crash dynamics. A CCR breach in *stETH* does not trigger Recovery Mode in *WETH*.

---

## Part II: Sustainability Analysis

**Framework Alignment:** [Stablecoin Sustainability Framework](#ref-framework-sustainability)

### 2.1 Business Model & "Yield via Pain"

**The "Why" of User-Set Rates:**

MakerDAO relies on "External Yield" (RWA/Treasuries) to pay the DAI Savings Rate (DSR). This makes it a "Bank" dependent on the Federal Reserve's interest rate policy. Liquity V2 rejects this model entirely—it wants **Internal Yield** generated purely from protocol activity.

**The Mechanism in Detail:**

1. **Rate Selection:** When opening a Trove, borrowers choose their own annual interest rate (e.g., 3%, 5%, 7%). This rate determines how much they pay to borrow BOLD.

2. **Redemption Ordering:** When arbitrageurs redeem BOLD (to restore the peg), the protocol routes redemptions to Troves with the **lowest interest rates first**. This creates a "Redemption Queue" where cheap borrowers are at the front.

3. **The Game Theory:**
   * If you set a **low rate** (e.g., 1%): You pay less interest, but you're first in line when redemptions occur. Your collateral gets claimed.
   * If you set a **high rate** (e.g., 8%): You pay more interest, but you're protected from redemptions—other Troves get hit first.

4. **Emergent Market Rate:** Users collectively bid up rates to avoid the "Redemption Cliff," creating an emergent "Market Rate" without any governance intervention. This rate represents the true cost of leverage in the BOLD ecosystem.

**Why This Matters for Sustainability:**

* **No External Dependency:** Unlike MakerDAO's reliance on T-Bill yields, Liquity V2's revenue comes from internal demand for leverage.
* **Self-Regulating:** If external rates rise, BOLD's redemption pressure increases, forcing borrowers to raise their rates—the system auto-tunes.
* **Pure DeFi:** No RWA custody risk, no TradFi counterparty exposure.

![Interest Rate Buckets](interest_rate_buckets.png)

<small>*Fig 2.1a: Interest Rate Bucket Architecture. Borrowers self-select into discrete interest rate buckets, creating stratified debt layers. This mechanism enables efficient redemption routing and incentivizes rate competition.*</small>

![Yield via Pain Feedback Loop](interest_rate_distribution.png)

<small>*Fig 2.1: The "Redemption Cliff." The chart above illustrates the game theory of V2. The X-axis represents the user-set interest rate, and the Y-axis represents the debt volume. Users naturally cluster their positions just to the right of the "Redemption Zone" (the red shaded area). This behavior creates an emergent "Market Rate" (the peak of the curve) that acts as the system's cost of capital, entirely driven by the collective fear of being redeemed.*</small>

**Key Metrics Analysis:**

**1. Liquidation Dependency Ratio (LDR): < 0.10 (Healthy)**
Unlike V1 or other models that rely on "Liquidation Penalties" for revenue, V2's primary revenue source is interest. This creates a sustainable model where the protocol thrives on valid usage, not user failure.

**2. Net Interest Margin (NIM): Variable (Resilient)**
Because users set the rates, the "Cost of Capital" and "Yield on Capital" are linked. If the market rate (RFR) rises, redemptions force borrowers to raise their rates, automatically increasing the protocol's NIM. It is an auto-tuning engine.

**3. HHI (Collateral Concentration): 0.56 (High Concentration)**
Fresh DefiLlama data (January 2026) shows **wstETH dominates collateral TVL at 72.2%**, followed by WETH (15.6%) and rETH (12.2%) ([DefiLlama, 2026](#ref-defillama-data)). Despite this concentration, WETH still generates the highest revenue (~\$5M vs ~\$0.5M for rETH), indicating WETH borrowers pay higher effective rates. The Bulkhead pattern ensures LST failures don't affect other branches.

![Branch Contribution Analysis](6_branch_contribution.png)

<small>*Fig 2.2: Branch Revenue Contribution. Despite wstETH's collateral dominance, WETH generates the majority of protocol revenue—suggesting different borrower behavior across branches.*</small>

### 2.2 Stress Test Framework (Standard Scenarios)

We evaluate V2 against the three standard stress scenarios mandated by the framework: a 70% **Price Shock** to test liquidation efficiency, a **Liquidity Freeze** to assess redemption-driven peg stability, and **Collateral Contagion** to verify the "Bulkhead" risk isolation mechanism. These simulations ensure the system remains solvent during extreme dislocations.

**Test 1: The 70% Collateral Crash (Price Shock)**

* **Scenario:** ETH price falls 70% in 48 hours. Gas fees spike to 500 gwei.
* **V2 Performance:**
  * The **Atomic Offset** mechanism is gas-efficient. It does not require thousands of auction transactions.
  * The **Yield Split (75%)** ensures Stability Pools are deep *before* the crash.
  * **Verdict:** ✅ **Passed (Robust).** Superior to auction-based models in high-volatility/high-gas regimes.

**Test 2: The Liquidity Freeze (Market Structure)**

* **Scenario:** LST liquidity on Curve/Uniswap dries up. Peg pressure mounts.
* **V2 Performance:**
  * Arbitrageurs can always redeem BOLD for the underlying LST at \$1.00 face value.
  * They can then take the LST to the primary issuer (Lido/RP) to exit to ETH.
  * **Verdict:** ✅ **Passed.** Redemption guarantees "Exit to Underlying" regardless of secondary market crashes.

**Test 3: The Collateral Contagion (Asset Failure)**

* **Scenario:** rETH Smart Contract bug. rETH value $\rightarrow$ 0.
* **V2 Performance:**
  * **Bulkhead:** Prevents rETH bad debt from claiming WETH assets.
  * **Peg Impact:** BOLD is partially backed by \$0 assets. The peg will break (trade below \$1) until the rETH branch is completely wound down or written off.
  * **Verdict:** ⚠️ **Degraded.** The Protocol survives, but the stablecoin peg temporarily breaks.

## Part III: Decentralization Analysis

**Framework Alignment:** [Stablecoin Decentralization Framework v3.0](#ref-framework-decentralization)

### 3.1 G-C-O-E Scoring Matrix

We apply the standard weighting: $w_G=0.25, w_C=0.30, w_O=0.25, w_E=0.20$.

**1. Governance (G): Gold (Score: 0.75)**

* **Metric:** Admin Keys = 0, but "Incentive Keys" = Distributed.
* **Analysis:** While the core protocol math (parameters) is immutable ("Code is Law"), Liquity V2 introduces **"Modular Initiative-based Governance"** using the LQTY token.
  * **Utility:** LQTY holders accrue **Voting Power** to steer 25% of protocol revenue to specific "Initiatives" (e.g., liquidity pools) and possess **Veto Power** to block malicious actors.
  * **Nuance:** This creates a bifurcation: The *Rules* are unstoppable, but the *Rewards* are governed. This protects the protocol from technical censorship but introduces "Soft Governance" pressure via incentive direction.

![Lorenz Curve](lorenz_curve.png)
<small>*Fig 3.1: Lorenz Curve of Voting Power (Jan 2026). The deviation from the "Line of Equality" visually represents the Gini Coefficient of **0.29** (Calculated from [fresh on-chain snapshot](../data/lqty_distribution_2026.csv)). This reflects the concentration of the LQTY staking token, which translates directly to **Voting Power** for incentive steering.*</small>

**2. Collateral (C): Red (Score: 0.20)**

![Collateral Composition](collateral_composition.png)
<small>*Fig 3.2: Collateral TVL Concentration (DefiLlama - January 2026). wstETH (72.2%), WETH (15.6%), rETH (12.2%). The HHI of 0.56 reflects concentration in Lido's wstETH. Note: wstETH dominates collateral while WETH dominates revenue (see Fig 2.2).*</small>

The critical risk for V2's decentralization score lies in its collateral composition.

* **Metric:** HHI = 0.66 (> 0.50 Threshold).
* **Analysis:** Unlike V1 (Native ETH), V2 relies on LSTs. These assets are governed by DAOs and have upgradable smart contracts. BOLD effectively imports the governance risk of Lido and Rocket Pool.
* **Binding Constraint:** This Score caps the Total Composite Score.

**3. Operational (O): Gold (Score: 0.75)**

![Frontend Shares](frontend_shares.png)
<small>*Fig 3.3: Frontend Operator Distribution. The "Headless Brand" model results in a decentralized access layer. No single frontend controls more than 20% of the traffic, ensuring that the protocol remains accessible even if the primary "Liquity.App" domain is seized.*</small>

* **Metric:** Headless Brand (63 Frontends).
* **Analysis:** V2 retains the "Kickback" model equivalent (fee sharing) that incentivizes third-party hosting. This ensures censorship resistance at the access layer. If "Liquity.App" is blocked, 62 others remain.

**4. Emergency (E): Platinum (Score: 1.0)**

* **Metric:** No Kill Switch.
* **Analysis:** There is no "Emergency Shutdown Module" (ESM) like in MakerDAO. The system cannot be turned off by regulators or the team.

### 3.2 Composite Score & Final Verdict

$$D_{raw} = 0.25(0.75) + 0.30(0.20) + 0.25(0.75) + 0.20(1.0) = 0.64$$

**The Binding Constraint Rule:**
The Framework states: *"If ANY individual dimension falls into 'Red', the composite score is capped at 0.50."*

* **Constraint Trigger:** Collateral Dimension (C) is Red.
* **Final Score:** **0.50 (Boundedly Decentralized)**.

**Risk Radar Profile:**
Liquity V2 is an **Unstoppable Protocol** built on **Stoppable Assets**. The code cannot be censored, but the collateral (rETH) can be frozen by its issuer. This is a deliberate design choice ("Pragmatic Sovereignty") to achieve scale.

![Risk Radar Diagram](liquity_v2_risk_radar.png)
<small>*Fig 3.4: Decentralization Risk Radar. The visual profile of Liquity V2 highlights the stark trade-off: Maximum scores in Governance, Operational, and Emergency dimensions, constrained by the "Red" score in Collateral Decentralization due to LST reliance.*</small>

---

## Technical Appendix

### Data Verification

**Table: Collateral Risk Concentration (HHI)**
*Composition of the backing assets (DefiLlama - January 2026).*

| Asset | Share of TVL | Risk Profile | Governance Score |
|:---|:---|:---|:---|
| **wstETH (Lido)** | 72.2% | DAO + Smart Contract | Gold (Market Leader) |
| **WETH** | 15.6% | Trustless | Platinum (Immutable) |
| **rETH (Rocket Pool)** | 12.2% | DAO + Smart Contract | Gold (Decentralized Node Ops) |
| **Total** | **100%** | **HHI = 0.56** | **Composite: Gold/Silver** |

---

## References

1. <span id="ref-liquity-v2-docs"></span>Liquity V2 Technical Documentation. (2025). *[Liquity V2 Documentation](https://docs.liquity.org/)*. GitBook.
2. <span id="ref-internal-backing"></span>Internal Research. (2026). *[Liquity V2 Backing Deep Dive](../Artifacts/Liquity_V2_Backing_DeepDive.md)*. Project Artifact.
3. <span id="ref-internal-decentralization"></span>Internal Research. (2026). *[Liquity V2 Decentralization Analysis](../Artifacts/Liquity_V2_Decentralization_Analysis.md)*. Project Artifact.
4. <span id="ref-internal-resilience"></span>Internal Research. (2026). *[Liquity V2 Economic Resilience](../Artifacts/Liquity_V2_Economic_Resilience.md)*. Project Artifact.
5. <span id="ref-liquity-api"></span>Liquity Protocol. (2026). *[Official V2 Statistics API](https://api.liquity.org/v2/ethereum.json)*. Real-time Data Endpoint.
6. <span id="ref-framework-sustainability"></span>Internal Research. (2025). *[Stablecoin Sustainability Framework](../../01_frameworks/Stablecoin-Sustainability-Framework.md)*. Methodological Framework.
7. <span id="ref-framework-decentralization"></span>Internal Research. (2025). *[Stablecoin Decentralization Framework](../../01_frameworks/Stablecoin-Decentralization-Framework.md)*. Methodological Framework.
8. <span id="ref-defillama-data"></span>DefiLlama. (2026). *[Liquity V2 TVL Data](https://defillama.com/protocol/liquity-v2)*. Retrieved January 15, 2026.

---

<div align="center">

| ← Previous | Home | Next → |
|:---|:---:|---:|
| [Research Overview](../README.md) | [Table of Contents](../README.md) | [Sky Ecosystem](../Sky-final/Sky-final.md) |

</div>
