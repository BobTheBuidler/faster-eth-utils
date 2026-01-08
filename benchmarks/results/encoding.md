#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.366532947786782e-06 | 2.2196932706857067e-06 | 6.20% | 6.62% | 1.07x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7994509200045536e-06 | 1.636562900132302e-06 | 9.05% | 9.95% | 1.10x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9534739966690647e-06 | 1.710511722688057e-06 | 12.44% | 14.20% | 1.14x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9787858353261077e-06 | 1.7946651934460207e-06 | 9.30% | 10.26% | 1.10x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9744088585438738e-06 | 1.689889531446702e-06 | 14.41% | 16.84% | 1.17x | ✅ |
| `int_to_big_endian[255]` | 1.5585714084637019e-06 | 1.3196276805719017e-06 | 15.33% | 18.11% | 1.18x | ✅ |
| `int_to_big_endian[256]` | 1.541789330685795e-06 | 1.321617797500493e-06 | 14.28% | 16.66% | 1.17x | ✅ |
| `int_to_big_endian[max]` | 1.8842922314006292e-06 | 1.5938862247195362e-06 | 15.41% | 18.22% | 1.18x | ✅ |
| `int_to_big_endian[one]` | 1.5353195862657221e-06 | 1.2991190559759755e-06 | 15.38% | 18.18% | 1.18x | ✅ |
| `int_to_big_endian[zero]` | 1.648878158721632e-06 | 1.4002496224885095e-06 | 15.08% | 17.76% | 1.18x | ✅ |
