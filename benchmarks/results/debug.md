#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.21540162039999586 | 0.2146958429999927 | 0.33% | 0.33% | 1.00x | ✅ |
| `pip_freeze` | 0.21543297379998877 | 0.21956387960000256 | -1.92% | -1.88% | 0.98x | ❌ |
| `platform_info` | 2.462349324090619e-06 | 2.537460577619326e-06 | -3.05% | -2.96% | 0.97x | ❌ |
| `python_version` | 9.73958276535589e-07 | 1.245043144453106e-06 | -27.83% | -21.77% | 0.78x | ❌ |
