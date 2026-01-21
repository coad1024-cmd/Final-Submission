# Part III: Experimental Results

## Visual Evidence: Attack Dynamics

Before detailing each experiment, observe the three key time-series from a successful attack:

### Figure 1: Stablecoin Price De-Peg

![Stablecoin Price De-Peg](images/stablecoin_price_depeg.png)

*The stablecoin maintains peg (~$1.00) until the attack iteration. At trigger, price drops sharply and fails to recover—the panic regime has begun.*

### Figure 2: Collateral Price and Supply Collapse

![Collateral Collapse](images/collateral_collapse_subplots.png)

*Top panel: CT price collapses from ~$80 to near-zero. Bottom panel: CT supply inflates as the mint-burn facility mints new CT for each AS redemption. This is the death spiral in action—price collapse and supply inflation reinforce each other.*

### Figure 3: Attacker Portfolio Value Over Time

![Attacker Portfolio History](images/attacker_portfolio_history.png)

*The attacker experiences an initial drawdown (the cost of breaking the peg). As CT collapses, the short position gains value, eventually dominating. The final portfolio value exceeds the initial—the attack is profitable.*

---

## Experiment 1: The Raw Dump

**Hypothesis:** A large stablecoin sell, without hedging, will break the peg and allow the attacker to profit from the chaos.

**Setup:**

- Attacker capital: 500M AS
- CT short position: None
- Trigger iteration: 150,000 (simulated ~10 days into the run)

**Results:**

| Metric | Value |
|:-------|------:|
| AS price (post-attack) | ~$0.60 |
| CT price (post-attack) | ~\$15 (from $80) |
| Attacker PnL | **−$87M** |

**Analysis:** The attack *works*—the peg breaks, the death spiral initiates, collateral collapses. But the attacker loses money. The slippage on selling 500M AS into a finite-liquidity pool exceeds any recoverable value.

**Conclusion:** Destruction is expensive. You cannot profit from a crash using only the asset you're crashing.

---

## Experiment 2: Short + Dump (The Soros Strategy)

**Hypothesis:** The exploitable value in a death spiral is not the stablecoin (which stabilizes around $0.50–$0.90) but the collateral token (which approaches zero). By shorting CT before triggering the dump, the attacker can capture this value.

**Setup:**

- Attacker capital: 500M AS
- CT short position: $300M notional
- Trigger iteration: 150,000

**Results:**

| Metric | Value |
|:-------|------:|
| CT price collapse | ~$80 → ~$1 (−98%) |
| Short profit | +$157M |
| Dump loss | −$89M |
| **Net PnL** | **+$68M** |

**Analysis:** The dynamics are identical to Experiment 1—same peg break, same death spiral. The difference is that the attacker is now positioned to *benefit* from the collapse rather than merely *cause* it. The short position converts the protocol's failure into the attacker's gain.

The breakeven point occurs when CT has lost approximately 60% of its value. Everything beyond that is profit.

---

## Experiment 3: Maximum Leverage

**Hypothesis:** If the death spiral is deterministic once triggered, the attacker should maximize short exposure. The trigger cost is fixed; the upside scales with leverage.

**Setup:**

- Attacker capital: 500M AS
- CT short position: $1B notional
- Trigger iteration: 150,000

**Results:**

| Metric | Value |
|:-------|------:|
| CT price collapse | ~$80 → ~$0.50 (−99%) |
| Short profit | +$507M |
| Dump loss | −$96M |
| **Net PnL** | **+$411M** |

**Analysis:** The dump cost remains approximately constant (the slippage saturates once the peg is decisively broken). But the short profit scales linearly with position size. With 3× the short exposure of Experiment 2, the attacker achieves 6× the net profit.

This is the core asymmetry: the attack has a **fixed cost** (break the peg) and a **variable upside** (capture the collapse with leverage).

---

## Sensitivity Analysis

To generalize beyond single runs, we conducted a parameter sweep across two dimensions:

- **X-axis:** Stablecoin dump size (trigger capital)
- **Y-axis:** CT short size (capture leverage)

The resulting heatmap reveals the **profitability frontier**:

![PnL Sensitivity Heatmap](images/pnl_heatmap.png)

**Key observations:**

1. **The Loss Zone (bottom region):** Small short positions cannot overcome the dump cost. The attacker loses money regardless of trigger size.

2. **The Breakeven Line:** A diagonal threshold separates profitable from unprofitable configurations. Below this line, shorting merely offsets losses; above it, profits scale with leverage.

3. **The Profit Zone (top region):** Net PnL scales linearly with short size while trigger cost saturates. The limiting factor is not capital to break the peg—it's liquidity to short the collateral.

**Strategic implication:** The attack's feasibility depends on **CT borrowing markets**. If an attacker cannot source sufficient short exposure, the attack fails even with unlimited trigger capital.

---

## Results Summary

| Experiment | Short Position | Net PnL | ROI |
|:-----------|---------------:|--------:|----:|
| Raw Dump | $0 | −$87M | — |
| Short + Dump | $300M | +$68M | 23% |
| Max Leverage | $1B | +$411M | 41% |

---

[← Back to Index](README.md) | [Previous: Framework ←](02_Framework.md) | [Next: Pool Sensitivity →](04_Pool_Sensitivity.md)
