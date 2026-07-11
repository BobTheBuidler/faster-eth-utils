#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.2346054932732935e-05 | 1.7145737387619528e-05 | 46.99% | 88.65% | 1.89x | ✅ |
| `keccak[bytes]` | 3.412765319593905e-05 | 1.8975916153178756e-05 | 44.40% | 79.85% | 1.80x | ✅ |
| `keccak[hexstr]` | 4.339138765854655e-05 | 2.0892198523085e-05 | 51.85% | 107.69% | 2.08x | ✅ |
| `keccak[int]` | 9.518660041510666e-05 | 1.979901134443009e-05 | 79.20% | 380.76% | 4.81x | ✅ |
| `keccak[text]` | 3.6575615739137535e-05 | 1.9442172883562624e-05 | 46.84% | 88.13% | 1.88x | ✅ |
