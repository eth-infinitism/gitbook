---
title: "The Application Layer: Wallets & SDKs"
description: "Explore how smart contract wallets, embedded SDKs, and standards like ERC-5792 power user experience in Account Abstraction."
sidebar_position: 4
---

# The Application Layer: Wallets & SDKs

## ⭐️ What is a Smart Contract Wallet?

Smart contract wallets (SCWs) are user accounts implemented as contracts. Unlike EOAs (Externally Owned Accounts), they:

- Execute logic inside `validateUserOp()` for flexible validation
- Support features like batched calls, session keys, and gas sponsorship
- Can be upgraded, delegated, or extended with plugins

SCWs are the primary building block of Account Abstraction (AA), enabling programmable UX beyond the constraints of traditional wallet paradigms.

---

## 🙊 Why We Don’t List Wallets or SDKs Here

While there are only a few dozen bundlers and Paymasters, the number of wallets and SDKs building on AA is already in the **hundreds**, and growing rapidly. Tracking them manually is difficult to manage — and risks becoming outdated or inadvertently favoring certain teams.

To solve this, the ecosystem has built a curated directory:

👉 **[WalletBeat](https://wallet.page/)**

This site acts as an evolving “L2Beat for wallets,” indexing wallets based on:

- Standards support
- Security
- Privacy
- Recovery flows and passkey support
- Feature sets like batching, paymasters, plugins, and more

It’s a go-to resource for developers and users evaluating wallet functionality.

---

## 🧩 Embedded Wallets and SDKs

Most apps don’t ask users to install a new wallet — they **embed** wallet functionality directly into the frontend, using SDKs. These SDKs often create a smart account under the hood, preconfigured to work with a hosted bundler and paymaster.

You may have encountered these flows already:
- "Sign in with Google" → creates a smart wallet
- "Claim token" → happens via a batched AA UserOp
- "Gasless swap" → uses a paymaster behind the scenes

While we don’t list SDKs here either, developers will find no shortage of options — from infra providers to open-source toolkits. A quick search, GitHub crawl, or dev meetup will surface leading options.

---

## ⚙️ ERC-5792: A Standard Interface for Wallet Interactions

> 🔗 [Official site: eip5792.xyz](https://www.eip5792.xyz/)

**ERC-5792** defines a modern JSON-RPC API for how dApps and wallets interact — especially for Account Abstraction use cases.

It introduces new methods like:

- `wallet_sendCalls`: send batched transactions
- `wallet_getCallsStatus`: check their result
- `wallet_getCapabilities`: query supported features like paymasters or atomicity

### Why This Matters

Under ERC-4337, different wallets may support different features — batching, session keys, sponsored gas, plugins, etc. ERC-5792 provides a **capability-discovery layer**, so apps can adapt to what the wallet supports.

This means:
- Safer fallback logic if a feature isn't supported
- Progressive UX — e.g., offer paymaster support only if present
- Cleaner RPC semantics — no need to hack around `eth_sendTransaction`

It helps AA apps scale across a fragmented wallet landscape while maintaining graceful UX.

### Key Capabilities in ERC-5792

- **Batching**: submit multiple calls, atomically or sequentially
- **Paymasters**: plug in gas sponsorship services
- **Atomic Execution**: ensure all-or-nothing behavior when needed
- **Session Keys**: temporarily delegated privileges

By making all this programmable and discoverable via JSON-RPC, ERC-5792 helps SCWs feel as smooth as EOAs — but with superpowers.

---

## ✅ Summary

The application layer is where AA meets users — and it’s evolving fast. Whether you’re embedding a wallet with an SDK, or building your own SCW from scratch, the tooling and standards are maturing.

To stay up to date:
- Browse [WalletBeat](https://wallet.page/)
- Review [ERC-5792](https://www.eip5792.xyz/)
- Explore session keys, plugins, and modular architectures

Account Abstraction isn’t just infra — it’s UX. And this is where it shines.

