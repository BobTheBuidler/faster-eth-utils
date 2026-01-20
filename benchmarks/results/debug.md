#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2392537156000003 | 0.23265604720000965 | 2.76% | 2.84% | 1.03x | ✅ |
| `pip_freeze` | 0.23451975679998896 | 0.2338851190000014 | 0.27% | 0.27% | 1.00x | ✅ |
| `platform_info` | 3.0811247079656192e-06 | 3.6636805265621906e-06 | -18.91% | -15.90% | 0.84x | ❌ |
| `python_version` | 1.2015619158136106e-06 | 1.4186294107443902e-06 | -18.07% | -15.30% | 0.85x | ❌ |
