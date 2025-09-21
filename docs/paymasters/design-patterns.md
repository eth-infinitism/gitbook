
# Design Patterns

## Practical design approaches for safe, scalable, and efficient Paymasters.


Beyond basic logic, well-architected Paymasters benefit from patterns that improve security, flexibility, and user experience. This section outlines common design techniques used in production-ready Paymasters.

---

## 🧰 Whitelist with Expiry

Grant gas sponsorship based on a short-lived whitelist:

- Store (address => expiry timestamp) mapping
- Only allow `validatePaymasterUserOp()` if `now < expiry`
- Good for beta access or trial runs

---

## 🔐 Signed API Approvals

The off-chain component signs metadata that gets embedded in `paymasterAndData`:

- Signature includes sender, callData hash, deadline, quota
- Contract validates signature on-chain
- Prevents reuse or forgery; allows detailed policies

---

## ⏳ Rate Limits and Quotas

Track per-user limits:

- Tx count per hour
- Gas budget per week
- Use a rolling window or resettable counter

Store these in ephemeral in-memory maps or external storage if staked.

---

## 💸 ERC-20 Gas Payment with Allowance

Let users pre-approve ERC-20 tokens:

- Call `transferFrom()` in `postOp()`
- Pull tokens only after successful execution
- Ensure price quotes are stable and front-run resistant

---

## 📉 Fallback and Failover Logic

If a Paymaster becomes invalid or fails:

- Fallback to an unauthenticated Paymaster for emergency gas
- Use `context` returned by `validatePaymasterUserOp()` to pass failover hints

---

## 🔄 Modular Composition

Split Paymaster logic into modules:

- Ruleset manager (e.g. quotas, blocklists)
- Signature verifier
- Gas accounting engine

This makes audits easier and allows permissionless extensions.

---

## 📘 ERC-7677 Standard

[ERC-7677](https://eips.ethereum.org/EIPS/eip-7677) standardizes the Paymaster interface and lifecycle for ERC-4337 systems. It defines:

- Minimal required methods
- Paymaster staking rules
- Shared validation behaviors

This makes it easier for bundlers and wallets to interoperate with any compliant Paymaster contract. If you're building a general-purpose or pluggable Paymaster, following ERC-7677 is highly recommended.

## ✅ Summary

Robust Paymasters combine simplicity with modular safeguards. These design patterns enable scalable sponsorship logic while defending against abuse, ensuring safe interaction between bundlers, users, and dApps.
