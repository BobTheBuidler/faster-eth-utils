#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.394715717043586e-06 | 2.141222995943097e-06 | 10.59% | 11.84% | 1.12x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7337159835668464e-06 | 1.5540486970348959e-06 | 10.36% | 11.56% | 1.12x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9013657355097216e-06 | 1.5761150663488815e-06 | 17.11% | 20.64% | 1.21x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8882030569557122e-06 | 1.623342763402587e-06 | 14.03% | 16.32% | 1.16x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9092161609602334e-06 | 1.5936867505435079e-06 | 16.53% | 19.80% | 1.20x | ✅ |
| `int_to_big_endian[255]` | 1.5689888903769465e-06 | 1.4386787555161948e-06 | 8.31% | 9.06% | 1.09x | ✅ |
| `int_to_big_endian[256]` | 1.6030564519555193e-06 | 1.438257642879394e-06 | 10.28% | 11.46% | 1.11x | ✅ |
| `int_to_big_endian[max]` | 1.965604867290554e-06 | 1.7732810873354752e-06 | 9.78% | 10.85% | 1.11x | ✅ |
| `int_to_big_endian[one]` | 1.5916799321956254e-06 | 1.4419566205514099e-06 | 9.41% | 10.38% | 1.10x | ✅ |
| `int_to_big_endian[zero]` | 1.7214927603603756e-06 | 1.542531508380556e-06 | 10.40% | 11.60% | 1.12x | ✅ |
