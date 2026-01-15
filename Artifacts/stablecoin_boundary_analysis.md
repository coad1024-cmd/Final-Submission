# The Non-Volatile Limit Case: A Boundary Analysis of Stablecoin Design

**Abstract**
This analysis explores the theoretical limit case of stablecoin design where reserve assets are strictly non-volatile relative to the unit of account. We demonstrate that under this constraint, the complex design space of stablecoins (comprising CDPs, algorithmic stabilization, and liquidation engines) collapses into a single degenerate solution: the Tokenized Narrow Bank. This result suggests that the "trilemma" and design diversity observed in the market are strictly functions of asset volatility and quality, rather than fundamental design choices.

---

## 1. Introduction: The Degeneracy Result

Current stablecoin literature focuses heavily on mechanism design to mitigate collateral volatility (e.g., liquidation parameters in MakerDAO, algorithmic expansion/contraction in Basis). This analysis posits that these mechanisms are not intrinsic necessities of decentralized currency, but rather **remedial structures** required solely due to the volatility of backing assets.

**Thesis:** *In a regime of strictly non-volatile collateral, all stablecoin designs converge to a fully-backed, primary-market-only model. Liquidation mechanisms, governance control parameters, and over-collateralization become mathematically redundant.*

## 2. Risk Taxonomy and Elimination Scope

Before deriving the optimal design, we must explicitly categorize standard stablecoin risks relative to our "Non-Volatile" constraint. Literature identifies five primary risks; we determine which are eliminated by assumption and which remain active constraints.

1.  **Credit Risk (Default Risk):** The risk of issuer default.
    *   *Status:* **Eliminated** via "Risk-Free Asset" assumption (e.g., theoretical T-Bills).
2.  **Market Risk & Volatility:** The risk of collateral value fluctuation against the peg.
    *   *Status:* **Eliminated** by the "Non-Volatile" constraint ($\sigma^2=0$).
3.  **Endogenous "Death Spiral" Risk:** The risk of reflexive adoption loops (common in algorithmic coins).
    *   *Status:* **Eliminated** by the "Fully Backed" constraint (disallowing endogenous collateral).
4.  **Liquidity Risk:** The risk of fire-sale slippage during redemptions.
    *   *Status:* **Eliminated** by the "HQLA / Infinite Depth" assumption.
5.  **Operational & Custodial Risk:** The risk of fraud, theft, legal freeze, or smart contract failure.
    *   *Status:* **RESIDUAL (Active).**

**Design Implication:** We have effectively eliminated liquidation risk and price-based insolvency commitments. However, **Operational and Custodial risks persist**. The resulting design, therefore, must not be viewed as "risk-free" but rather as a system optimized specifically to manage these residual threats.

## 3. The Limit-Case Model: "Zero-Volatility Primary-Market-Only Tokenized Liability"

Under the assumption of rational agents and risk-free reserves, the optimal design is reduced to:

1.  **Reserve Composition:** 100% Non-Volatile Assets ($A_{nv}$).
2.  **Capital Structure:** $1:1$ Backing + $\epsilon$ Operational Buffer.
3.  **Mechanism:** Direct Primary Market Mint/Burn.

### 3.1 Formal Definition

Let $S$ be the supply of stablecoins.
Let $A$ be the market value of reserve assets.
Let $L$ be the liability value of the stablecoins ($1 \cdot S$).

In standard models, $A$ is a random variable $A(t)$ with variance $\sigma^2 > 0$. Stability requires $A(t) > L(t)$ at all times, necessitating over-collateralization factor $k$ such that $A(0) = k \cdot L(0)$ where $k > 1$.

In our Limit Case, $\sigma^2 = 0$.
Therefore, $A(t)$ is deterministic regarding price.
The solvency constraint $A(t) \ge L(t)$ is satisfied if $A(0) \ge L(0)$ and operations are atomic.
**Result:** $k \to 1$.

This limit case should be understood as a degenerate baseline: any deviation from these assumptions immediately reintroduces liquidation, leverage constraints, or governance complexity.

## 4. Validation of Claims

We validate the redundancy of complex mechanisms through state transition analysis.

### 4.1 Redundancy of Liquidation Mechanisms
*Scenario:* A user mints 100 coins against $100 of collateral.
*Standard Model:* If collateral drops to $90, a liquidator triggers to sell asset and burn debt.
*Limit Model:* Collateral value $V_c$ is constant.
$$V_c(t) = 100 \quad \forall t$$
$$CR(t) = \frac{V_c(t)}{Debt} = \frac{100}{100} = 100\%$$
**Conclusion:** The trigger condition for liquidation ($CR(t) < \text{LiquidationRatio}$) is unreachable. The liquidation logic is dead code.

### 4.2 Peg Invariance under Demand Shocks
*Assumption:* Rational Arbitrageurs exist. Operational friction $f \approx 0$.
*Standard Model:* Massive redemptions can dislocate price if asset liquidity is thin (slippage).
*Limit Model:* Reserve is HQLA (High Quality Liquid Asset). We additionally assume that reserve assets are sufficiently liquid relative to outstanding supply, eliminating price impact during redemptions; this is a liquidity assumption, not a volatility one.
$$P_{coin} = \frac{A_{liquid}}{S}$$
Since every unit of $S$ is matched by $A_{liquid}$ on a 1:1 basis, the protocol can honor 100% redemption demand without slippage.
**Result:** Run risk is eliminated as a price-driven solvency concern, though operational and coordination-driven runs remain possible. Consequently, the absence of liquidity risk **does not remove the need for risk management**; it simply isolates **Operational and Custodial risks** as the sole remaining variables requiring active design intervention.

## 5. Residual Risk and Capital Structure

While market risk is zero, **Operational Risk** (OpRisk) remains non-zero. The model requires an Equity Tranche ($E$) to absorb these shocks (e.g., smart contract bugs, theft).

### 5.1 Governance Rules for Buffer
1.  **Subordination:** $E$ is strictly junior to depositor claims ($D$). $Assets = D + E$.
2.  **Dissolution Threshold:** If $E(t) < E_{min}$ (e.g., 0.5% of Supply), Minting functions **HALT** automatically.
3.  **No Discretion:** Recapitalization can only occur via external injection of equity tokens, not by diluting stablecoin holders or printing unbacked coins.
4.  **Exhaustion:** If $E$ is fully exhausted, the system enters wind-down mode with proportional asset redemption; stablecoin holders are never diluted or haircut during normal operation.

## 6. Scope and Limitations

This analysis assumes a specific, idealized environment. These limitations are not oversights but deliberate exclusions required to isolate the non-volatile limit case. The results **do not** hold if:
*   **Custodial Risk exists:** If the physical custodian of the T-Bills freezes assets, the "Non-Volatile" assumption essentially fails (value goes to 0 accessible).
*   **Censorship resistance is required:** This model relies on off-chain assets, implying dependence on traditional legal structures.
*   **Negative Rates:** If the risk-free rate becomes negative, the $E$ buffer bleeds, eventually violating the solvency constraint.

## 7. Conclusion

The "Limit-Case Stablecoin" in a non-volatile environment is not a new invention; it is a rediscovery of the **Narrow Bank**.
This confirms that the complexity observed in DeFi stablecoins (DAI, Liquity, etc.) is not a feature of "decentralization" but a necessary defense against the **volatility of endogenous collateral**. When volatility is removed, the design space collapses, and the most efficient structure is a simple, automated 1:1 warehouse receipt system with a junior capital buffer. This result should be read as a baseline against which volatile-world designs can be evaluated.

Future research should focus on the **integration of volatility** (the reality) rather than the optimization of static pegs, as the latter is a solved problem under these constraints.
