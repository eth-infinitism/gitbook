---
title: L2s
description: Why Layer 2s matter for smart accounts and account abstraction.
sidebar_position: 1
---

# ⛓️ L2s and Account Abstraction

Account Abstraction (AA) thrives on Layer 2s (L2s). Lower gas costs, faster finality, and upgrade flexibility make L2s the ideal environment for smart wallets to flourish.

This section explores how L2 infrastructure supports AA and what makes each chain unique in its approach.

---

## 🧠 Why L2s Matter

- Smart accounts often include extra gas overhead (e.g. validation logic, Paymasters)
- ERC-4337 is more affordable on L2s due to reduced transaction costs
- Many AA-first apps and wallets deploy to L2s before L1

L2s are not just cheaper — they are often **more AA-friendly**.

---

## 🔧 Infrastructure Differences

Each L2 implements different architecture:
- Some support the **Shared Mempool** (see Bundlers section)
- Others have custom EntryPoint deployments and gas constraints
- Native AA proposals (like RIP-7560) are often tested on L2 first

---

## 🔍 Deployment Considerations

When deploying an AA system to an L2:
- Confirm EntryPoint version and Paymaster compatibility
- Monitor bundler participation and mempool stability
- Use deterministic addresses via `CREATE2` or `initCode`

---

## 🧪 Example Chains

- **Optimism**: Part of the Superchain, supports RIP-7560 pilots
- **Arbitrum**: Supports Shared Mempool, fast adoption of ERC-4337 infra
- **Base**: Coinbase-backed L2 with active AA integrations
- **zkSync / Scroll / Linea**: EVM compatibility varies; entryPoint support may differ

---

## 📚 Related Pages

- [RIP-7560](./rip-7560.md)
- [Optimism Superchain Standards](./optimism-superchain-standards.md)

---

## ✅ Summary

L2s are the natural home for smart accounts. They reduce cost barriers, enable faster iteration, and often drive innovation in AA standards like RIP-7560. Each L2 has unique tradeoffs that developers should understand when building or deploying smart wallets.

