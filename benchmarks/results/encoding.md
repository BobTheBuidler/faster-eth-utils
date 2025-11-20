#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.0132542791634533e-06 | 1.7465334110495253e-06 | 13.25% | 15.27% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.5019380682387307e-06 | 1.3535115556996394e-06 | 9.88% | 10.97% | 1.11x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.6610613081318764e-06 | 1.3860345987839795e-06 | 16.56% | 19.84% | 1.20x | ✅ |
| `big_endian_to_int[one-byte]` | 1.661613984763427e-06 | 1.5148072702805479e-06 | 8.84% | 9.69% | 1.10x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.6586004315025947e-06 | 1.3826071074138437e-06 | 16.64% | 19.96% | 1.20x | ✅ |
| `int_to_big_endian[255]` | 1.4781726470949101e-06 | 1.614899394278276e-06 | -9.25% | -8.47% | 0.92x | ❌ |
| `int_to_big_endian[256]` | 1.4716599919003474e-06 | 1.6095873432818711e-06 | -9.37% | -8.57% | 0.91x | ❌ |
| `int_to_big_endian[max]` | 1.865379557452259e-06 | 1.851522335602311e-06 | 0.74% | 0.75% | 1.01x | ✅ |
| `int_to_big_endian[one]` | 1.4671272700358409e-06 | 1.5919715133531984e-06 | -8.51% | -7.84% | 0.92x | ❌ |
| `int_to_big_endian[zero]` | 1.562094553440097e-06 | 1.693393107297939e-06 | -8.41% | -7.75% | 0.92x | ❌ |
