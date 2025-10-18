#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.248182064785072e-06 | 2.1248475784791043e-06 | 5.49% | 5.80% | 1.06x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6924308672063912e-06 | 1.4982051705737477e-06 | 11.48% | 12.96% | 1.13x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7963958863853737e-06 | 1.7026442779111222e-06 | 5.22% | 5.51% | 1.06x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8021943678691721e-06 | 1.6973901790958218e-06 | 5.82% | 6.17% | 1.06x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7836156400331397e-06 | 1.6940992764220182e-06 | 5.02% | 5.28% | 1.05x | ✅ |
| `int_to_big_endian[255]` | 1.6292768235210935e-06 | 1.7330311527877414e-06 | -6.37% | -5.99% | 0.94x | ❌ |
| `int_to_big_endian[256]` | 1.6102611583131407e-06 | 1.7224123800320346e-06 | -6.96% | -6.51% | 0.93x | ❌ |
| `int_to_big_endian[max]` | 1.9954641459046596e-06 | 2.074229008903554e-06 | -3.95% | -3.80% | 0.96x | ❌ |
| `int_to_big_endian[one]` | 1.6095583116445655e-06 | 1.726945576253095e-06 | -7.29% | -6.80% | 0.93x | ❌ |
| `int_to_big_endian[zero]` | 1.7017490153153088e-06 | 1.7637090256090408e-06 | -3.64% | -3.51% | 0.96x | ❌ |
