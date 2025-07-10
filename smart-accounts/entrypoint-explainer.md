---
title: The EntryPoint Contract
description: The heart of ERC-4337 — how EntryPoint validates, simulates, and executes UserOperations.
sidebar_position: 2
---

# The EntryPoint Contract

The **EntryPoint** contract is the core of ERC-4337. It acts as the universal gateway for all smart contract wallet interactions under Account Abstraction, coordinating validation, execution, sponsorship, and bundling logic.

---

## ⭐️ Why EntryPoint Exists

In ERC-4337, transactions don’t originate from EOAs — they’re replaced by `UserOperation` structs. The EntryPoint contract is the canonical place where these `UserOperation`s are:

1. **Validated** — Checks signatures, nonces, paymaster rules, and any custom logic defined by the wallet (e.g. balance checks, calldata constraints, or app-specific conditions)
2. **Executed** — Performs the user-specified logic (via `callData`) — which can include batching multiple calls, invoking plugins, or other programmable behaviors defined by the smart wallet
3. **Charged** — Calculates gas usage and deducts fees from the wallet’s deposit, or from a Paymaster if sponsorship is used
4. **Settled** — Optionally runs `postOp()` logic (e.g. logging, refunding, or slashing) depending on success or failure of execution


This creates a permissionless layer for smart contract wallets to operate **without modifying Ethereum consensus**, while also protecting protocol participants (accounts, bundlers, paymasters) from DoS and griefing attacks through deposits, staking, and strict validation rules.

> 💡 EntryPoint is not just an execution hub, but also a guardrail for economic and operational safety.


---

## 🛠 Core Responsibilities

The EntryPoint contract performs the following:

### ✅ `handleOps(UserOperation[] ops, address beneficiary)`
Main entry for bundlers:
- Loops over each UserOp
- Validates each via `validateUserOp()` on the wallet
- If valid, executes the call
- Charges gas costs and transfers to `beneficiary` (usually the bundler)

### 🧪 `simulateValidation(UserOperation op)`
Used off-chain by bundlers before inclusion:
- Runs all validation logic
- Reverts with detailed status (including aggregator or paymaster info)
- Helps detect invalid or malicious ops before execution

### 💸 `depositTo(address target)` and `balanceOf(address)`
- Wallets and paymasters must fund gas fees through deposits
- EntryPoint holds ETH balances for them
- These are used to settle costs post-execution

### ⛓ `addStake()`, `unlockStake()`, `withdrawStake()`
- Required for **paymasters**
- Prevents griefing attacks and enforces economic alignment

---

## 🔐 Validation Workflow

For each UserOp, EntryPoint invokes:

```solidity
wallet.validateUserOp(userOp, userOpHash, missingFunds) returns (sigTimeRange)
```

- Verifies the user’s signature or session logic
- Ensures nonce correctness
- Top-ups the wallet if `missingFunds > 0`
- If a paymaster is used, also calls:

```solidity
paymaster.validatePaymasterUserOp(...)
```

Validation failures are non-reverting and classified using a `FailedOp` status — important for bundlers deciding which ops to include.

---

## ↩️ Simulation & Reversion by Design

Simulation is a core design pattern:
- `simulateValidation()` is expected to revert
- Reversion includes encoded data for bundlers
- Off-chain tools like `eth_call` and `debug_traceCall` can interpret these reverts

---

## 💾 Onchain State Held by EntryPoint

- ETH balances for wallets and paymasters
- Stake and unstake timers for paymasters
- No app-specific logic — it remains neutral and stateless beyond coordination

---

## 🛠️ Compatibility & Deployment

- Only one EntryPoint should be deployed per chain
- Major bundlers hardcode the address (often `0x0576…`)
- Most wallets explicitly reference it in `UserOperation.entryPoint`

---

## 🔄 Versioning & Upgrades

The EntryPoint contract is not upgradeable. Instead, new versions are deployed as entirely new contracts — requiring coordinated migration by wallets, bundlers, and paymasters.

Below are the major versions released to date:

### EntryPoint v0.8


📄 [Release notes](https://github.com/eth-infinitism/account-abstraction/releases/tag/v0.8.0)

🔗 **Deployment address**: `0x4337084d9e255ff0702461cf8895ce9e3b5ff108`

More detailed deployment info can be found [here](https://github.com/eth-infinitism/account-abstraction/tree/develop/deployments/ethereum)


### EntryPoint v0.7

📄 [Release notes](https://github.com/eth-infinitism/account-abstraction/releases/tag/v0.7.0)

🔗 **Deployment address**: `0x0000000071727De22E5E9d8BAf0edAc6f37da032`

### EntryPoint v0.6

📄 [Release notes](https://github.com/eth-infinitism/account-abstraction/releases/tag/v0.6.0)

🔗 **Deployment address**: `0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789`


---

## 🏡 Local Deployment of EntryPoint

To experiment with ERC-4337 on a local network, you can deploy the EntryPoint contract using the official [`account-abstraction`](https://github.com/eth-infinitism/account-abstraction/) repository.

This tool uses a fixed `create2` salt, so you'll get the **same EntryPoint address** on your local network as on mainnet-compatible chains — ensuring portability and compatibility with off-the-shelf tooling.

### 🏗️ Deployment Steps

1. **Clone the repository**  
   ```bash
   git clone https://github.com/eth-infinitism/account-abstraction.git
   cd account-abstraction
   ```

2. **Add your network RPC**  
   Edit `hardhat.config.ts` and add your local RPC under the `networks` section.

3. **Set your deployer account**  
   Export the `MNEMONIC_FILE` environment variable to point to a file containing the mnemonic for your deployer account.

   ```bash
   export MNEMONIC_FILE=./mnemonic.txt
   ```

4. **Deploy the contract**  
   Use Hardhat to deploy to your local network:

   ```bash
   yarn deploy --network NETWORK_NAME
   ```

   Replace `NETWORK_NAME` with the name of your local network as configured in Hardhat.

That’s it — the script handles the `create2` deployment mechanics under the hood, ensuring deterministic EntryPoint addresses across environments.

---

## 🧠 Summary

The EntryPoint contract is the *hub* of ERC-4337. It’s not just a dispatcher — it enforces economic rules, ensures permissionless access, and provides the backbone for UX-enhancing features like validation, sponsorship and batching.

By understanding EntryPoint, you understand how smart contract wallets actually run — and how the whole AA stack hangs together.
