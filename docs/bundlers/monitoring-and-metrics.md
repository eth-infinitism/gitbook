
# Monitoring and Metrics

## How to track and debug bundler performance in ERC-4337 systems.



Running a reliable bundler requires robust observability. From mempool activity to simulation results and gas refunds, operators need insight into every layer of the ERC-4337 stack.

---

## 📊 What to Monitor

### UserOp Lifecycle

- Ingress: Count of UserOps received per second
- Validation results: pass/fail reasons
- Bundle size and frequency
- Inclusion latency (time-to-handleOps)

### Simulation

- Calls to `simulateValidation`
- Revert rates by failure class (signature, paymaster, initCode)
- Gas estimation accuracy

### EntryPoint Interaction

- Successful vs failed `handleOps()` calls
- Average gas used per UserOp
- Revenue tracking: priority fee, refund breakdown

---


## 🔄 Integration with Alerting

- Alert on sudden spikes in rejected UserOps
- Monitor bundler uptime (especially if self-hosted)
- Track deviation between simulated and actual gas usage

---

## ✅ Summary

A performant and trustworthy bundler is a transparent one. Whether you're running infrastructure at scale or testing locally, observability is essential to understanding mempool dynamics, simulation accuracy, and end-to-end UserOp throughput.
