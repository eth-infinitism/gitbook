---
title: UserOp Mempool Overview
description: Architecture and behavior of the ERC-4337 alternative mempool.
sidebar_position: 3
---

# UserOp Mempool Overview

ERC-4337 introduces a new mempool paradigm distinct from Ethereum’s canonical tx pool. Instead of `eth_sendTransaction`, users submit `UserOperations` to an **alt mempool** that is monitored by bundlers.

---

## 📬 Submission Path

- `eth_sendUserOperation` is the new RPC endpoint
- Users submit to a bundler directly or via RPC relayers
- Bundlers maintain a local mempool of unconfirmed `UserOperations`

This design enables wallets to express rich behavior without protocol changes.

---

## 🧱 Architectural Differences

| Canonical Tx Mempool | ERC-4337 Alt Mempool           |
|----------------------|-------------------------------|
| EOAs only            | Smart contract senders        |
| Native fee model     | Custom logic + paymasters     |
| Global propagation   | Per-bundler propagation       |
| Consensus-integrated | Application-layer only        |

Each bundler historically ran its own isolated mempool. This avoided polluting Ethereum's core infrastructure, but introduced new challenges around censorship and redundancy.

---

## 🧪 Validation at Ingress

Bundlers simulate incoming `UserOperations` before accepting them:
- Run `simulateValidation()` against the EntryPoint
- Discard any that revert or exceed limits
- Optionally enforce custom reputation or rate limits

---

## 🧵 Fragmentation & Interoperability

Historically, the alt mempool wasn’t globally propagated:
- Users could be censored or de-prioritized by specific bundlers
- Mempool fragmentation limited redundancy and reach

This changed with the launch of the **Shared Mempool**:
- Bundlers now gossip `UserOperations` to peers
- Each bundler advertises its mempool metadata via IPFS
- Peers use this metadata to determine whether and how to share UserOps

The Shared Mempool is live on Ethereum, Arbitrum, and Optimism, coordinated by Etherspot, Candide, Silius, and others. This significantly improves decentralization and availability.

These issues are covered in more depth on the [Censorship Resistance](./censorship-resistance.md) page.

---

## ✅ Summary

The alt mempool is where all ERC-4337 activity begins. With the Shared Mempool, it has become a more decentralized and resilient submission layer. Understanding how UserOps are submitted, validated, and propagated is key to debugging, censorship resistance, and reliable smart wallet UX.
