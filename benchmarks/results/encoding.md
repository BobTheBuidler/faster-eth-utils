#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3440170820615745e-06 | 2.0020127223673936e-06 | 14.59% | 17.08% | 1.17x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7571410613225917e-06 | 1.5670169152200524e-06 | 10.82% | 12.13% | 1.12x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.917942209290469e-06 | 1.6179114756021797e-06 | 15.64% | 18.54% | 1.19x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9044582898181048e-06 | 1.6121056382963107e-06 | 15.35% | 18.13% | 1.18x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9272446912247627e-06 | 1.6137742182878688e-06 | 16.27% | 19.42% | 1.19x | ✅ |
| `int_to_big_endian[255]` | 1.5280623142865581e-06 | 1.4352195730007672e-06 | 6.08% | 6.47% | 1.06x | ✅ |
| `int_to_big_endian[256]` | 1.5340698523038372e-06 | 1.3324622206607362e-06 | 13.14% | 15.13% | 1.15x | ✅ |
| `int_to_big_endian[max]` | 1.928901805025988e-06 | 1.7542286761611907e-06 | 9.06% | 9.96% | 1.10x | ✅ |
| `int_to_big_endian[one]` | 1.5296785918253109e-06 | 1.3093916234103605e-06 | 14.40% | 16.82% | 1.17x | ✅ |
| `int_to_big_endian[zero]` | 1.6568662901458426e-06 | 1.4014980301031503e-06 | 15.41% | 18.22% | 1.18x | ✅ |
