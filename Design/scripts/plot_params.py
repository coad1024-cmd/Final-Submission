import matplotlib.pyplot as plt
import numpy as np

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# --- Subplot 1: Redemption Price vs Congestion for different (k, n) ---
q_ratio = np.linspace(0, 1, 100)

params = [
    (0.10, 2, 'k=0.10, n=2 (current)', 'blue', '-'),
    (0.20, 2, 'k=0.20, n=2 (recommended)', 'green', '-'),
    (0.20, 5, 'k=0.20, n=5', 'orange', '--'),
    (0.50, 5, 'k=0.50, n=5', 'red', '--'),
]

for k, n, label, color, style in params:
    price = 1 - k * np.power(q_ratio, n)
    ax1.plot(q_ratio * 100, price, label=label, color=color, linestyle=style, linewidth=2)

ax1.axhline(y=0.90, color='gray', linestyle=':', alpha=0.7, label='Floor (90%)')
ax1.set_xlabel('Congestion (Q/L %)', fontsize=12)
ax1.set_ylabel('Redemption Price', fontsize=12)
ax1.set_title('Redemption Curve Shape by Parameters', fontsize=14)
ax1.legend(loc='lower left')
ax1.set_xlim(0, 100)
ax1.set_ylim(0.85, 1.01)
ax1.grid(True, alpha=0.3)

# --- Subplot 2: Liquidity Drained vs Fear Level ---
fear_levels = np.linspace(0.01, 0.15, 50)

def drain_pct(fear, k, n):
    if fear >= k:
        return 1.0
    return min((fear / k) ** (1/n), 1.0)

for k, n, label, color, style in params:
    drain = [drain_pct(f, k, n) for f in fear_levels]
    ax2.plot(fear_levels * 100, [d * 100 for d in drain], label=label, color=color, linestyle=style, linewidth=2)

ax2.set_xlabel('Fear Level (%)', fontsize=12)
ax2.set_ylabel('Liquidity Drained Before Run Stops (%)', fontsize=12)
ax2.set_title('Run Dampening: Lower is Better', fontsize=14)
ax2.legend(loc='upper left')
ax2.set_xlim(0, 15)
ax2.set_ylim(0, 105)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('parameter_analysis.png', dpi=150, bbox_inches='tight')
print("Saved to parameter_analysis.png")
