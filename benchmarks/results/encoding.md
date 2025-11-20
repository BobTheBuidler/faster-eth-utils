#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1578437073575916e-06 | 1.862463429384789e-06 | 13.69% | 15.86% | 1.16x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6716247963184227e-06 | 1.46144596579746e-06 | 12.57% | 14.38% | 1.14x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7891375362338168e-06 | 1.5829092449150173e-06 | 11.53% | 13.03% | 1.13x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7706287190538424e-06 | 1.4964568244930967e-06 | 15.48% | 18.32% | 1.18x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7813356711654208e-06 | 1.49371763169936e-06 | 16.15% | 19.26% | 1.19x | ✅ |
| `int_to_big_endian[255]` | 1.59557387608084e-06 | 1.7082397497696862e-06 | -7.06% | -6.60% | 0.93x | ❌ |
| `int_to_big_endian[256]` | 1.610688822879765e-06 | 1.6792586250295565e-06 | -4.26% | -4.08% | 0.96x | ❌ |
| `int_to_big_endian[max]` | 1.9390618987273534e-06 | 2.0693319726512254e-06 | -6.72% | -6.30% | 0.94x | ❌ |
| `int_to_big_endian[one]` | 1.5839739808798013e-06 | 1.691360442720806e-06 | -6.78% | -6.35% | 0.94x | ❌ |
| `int_to_big_endian[zero]` | 1.6815339696827789e-06 | 1.7626196513346404e-06 | -4.82% | -4.60% | 0.95x | ❌ |
