# Redemption Curve Parameter Analysis

| k | n | Normal Slip | Drain@2% | Drain@5% | Drain@10% |
|---|---|-------------|----------|----------|------------|
| 0.05 | 2 | 0.013% | 63.2% | 100.0% | 100.0% |
| 0.10 | 2 | 0.025% | 44.7% | 70.7% | 100.0% |
| 0.15 | 2 | 0.038% | 36.5% | 57.7% | 81.6% |
| 0.20 | 2 | 0.050% | 31.6% | 50.0% | 70.7% |
| 0.10 | 3 | 0.001% | 58.5% | 79.4% | 100.0% |
| 0.15 | 3 | 0.002% | 51.1% | 69.3% | 87.4% |
| 0.20 | 3 | 0.003% | 46.4% | 63.0% | 79.4% |
| 0.10 | 4 | 0.000% | 66.9% | 84.1% | 100.0% |
| 0.15 | 4 | 0.000% | 60.4% | 76.0% | 90.4% |
| 0.20 | 4 | 0.000% | 56.2% | 70.7% | 84.1% |
| 0.20 | 5 | 0.000% | 63.1% | 75.8% | 87.1% |
| 0.30 | 5 | 0.000% | 58.2% | 69.9% | 80.3% |
| 0.50 | 5 | 0.000% | 52.5% | 63.1% | 72.5% |

## Key Insights

- **Higher k (max discount)** = More liquidity drained before run stops
- **Higher n (convexity)** = Steeper penalties at high congestion, gentler at low
- **Trade-off**: Low k protects liquidity but causes more slippage in normal times
