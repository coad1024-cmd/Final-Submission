# When Price Stood Still: Designing the Non-Volatile Stablecoin

*Price stability is the easy part. Delivery is where systems fail.*

## Introduction: The Zero-Volatility Thesis

What happens if we assume the market price of a reserve asset never moves? Consider a theoretical limit case where reserve volatility is exactly zero ($\sigma^2 = 0$). In this world, the foundational problem of algorithmic stablecoins—maintaining a peg against closing prices—vanishes. The solvency constraint ($C_t P_t \ge D_t$) simplifies to a trivial identity: $C_t \ge D_t$. If you hold the nominal reserves, you are solvent.

Yet, history suggests that even if a stablecoin held perfectly stable assets—like tokenized T-Bills or fiat deposits—it could still fail. It wouldn't fail from price collapse; it would fail from **delivery risk**.

When market risk is removed, the binding constraints shift. The engineering challenge transitions from financial engineering (managing collateral ratios) to systems engineering (guaranteeing legal and technical delivery). This article explores the architecture of a stablecoin designed not to survive price volatility, but to survive the much more insidious risks of custody, settlement, and operations.

## The Risk Shift: From Volatility to Basel III

In traditional finance, the Basel III framework categorizes risks to ensure bank solvency. Applied to our $\sigma^2 = 0$ stablecoin, we see a clear taxonomy emerge. With market risk eliminated by assumption, we are left with four distinct enemies: **Credt Risk**, **Counterparty Risk**, **Operational Risk**, and **Liquidity Risk**.

### 1. Credit Risk: The Solvency Invariant

Credit risk in this context is the potential for the custodian holding the reserves to default. Even if the asset (e.g., a T-Bill) is risk-free, the *holder* of that asset is not.

To mitigate this, we define the **Solvency Invariant**:

$$ \text{PoR}_t \ge D_t $$

Where $\text{PoR}_t$ is the Proof of Reserve attested by the custodian, and $D_t$ is the total on-chain supply. This invariant demands that the system cannot mint a single token unless a cryptographic proof exists that the backing assets are legally held. If the invariant is violated—if an attestation fails or goes stale—the system must halt minting immediately. It is a hard stop. The code simply refuses to expand liability without proof of asset possession.

### 2. Counterparty Risk: The Diversification Invariant

If a single custodian holds 100% of the reserves, the system has a single point of failure (SPOF). A regulatory seizure, a hack, or an insider attack at that one entity brings the entire network down.

We address this with the **Diversification Invariant**:

$$ \text{MaxExposure}_i \le \frac{C_t}{n}(1 + \epsilon) $$

Here, $n$ is the number of custodians (minimum 3), and $\epsilon$ is a small tolerance. This rule forces the system to split reserves across multiple, legally distinct jurisdictions. If one custodian becomes "impaired" (unreachable or seized), the system isolates that 33% (for $n=3$) and allows users to redeem pro-rata from the remaining healthy custodians. The network protects itself from the failure of any single node in the physical world.

### 3. Operational Risk: The Immutability Invariant

Operational risk covers the "human element"—bugs, bad governance, admin key compromises, and rug pulls. In most protocols, this is the hardest risk to quantify.

Our design eliminates this by enforcing the **Immutability Invariant**:

$$ \frac{\partial \text{Logic}}{\partial t} = 0 $$

The protocol's logic is frozen at deployment. There are no admin keys, no governance votes to change parameters, and no ability to "upgrade" the contract. Parameters like the redemption curve shape or custodian limits are hardcoded. While this renders the protocol inflexible, it also makes it incorruptible. No one can steal the reserves by voting to change the withdrawal logic. The machine simply runs.

### 4. Liquidity Risk: The Convex Redemption Curve

The final and most binding constraint is liquidity. Even if you have the reserves ($C_t \ge D_t$), you might not have them *available* on-chain right now. Settlement takes time (T+1), but blockchain users demand instant execution.

If everyone tries to redeem at once, an "instant liquidity" crisis occurs. To solve this without freezing withdrawals, we implement a **Convex Redemption Curve**.

Instead of a fixed $1.00 price, redemptions are priced dynamically based on congestion:

$$ P_{\text{redeem}} = \max\left(1 - k \cdot \left(\frac{Q_t}{L_t}\right)^n, \, P_{\min}\right) $$

where $Q_t$ is the recent demand and $L_t$ is the liquid reserve. As demand spiked, the redemption price drops. This creates a "soft brake" on bank runs. Panic redeemers pay a penalty (slippage), while patient holders are incentivized to buy the discounted tokens and wait for the custodians to replenish the on-chain liquidity (T+1). This effectively acts as congestion pricing for the blockchain-to-banking bridge.

## Conclusion

By stripping away price volatility, we exposed the stark reality of stablecoin engineering: the hardest problems are not about financial markets, but about **trust** and **delivery**.

The Non-Volatile design doesn't promise to hold a peg perfectly during a panic. Instead, it promises something more valuable: **guaranteed execution**. Through strict invariants on solvency, diversification, and immutability, and a congestion-based pricing model for liquidity, it ensures that users can always exit—if they are willing to pay the price of immediacy—and that the system itself cannot be broken by the failure of any single human or institution.
