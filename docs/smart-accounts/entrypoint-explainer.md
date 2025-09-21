
# The EntryPoint Contract

## The heart of ERC-4337 — how EntryPoint validates, simulates, and executes UserOperations.





The **EntryPoint** contract is the core of ERC-4337. It acts as the universal gateway for all smart contract wallet interactions under Account Abstraction, coordinating validation, execution, sponsorship, and bundling logic.


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


## ↩️ Simulation & Reversion by Design

Simulation is a core design pattern:


- `simulateValidation()` is expected to revert
- Reversion includes encoded data for bundlers
- Off-chain tools like `eth_call` and `debug_traceCall` can interpret these reverts


## 🛠️ Compatibility & Deployment

- Only one EntryPoint should be deployed per chain
- Major bundlers hardcode the address (often `0x0576…`)
- Most wallets explicitly reference it in `UserOperation.entryPoint`


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
