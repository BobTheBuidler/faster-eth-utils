#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.30434619099997917 | 0.3025692637999896 | 0.58% | 0.59% | 1.01x | ✅ |
| `pip_freeze` | 0.29416326279999794 | 0.2983381386000019 | -1.42% | -1.40% | 0.99x | ❌ |
| `platform_info` | 2.5609205483480563e-06 | 3.1052548545549663e-06 | -21.26% | -17.53% | 0.82x | ❌ |
| `python_version` | 1.1036042344478888e-06 | 1.3104644517299396e-06 | -18.74% | -15.79% | 0.84x | ❌ |
