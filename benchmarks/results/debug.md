#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2607430179999938 | 0.2517382102000056 | 3.45% | 3.58% | 1.04x | ✅ |
| `pip_freeze` | 0.250283072000002 | 0.27380006460001594 | -9.40% | -8.59% | 0.91x | ❌ |
| `platform_info` | 2.9423615487046914e-06 | 3.3206060985318942e-06 | -12.86% | -11.39% | 0.89x | ❌ |
| `python_version` | 1.1301793570480583e-06 | 1.3702071647151257e-06 | -21.24% | -17.52% | 0.82x | ❌ |
