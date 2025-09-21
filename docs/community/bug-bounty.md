
# Account Abstraction Bug Bounty

## Details of the Ethereum Foundation's bug bounty program for Account Abstraction.


The Ethereum Foundation (EF) launched a dedicated bug bounty program in **September 2024** to help secure the Account Abstraction (ERC-4337) ecosystem. The program is hosted on [HackenProof](https://hackenproof.com/programs/account-abstraction-bugs) and offers rewards of up to **$250,000** for critical vulnerabilities.

---

## 🎯 Scope and Goals

The bounty program encourages security researchers to:

- Identify vulnerabilities in the ERC-4337 and ERC-7562 specs
- Find bugs in the reference implementation
- Help prevent denial-of-service and validation bypass exploits

---

## 🔍 In-Scope Targets

- [ERC-4337 Specification](https://github.com/ethereum/ercs/blob/master/ERCS/erc-4337.md)
- [ERC-7562 Specification](https://github.com/ethereum/ercs/blob/master/ERCS/erc-7562.md)
- [Reference Implementation](https://github.com/eth-infinitism/account-abstraction) (core and utils directories)

🚨 Only versions **v0.6.0**, **v0.7.0**, and **v0.8.0** are eligible for rewards.

---

## 🧪 Focus Areas

- Critical validation flaws
- Inconsistencies in simulation vs on-chain behavior
- Gas griefing or refund abuse
- Low-cost attack vectors to ban staked actors

---

## 💰 Reward Tiers

| Severity  | Reward Range         | Examples |
|-----------|----------------------|----------|
| Critical  | $100,000 – $250,000 | Bypass validation, steal deposits |
| High      | $25,000 – $50,000   | DoS a bundle post-validation |
| Medium    | $5,000 – $10,000    | Mempool attack not covered by 7562 |
| Low       | $1,000 – $2,000     | Minor overpayment bugs |

---

## ⛔ Out of Scope

- Attacks on specific implementation of bundlers or paymasters
- Network-level DoS (e.g. flooding peers)
- General libp2p vulnerabilities

---

## 📋 Rules

- Submit reproducible reports through HackenProof
- Testing must avoid harming live deployments
- KYC required for reward disbursement
- First reporter wins — no duplicate rewards
- Public disclosure requires EF approval

---

## 🕒 Timelines

- Response: Within 3 business days
- Triage: 14 business days
- Reward: 14 business days
- Fix: Within 90 business days

---

For full terms and submission portal, visit:
👉 [Account Abstraction Bug Bounty on HackenProof](https://hackenproof.com/programs/account-abstraction-bugs)

---

## ✅ Summary

The bug bounty protects the ERC-4337 ecosystem at the infrastructure level. With high rewards and focused targets, it invites researchers to help harden smart wallet safety and simulation integrity.
