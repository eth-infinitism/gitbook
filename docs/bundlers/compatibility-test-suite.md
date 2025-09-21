
# Compatibility Test Suite

## Overview and link to external bundler conformance test results.

This Bundler Compatibility Test Suite results page serves as a reference for ongoing compatibility testing across bundlers in the ERC-4337 ecosystem.

An external test suite has been developed to verify that bundlers:

- Correctly implement the EntryPoint interface
- Respect simulation and validation rules
- Safely handle edge cases and reverts

---

## 🔍 What’s Being Tested?

- EntryPoint version support (v0.6, v0.7, v0.8)
- Proper `simulateValidation()` implementation
- Bundle construction and submission behavior
- Error reporting and handling

The tests simulate a wide variety of `UserOperations`, from valid edge cases to intentionally malformed payloads.

---

## 🧪 Test Results

Test results are tracked live at:

👉 <a href="https://bundlers.erc4337.io/" target="_blank">https://bundlers.erc4337.io/</a>

This includes:

- A matrix of passing/failing tests for each bundler
- Notes on client-specific quirks or deviations
- Historical conformance data

---

## 🛠️ How to Contribute

Published your own open source bundler? To add your bundler to the list, please [submit a PR](https://github.com/eth-infinitism/bundler-test-executor).

Feedback and patches are encouraged to expand the coverage and ensure consistent behavior across the ecosystem.

---

## ✅ Summary

This test suite helps ecosystem participants confidently choose, integrate, or build bundlers. Check the linked dashboard for up-to-date compliance information.
