#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.2767981114864497e-06 | 1.9972349342259422e-06 | 12.28% | 14.00% | 1.14x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.723315633467031e-06 | 1.5805199900456913e-06 | 8.29% | 9.03% | 1.09x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.958074871075913e-06 | 1.7738276100215183e-06 | 9.41% | 10.39% | 1.10x | ✅ |
| `big_endian_to_int[one-byte]` | 1.943560765747887e-06 | 1.7777848220351476e-06 | 8.53% | 9.32% | 1.09x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.89074278781917e-06 | 1.7225094241893213e-06 | 8.90% | 9.77% | 1.10x | ✅ |
| `int_to_big_endian[255]` | 1.5897680576795087e-06 | 8.728071303358282e-07 | 45.10% | 82.14% | 1.82x | ✅ |
| `int_to_big_endian[256]` | 1.5789484200715816e-06 | 8.773242324965296e-07 | 44.44% | 79.97% | 1.80x | ✅ |
| `int_to_big_endian[max]` | 1.9850134406554727e-06 | 1.1119545319773043e-06 | 43.98% | 78.52% | 1.79x | ✅ |
| `int_to_big_endian[one]` | 1.5821344671795234e-06 | 8.701918778136494e-07 | 45.00% | 81.81% | 1.82x | ✅ |
| `int_to_big_endian[zero]` | 1.6661688987633544e-06 | 1.0594362180035144e-06 | 36.41% | 57.27% | 1.57x | ✅ |
