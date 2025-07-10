---
title: Core Standards
description: The foundational specifications of Account Abstraction, including ERC-4337, validation rules, and protocol-level proposals like RIP-7560.
sidebar_position: 1
---

# 🌿 Core Standards

This section summarizes the foundational specifications that make up the Account Abstraction ecosystem — both live standards and emerging protocol-level proposals.

Each spec in this section plays a critical role in enabling smart contract wallets to function securely, flexibly, and permissionlessly on Ethereum.

## 📄 Included Standards

- **ERC-4337**: The backbone of account abstraction via a decentralized alt-mempool and EntryPoint contract.
- **ERC-7562**: Defines validation-phase restrictions to protect bundlers from griefing and ensure deterministic behavior.
- **EIP-7701**: A protocol-level proposal to bring native account abstraction to Ethereum, building on the lessons of ERC-4337.
- **RIP-7560**: Adds native account abstraction to L2s via a new transaction type, enabling built-in validation, gas delegation, and onchain paymasters — without relying on ERC-4337 infrastructure.
- **RIP-7711**: Establishes interface and behavior rules for AA wallet deployment and upgradeability under RIP-7560.
- **RIP-7712**: Specifies how to manage gas payments and refunds under RIP-7560’s delegated fee model.



Together, these documents define the validation logic, execution model, gas flow, and wallet behavior of smart accounts — both in today’s ERC-4337 world and in the upcoming native AA future.

> 🧠 If you're building wallets, bundlers, paymasters, or infra — this is where to go deep.
