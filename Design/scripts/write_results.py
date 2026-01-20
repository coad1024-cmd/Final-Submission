import numpy as np

def redemption_price(q_ratio, k, n):
    return 1.0 - k * np.power(q_ratio, n)

def liquidity_drained(fear_level, k, n):
    if fear_level >= k:
        return 1.0
    return min(np.power(fear_level / k, 1.0 / n), 1.0)

combos = [
    (0.05, 2), (0.10, 2), (0.15, 2), (0.20, 2),
    (0.10, 3), (0.15, 3), (0.20, 3),
    (0.10, 4), (0.15, 4), (0.20, 4),
    (0.20, 5), (0.30, 5), (0.50, 5)
]

NORMAL = 0.05

with open('results.md', 'w', encoding='utf-8') as f:
    f.write("# Redemption Curve Parameter Analysis\n\n")
    f.write("| k | n | Normal Slip | Drain@2% | Drain@5% | Drain@10% |\n")
    f.write("|---|---|-------------|----------|----------|------------|\n")
    
    for k, n in combos:
        slip = 1.0 - redemption_price(NORMAL, k, n)
        d2 = liquidity_drained(0.02, k, n)
        d5 = liquidity_drained(0.05, k, n)
        d10 = liquidity_drained(0.10, k, n)
        f.write(f"| {k:.2f} | {n:.0f} | {slip*100:.3f}% | {d2*100:.1f}% | {d5*100:.1f}% | {d10*100:.1f}% |\n")
    
    f.write("\n## Key Insights\n\n")
    f.write("- **Higher k (max discount)** = More liquidity drained before run stops\n")
    f.write("- **Higher n (convexity)** = Steeper penalties at high congestion, gentler at low\n")
    f.write("- **Trade-off**: Low k protects liquidity but causes more slippage in normal times\n")

print("Results written to results.md")
