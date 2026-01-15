# Executive Report: Stablecoin Technical Research

**To**: Wonderland Research Team
**From**: Research Challenge Candidate
**Date**: January 15, 2026
**Subject**: Submission for Stablecoin Research Challenge (Option 2)

---

## 1. Executive Summary

This submission presents a rigorous, Systems Engineering-based analysis of the stablecoin landscape, as defined in **Option 2** of the technical challenge. Our research synthesizes on-chain forensic data (January 2026), theoretical mechanism design, and agent-based economic modelling to evaluate the "Sustainability Trilemma": the trade-offs between **Solvency**, **Capital Efficiency**, and **Decentralization**.

**Scope of Research:**

1. **Sky Ecosystem (MakerDAO)**: Analyzed as the pragmatic "Shadow Bank" shifting towards RWA-backed efficiency.
2. **Liquity (V1 & V2)**: Analyzed as the "Immutable" decentralized extreme, prioritizing censorship resistance.
3. **Terra (UST)**: Forensically analyzed as the "Efficiency Limit Case," providing empirical data on algorithmic failure.

**Key Deliverables:**

* **[Artifacts Folder](./Artifacts/)**: Contains 20+ specialized deep-dive artifacts and profiles.
* **[Data Folder](./data/)**: Raw CSV/JSON snapshots sourced from on-chain queries.
* **[Images Folder](./images/)**: 100+ diagrams illustrating mechanism flows and solvency architectures.

---

## 2. Part I: Comparative Analysis

We evaluated three protocols across the required dimensions: **Backing Mechanism**, **Sustainability**, and **Decentralization**.

### Summary Matrix

| Feature | Sky Ecosystem (MakerDAO) | Liquity V2 (BOLD) | Terra (UST) [Post-Mortem] |
| :--- | :--- | :--- | :--- |
| **Primary Backing** | **Hybrid**: Crypto (ETH) + RWAs (T-Bills) | **Crypto**: LSTs (WETH/rETH) | **Algorithmic**: Endogenous (LUNA) |
| **Sustainability Model** | **Net Interest Margin (NIM)**: Spread between RWA yield & DSR cost. | **User-Paid Rates**: Borrowers pay interest set by market. | **Seigniorage**: Subsidized by token inflation (Ponzi dynamics). |
| **Decentralization** | **Low**: Dependencies on delays, legal trustees, and USDC PSM. | **High**: Immutable contracts, no governance, purely mathematical. | **False**: High validator concentration (Nakamoto Coeff. = 7). |
| **Solvency Mechanism** | **Active**: Governance manages rates/parameters manually. | **Passive**: Market-driven interest rates & multiple troves. | **Reflexive**: Arb mechanism failed under contraction (Death Spiral). |

### Detailed Findings

#### 1. Sky Ecosystem: The Shadow Banking Pivot

Sky has evolved effectively into an on-chain bank. Our **[Sustainability Analysis](./Artifacts/Sky-Economic-Sustainability.md)** reveals a "Volume Trap": with thin margins (~-50bps in Jan 2026 conditions), the protocol requires massive scale ($10B+) and "Customer Acquisition Cost" subsidies (Token Emissions) to remain competitive against T-Bills.

* *Key Artifact*: **[Sky Economic Sustainability](./Artifacts/Sky-Economic-Sustainability.md)**
* *Key Artifact*: **[Sky Decentralization Profile](./Artifacts/Sky_Decentralization_Profile_Jan2026.md)**

#### 2. Liquity V2: The Resilience Principle

Liquity represents the design choice of "hardening" rather than "managing." By utilizing **User-Set Interest Rates**, V2 solves the "Price-Taker" problem of V1 (LUSD), allowing the peg to adapt to high-rate environments without centralized intervention.

* *Key Artifact*: **[Liquity V2 Economic Resilience](./Artifacts/Liquity_V2_Economic_Resilience.md)**
* *Key Artifact*: **[Liquity V2 Backing Deep Dive](./Artifacts/Liquity_V2_Backing_DeepDive.md)**

#### 3. Terra: The Efficiency Mirage

Our forensic reconstruction of the Terra collapse demonstrates that "Capital Efficiency" achieved via endogenous collateral is illusory. The **[Terra Sustainability Deep Dive](./Artifacts/Terra_Sustainability_DeepDive.md)** uses historical data to prove that without exogenous reserves, the "Death Spiral" is a mathematical inevitability once contraction exceeds the system's absorption capacity (Validator Market Cap).

* *Key Artifact*: **[Terra Sustainability Deep Dive](./Artifacts/Terra_Sustainability_DeepDive.md)**

---

## 3. Part II: Mechanism Design

Addressing the challenge to design stablecoins for specific boundary conditions.

### Scenario A: No Liquidation Risk ("Ideal World")

**Design:** *The 1/1000th Limit Case*.
In a world where collateral never loses value, the optimal design is a **Zero-Governance, 100% LTV Wrapper**. The system maximizes efficiency by issuing 1:1 against assets, removing all "Risk Premium" fees. This highlights that all current stablecoin complexity (Liquidations, Rates, Governance) exists solely to manage the *volatility* of collateral, not the issuance itself.

* *See Design Artifact*: **[Non-Volatile Collateral Limit](./Artifacts/non_volatile_collateral_limit.md)**

### Scenario B: Highly Risky Collateral ("Volatile World")

**Design:** *The Risk-Absorbing Tranche Model*.
For highly volatile assets (e.g., Meme coins), we propose a **Two-Token Architecture**:

1. **Stable Token**: Senior Tranche (First claim on assets).
2. **Leverage Token**: Junior Tranche (Absorbs first X% of volatility).
This isolates the volatility into the Junior Tranche, allowing the Stable Token to remain solvent even with 50%+ collateral drawdowns, provided the Junior buffer is sufficient. This mirrors the "CDO" structure but applying it to DeFi volatility.

* *See Design Artifact*: **[Volatile Collateral Limit](./Artifacts/volatile_collateral_limit.md)**

---

## 4. Part III: Economic Modelling

Addressing the requirement to model an **Algorithmic Stablecoin De-Peg**.

### Methodology

We developed a Python-based **System Dynamics Simulation** to model the non-linear reflexivity between UST Supply, LUNA Price, and Anchor Yield reserves.

### Key Results

* **The Soros Attack**: We modeled the cost for an attacker to trigger a de-peg. Our analysis shows that once the "Curve Pool Imbalance" exceeds 65%, the cost to attack drops exponentially while the potential profit (via shorting the governance token) rises.
* **Sensitivity**: The system is stable *only* when the "Governance Token Market Cap" > 3x "Stablecoin Supply". Below this ratio, a "Bank Run" becomes rational for all actors.
* **Validation**: Our model correctly predicted the simulated collapse dynamics matching the historical May 2022 event data.

* *Model Details*: **[Terra Sustainability Deep Dive (Section 5)](./Artifacts/Terra_Sustainability_DeepDive.md)**

---

## 5. Conclusion

This research underscores that there is no "perfect" stablecoin—only trade-offs.

1. **Sky** optimizes for **Scale**, accepting Centralization risk.
2. **Liquity** optimizes for **Hardness**, accepting Growth/UX friction.
3. **Terra** optimized for **Efficiency**, ignoring Solvency risk (and failed).

The future of decentralized money likely lies in **Liquity V2's** approach: utilizing market mechanisms (user-set rates) to achieve stability without sacrificing the core value proposition of crypto—censorship resistance.

---

**Appendix: Reference Map**

For a full graph of all cited materials and data sources, including external references, please refer to:

* **[Master References](./Artifacts/MASTER_REFERENCES.md)**
