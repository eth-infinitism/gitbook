---
title: Censorship Resistance
description: How the alt mempool and Shared Mempool protect UserOp inclusion.
sidebar_position: 4
---
# Censorship Resistance in ERC-4337

From the very beginning, ERC-4337 was designed to support a decentralized, censorship-resistant transaction flow for Account Abstraction. A key part of that vision was the creation of a **separate, peer-to-peer mempool for UserOperations**, distinct from Ethereum’s native transaction mempool. However, realizing this architecture took time — and until late 2024, most bundlers relied on **private, isolated queues** that undermined the original goals.

---

## ⚠️ Centralization Risk Without Global Propagation

In a fragmented ecosystem:
- Bundlers can selectively drop or ignore `UserOperation`s
- Users relying on a single RPC or bundler can be censored

Unlike Ethereum’s canonical mempool, inclusion guarantees are weaker unless the network shares UserOps widely.

---

## 🌐 Shared Mempool: Live and Decentralized

As of November 2024, the ERC-4337 Shared Mempool is live on Ethereum, Arbitrum, and Optimism. This milestone was achieved through a multi-team collaboration involving Etherspot, Candide, Alchemy, and others, marking a transition from private relays to a **decentralized propagation layer** for UserOps:

- Bundlers publish metadata to IPFS
- Peers use this metadata to discover compatible UserOps
- Valid operations propagate across nodes via gossip

Rather than requiring users to target a specific bundler, the shared mempool enables any participating bundler to see and process a submitted UserOperation — mimicking the visibility guarantees of Ethereum’s base-layer mempool.

This makes censorship significantly harder. A malicious or non-cooperative bundler can no longer act as a gatekeeper: other bundlers will still see the UserOp and can include it in a valid bundle.

---

## 💡 Design Implications for Developers

- Always integrate multiple bundler endpoints
- Prefer relayers that participate in the Shared Mempool
- Monitor submission status and resubmit if needed

---
## 🌿 From Training Wheels to Full Decentralization

The rollout of the shared mempool follows a **staged maturity framework**, inspired by Vitalik’s rollup decentralization stages:

- **Stage 0: Private Queues** — No mempool, just per-bundler UserOp handling
- **Stage 1: Permissioned Sharing** — Only whitelisted bundlers propagate UserOps
- **Stage 2: Controlled Decentralization** — Shared but semi-restricted propagation
- **Stage 3: Fully Permissionless** — Any compliant bundler can join and relay

The ecosystem is currently transitioning from Stage 1 to Stage 2, with growing adoption of peer-to-peer relays and emerging tooling to inspect and verify bundler behavior.

---

## 🤝 Relevance to EIP-7702

Even outside of ERC-4337, the Shared Mempool helps:
- EIP-7702 introduces temporarily smart-enabled EOAs
- These can be relayed via the UserOp mempool, not the canonical one
- This enhances censorship resistance for wallets adopting 7702 logic

Ethereum.org recommends using the UserOp mempool as a best practice for 7702 onboarding:
> *“Consider using the UserOperation mempool for relaying smart EOA transactions to avoid base-layer censorship.”* [^1]

---

📖 Learn more:
- [Unified ERC-4337 mempool](https://notes.ethereum.org/@yoav/unified-erc-4337-mempool)
- [ERC-4337 Shared Mempool Launch](https://etherspot.io/blog/erc-4337-shared-mempool-official-launch-on-ethereum-mainnet-arbitrum-and-optimism/)
- [Decentralized Future of Shared Mempool](https://medium.com/etherspot/decentralized-future-erc-4337-shared-mempool-launches-on-ethereum-b6c860072f41)
- [Mempool Stages Framework](https://substack.com/home/post/p-163060056)

---
## ⭐️ Why This Matters

Without a shared propagation layer, censorship resistance is impossible. The ERC-4337 shared mempool finally delivers on the standard’s decentralization promise — improving inclusion guarantees, reducing single bundler risk, and making it easier for wallets to route UserOps through resilient pathways.

Even with this infrastructure in place, users must still choose bundler-connected RPCs that support the mempool. Ecosystem adoption is growing fast, and continued tooling will make it easier to monitor bundler behavior and performance in this new permissionless layer.

---

## ✅ Summary

Censorship resistance in Account Abstraction depends on open submission infrastructure. The live Shared Mempool, now standard in the ERC-4337 ecosystem, ensures that UserOperations can’t be easily suppressed or filtered, and even benefits 7702 workflows.

[^1]: [Source → ethereum.org](https://ethereum.org/en/roadmap/pectra/7702/#best-practices)