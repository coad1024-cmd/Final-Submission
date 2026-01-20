# Part III: Attack Analysis & Profitability

## 1. The Economics of the Attack

A rational attacker does not profit from breaking the peg alone. Profit arises from **positioning against the consequences** of the peg break.

The attack structure is asymmetric:

* **Trigger (Cost):** Large AS sell. Incurs slippage. Fixed cost.
* **Capture (Benefit):** CT short position. Gains from collateral collapse. Variable upside (scales with leverage).

$$\text{Net PnL} = (\text{Short Profit} \times \text{Leverage}) - \text{Trigger Cost}$$

---

## 2. The Redemption Attack (Infinite Money Glitch)

Beyond speculative shorting, the **Redemption Attack** exploits the protocol's solvency mechanism directly.

### The Mechanism

1. **Trigger:** Dump AS to push price < $0.95.
2. **Loop:**
    * Buy AS at discount (e.g., $0.80).
    * Redeem for $1.00 of CT (Printing new tokens).
    * Sell CT immediately (Crashing price further).
    * Repeat.

### Results

* **Hyper-Inflation:** Unlike a passive death spiral, the attacker *forces* redemption. In simulations, CT supply exploded from **345M to >2B** in defined iterations.
* **Systemic Failure:** CT price goes to **ZERO**. The maximization of "Arbitrage Profit" guarantees the destruction of the collateral.

---

## 3. Profitability Frontier (Sensitivity Analysis)

We conducted a parameter sweep (Stablecoin Dump Size vs. CT Short Size) to find the breakeven point.

![PnL Sensitivity Heatmap](images/pnl_heatmap.png)

### Key Observations

1. **The Loss Zone:** Small short positions cannot overcome the initial dump cost.
2. **The Profit Zone:** Net PnL scales linearly with short size. The limiting factor is not capital to break the peg—it's **liquidity to short the collateral**.
3. **Breakeven:** A diagonal threshold separates the zones. The attack is viable only if sufficient CT borrow liquidity exists.

### Strategic Implication

Dual-token systems are **structurally exploitable**. The mechanism that maintains the peg becomes the weapon that destroys it. This destruction can be monetized by any actor with sufficient capital and access to unintended leverage (Shorts/Perps).

---

[← Back to Index](README.md) | [Previous: Market Simulations ←](02_Market_Simulation.md) | [Next: Conclusions →](04_Conclusion.md)
