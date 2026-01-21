#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 2.9297828086135356e-05 | 1.6520257745293866e-05 | 43.61% | 77.34% | 1.77x | ✅ |
| `keccak[bytes]` | 3.147797122928794e-05 | 1.7880438033421785e-05 | 43.20% | 76.05% | 1.76x | ✅ |
| `keccak[hexstr]` | 3.915527240833659e-05 | 2.0062436747549868e-05 | 48.76% | 95.17% | 1.95x | ✅ |
| `keccak[int]` | 8.887237775133958e-05 | 1.9390475254143367e-05 | 78.18% | 358.33% | 4.58x | ✅ |
| `keccak[text]` | 3.415438535535011e-05 | 1.8905845883226598e-05 | 44.65% | 80.66% | 1.81x | ✅ |
