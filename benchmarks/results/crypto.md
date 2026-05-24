#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.3125647056238145e-05 | 1.864693014347671e-05 | 43.71% | 77.65% | 1.78x | ✅ |
| `keccak[bytes]` | 3.536805175561602e-05 | 1.935785955284233e-05 | 45.27% | 82.71% | 1.83x | ✅ |
| `keccak[hexstr]` | 4.335035477858662e-05 | 2.143409358141318e-05 | 50.56% | 102.25% | 2.02x | ✅ |
| `keccak[int]` | 9.605299123150776e-05 | 2.0366502971097044e-05 | 78.80% | 371.62% | 4.72x | ✅ |
| `keccak[text]` | 3.7070511359590904e-05 | 2.0149475574544853e-05 | 45.65% | 83.98% | 1.84x | ✅ |
