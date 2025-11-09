#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.316419571347759e-06 | 1.8674530982100957e-06 | 19.38% | 24.04% | 1.24x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6976563475915496e-06 | 1.4504005394602011e-06 | 14.56% | 17.05% | 1.17x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.8161905154501492e-06 | 1.5158556363358706e-06 | 16.54% | 19.81% | 1.20x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8061780700087897e-06 | 1.5050874859280244e-06 | 16.67% | 20.00% | 1.20x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7972554429685609e-06 | 1.5240969095546815e-06 | 15.20% | 17.92% | 1.18x | ✅ |
| `int_to_big_endian[255]` | 1.6312239223269567e-06 | 1.7320067071158156e-06 | -6.18% | -5.82% | 0.94x | ❌ |
| `int_to_big_endian[256]` | 1.6144769789518451e-06 | 1.7088763723004239e-06 | -5.85% | -5.52% | 0.94x | ❌ |
| `int_to_big_endian[max]` | 1.9665557008864646e-06 | 2.0941406222506343e-06 | -6.49% | -6.09% | 0.94x | ❌ |
| `int_to_big_endian[one]` | 1.7143991554370845e-06 | 1.7158719880455397e-06 | -0.09% | -0.09% | 1.00x | ❌ |
| `int_to_big_endian[zero]` | 1.722989913130457e-06 | 1.790066544998281e-06 | -3.89% | -3.75% | 0.96x | ❌ |
