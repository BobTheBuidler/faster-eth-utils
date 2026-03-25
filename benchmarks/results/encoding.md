#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.439000076989789e-06 | 2.1343784813257757e-06 | 12.49% | 14.27% | 1.14x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7359717294628567e-06 | 1.54644394759766e-06 | 10.92% | 12.26% | 1.12x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.8754848440483007e-06 | 1.5906343936990648e-06 | 15.19% | 17.91% | 1.18x | ✅ |
| `big_endian_to_int[one-byte]` | 1.889152369864806e-06 | 1.5831561896551247e-06 | 16.20% | 19.33% | 1.19x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.891379187725675e-06 | 1.5738920281621202e-06 | 16.79% | 20.17% | 1.20x | ✅ |
| `int_to_big_endian[255]` | 1.5118628535181505e-06 | 1.4530990584954297e-06 | 3.89% | 4.04% | 1.04x | ✅ |
| `int_to_big_endian[256]` | 1.5579538593443515e-06 | 1.4632500645846068e-06 | 6.08% | 6.47% | 1.06x | ✅ |
| `int_to_big_endian[max]` | 1.9041026815937002e-06 | 1.766303213814117e-06 | 7.24% | 7.80% | 1.08x | ✅ |
| `int_to_big_endian[one]` | 1.5310814383497162e-06 | 1.4479617851512114e-06 | 5.43% | 5.74% | 1.06x | ✅ |
| `int_to_big_endian[zero]` | 1.6855991997690347e-06 | 1.5380813870201571e-06 | 8.75% | 9.59% | 1.10x | ✅ |
