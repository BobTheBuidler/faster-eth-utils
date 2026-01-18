#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2277977078000049 | 0.22861374519998207 | -0.36% | -0.36% | 1.00x | ❌ |
| `pip_freeze` | 0.22848887340001056 | 0.2300863186000015 | -0.70% | -0.69% | 0.99x | ❌ |
| `platform_info` | 3.085534120932452e-06 | 3.6734766483448577e-06 | -19.05% | -16.01% | 0.84x | ❌ |
| `python_version` | 1.143057390393047e-06 | 1.38055908531445e-06 | -20.78% | -17.20% | 0.83x | ❌ |
