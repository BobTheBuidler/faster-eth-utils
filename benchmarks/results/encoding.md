#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1764981656739e-06 | 1.9729574828604132e-06 | 9.35% | 10.32% | 1.10x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7078180221920848e-06 | 1.6167685394458913e-06 | 5.33% | 5.63% | 1.06x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.8206999201050716e-06 | 1.6680779520349202e-06 | 8.38% | 9.15% | 1.09x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8183480070057348e-06 | 1.6809442617836952e-06 | 7.56% | 8.17% | 1.08x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.8029805918962391e-06 | 1.6700313328921244e-06 | 7.37% | 7.96% | 1.08x | ✅ |
| `int_to_big_endian[255]` | 1.6017817712317278e-06 | 1.7245714668782739e-06 | -7.67% | -7.12% | 0.93x | ❌ |
| `int_to_big_endian[256]` | 1.5898983907395852e-06 | 1.7191889513337539e-06 | -8.13% | -7.52% | 0.92x | ❌ |
| `int_to_big_endian[max]` | 1.9615277049424943e-06 | 2.0883641393505876e-06 | -6.47% | -6.07% | 0.94x | ❌ |
| `int_to_big_endian[one]` | 1.6258198533316463e-06 | 1.7227303863592463e-06 | -5.96% | -5.63% | 0.94x | ❌ |
| `int_to_big_endian[zero]` | 1.7069967038090195e-06 | 1.7772203531130263e-06 | -4.11% | -3.95% | 0.96x | ❌ |
