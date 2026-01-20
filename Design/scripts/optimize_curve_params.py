import numpy as np
import pandas as pd

def redemption_price(q_ratio, k, n):
    """
    Calculates redemption price for a given congestion ratio Q/L.
    P = 1 - k * (Q/L)^n
    """
    return 1.0 - k * np.power(q_ratio, n)

def liquidity_drained(fear_level, k, n):
    """
    Calculates the % of liquidity drained before the run stops.
    Users STOP redeeming when Price <= (1 - Fear).
    1 - k * (Q/L)^n = 1 - Fear
    k * (Q/L)^n = Fear
    (Q/L)^n = Fear / k
    Q/L = (Fear / k)^(1/n)
    
    Returns 1.0 (100%) if the run never stops (i.e. if Fear > k).
    """
    if fear_level >= k:
        return 1.0
    
    drain_pct = np.power(fear_level / k, 1.0 / n)
    return min(drain_pct, 1.0)

def optimize_parameters():
    print("Optimization Analysis: Redemption Curve Parameters (k, n)")
    print("---------------------------------------------------------")
    print("Assumption: Users redeem if Price > (1 - FearLevel)")
    print("Objective:  Minimize Liquidity Drained for a given FearLevel")
    print("Constraint: Normal usage (5% liquidity) must have Slippage < 0.1% (Price > 0.999)\n")

    # Parameters to sweep
    k_values = np.linspace(0.05, 0.50, 46) # 5% to 50% max discount
    n_values = np.linspace(1.0, 20.0, 39)  # Convexity 1 to 20
    
    # Constraints
    NORMAL_USAGE_RATIO = 0.05
    MAX_NORMAL_SLIPPAGE = 0.001 # 10 basis points

    results = []

    for k in k_values:
        for n in n_values:
            # Check Constraint
            p_normal = redemption_price(NORMAL_USAGE_RATIO, k, n)
            slippage_normal = 1.0 - p_normal
            
            if slippage_normal > MAX_NORMAL_SLIPPAGE:
                continue # Valid constraint violation
            
            # Calculate Performance (Drained Liquidity) for different Fear Levels
            # Fear = perceived probability of insolvency (or expected haircut)
            
            # 2% Fear (Minor Panic)
            drain_02 = liquidity_drained(0.02, k, n)
            
            # 5% Fear (Moderate Panic)
            drain_05 = liquidity_drained(0.05, k, n)
            
            # 10% Fear (Serious Crisis)
            drain_10 = liquidity_drained(0.10, k, n)
            
            results.append({
                'k': k,
                'n': n,
                'Normal_Price': p_normal,
                'Drain_Fear_2%': drain_02,
                'Drain_Fear_5%': drain_05,
                'Drain_Fear_10%': drain_10
            })

    df = pd.DataFrame(results)
    
    # Ranking Logic: Weighted minimal drainage?
    # Let's find the pareto frontier or just sort by a composite score.
    # Score = Average Drained % across scenarios (Lower is better)
    
    df['Composite_Drain'] = (df['Drain_Fear_2%'] + df['Drain_Fear_5%'] + df['Drain_Fear_10%']) / 3.0
    
    # Sort by best performance
    df_sorted = df.sort_values(by='Composite_Drain')
    
    print("Top 10 Parameter Sets (Minimizing Liquidity Drain, subject to Normal Usage constraint):")
    print(df_sorted.head(10).to_string(index=False, float_format="%.4f"))
    
    print("\n\nAnalysis of Specific 'Standard' Choices:")
    standards = [(0.10, 2.0), (0.15, 2.0), (0.20, 2.0), (0.10, 4.0), (0.20, 5.0)]
    print(f"{'k':<6} {'n':<6} {'NormalPrice':<12} {'Drain(F=2%)':<12} {'Drain(F=5%)':<12} {'Drain(F=10%)'}")
    print("-" * 70)
    for k, n in standards:
        p = redemption_price(NORMAL_USAGE_RATIO, k, n)
        d2 = liquidity_drained(0.02, k, n)
        d5 = liquidity_drained(0.05, k, n)
        d10 = liquidity_drained(0.10, k, n)
        print(f"{k:<6.2f} {n:<6.1f} {p:<12.5f} {d2:<12.2%} {d5:<12.2%} {d10:.2%}")

if __name__ == "__main__":
    optimize_parameters()
    
    # Also save full results to CSV
    import numpy as np
    import pandas as pd
    
    k_values = np.linspace(0.05, 0.50, 10)
    n_values = np.linspace(1.0, 10.0, 10)
    
    rows = []
    for k in k_values:
        for n in n_values:
            p_normal = 1.0 - k * (0.05 ** n)
            if 1.0 - p_normal > 0.001:
                continue
            d2 = min((0.02 / k) ** (1/n), 1.0) if 0.02 < k else 1.0
            d5 = min((0.05 / k) ** (1/n), 1.0) if 0.05 < k else 1.0
            d10 = min((0.10 / k) ** (1/n), 1.0) if 0.10 < k else 1.0
            rows.append({'k': k, 'n': n, 'NormalPrice': p_normal, 'Drain_2pct': d2, 'Drain_5pct': d5, 'Drain_10pct': d10})
    
    df = pd.DataFrame(rows)
    df['AvgDrain'] = (df['Drain_2pct'] + df['Drain_5pct'] + df['Drain_10pct']) / 3
    df = df.sort_values('AvgDrain')
    df.to_csv('curve_optimization.csv', index=False)
    print("Results saved to curve_optimization.csv")
