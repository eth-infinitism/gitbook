
# FAQs

## Frequently asked questions about ERC-4337 and Account Abstraction.

## ❓ What is Account Abstraction?

Account Abstraction (AA) is a way to move Ethereum’s user accounts from EOAs (Externally Owned Accounts) to programmable **smart accounts**. With AA, wallets can customize signature logic, add social recovery, enable gasless transactions, and more.

---

## ❓ What is ERC-4337?

ERC-4337 is an account abstraction standard that works **without Ethereum protocol changes**. It introduces:
- A new transaction type called **UserOperation**
- A decentralized **UserOp mempool**, distinct from the traditional txpool, allowing bundlers to independently collect and simulate operations
- A shared execution pipeline via the **EntryPoint contract**
- Support for smart wallet features like Paymasters, session keys, and custom validation

This alt mempool architecture is critical for ensuring **censorship resistance** and **decentralized inclusion** of smart account activity.

---

## ❓ Will Account Abstraction become native to Ethereum?

Yes — multiple proposals aim to integrate AA directly into the Ethereum protocol. The leading one for Ethereum mainnet is **EIP-7701**, which introduces a new transaction type (`AA_TX_TYPE`) allowing EOAs to delegate signature validation to contracts. This eliminates the need for simulation and EntryPoint contracts.

EIP-7701 complements earlier L2-native proposals like **RIP-7560**, and is designed to unify smart and traditional accounts under a flexible, protocol-native model.

---

## ❓ What’s the difference between 4337, 7701, and 7702?

- **ERC-4337**: Application-layer abstraction using UserOperations and bundlers
- **EIP-7701**: Native protocol support for AA on Ethereum Layer 1 using `AA_TX_TYPE` transactions and contract-based validation
- **EIP-7702**: A proposal for temporary validation delegation during a transaction — offers benefits of AA like batching and gas sponsorship, but cannot offer the same level of security as the original EOA will always have full access to the account (cannot be revoked)

These models can be used together. For example, ERC-4337 can relay EIP-7702 transactions through the UserOp mempool for censorship resistance. EIP-7701 envisions a future where smart account logic is validated natively by block builders.


---

## ❓ What is a Bundler?

A Bundler is a block builder that focuses on UserOperations. It:

- Collects UserOps from the mempool
- Simulates and validates them
- Submits them to the EntryPoint in a single legacy transaction

Bundlers earn fees by batching and submitting UserOps.

---

## ❓ What’s the purpose of the EntryPoint?

EntryPoint is the core contract in ERC-4337. It:

- Validates UserOperations
- Manages deposits, gas, and Paymasters
- Routes execution to smart accounts

It’s stateless and can be upgraded over time (new versions are deployed and whitelisted).

---

## ❓ How do Paymasters work?

Paymasters sponsor gas for users. They:

- Inspect the UserOp and decide whether to pay
- Can use policies like NFT ownership, token balances, payloads signed offchain, etc.
- Stake ETH and deposit funds in the EntryPoint

---

## ❓ What chains support ERC-4337?

Most major EVM-compatible chains support 4337, including:

- Ethereum Mainnet
- Optimism, Arbitrum, Base, zkSync, Lineam, Polygon, Scroll, Avalanche, and many others

---

## ❓ Do I need to deploy my own EntryPoint?

No, most wallets and bundlers share a canonical EntryPoint. Only deploy yourself if you are developing locally. See [Local Deployment of EntryPoint](../smart-accounts/entrypoint-explainer.md#local-deployment-of-entrypoint).

---

## ❓ How do wallets support AA?

Wallets can:

- Use smart accounts with custom validation
- Rely on bundlers to relay UserOps
- Integrate Paymaster logic for sponsored gas

---

## ❓ Where can I ask questions or get support?

- [Twitter](https://twitter.com/erc4337)
- [Infinitism Discord](https://discord.gg/8s55fSSauF)
- [Telegram](https://t.me/+aIMWB_k4hxU0MzVk)
- [ERC-4337 on Ethereum Magicians](https://ethereum-magicians.org/t/erc-4337-account-abstraction-via-entry-point-contract-specification/7160)
- GitHub Discussions in [eth-infinitism](https://github.com/eth-infinitism)

---

## Contributing

If you have relevant questions that should be included in this list, please submit a pull request with the question and answer following the format above.

### Format for Adding Questions

When adding new questions, please use the following format:

```markdown
## ❓ Question
Answer goes here.

> Answers can include basic Markdown formatting — lists, code blocks, **bold**, _italics_, etc.
```
