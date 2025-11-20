#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 2.9177398065692522e-05 | 1.5609412819362884e-05 | 46.50% | 86.92% | 1.87x | ✅ |
| `keccak[bytes]` | 3.094149623723893e-05 | 1.7356138421468692e-05 | 43.91% | 78.27% | 1.78x | ✅ |
| `keccak[hexstr]` | 3.881743067039129e-05 | 1.9704454833930156e-05 | 49.24% | 97.00% | 1.97x | ✅ |
| `keccak[int]` | 8.599978872556565e-05 | 2.7411904529933758e-05 | 68.13% | 213.73% | 3.14x | ✅ |
| `keccak[text]` | 3.320899981947344e-05 | 1.799143104337108e-05 | 45.82% | 84.58% | 1.85x | ✅ |
