#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.107115504704398e-05 | 1.6590355660244937e-05 | 46.61% | 87.28% | 1.87x | ✅ |
| `keccak[bytes]` | 3.2907385724565205e-05 | 1.849641495747037e-05 | 43.79% | 77.91% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.0872316469422104e-05 | 2.0495797650703683e-05 | 49.85% | 99.42% | 1.99x | ✅ |
| `keccak[int]` | 9.140515573543683e-05 | 2.0303615608790712e-05 | 77.79% | 350.19% | 4.50x | ✅ |
| `keccak[text]` | 3.4649088878041354e-05 | 1.9347624654558062e-05 | 44.16% | 79.09% | 1.79x | ✅ |
