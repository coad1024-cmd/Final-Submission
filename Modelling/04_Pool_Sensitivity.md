# Part IV: Pool Size Sensitivity Analysis

## Hypothesis: Liquidity as Defense

**Core Question:** Does deeper pool liquidity protect against profitable attacks?

The hypothesis is that:

- **Deeper pools** increase the trigger cost (more slippage to break the peg)
- **Shallow pools** decrease the trigger cost (easier to de-peg)
- The **capture mechanism** (short profit) remains constant regardless of pool depth

If true, there exists a **critical liquidity threshold** below which attacks become profitable.

---

## Experimental Design

We vary pool liquidity across five configurations:

| Scenario | Pool Multiplier | AS/USD TVL | CT/USD TVL |
|:---------|:---------------:|-----------:|-----------:|
| Very Shallow | 0.25× | $4.6B | $6.9B |
| Shallow | 0.5× | $9.25B | $13.8B |
| **Baseline** | **1×** | **$18.5B** | **$27.6B** |
| Deep | 2× | $37B | $55.2B |
| Very Deep | 5× | $92.5B | $138B |

**Control variables:**

- Attack parameters: 500M AS dump, $300M CT short
- Attack timing: Iteration 150,000
- Behavioral parameters: Unchanged

**Measured outcomes:**

- Trigger cost (slippage on AS dump)
- CT price collapse magnitude
- Net attacker PnL

---

## Experimental Setup

The experiment script (`run_pool_sensitivity.py`) systematically varies pool liquidity:

```python
POOL_MULTIPLIERS = [0.25, 0.5, 1.0, 2.0, 5.0]

# Base parameters (1× scenario)
BASE_AS_POOL = 9.25e9       # 9.25B AS
BASE_USD_POOL = 9.25e9      # $9.25B USD
BASE_CT_POOL = 172.7e6      # 172.7M CT
BASE_CT_USD_POOL = 13.8e9   # $13.8B USD

for multiplier in POOL_MULTIPLIERS:
    # Scale pool liquidity
    as_pool_qty = BASE_AS_POOL * multiplier
    usd_pool_qty = BASE_USD_POOL * multiplier
    ct_pool_qty = BASE_CT_POOL * multiplier
    ct_usd_pool_qty = BASE_CT_USD_POOL * multiplier
    
    # Run simulation with scaled parameters
    results = run_attack_simulation(
        as_pool_qty, usd_pool_qty, ct_pool_qty, ct_usd_pool_qty,
        attack_amount=500e6,
        short_amount=300e6
    )
    
    record_results(multiplier, results)
```

---

## Expected Results

Based on AMM mechanics, we expect:

### Trigger Cost Scaling

Slippage in constant-product AMMs scales approximately as:

$$\text{Slippage} \propto \frac{\text{Trade Size}}{\sqrt{k}}$$

Where $k = x \cdot y$ is the pool constant. Doubling pool depth should reduce slippage by ~30%.

### Death Spiral Dynamics

The death spiral is *scale-invariant* once triggered—arbitrage percentages remain constant. A 10% de-peg triggers arbitrage regardless of absolute pool size.

### Predicted Profitability Frontier

| Liquidity | Trigger Cost | Short Profit | Net PnL | Profitable? |
|:---------:|-------------:|-------------:|--------:|:-----------:|
| 0.25× | Low (~$45M) | +$150M | +$105M | ✅ Yes |
| 0.5× | Moderate (~$65M) | +$155M | +$90M | ✅ Yes |
| 1× | Baseline (~$89M) | +$157M | +$68M | ✅ Yes |
| 2× | High (~$120M) | +$160M | +$40M | ✅ Marginal |
| 5× | Very High (~$200M) | +$165M | −$35M | ❌ No |

---

## Running the Experiment

```bash
cd pipeline/simulations/Algo-Attack-Model/DualTokenSim

# Run pool sensitivity sweep
python -m source.simulations.simulation_runners.run_pool_sensitivity

# Outputs saved to:
# - sensitivity_analysis_results/pool_sensitivity/results.csv
# - sensitivity_analysis_results/pool_sensitivity/pnl_vs_liquidity.png
```

---

## Results

The simulation reveals a **counterintuitive finding**: shallow pools are actually *worse* for the attacker, not better.

![Attack Profitability vs Pool Depth](images/pnl_vs_liquidity.png)

*Left: Trigger cost (red) vs short profit (green) by pool depth. Right: Net PnL across liquidity scenarios.*

### Experimental Results

| Multiplier | AS/USD TVL | Trigger Cost | Short Profit | Net PnL | CT Final Price |
|:----------:|-----------:|-------------:|-------------:|--------:|---------------:|
| 0.25× | $4.6B | $117M | $80M | −$37M | $58.67 |
| 0.5× | $9.25B | $62M | $36M | −$26M | $70.49 |
| 1× | $18.5B | $32M | $17M | −$15M | $75.49 |
| 2× | $37B | $17M | $8M | −$10M | $77.94 |
| 5× | $92.5B | $9M | $3M | −$6M | $79.30 |

### Analysis

**The paradox:** Shallow pools *increase* the attack's trigger cost rather than decreasing it.

This occurs because:

1. **Slippage scales inversely with liquidity** - A 500M AS dump into a \$4.6B pool incurs ~10% slippage; into a $92.5B pool, only ~0.5%

2. **Price impact is proportional to pool size** - The constant-product formula means the same dump moves smaller pools more, creating immediate loss

3. **Death spiral is muted in shallow pools** - With less arbitrage capital flowing through small pools, the reflexive loop runs slower

**The implication:** Liquidity is a double-edged sword. Deeper pools reduce the attacker's slippage (good for attacker) but also resist the death spiral (bad for attacker). The optimal attack liquidity is *moderate*—enough to execute without excessive slippage, but not so deep that the system resists collapse.

> [!NOTE]
> These results are based on a reduced iteration count (10,000) for speed. Full-length simulations (200,000+ iterations) would allow the death spiral more time to propagate, potentially changing the profitability frontier.

---

[← Back to Index](README.md) | [Previous: Experiments ←](03_Experiments.md) | [Next: Conclusions →](05_Conclusions.md)
