
# Modular Accounts

## Compare ERC-6900 and ERC-7579 for building smart wallet systems.

Modular account standards define how smart accounts can be extended with plug-ins, permissions, and upgradeable logic. Two main proposals in the ecosystem are **ERC-6900** and **ERC-7579**.

This page compares them from a developer perspective.

---

## 🖇️ What Is Modularity?

A modular smart account:
- Delegates logic to external modules (e.g., signature validation, permission checks)
- Enables upgrades or feature toggles without full redeployments
- Improves auditability by isolating logic

> 💡 Modular accounts benefit from [RIP-7712](../core-standards/rip-7712.md), which enables plugin-specific nonces and parallel execution lanes.


---

## ✳️ ERC-6900: Generalized Permission Graphs

- Proposes a universal registry for modules and permissions
- Emphasizes **graph-based delegation** (who can do what, on behalf of whom)
- Enables fine-grained and reusable access control

**Use case:** protocol-governed wallets, DAOs, nested delegation

**Pros:**

- Very flexible
- Shared registry enables interoperability
- Deep control over auth trees

**Cons:**

- More complex to reason about
- New mental model for devs unfamiliar with graphs

---

## ❇️ ERC-7579: Wallet-Centric Modules

- Defines **runtime module loading** for smart accounts
- Compatible with ERC-4337; enables session key enforcement via wallet-controlled module validation
- Modules attach to wallets and expose specific interfaces

**Use case:** app-specific wallets, extensible UX, plugins

**Pros:**

- Simple to integrate
- Plug-and-play UX modules (e.g., multisig, rate limiting)
- Deployed in production (Candide)

**Cons:**

- Modules are not shared across wallets
- Less granular permissioning than 6900

---

## 🌍 Ecosystem Adoption

For up-to-date information on ecosystem support and implementation of modular smart account standards, refer to the following official sources:

- [ERC-6900](https://erc6900.io/): Plugin-based modular account registry and validation
- [ERC-7579](https://erc7579.com/): Minimal modular interface layer for smart accounts

These pages track real-time contributions and adoption by wallet teams, infra providers, and AA tooling projects.


---

## 📚 Related Pages

- [Session Keys & Delegation](./session-keys-and-delegation.md)
- [Introduction to Smart Accounts](./README.md)

---

## ✅ Summary

Both ERC-6900 and ERC-7579 push smart accounts toward a modular future. 6900 prioritizes permission graphs and registry-level reuse, while 7579 focuses on local extensibility and simple UX. Choose based on your app’s architecture and user control requirements.