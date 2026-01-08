#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23610049100001335 | 0.23590035700000273 | 0.08% | 0.08% | 1.00x | ✅ |
| `pip_freeze` | 0.23578528740000593 | 0.23690887240001074 | -0.48% | -0.47% | 1.00x | ❌ |
| `platform_info` | 3.126739581989687e-06 | 3.47703645884863e-06 | -11.20% | -10.07% | 0.90x | ❌ |
| `python_version` | 1.17946308651578e-06 | 1.3480374900121258e-06 | -14.29% | -12.51% | 0.87x | ❌ |
