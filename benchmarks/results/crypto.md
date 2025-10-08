#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 8.399955226020775e-05 | 6.895347330678769e-05 | 17.91% | 21.82% | 1.22x | ✅ |
| `keccak[bytes]` | 8.592109492852146e-05 | 7.034770601447889e-05 | 18.13% | 22.14% | 1.22x | ✅ |
| `keccak[hexstr]` | 9.570088920651054e-05 | 7.428497157132461e-05 | 22.38% | 28.83% | 1.29x | ✅ |
| `keccak[int]` | 0.00015057057110721796 | 8.272794726726656e-05 | 45.06% | 82.01% | 1.82x | ✅ |
| `keccak[text]` | 8.887096717203977e-05 | 7.135501512817108e-05 | 19.71% | 24.55% | 1.25x | ✅ |
