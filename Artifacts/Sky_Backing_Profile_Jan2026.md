# Sky Ecosystem (MakerDAO): Backing Profile

**Date:** January 5, 2026
**Framework Version:** 1.0 (Kinetic Solvency Framework)
**Status:** 🟡 **Structurally Robust / Politically Fragile**

---

## 1. Backing Scorecard

| Dimension | Score (0-10) | Status | Key Driver |
|:---|:---|:---|:---|
| **Asset Quality (A)** | **8/10** | 🟢 **Liquid** | 60% HQLA (Treasuries/USDC). 40% Crypto (ETH). Zero Gov Token backing. |
| **Custody Risk (C)** | **2/10** | 🔴 **Critical** | **42%** exposure to Circle/Coinbase ([Decentralization Profile §2.2](./Sky_Decentralization_Profile_Jan2026.md)). |
| **Engine Speed (E)** | **9/10** | 🟢 **Atomic** | Flash Loan native. Keeper HHI 0.11 ([Decentralization Profile §2.3](./Sky_Decentralization_Profile_Jan2026.md)). |
| **Redemption (R)** | **9/10** | 🟢 **Robust** | **$3.99B** in PSM Pocket for instant 1:1 exit ([Sustainability Profile F5](./Sky_Sustainability_Profile_Jan2026.md)). |

### Composite Verdict

* **Kinetic Solvency (Physics):** **9.0/10**. The "Machine" is state-of-the-art.
* **Static Solvency (Assets):** **5.0/10**. The "Portfolio" is essentially a regulated bank.
* **Final Classification:** **Robust Engine / Fragile Assets**

> **Verdict:** Sky's "Kinetic Engine" (Liquidation 2.0) has solved the mechanical congestion issues of 2020. However, the system has traded **Throughput Risk** for **Censorship Risk**. It is mechanistically bulletproof but legally vulnerable.

---

## 2. Dimension Analysis

### 2.1 Asset Quality & Custody ( The "Static" View)

* **RWA Dominance:** ~68% of backing is Real World Assets / Treasuries.
* **Counterparty Cliff:** 42% of all backing is held by a single entity (Circle/Coinbase).
* **Implication:** The system is solvent *if and only if* the US Legal System enforces property rights.

### 2.2 Kinetic Engine (The "Dynamic" View)

* **Mechanism:** Dutch Auction (`Clip`) with Flash Loan settlement (`take()`).
* **Speed:** Atomic. Liquidators need **$0 balance sheet**.
* **Throughput:** Validated. Unlike 2020 (English Auctions), "Zero Bids" are game-theoretically impossible as price approaches zero.
* **Keepers:** Highly competitive execution market (HHI 0.11).

### 2.3 Financial Resilience (The Backstop)

* **Surplus Buffer:** **$247M** (Facts F6). Provides a first-loss cushion.
* **MKR/SKY Dilution:** Infinite theoretic backstop, but reliant on market confidence in the governance token.

---

## 3. Stress Test Results

### Test 1: Black Thursday Redux (Flash Crash)

* **Scenario:** ETH drops 50% in 1 hour. Gas spikes to 500 gwei.
* **Impact:** Massive wave of liquidations.
* **Result:** **pass.** Flash Loan liquidators clear debt instantly. No capital constraint.
* **Contrast:** In 2020, this failed ($5.67M Bad Debt). Today, it is a routine operational event.

### Test 2: The "Freeze" (Regulatory Shock)

* **Scenario:** OFAC sanctions the RWA/USDC vaults.
* **Impact:** **42% of backing vanishes** ($4B+ loss).
* **Result:** **Insolvency.** Surplus buffer ($247M) is wiped out instantly.
* **Resilience:** ❌ **None.** The "Kinetic Engine" cannot auction frozen assets. The "Machine" works, but the "Fuel" is gone.

---

## 4. Conclusion & Recommendations

The Backing Mechanism has successfully evolved from "Beta" (2020) to "Production" (2026). The transition to Dutch Auctions and Flash Loans represents the **Gold Standard** for on-chain liquidation engines.

**Recommendations:**

1. **Maintain Surplus:** Ensure Surplus Buffer scales with RWA exposure (Target > 5% of Debt).
2. **OSM Defense:** Maintain the 1-hour delay despite the user friction; it is the only defense against Oracle Flash Crashes.
3. **Jurisdictional Diversification:** (Echoing Decentralization Profile) Split RWA custody across non-US/legal-distinct jurisdictions to mitigate "Single Stroke" seizure risk.

---

### Data Sources & References

* **Decentralization Profile:** [Sky_Decentralization_Profile_Jan2026.md](./Sky_Decentralization_Profile_Jan2026.md)
* **Sustainability Profile:** [Sky_Sustainability_Profile_Jan2026.md](./Sky_Sustainability_Profile_Jan2026.md)
* **Deep Dive:** [Sky_Backing_DeepDive.md](./Sky_Backing_DeepDive.md)
