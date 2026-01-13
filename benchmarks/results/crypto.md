#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.138374301172054e-05 | 1.6905828670787614e-05 | 46.13% | 85.64% | 1.86x | ✅ |
| `keccak[bytes]` | 3.3413910739722055e-05 | 1.888741070579366e-05 | 43.47% | 76.91% | 1.77x | ✅ |
| `keccak[hexstr]` | 4.145023677640801e-05 | 2.118425941048097e-05 | 48.89% | 95.67% | 1.96x | ✅ |
| `keccak[int]` | 9.417784996238284e-05 | 2.8944317780091798e-05 | 69.27% | 225.38% | 3.25x | ✅ |
| `keccak[text]` | 3.553372883129805e-05 | 1.9393807704607094e-05 | 45.42% | 83.22% | 1.83x | ✅ |
