# Part V: Curve (StableSwap) vs Uniswap

## Hypothesis: The Flat Curve Defense (Results: **Mixed**)

**Core Question:** Can replacing the Constant-Product (Uniswap) formula with a StableSwap (Curve) formula protect the peg?

**The Logic:**

- **Uniswap ($xy=k$):** High slippage for large trades. A large dump moves the price significantly.
- **StableSwap (Invariant):** Extremely low slippage near the peg. A large dump should be absorbed with minimal price impact **up to the amplification limit**, after which slippage increases vertically.

**Prediction:** StableSwap pools will make the attack *cheaper to trigger* (less slippage) but might dampen the death spiral by maintaining the peg longer.

---

## Experimental Design

We compared four pool configurations:

1. **Uniswap (Control):** Standard Constant-Product AMM
2. **Curve (A=10):** Low amplification (behaves like Uniswap)
3. **Curve (A=100):** Moderate amplification (standard for stablecoins)
4. **Curve (A=500):** High amplification (extremely flat curve)

**Control variables:**

- Attack: 500M AS dump
- Liquidity: ~$18.5B (1x Baseline)

---

## Results

![Curve vs Uniswap Comparison](images/curve_vs_uniswap.png)

*Left: Attack Economics. Right: Net PnL. Center: Max Price Impact.*

### Quantitative Data

| Pool Type | Trigger Cost | Short Profit | Net PnL | Min AS Price | Profitability |
|:----------|-------------:|-------------:|--------:|-------------:|:--------------|
| **Uniswap** | $32.2M | **$17.4M** | −$14.8M | $0.9006 | ❌ No |
| **Curve (A=10)** | $31.4M | $0.6M | −$30.9M | $0.8855 | ❌ No |
| **Curve (A=100)** | $29.5M | $0.7M | −$28.7M | **$0.8885** | ❌ No |
| **Curve (A=500)** | **$29.6M** | $2.1M | −$27.5M | $0.8878 | ❌ No |

### Key Findings

1. **Trigger Cost is Lower on Curve:** As predicted, the "flatter" curve means the attacker pays less slippage to dump the same 500M AS (\$29.6M vs \$32.2M).

2. **Collateral is PROTECTED:** This is the surprise finding. In the Uniswap model, the CT price crashed to ~\$75. In the Curve models, CT price stayed near ~\$79.50. The death spiral *did not fire*.

3. **The "De-Peg Trap":** Despite protecting the collateral, the Stablecoin price in the Curve pools dropped *lower* (\$0.88) than in the Uniswap pool (\$0.90) and—crucially—**stayed there**.

### Analysis: The "Flat Curve" Paradox

Why did the death spiral fail to trigger effectively in the Curve pools?

In a Convex (Uniswap) pool, arbitrage is efficient. If AS drops to \$0.90, buying it pushes the price up quickly. This creates a rapid feedback loop of "Buy AS -> Mint CT -> Sell CT".

In a Flat (Curve) pool that has been pushed *off* its plateau:

1. The attacker dumps 500M AS, pushing the price to the "cliff" edge (\$0.88).
2. The pool is now unbalanced (too much AS).
3. Because the curve is flat *near the peg* but steep *off the peg*, arbitrageurs buying back AS struggle to push the price back up the cliff.
4. The price languishes at \$0.88.
5. While the arbitrage opportunity exists (\$1.00 - \$0.88 = \$0.12$), the *volume* of arbitrage required to restore the peg is massive.
6. The simulation reveals a **liquidity trap**: The pool becomes a "stable" de-pegged asset.

### Strategic Implication

Switching to a Curve-style pool **trades one risk for another**:

- **Uniswap Risk:** High volatility, rapid death spiral, complete collapse.
- **Curve Risk:** "Sticky" de-pegs. Once the price falls off the flat plateau, it forces the protocol into a zombie state where it trades at a permanent discount (\$0.88), but the collateral (and thus the protocol) survives.

**Verdict:** Curve pools are better for **survival** (preventing zero), but worse for **recovery** (harder to re-peg after a massive shock).

---

[← Back to Index](README.md) | [Previous: Pool Sensitivity ←](04_Pool_Sensitivity.md) | [Next: Conclusions →](05_Conclusions.md)
