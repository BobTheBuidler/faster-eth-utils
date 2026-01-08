#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.208595553973035e-05 | 1.68508171760307e-05 | 47.48% | 90.41% | 1.90x | ✅ |
| `keccak[bytes]` | 3.4435747075916387e-05 | 1.8916136232350053e-05 | 45.07% | 82.04% | 1.82x | ✅ |
| `keccak[hexstr]` | 4.289819770384931e-05 | 2.1322611790346753e-05 | 50.29% | 101.19% | 2.01x | ✅ |
| `keccak[int]` | 9.795389361409546e-05 | 2.8577739029034886e-05 | 70.83% | 242.76% | 3.43x | ✅ |
| `keccak[text]` | 3.659905905597128e-05 | 1.9719773419907066e-05 | 46.12% | 85.60% | 1.86x | ✅ |
