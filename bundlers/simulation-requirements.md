---
title: Simulation Requirements
sidebar_position: 5
description: What bundlers must validate before including a UserOperation.
---

# Simulation Requirements for Bundlers

Before a `UserOperation` can be included in a bundle and submitted to the EntryPoint contract, bundlers must simulate it off-chain. This ensures that the operation will not revert during the validation phase of on-chain execution — preventing gas losses for the bundler.


---

## ⭐️ Why Simulate?

Bundlers are economically exposed — they pay for gas upfront and only get reimbursed if the `UserOperation` succeeds. Simulation is essential to:

- Prevent inclusion of invalid or failing operations
- Detect `validateUserOp()` or `validatePaymasterUserOp()` reverts
- Estimate gas costs
- Maintain alt mempool health

***

## 🔍 What Gets Simulated?

Bundlers use the `simulateValidation()` function from the EntryPoint to emulate validation logic without consuming gas:

- **Account logic**: `validateUserOp()` — runs wallet-defined validation, which may include signature checks, nonce, balance, time windows, and even app-specific constraints
- **Paymaster logic**: `validatePaymasterUserOp()` — if present, checks stake and any custom rules for sponsorship eligibility
- **Deployment logic**: `initCode` is simulated to deterministically deploy the smart account — validating factory behavior and prefund correctness

If any part fails, EntryPoint reverts with a `FailedOp` or `FailedOpWithRevert` — these are used by bundlers to classify errors and decide inclusion.

***

## 📐 Trace Tools

Bundlers often rely on `debug_traceCall` to simulate `handleOps()` before submitting the bundle. This gives access to:

- Gas usage estimates
- Error attribution (account vs paymaster vs factory)
- Stack traces for debugging reverts

This trace data is critical for detecting whether a failure is due to temporary issues (e.g. nonce, funding) or structural problems (e.g. logic bug, misconfiguration).

***

## ⚖️ Consequences of Failure

If a bundler submits a bundle and a `UserOperation` reverts during validation onchain:

- The bundler pays for all gas used
- The EntryPoint emits a `FailedOp()` with the index and reason
- This may be used for local reputation tracking (e.g., ERC-7562 bans)

To avoid this, bundlers maintain internal rules to simulate before submission and may locally reject wallets or paymasters that repeatedly fail.

***

## 🛂 Optional Behaviors

Some bundlers add prechecks beyond `simulateValidation()`, such as:

- Reputation lists or ban scoring (see: ERC-7562)
- Throttling factories that frequently deploy broken contracts
- Estimating maximum acceptable `preVerificationGas`

These behaviors are not required by ERC-4337 but are common in production bundlers to improve efficiency and robustness.

***

## ✅ Summary

Simulation is a critical preflight step for bundlers. It ensures only valid `UserOperation`s are included in bundles, protects bundlers from gas griefing, and enables better mempool hygiene. Errors are surfaced through trace tools and `FailedOp()` events, enabling bundlers to penalize unreliable actors based on local policy.
