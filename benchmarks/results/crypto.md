#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.118484671294364e-05 | 1.685450445052086e-05 | 45.95% | 85.02% | 1.85x | ✅ |
| `keccak[bytes]` | 3.3481048452435207e-05 | 1.892321656719374e-05 | 43.48% | 76.93% | 1.77x | ✅ |
| `keccak[hexstr]` | 4.128629818304689e-05 | 2.1263452037239274e-05 | 48.50% | 94.17% | 1.94x | ✅ |
| `keccak[int]` | 9.435431627407759e-05 | 2.87302353332752e-05 | 69.55% | 228.41% | 3.28x | ✅ |
| `keccak[text]` | 3.54415625369047e-05 | 1.9646590335911683e-05 | 44.57% | 80.40% | 1.80x | ✅ |
