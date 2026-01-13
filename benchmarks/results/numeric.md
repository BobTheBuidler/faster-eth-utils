#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.422255562335518e-05 | 6.636246844663471e-05 | 10.59% | 11.84% | 1.12x | ✅ |
| `clamp[at-lower]` | 7.30135950652063e-05 | 6.506897329792501e-05 | 10.88% | 12.21% | 1.12x | ✅ |
| `clamp[at-upper]` | 7.376281866800821e-05 | 6.456532190652137e-05 | 12.47% | 14.25% | 1.14x | ✅ |
| `clamp[below-lower]` | 6.814159020791928e-05 | 5.688464732098336e-05 | 16.52% | 19.79% | 1.20x | ✅ |
| `clamp[within-bounds]` | 7.273161552294593e-05 | 6.526402579848153e-05 | 10.27% | 11.44% | 1.11x | ✅ |
