#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.119115875784329e-05 | 1.6842832339897864e-05 | 46.00% | 85.19% | 1.85x | ✅ |
| `keccak[bytes]` | 3.322113679528832e-05 | 1.8889511342530457e-05 | 43.14% | 75.87% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.129996726308913e-05 | 2.1320825691554062e-05 | 48.38% | 93.71% | 1.94x | ✅ |
| `keccak[int]` | 9.378251728366354e-05 | 2.8686787209372798e-05 | 69.41% | 226.92% | 3.27x | ✅ |
| `keccak[text]` | 3.5556675276803045e-05 | 1.9499256485651864e-05 | 45.16% | 82.35% | 1.82x | ✅ |
