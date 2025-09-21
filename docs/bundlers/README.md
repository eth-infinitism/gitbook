
# 📦 Bundlers

## Overview of Bundlers in the ERC-4337 architecture.

Bundlers are the relayers of ERC-4337. They collect `UserOperations`, simulate them for validity, and package them into a call to the EntryPoint contract on-chain.

They are a critical part of the infrastructure that makes Account Abstraction work without consensus-layer changes.

---

## 🧠 What Do Bundlers Do?

- Monitor the alt mempool for `UserOperations`
- Simulate operations using EntryPoint’s `simulateValidation`
- Group valid ops into bundles
- Submit via `handleOps()` to the EntryPoint
- Pay gas and earn fees (like a miner)

---

## 🔍 Why Are They Needed?

Ethereum’s base protocol doesn’t natively support `UserOperation`-style logic. Bundlers:

- Act like “miners for smart wallets”
- Provide validation guarantees for off-chain mempools
- Allow modular signature and sponsorship logic without protocol changes

---

## 🏗️ EntryPoint Compatibility

All bundlers interact with a canonical **EntryPoint contract**, which is deployed at a fixed address per network (e.g. v0.6, v0.7, v0.8).

They must support:

- `handleOps()` to process batched `UserOperations`
- `simulateValidation()` to precheck operations without state changes

---

## 🤑 Incentives

Bundlers receive:

- Priority fees specified in each `UserOperation`
- Refunds from the account or Paymaster for gas used

They compete similarly to miners, but operate entirely in the mempool layer.

---

## 🔐 Security Considerations

- Bundlers must not include `UserOps` that fail simulation
- They should enforce ERC-7562 constraints on validation logic
- A single bad UserOp can revert the whole bundle — simulate carefully

---

## ✅ Summary

Bundlers are essential to ERC-4337. They verify, package, and submit smart wallet transactions in a decentralized, incentive-aligned way. While they operate off-chain, their correctness directly impacts the security and UX of Account Abstraction flows.

