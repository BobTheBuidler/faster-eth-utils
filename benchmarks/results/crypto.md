#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1790541323187175e-05 | 1.6714037627366625e-05 | 47.42% | 90.20% | 1.90x | ✅ |
| `keccak[bytes]` | 3.3451729767790585e-05 | 1.848676572118014e-05 | 44.74% | 80.95% | 1.81x | ✅ |
| `keccak[hexstr]` | 4.163728881515681e-05 | 2.1051883862118683e-05 | 49.44% | 97.78% | 1.98x | ✅ |
| `keccak[int]` | 9.312143062806912e-05 | 2.8222256956887237e-05 | 69.69% | 229.96% | 3.30x | ✅ |
| `keccak[text]` | 3.5399686371281525e-05 | 1.937024825504063e-05 | 45.28% | 82.75% | 1.83x | ✅ |
