# Liquity V1 (LUSD): Backing Mechanism Profile (Pillar I)

**Authors**: Research Challenge Team
**Date**: January 2026
**Series**: Liquity Research Series (Part I - V1)
**Framework**: [General Backing Framework](./general_backing_framework.md)

---

## 1. Executive Verdict

**Status:** 🟢 **The Platinum Standard**

Liquity V1 is the "Hard Rock" of decentralized stablecoins. It represents the theoretical limit of **Immutable Solvency**. By accepting only Ether (ETH) as collateral and enforcing a rigid 110% Minimum Collateral Ratio (MCR) with **zero administrative keys**, it eliminates all counterparty and governance risks. Its solvency engine relies entirely on the **Stability Pool** (instant offset) and **Redistribution** (socialized debt), creating a system that is mathematically constrained to be solvent as long as the ETH price does not drop faster than the liquidation speed ([Internal Research, 2026](#ref-general-framework)).

### The Solvency Lens

* **Kinetic Solvency (Physics):** **Rapid**. The Stability Pool provides atomic, instant liquidations without the need for auctions.
* **Static Solvency (Assets):** **Pristine**. 100% ETH backed. No "Legal Fictions" (RWA) or "Casinos" (Altcoins).

---

## 2. Backing Scorecard (Pillar I)

| Dimension | Score (0-10) | Status | Key Driver |
| :--- | :--- | :--- | :--- |
| **Asset Quality** | **10/10** | 🟢 **Pristine** | **ETH Only.** No USDC, no wBTC, no Governance Tokens. |
| **Custody Risk** | **10/10** | 🟢 **Trustless** | **Immutable Smart Contracts.** No admin keys. No upgradeability. |
| **Engine Speed** | **9/10** | 🟢 **Atomic** | **Stability Pool** allows instant debt offset. No auction delay. Gas efficient. |
| **Redemption LCR** | **10/10** | 🟢 **Hard Peg** | **Direct Redemption.** User can swap 1 LUSD for $1 of ETH at any time (minus fee). |

---

## 3. Evidence Classification

### 3.1 Verified Facts (Type A)

* **F1 (Immutable):** The contracts are non-upgradeable. No governance vote can change the MCR or seize funds.
* **F2 (Hard Peg):** The `redeemCollateral()` function guarantees \$1 parity (\$1 LUSD -> \$1 ETH) regardless of market price.
* **F3 (Stability Pool):** Verified mechanism where LUSD holders act as "First Responders" to absorb bad debt instantly.

### 3.2 Risk Scenarios (Type D)

* **Scenario A (The Flash Crash):** ETH drops 50% in 1 block.
  * *Result:* Stability Pool drains. Redistribution passes bad debt to all other troves.
  * *Defense:* **Recovery Mode** kicks in at 150% TCR, blocking risky transactions and allowing liquidations up to 150%.
* **Scenario B (Oracle Failure):** Chainlink ETH feed freezes.
  * *Result:* Price blind.
  * *Defense:* **Dual Oracle System**. Falls back to Tellor if Chainlink freezes or deviates >50%. If both fail, the system essentially freezes (safely) until data resumes.

---

## 4. Conclusion

* **Is it backed?** Yes. Over-collateralized by the most liquid decentralized asset (ETH).
* **Can you redeem it?** Yes. Anytime. The protocol *is* the market maker of last resort.
* **Is it safe?** It is the safest stablecoin design possible on Ethereum today, trading efficiency (capital) for security.

---

### Series Navigation

* **Part I: Backing Profile (V1)** (You are here)
* [Part II: V1 Backing Deep Dive](./Liquity_V1_Backing_DeepDive.md)
* [Part III: V1 Sustainability Profile](./Liquity_V1_Sustainability_Profile.md)
* [Part IV: V1 Decentralization Profile](./Liquity_V1_Decentralization_Profile.md)
* [Comparison: V2 Backing Profile](./Liquity_V2_Backing_Profile.md)

---

## References

<span id="ref-liquity-v1-docs"></span>Liquity. (2021). *[Liquity V1 Documentation](https://docs.liquity.org/)*. Project Documentation.

<span id="ref-general-framework"></span>Internal Research. (2026). *[General Backing Framework](./general_backing_framework.md)*. Canonical Methodology.
