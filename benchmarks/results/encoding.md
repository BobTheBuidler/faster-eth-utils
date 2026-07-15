#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.2757914305032417e-06 | 2.1655204029439834e-06 | 4.85% | 5.09% | 1.05x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.8449473329540995e-06 | 1.6433551045351681e-06 | 10.93% | 12.27% | 1.12x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9447867789969172e-06 | 1.8082706878811497e-06 | 7.02% | 7.55% | 1.08x | ✅ |
| `big_endian_to_int[one-byte]` | 1.955664843895188e-06 | 1.9119719738068556e-06 | 2.23% | 2.29% | 1.02x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.8994367300831507e-06 | 1.7786859485184713e-06 | 6.36% | 6.79% | 1.07x | ✅ |
| `int_to_big_endian[255]` | 1.710496217864501e-06 | 1.0357811977622998e-06 | 39.45% | 65.14% | 1.65x | ✅ |
| `int_to_big_endian[256]` | 1.594962137252691e-06 | 9.37044107834972e-07 | 41.25% | 70.21% | 1.70x | ✅ |
| `int_to_big_endian[max]` | 1.9885114922429658e-06 | 1.171559426753324e-06 | 41.08% | 69.73% | 1.70x | ✅ |
| `int_to_big_endian[one]` | 1.5923154241058239e-06 | 9.501973316834083e-07 | 40.33% | 67.58% | 1.68x | ✅ |
| `int_to_big_endian[zero]` | 1.668366769454113e-06 | 1.1003846798405825e-06 | 34.04% | 51.62% | 1.52x | ✅ |
