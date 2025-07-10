---
title: Session Keys & Delegation
description: Local signing, permissions, and EIP-7702 in smart wallets.
sidebar_position: 3
---

# Session Keys & Delegation

Session keys and delegation allow smart accounts to temporarily authorize actions without exposing the main wallet key. These patterns unlock new UX for games, dApps, and mobile wallets — though they are not yet standardized and are implemented wallet-by-wallet.

---

## 🔐 What Are Session Keys?

Session keys are ephemeral keypairs that:
- Are authorized by the smart account
- Have a defined scope (methods, dApps, gas limit)
- Can be revoked or time-limited

They allow:
- Local signing in dApps
- Multiplatform delegation
- Non-interactive usage (e.g., scheduled jobs)

---

## 🛂 Delegation Models

### Static Delegation
- Grant a key ongoing permission to act on the account
- Must be explicitly revoked

### Dynamic Delegation
- Sign a session token with constraints (e.g., `validUntil`, `targetContract`)
- Enforced in `validateUserOp()` by wallet-specific logic (e.g., a plugin or auth module); not natively supported by ERC-4337


---

## 🪄 EIP-7702: Temporary Smart Wallet Mode for EOAs

EIP-7702 lets EOAs temporarily delegate control to smart contract logic **for a single transaction**.

- Uses the same address as the EOA
- Includes a `contractCode` and `validationData`
- Restores to an EOA after execution

This supports passkeys, session UX, and smart extensions **without permanent migration** to a smart wallet.

ethereum.org recommends submitting 7702-based txs through the **UserOperation mempool** to preserve censorship resistance:
> *“Consider using the UserOperation mempool for relaying smart EOA transactions to avoid base-layer censorship.”*  
[Read more →](https://ethereum.org/en/roadmap/pectra/7702/#best-practices)

---

## ⚙️ Implementation Notes

- Many ERC-4337 wallets use signature aggregation modules
- Session key delegation can be done via plugin (ERC-6900/7579)
- Tokens or NFTs can act as auth factors (e.g., token gating)

---

## ✅ Summary

Session keys and delegation expand smart account usability across devices and flows. With EIP-7702, even EOAs gain the ability to temporarily act like smart wallets — enabling powerful hybrid UX that balances flexibility, security, and compatibility.