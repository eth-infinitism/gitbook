
# 🧠 Smart Accounts

## Capabilities, architecture, and role of smart accounts in Account Abstraction (AA).





Smart accounts are smart contract-based wallets that serve as the foundation of Account Abstraction (AA). Unlike EOAs (Externally Owned Accounts), which rely on one master private key and ECSDA only protocol-level signature checks, smart accounts embed custom logic for authentication, authorization, network fee payment, nonce management and execution.

Through the ERC-4337 standard, AA unlocks powerful UX and security features without compromising on decentralization and censorship resistance.


## 📐 Architecture

Each smart account is a contract that:


- Implements a `validateUserOp()` function for on-chain validation, simulated off-chain by bundlers
- Interacts with the **EntryPoint** contract for validation and execution
- May use internal modules (via standards like ERC-6900 or 7579)

Smart accounts don’t need to exist at first — they can be deterministically deployed with `initCode`, using a factory contract and CREATE2.


## 🛠 Upgradeability and Custom Logic

Depending on design:


- Some smart accounts are immutable (minimal proxies)
- Others use upgradeable patterns
- Logic can be extended via plugins, hooks, or modules

Security audits and upgrade policies become critical at scale.


## ✅ Summary

Smart accounts are programmable wallets that support richer UX and security than EOAs. They’re the cornerstone of Account Abstraction, built on standards like ERC-4337 and integrated with modular features like session keys and gas abstraction.

