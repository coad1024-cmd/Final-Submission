# Part VI: Market Simulation - Gaussian vs Hawkes Process

## Hypothesis: The "Fat Tail" Risk

**Core Question:** Does the statistical model of market behavior impact the protocol's survivability?

**The Logic:**

- **Gaussian (Random Walk):** Buy/Sell orders are normally distributed. Large shocks are statistically impossible (e.g., a "3-sigma" event happens once every 370 days; a "6-sigma" event happens once every 1.5 million years).
- **Hawkes Process (Self-Exciting):** Volatility is "clumped". A large sell order increases the probability of *subsequent* sell orders. This models Panic, FOMO, and Liquidation Cascades.

**Prediction:** Under a Hawkes process, the protocol will fail spontaneously due to a "volatility explosion" even without a strategic attacker, whereas the Gaussian model will remain stable indefinitely.

---

## Experimental Design

We ran two simulations with identical starting conditions (~$18.5B Liquidity):

1. **Control (Gaussian):** Standard simulator configuration with random purchase generation.
2. **Treatment (Hawkes):** A self-exciting process where Intensity ($\lambda$) increases with recent volume and price deviations.

---

## Results

![Gaussian vs Hawkes Comparison](images/hawkes_vs_gaussian.png)

*Top: Stablecoin Price. Bottom: Trading Volume/Intensity.*

### Observations

1. **Gaussian Stability:** The blue line (Gaussian) oscillates gently around $1.00. The deviations are predictable and mean-reverting. The protocol absorbs the noise effortlessly.

2. **Hawkes Instability:** The red line (Hawkes) initially resembles the Gaussian line. However, around iteration 3,000, a small price drop triggers a feedback loop.
    - **Self-Excitation:** The initial drop causes "panic selling" (higher intensity).
    - **Liquidity Drain:** The increased volume drains the pool reserves.
    - **Crash:** The simulation **crashed** with `ValueError: Output reserve must be positive`. The protocol was drained to zero.

### Mathematical Insight

The Hawkes intensity function is defined as:

$$ \lambda(t) = \mu + \alpha \sum_{t_i < t} e^{-\beta(t - t_i)} $$

If $\alpha \ge 1$, the process becomes **supercritical** (explosive). In our simulation, we set $\alpha = 0.9$, which is ostensibly stable. However, we added a "Panic Multiplier" when price < 0.95.

This effectively pushed $\alpha > 1$ during the dip, causing a **Phase Transition** from stability to collapse.

### Strategic Implication

Most stablecoin risk models (including VaR) assume Gaussian distribution. They under-price tail risk by orders of magnitude.

**The "Black Swan" isn't an external event—it's an internal property of the market structure.**

A protocol that is "stable" under Gaussian assumptions (like Terra was for 2 years) can be structurally doomed under self-exciting conditions.

---

[← Back to Index](README.md) | [Previous: Curve vs Uniswap ←](05_Curve_Comparison.md) | [Next: Conclusions →](07_Conclusions.md)
