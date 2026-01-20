import numpy as np

def redemption_price(q_ratio, k, n):
    return 1.0 - k * np.power(q_ratio, n)

def liquidity_drained(fear_level, k, n):
    if fear_level >= k:
        return 1.0
    return min(np.power(fear_level / k, 1.0 / n), 1.0)

# Specific parameter combos to test
combos = [
    (0.05, 2), (0.10, 2), (0.15, 2), (0.20, 2),
    (0.10, 3), (0.15, 3), (0.20, 3),
    (0.10, 4), (0.15, 4), (0.20, 4),
    (0.20, 5), (0.30, 5), (0.50, 5)
]

NORMAL = 0.05  # 5% of liquidity used in normal conditions

print("k      n      NormalSlip   Drain@2%   Drain@5%   Drain@10%")
print("-" * 60)

for k, n in combos:
    slip = 1.0 - redemption_price(NORMAL, k, n)
    d2 = liquidity_drained(0.02, k, n)
    d5 = liquidity_drained(0.05, k, n)
    d10 = liquidity_drained(0.10, k, n)
    
    print(f"{k:.2f}   {n:.0f}      {slip*100:.3f}%       {d2*100:.1f}%       {d5*100:.1f}%       {d10*100:.1f}%")
