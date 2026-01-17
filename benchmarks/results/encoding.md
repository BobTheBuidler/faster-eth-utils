#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3405843310142718e-06 | 2.0398758598752255e-06 | 12.85% | 14.74% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7423497400434744e-06 | 1.603891744988331e-06 | 7.95% | 8.63% | 1.09x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9269767887252775e-06 | 1.6943780262475428e-06 | 12.07% | 13.73% | 1.14x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9242405061991907e-06 | 1.6969506883667636e-06 | 11.81% | 13.39% | 1.13x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.918089065090313e-06 | 1.6874493423576328e-06 | 12.02% | 13.67% | 1.14x | ✅ |
| `int_to_big_endian[255]` | 1.554571751475814e-06 | 1.2939416032304273e-06 | 16.77% | 20.14% | 1.20x | ✅ |
| `int_to_big_endian[256]` | 1.5594850124024812e-06 | 1.2798264833523838e-06 | 17.93% | 21.85% | 1.22x | ✅ |
| `int_to_big_endian[max]` | 1.9447340886600036e-06 | 1.6108507935681162e-06 | 17.17% | 20.73% | 1.21x | ✅ |
| `int_to_big_endian[one]` | 1.5619707440857212e-06 | 1.2750043483451727e-06 | 18.37% | 22.51% | 1.23x | ✅ |
| `int_to_big_endian[zero]` | 1.6641043930620242e-06 | 1.3899456161277498e-06 | 16.47% | 19.72% | 1.20x | ✅ |
