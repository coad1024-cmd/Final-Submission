# Part III: Attack Analysis & Profitability

## 1. The Economics of the Attack

A rational attacker does not profit from breaking the peg alone. Profit arises from **positioning against the consequences** of the peg break.

The attack structure is asymmetric:

* **Trigger (Cost):** Large **AS** sell. Incurs slippage. Fixed cost.
* **Capture (Benefit):** Large **CT** short position. Gains from collateral collapse. Variable upside (scales with leverage).

$$\text{Net PnL} = (\text{Short Profit} \times \text{Leverage}) - \text{Trigger Cost}$$

---

## 2. Profitability Frontier (Sensitivity Analysis)

We conducted a parameter sweep (Stablecoin Dump Size vs. CT Short Size) to find the breakeven point.

![PnL Sensitivity Heatmap](images/pnl_heatmap.png)
<small>*Fig 1: Net PnL Heatmap. X-Axis = Dump Size (Trigger Cost). Y-Axis = Short Size (Potential Reward).*</small>

**Heatmap Analysis:**

* **Red Zone (Bottom Left):** The "Suicide Zone". The attacker dumps **AS** (paying trigger cost) but has an insufficient short position to recover the loss.
* **Green Zone (Top Right):** The "Profitable Zone". Large short positions (>$500M) easily absorb the fixed cost of the dump, generating massive net profits.
* **The Threshold:** Profitability begins roughly when `Short Size > 1.5x Dump Size`. This ratio is critical for the attacker's capital planning.

### Key Observations

1. **The Loss Zone:** Small short positions cannot overcome the initial dump cost.
2. **The Profit Zone:** Net PnL scales linearly with short size. The limiting factor is not capital to break the peg—it's **liquidity to short the collateral**.
3. **Breakeven:** A diagonal threshold separates the zones. The attack is viable only if sufficient CT borrow liquidity exists.

### Strategic Implication

Dual-token systems are **structurally exploitable**. The mechanism that maintains the peg becomes the weapon that destroys it. This destruction can be monetized by any actor with sufficient capital and access to unintended leverage (Shorts/Perps).

---

<div align="center">

| [Previous] | Home | [Next] |
| :--- | :---: | ---: |
| [2. Market Simulations](02_Market_Simulation.md) | [Table of Contents](../README.md) | [4. Conclusions →](04_Conclusion.md) |

</div>
