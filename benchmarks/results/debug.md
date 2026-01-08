#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23079425779999382 | 0.23153058080000619 | -0.32% | -0.32% | 1.00x | ❌ |
| `pip_freeze` | 0.22587804979999646 | 0.2274020541999903 | -0.67% | -0.67% | 0.99x | ❌ |
| `platform_info` | 3.1298734861324104e-06 | 3.445928672205984e-06 | -10.10% | -9.17% | 0.91x | ❌ |
| `python_version` | 1.2769975534275538e-06 | 1.2226872119704501e-06 | 4.25% | 4.44% | 1.04x | ✅ |
