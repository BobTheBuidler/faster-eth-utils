#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1869154170943244e-06 | 1.979973172366961e-06 | 9.46% | 10.45% | 1.10x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6846252027256636e-06 | 1.497269690139669e-06 | 11.12% | 12.51% | 1.13x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7950081872147232e-06 | 1.5252260486212265e-06 | 15.03% | 17.69% | 1.18x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8056804413319156e-06 | 1.521386486740309e-06 | 15.74% | 18.69% | 1.19x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.766199054842615e-06 | 1.5329760954839023e-06 | 13.20% | 15.21% | 1.15x | ✅ |
| `int_to_big_endian[255]` | 1.5762537670042328e-06 | 1.697567787752612e-06 | -7.70% | -7.15% | 0.93x | ❌ |
| `int_to_big_endian[256]` | 1.5929966296244727e-06 | 1.6951702904239005e-06 | -6.41% | -6.03% | 0.94x | ❌ |
| `int_to_big_endian[max]` | 1.926814316094008e-06 | 1.937995466031393e-06 | -0.58% | -0.58% | 0.99x | ❌ |
| `int_to_big_endian[one]` | 1.5924748596570574e-06 | 1.6867366062857634e-06 | -5.92% | -5.59% | 0.94x | ❌ |
| `int_to_big_endian[zero]` | 1.6874109985482897e-06 | 1.7450723847619866e-06 | -3.42% | -3.30% | 0.97x | ❌ |
