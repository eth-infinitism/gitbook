
# Session Keys & Delegation

## Local signing, permissions, and EIP-7702 in smart wallets.





Session keys and delegation allow smart accounts to temporarily authorize actions without exposing the main wallet key. These patterns unlock new UX for games, dApps, and mobile wallets — though they are not yet standardized and are implemented wallet-by-wallet.


## 🛂 Delegation Models

### Static Delegation
- Grant a key ongoing permission to act on the account
- Must be explicitly revoked

### Dynamic Delegation
- Sign a session token with constraints (e.g., `validUntil`, `targetContract`)
- Enforced in `validateUserOp()` by wallet-specific logic (e.g., a plugin or auth module); not natively supported by ERC-4337



## ⚙️ Implementation Notes

- Many ERC-4337 wallets use signature aggregation modules
- Session key delegation can be done via plugin (ERC-6900/7579)
- Tokens or NFTs can act as auth factors (e.g., token gating)

---

## ✅ Summary

Session keys and delegation expand smart account usability across devices and flows. With EIP-7702, even EOAs gain the ability to temporarily act like smart wallets — enabling powerful hybrid UX that balances flexibility, security, and compatibility.