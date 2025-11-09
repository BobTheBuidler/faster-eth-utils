#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.130427778780467e-06 | 1.853739338143005e-06 | 12.99% | 14.93% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6616518836230806e-06 | 1.4396377041295212e-06 | 13.36% | 15.42% | 1.15x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.782880905031426e-06 | 1.4758520554734511e-06 | 17.22% | 20.80% | 1.21x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7814282487347026e-06 | 1.4863903069720595e-06 | 16.56% | 19.85% | 1.20x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7590479820215394e-06 | 1.4806208375294989e-06 | 15.83% | 18.80% | 1.19x | ✅ |
| `int_to_big_endian[255]` | 1.5848075291757612e-06 | 1.7710000510993438e-06 | -11.75% | -10.51% | 0.89x | ❌ |
| `int_to_big_endian[256]` | 1.5699479033133615e-06 | 1.6719009561530486e-06 | -6.49% | -6.10% | 0.94x | ❌ |
| `int_to_big_endian[max]` | 1.9073416353644286e-06 | 1.9906503397726857e-06 | -4.37% | -4.18% | 0.96x | ❌ |
| `int_to_big_endian[one]` | 1.5742983976721724e-06 | 1.6759414683811716e-06 | -6.46% | -6.06% | 0.94x | ❌ |
| `int_to_big_endian[zero]` | 1.6864667268476581e-06 | 1.7383402666062872e-06 | -3.08% | -2.98% | 0.97x | ❌ |
