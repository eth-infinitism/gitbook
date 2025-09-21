
# The Application Layer: Wallets & SDKs

## Explore how smart contract wallets, embedded SDKs, and standards like ERC-5792 power user experience in Account Abstraction.





## ⭐️ What is a Smart Contract Wallet?

Smart contract wallets (SCWs) are user accounts implemented as contracts. Unlike EOAs (Externally Owned Accounts), they:



- Execute logic inside `validateUserOp()` for flexible validation
- Support features like batched calls, session keys, and gas sponsorship
- Can be upgraded, delegated, or extended with plugins

SCWs are the primary building block of Account Abstraction (AA), enabling programmable UX beyond the constraints of traditional wallet paradigms.


## 🧩 Embedded Wallets and SDKs

Most apps don’t ask users to install a new wallet — they **embed** wallet functionality directly into the frontend, using SDKs. These SDKs often create a smart account under the hood, preconfigured to work with a hosted bundler and paymaster.

You may have encountered these flows already:


- "Sign in with Google" → creates a smart wallet
- "Claim token" → happens via a batched AA UserOp
- "Gasless swap" → uses a paymaster behind the scenes

While we don’t list SDKs here either, developers will find no shortage of options — from infra providers to open-source toolkits. A quick search, GitHub crawl, or dev meetup will surface leading options.


## ✅ Summary

The application layer is where AA meets users — and it’s evolving fast. Whether you’re embedding a wallet with an SDK, or building your own SCW from scratch, the tooling and standards are maturing.

To stay up to date:


- Browse [WalletBeat](https://wallet.page/)
- Review [ERC-5792](https://www.eip5792.xyz/)
- Explore session keys, plugins, and modular architectures

Account Abstraction isn’t just infra — it’s UX. And this is where it shines.

