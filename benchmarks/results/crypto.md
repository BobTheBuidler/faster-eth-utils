#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.115370229524692e-05 | 1.6884884590802724e-05 | 45.80% | 84.51% | 1.85x | ✅ |
| `keccak[bytes]` | 3.3239672428438246e-05 | 1.898093347110915e-05 | 42.90% | 75.12% | 1.75x | ✅ |
| `keccak[hexstr]` | 4.142391878186829e-05 | 2.1128653295827952e-05 | 48.99% | 96.06% | 1.96x | ✅ |
| `keccak[int]` | 9.336226336107465e-05 | 2.8380422233691705e-05 | 69.60% | 228.97% | 3.29x | ✅ |
| `keccak[text]` | 3.548494375611129e-05 | 1.958020072339279e-05 | 44.82% | 81.23% | 1.81x | ✅ |
