
# Reading Material

## Curated blog posts, specs, and ecosystem discussions on Account Abstraction.

This page collects useful articles, posts, and discussions related to Account Abstraction (ERC-4337 and beyond). Each section groups readings by a focus area.

We also recommend subscribing to our [Substack](https://substack.com/@erc4337/) for the latest updates

---

## 🧱 Foundational Posts


- **[ERC-4337: Account Abstraction Without Protocol Changes](https://medium.com/infinitism/erc-4337-account-abstraction-without-ethereum-protocol-changes-d75c9d94dc4a)**  
The original blog post by Vitalik Buterin outlining the vision behind ERC-4337.

- **[Unified ERC-4337 mempool](https://notes.ethereum.org/@yoav/unified-erc-4337-mempool)**
What does censorship-resistance require of ERC-4337 and how can we prevent mempool fragmentation?



---

## 📜 AA Standards

### Core Standards

- [ERC-4337: Account Abstraction Using Alt Mempool](https://eips.ethereum.org/EIPS/eip-4337)
- [ERC-7562: Account Abstraction Validation Scope Rules](https://eips.ethereum.org/EIPS/eip-7562)
- [EIP-7701: Native Account Abstraction](https://eips.ethereum.org/EIPS/eip-7701)

### Core Standards: Rollups

- [RIP-7560: Native Account Abstraction](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7560.md)
- [RIP-7711: Validation-Execution Separation in Native Account Abstraction](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7711.md)
- [RIP-7712: Enable RIP-7560 transactions using a two-dimensional nonce](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7712.md)

### Supporting Standards

- [EIP-5792: Wallet Call API](https://eips.ethereum.org/EIPS/eip-5792)
- [EIP-7702: Set Code for EOAs](https://eips.ethereum.org/EIPS/eip-7702)
- [ERC-6900: Modular Smart Contract Accounts](https://eips.ethereum.org/EIPS/eip-6900)
- [ERC-7579: Minimal Modular Smart Accounts](https://eips.ethereum.org/EIPS/eip-7579)
- [ERC-6492: Signature Validation for Predeploy Contracts](https://eips.ethereum.org/EIPS/eip-6492)
- [ERC-7677: Paymaster Web Service Capability](https://eips.ethereum.org/EIPS/eip-7677)
- [ERC-7679: UserOperation Builder](https://eips.ethereum.org/EIPS/eip-7679)
- [ERC-7715: Grant Permissions from Wallets](https://eips.ethereum.org/EIPS/eip-7715)
- [ERC-7769: JSON-RPC API for ERC-4337](https://eips.ethereum.org/EIPS/eip-7769)
- [RIP-7212: Precompile for secp256r1 Curve Support](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7212.md)

---

## 🤿 Deep Dives

- **[You Could Have Invented Account Abstraction - 4 part series](https://www.alchemy.com/blog/account-abstraction)**
  Reverse engineering AA capabilities while preseving strong censorship resistance and decentralization to better understand the reasoning behind ERC-4337's architecture.

- **[What are Paymasters?](https://www.alchemy.com/overviews/what-is-a-paymaster)**  
  Technical overview of the different types of paymasters and how they work.

- **[What happens to a UserOp within a Bundler?](https://jiffylabs.hashnode.dev/what-happens-to-a-userop-within-a-bundler)**
  Why do we need a bundler when you can just relay the UserOp directly to the entrypoint from an EOA?

- **[Mempool Stages Framework](https://substack.com/home/post/p-163060056)**
The ERC-4337 Team introduced a framework which categorizes Bundler Mempool development into distinct stages. As the framework progresses, it enhances user benefits at every stage, such as censorship resistance, decentralization, and permissionless.

---

## 📰 In the news

- **[Shared Mempool: Official Launch on Ethereum Mainnet, Arbitrum and Optimism](https://etherspot.io/blog/erc-4337-shared-mempool-official-launch-on-ethereum-mainnet-arbitrum-and-optimism/)**
  The ERC-4337 shared mempool goes live on Ethereum, Arbitrum and Optimism. The mempool is what allows AA while preserving decentralization. 

- **[Toyota: How to Introduce Mobility into the Public Blockchain with ERC-4337](https://www.toyota-blockchain-lab.org/library/how-to-introduce-mobility-into-the-public-blockchain)**
SCW == Smart *Car* Wallet? Interesting research by the Toyota Blockchain Lab on using ERC-4337 to manage open and transferable accounts for cars themselves 
- **[Visa: What is Account Abstraction? Exploring new techniques for blockchain payment processing](https://usa.visa.com/solutions/crypto/rethink-digital-transactions-with-account-abstraction.html)**  
  The team at Visa has deployed experimental Visa Paymaster contracts on Ethereum's Goerli Testnet to explore the power of AA.

- **[Visa: Auto Payments for Self-Custodial Wallets](https://usa.visa.com/solutions/crypto/auto-payments-for-self-custodial-wallets.html)**  
  The team at Visa continues their research into AA and the innovative payment solutions it offers, and explore automatic recurring payments capabilities for self-custodial accounts.


---

## 💬 Discussions and Threads

- **[Ethereum Magicians: ERC-4337 Thread](https://ethereum-magicians.org/t/erc-4337-account-abstraction-via-entry-point-contract-specification/7160)**
  The thread on Ethereum Magicians for the ERC-4337 standard.
- **[Ethereum Magicians: RIP-7560 Thread](https://ethereum-magicians.org/t/rip-7560-native-account-abstraction/16664)**
  The thread on Ethereum Magicians for the RIP-7560 standard.
- **[The road to Post-Quantum Ethereum transaction is paved with Account Abstraction](https://ethresear.ch/t/the-road-to-post-quantum-ethereum-transaction-is-paved-with-account-abstraction-aa/21783)**
  Exploring the feasibility of implementing a post-quantum signature scheme for Ethereum with AA

---

## 📊 Useful Metrics

- **[BundlerBear](https://www.bundlebear.com/erc4337-overview/all)**
  BundleBear is a dataset that tracks the adoption of smart accounts.


---

## Contributing

If you have relevant resources that should be included in this list, please submit a pull request with the resource details following the format above.

### Format for Adding Resources

When adding new resources, please use the following format:

```markdown
- **[Title of the Resource](link-to-resource)**
  Brief description of the content
```
