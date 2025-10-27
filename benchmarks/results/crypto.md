#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 8.423578500930491e-05 | 6.860351564557868e-05 | 18.56% | 22.79% | 1.23x | ✅ |
| `keccak[bytes]` | 8.636884153630143e-05 | 7.022653715637805e-05 | 18.69% | 22.99% | 1.23x | ✅ |
| `keccak[hexstr]` | 9.596134401590461e-05 | 7.347401358910191e-05 | 23.43% | 30.61% | 1.31x | ✅ |
| `keccak[int]` | 0.00015137116360950092 | 8.144136990407685e-05 | 46.20% | 85.87% | 1.86x | ✅ |
| `keccak[text]` | 8.851004487734413e-05 | 7.114075161151844e-05 | 19.62% | 24.42% | 1.24x | ✅ |
