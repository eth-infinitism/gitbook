---
title: Paymasters
description: How paymasters enable gas abstraction in ERC-4337.
sidebar_position: 1
---

# 💰 Paymasters

A **Paymaster** is a smart contract that can sponsor gas fees on behalf of users. This allows users to send transactions without needing ETH, improving onboarding and UX.

---

## 🔧 What Do Paymasters Do?

Paymasters interact with the EntryPoint during the validation phase of a `UserOperation`. They are responsible for:

- Verifying that the operation meets their criteria
- Covering gas costs if validation succeeds
- Having sufficient stake and deposit with the EntryPoint

They enable **gas abstraction** by allowing:
- ERC-20-based fee payments
- Third-party gas sponsorship
- Business logic gating (e.g. ad views, subscriptions)

---

## 🧪 How Are Paymasters Invoked?

If a `UserOperation` includes a non-empty `paymasterAndData` field, the EntryPoint calls:

- `validatePaymasterUserOp(userOp, requestId, maxCost)`

This method is expected to:
- Check if it’s willing to sponsor the op
- Optionally return context data
- Revert if the op should be rejected

Later, if the operation succeeds, the EntryPoint calls:

- `postOp(mode, context, actualGasCost)`

This allows the Paymaster to finalize accounting or take post-op actions.

---

## 💸 Staking and Security

To prevent griefing (e.g., spamming ops that fail), Paymasters must:
- Deposit ETH to cover potential costs
- Stake additional ETH as a safety requirement
- Wait through an unstake delay if they want to withdraw

If a sponsored op fails validation or execution, the Paymaster pays the gas. Thus, it's critical to simulate carefully and enforce strict checks in `validatePaymasterUserOp`.

---

## ⚠️ Common Attacks and Design Considerations

- **Replay abuse**: ensure ops are only valid once
- **Gas griefing**: require off-chain checks before sponsorship
- **Whitelist bypass**: signatures or preconditions must be enforced securely
- **Stake draining**: validate preconditions tightly, and monitor gas costs

---

## 🔄 Stateless vs Contextual Paymasters

Some Paymasters simply check a whitelist or signature and return — these are stateless. Others encode server-verified rules, access passes, or custom logic using:

- Rate-limiting APIs
- Game logic
- DApp identity protocols

These typically return context to `postOp()` to complete the flow.

---

## ✅ Summary

Paymasters are essential for enabling gasless UX in Account Abstraction. They let dApps or wallets pay for users’ gas under custom conditions. But to do this safely, they must be staked, carefully simulate all sponsored ops, and implement robust validation logic.

