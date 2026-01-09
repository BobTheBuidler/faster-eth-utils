#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.319845601015094e-05 | 6.616527453816412e-05 | 9.61% | 10.63% | 1.11x | ✅ |
| `clamp[at-lower]` | 7.296498255929674e-05 | 6.615398680550894e-05 | 9.33% | 10.30% | 1.10x | ✅ |
| `clamp[at-upper]` | 7.201846810755334e-05 | 6.803234215412062e-05 | 5.53% | 5.86% | 1.06x | ✅ |
| `clamp[below-lower]` | 6.69501541191349e-05 | 5.8215940942125097e-05 | 13.05% | 15.00% | 1.15x | ✅ |
| `clamp[within-bounds]` | 7.253597227124868e-05 | 6.782181572165744e-05 | 6.50% | 6.95% | 1.07x | ✅ |
