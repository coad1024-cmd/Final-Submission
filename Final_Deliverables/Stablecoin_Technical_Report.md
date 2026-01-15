# Stablecoin Technical Report: The Solvency-Efficiency Frontier

**Version**: 1.5 (Final)
**Date**: January 15, 2026

---

## 1. Introduction: The Sustainability Trilemma

The fundamental problem of stablecoin engineering is that **Solvency**, **Capital Efficiency**, and **Decentralization** cannot be simultaneously maximized. A protocol must choose two, or accept significant compromise.

This report tells the story of how four major protocols—**Sky (MakerDAO)**, **Liquity V1**, **Liquity V2**, and **Terra (UST)**—navigated this trilemma, representing the full spectrum of architectural choices.

---

## 2. Sky Ecosystem: The Evolution into Shadow Banking

The story of MakerDAO (now Sky) is one of a **structural yield pivot**. In the early "DeFi Summer" era (2020-2022), the protocol earned massive revenues from volatility. Users were willing to pay 5-10% fees to leverage long ETH positions. The surplus buffer grew rapidly, funded by this volatility tax.

However, as crypto yields compressed in 2023-2024, Sky faced a "Volume Trap." To maintain its peg and attract TVL, it had to offer a **Dai Savings Rate (DSR)** that competed with external risk-free rates (US Treasuries). This forced the protocol to pivot its backing from crypto-native assets to **Real World Assets (RWAs)**.

### The Mechanism of Centralization

This pivot was not merely a portfolio rebalancing; it was an override of the protocol's trust assumptions.

* **The RWA Adapter**: Unlike `Join` adapters for ETH which are atomic, RWA adapters rely on legal trustees. If a T-Bill custodian freezes assets, the on-chain `Vat` cannot liquidate them.
* **The Negative Margin**: In Jan 2026, with DSR at ~5.5% (driven by competition) and T-Bills at ~5.0%, the protocol holds a negative Net Interest Margin (NIM) on its core book.

*(See Artifacts: [Sky Economic Sustainability](./Artifacts/Sky-Economic-Sustainability.md), [Sky Backing](./Artifacts/Sky_Backing_Profile_Jan2026.md))*

---

## 3. Liquity V1 (LUSD): The Static Baseline

Before V2, Liquity V1 established the "Baseline" for decentralized stablecoins. It prioritized **Immutability** above all.

### The Mechanism of Hardness

* **0% Interest Rate**: The protocol charged a one-time borrowing fee (0.5% - 5%) rather than continuous interest.
* **Hard Peg via Redemption**: Any holder could exchange 1 LUSD for $1 of ETH from the lowest-collateral Trove. This created a hard price floor at $1.00 - (Fee).
* **Immutable Contracts**: No governance keys. No ability to upgrade.

### The Limitation

V1 thrived in low-rate environments. However, when global risk-free rates rose to 5% (2023-2026), LUSD struggled. Because it paid 0% yield and cost 0% interest, it had no mechanism to incentivize holding demand when competitors offered 5%. It traded often below peg, relying entirely on the "Hard Floor" of redemption arbitrage. This proved that **Static Parameters cannot survive Dynamic Markets**.

*(See Artifacts: [Liquity V1 Sustainability](./Artifacts/Liquity_V1_Sustainability_Profile.md))*

---

## 4. Liquity V2 (BOLD): The Immutable Controller

Liquity V2 represents the evolution of the "Physics" approach. It retains the permissionless nature of V1 but solves the "Static Parameter" problem using **Market Dynamics**.

### The V2 Solution: User-Set Rates

Instead of a Governance DAO voting on interest rates (as Sky does):

1. **Borrowers set their own rates** via the `TroveManager`.
2. **The Redistribution Market**: When the system needs to contract (Redemption), it targets the borrowers paying the *lowest* interest rates first.

The rate thus becomes a **Protection Premium**. Users pay the market rate not because a DAO forces them, but to protect their positions from "premature redemption." This utilizes **Control Theory**—the "error signal" (peg deviation) is corrected by decentralized agents acting in their own self-interest.

*(See Artifacts: [Liquity V2 Backing](./Artifacts/Liquity_V2_Backing_Profile.md), [Economic Resilience](./Artifacts/Liquity_V2_Economic_Resilience.md))*

---

## 5. Terra (UST): The Algorithm that Failed

Terra attempted to cheat the Trilemma. It offered **High Efficiency** (no collateral required) and **Decentralization** (no custodians) by claiming "Endogenous Backing."

### The Reflexivity Trap

The system relied on the **Virtual Liquidity Pool (VLP)** concept: the idea that \$1 of LUNA could always be minted to absorb \$1 of UST selling pressure.
Our forensic modeling shows why this failed mathematically. The stability of the system relies on the assumption:
$$ \text{MarketCap}_{LUNA} > \text{Supply}_{UST} + \text{PanicBuffer} $$

As UST supply grew, it effectively leveraged the LUNA market cap. When the "Soros Attack" triggered a de-peg:

1. **The Bank Run**: Users rushed to exit UST used the `MarketModule` to mint LUNA.
2. **Hyperinflation**: The minting expanded LUNA supply exponentially.
3. **Value Collapse**: LUNA price collapsed faster than supply could expand, reducing the total backing value.

*(See Artifact: [Terra Sustainability and Attack Model](./Artifacts/Terra_Sustainability_DeepDive.md))*

---

## 6. Design Analysis: Solving the Boundary Conditions

The Challenge asked for designs in two extreme "Worlds." Here is how we apply our research findings to solve them.

### World A: The "Non-Volatile" World

**Premise**: Collateral never loses value (e.g., Tokenized Gold, CBDC).
**Solution: The Atomic Wrapper**
In this world, concepts like "Liquidations" or "Stability Pools" are waste. If $S(t) \equiv C(t)$ (Value is constant), the optimal design is a simple wrapper contract. It mints 1:1 and redeems 1:1.

* **Result**: 100% Capital Efficiency. 0% Interest.
* **Insight**: This proves that 99% of DeFi complexity exists solely to manage the *volatility risk* of collateral.

### World B: The "High Volatility" World

**Premise**: Collateral is highly volatile (Meme Coins).
**Solution: The Dual-Tranche "CDO"**
A standard stablecoin cannot survive a 50% drop. We must separate the token into risk tranches:

1. **Senior Token (Stable)**: Has the *first claim* on the underlying assets.
2. **Junior Token (Leverage)**: Has the *last claim*.

If the collateral drops 40%, the Junior Token takes a 100% loss, but the Senior Token remains fully backed (1.00 USD). We replace "Liquidating the User" with "Liquidating the Tranche."

* **Mechanism**: A `rebalance()` function auctions off the Junior tranche position to recapitalize the system whenever the buffer thins, protecting the Senior users at all costs.

---

## 7. Modelling: The Economics of Attack

We simulated a "Bear Raid" on an Algorithmic Stablecoin to define the precise cost of malice.

**The Equation of Profitability**:
$$ \Pi_{profit} \approx \left[ \text{ShortSize} \times (P_{start} - P_{end}) \right] - \left[ \text{AttackVolume} \times \text{Slippage}(Imbalance) \right] $$

Our simulation reveals a specific **tipping point**:
When the Governance Token Market Cap falls below **150%** of the Stablecoin Supply, the slippage cost to force a de-peg becomes lower than the profit from shorting the governance token.

At this ratio, the system is **Integrally Unstable**. It is rational for even "honest" whales to attack the system to front-run the inevitable collapse. This suggests that "Algorithmic" stablecoins require a massive over-collateralization of "Trust" (Market Cap) relative to "Debt" (Stablecoin Supply) to remain viable.

---

## 8. Conclusion

The "Stablecoin Wars" have settled into a clear spectrum:

* **Sky** has won the war for **Scale** by integrating with the traditional banking system. It is a robust, pragmatic, but centralized product.
* **Liquity** has won the war for **Resilience** by removing human governance. It is the closest we have to "Digital Gold Standard" banking.
* **Terra** remains the gravestone warning that **Efficiency** cannot be counterfeited by algorithms.

For a senior developer building the next generation, the lesson is clear: **Do not try to remove the collateral.** You can manage it (Sky) or you can automate it (Liquity), but you cannot algorithmically replace it.
