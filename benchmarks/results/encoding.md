#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 1.961316598906103e-06 | 1.9694888082691168e-06 | -0.42% | -0.41% | 1.00x | ❌ |
| `big_endian_to_int[empty-bytes]` | 1.480110748020507e-06 | 1.4468096851822304e-06 | 2.25% | 2.30% | 1.02x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.626288219939419e-06 | 1.5957766469448094e-06 | 1.88% | 1.91% | 1.02x | ✅ |
| `big_endian_to_int[one-byte]` | 1.6291255050006089e-06 | 1.672595901319229e-06 | -2.67% | -2.60% | 0.97x | ❌ |
| `big_endian_to_int[two-bytes]` | 1.6038543487235167e-06 | 1.581692182534837e-06 | 1.38% | 1.40% | 1.01x | ✅ |
| `int_to_big_endian[255]` | 1.3600004472386631e-06 | 8.347851885702905e-07 | 38.62% | 62.92% | 1.63x | ✅ |
| `int_to_big_endian[256]` | 1.3594081867333068e-06 | 8.222468479132052e-07 | 39.51% | 65.33% | 1.65x | ✅ |
| `int_to_big_endian[max]` | 1.7432990615145632e-06 | 1.05327211898224e-06 | 39.58% | 65.51% | 1.66x | ✅ |
| `int_to_big_endian[one]` | 1.352779900616492e-06 | 8.294124855816904e-07 | 38.69% | 63.10% | 1.63x | ✅ |
| `int_to_big_endian[zero]` | 1.350780689266111e-06 | 9.113591147188681e-07 | 32.53% | 48.22% | 1.48x | ✅ |
