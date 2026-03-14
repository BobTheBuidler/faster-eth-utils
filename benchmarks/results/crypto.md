#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.123638438614482e-05 | 1.703858771348902e-05 | 45.45% | 83.33% | 1.83x | ✅ |
| `keccak[bytes]` | 3.297397680293449e-05 | 1.8888792587279946e-05 | 42.72% | 74.57% | 1.75x | ✅ |
| `keccak[hexstr]` | 4.108650960177406e-05 | 2.0794942872889293e-05 | 49.39% | 97.58% | 1.98x | ✅ |
| `keccak[int]` | 9.416573676581633e-05 | 2.0909125021567923e-05 | 77.80% | 350.36% | 4.50x | ✅ |
| `keccak[text]` | 3.552717793884792e-05 | 1.9369099104460326e-05 | 45.48% | 83.42% | 1.83x | ✅ |
