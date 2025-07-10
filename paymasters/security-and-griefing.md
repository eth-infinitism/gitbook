---
title: Security and Griefing
description: How Paymasters are secured in ERC-4337 and the risks of abuse or DoS.
sidebar_position: 3
---

# Paymasters: Security and Griefing Protection

Paymasters introduce a new layer of gas abstraction, but they also open new attack surfaces. A malicious user could try to:
- Drain the Paymaster’s deposit by spamming invalid operations
- Trick the Paymaster into sponsoring high-cost or reverted calls
- Exploit timeouts or race conditions in verification logic

ERC-4337 includes several protections to prevent these issues.

---

## 🔐 Stake Requirement

To operate, a Paymaster must:
- **Register** with the EntryPoint contract
- **Stake ETH** (minimum amount set by EntryPoint)
- **Maintain a deposit** to pay for gas

Staked Paymasters are subject to slashing if they misbehave or allow griefing.

---

## 🧪 Deterministic Validation

`validatePaymasterUserOp()` must:
- Avoid `SSTORE`, `BLOCKHASH`, or other non-deterministic behavior
- Not depend on variable external state (unless staked)
- Run within strict gas bounds enforced by bundlers

These constraints reduce DoS risk and make validation safely simulatable.

---

## 📦 Bundler Simulation

Before including a UserOp in a bundle, a bundler will:
1. Simulate the full operation off-chain
2. Measure gas cost and return data
3. Reject anything that might revert or exceed limits

This ensures Paymasters don’t get unexpectedly charged on-chain.

---

## 🛡️ PostOp Protections

Paymasters can implement logic in `postOp()` to:
- Reclaim unspent gas
- Log usage or enforce backend quotas
- Blocklist abusers

However, `postOp()` runs **after the UserOp executes**, and must also be gas-safe.

---

## ✅ Summary

Paymasters must balance flexibility with caution. The ERC-4337 spec enforces staking, deterministic validation, and bundler simulation to keep Paymasters safe from griefing and gas theft. A well-designed Paymaster should assume hostile inputs and protect its deposit at all times.
