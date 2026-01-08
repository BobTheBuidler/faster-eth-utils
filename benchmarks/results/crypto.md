#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.119317702877365e-05 | 1.6805515037077456e-05 | 46.12% | 85.61% | 1.86x | ✅ |
| `keccak[bytes]` | 3.338429815365963e-05 | 1.8826850729538037e-05 | 43.61% | 77.32% | 1.77x | ✅ |
| `keccak[hexstr]` | 4.153215677480466e-05 | 2.123095159135834e-05 | 48.88% | 95.62% | 1.96x | ✅ |
| `keccak[int]` | 9.551959573497874e-05 | 2.8676571330562346e-05 | 69.98% | 233.09% | 3.33x | ✅ |
| `keccak[text]` | 3.547941402721334e-05 | 1.9469542171599512e-05 | 45.12% | 82.23% | 1.82x | ✅ |
