#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.2198687672330514e-06 | 2.2909354901902997e-06 | -3.20% | -3.10% | 0.97x | ❌ |
| `big_endian_to_int[empty-bytes]` | 1.7226669363464182e-06 | 1.7150521750260051e-06 | 0.44% | 0.44% | 1.00x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9316880380996755e-06 | 1.898229141078304e-06 | 1.73% | 1.76% | 1.02x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9424408551912714e-06 | 1.8045858371668753e-06 | 7.10% | 7.64% | 1.08x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.966110264269512e-06 | 1.805946170775126e-06 | 8.15% | 8.87% | 1.09x | ✅ |
| `int_to_big_endian[255]` | 1.5776349718861706e-06 | 1.6035550864799228e-06 | -1.64% | -1.62% | 0.98x | ❌ |
| `int_to_big_endian[256]` | 1.5939216500780576e-06 | 1.6038604348281435e-06 | -0.62% | -0.62% | 0.99x | ❌ |
| `int_to_big_endian[max]` | 2.0027991249591745e-06 | 2.0302815328778656e-06 | -1.37% | -1.35% | 0.99x | ❌ |
| `int_to_big_endian[one]` | 1.57121215000109e-06 | 1.5857846670887414e-06 | -0.93% | -0.92% | 0.99x | ❌ |
| `int_to_big_endian[zero]` | 1.6291257410943636e-06 | 1.6500941708933679e-06 | -1.29% | -1.27% | 0.99x | ❌ |
