#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.24234906399999545 | 0.249295249599993 | -2.87% | -2.79% | 0.97x | ❌ |
| `pip_freeze` | 0.2470429259999946 | 0.24904396919998817 | -0.81% | -0.80% | 0.99x | ❌ |
| `platform_info` | 3.079993188289547e-06 | 3.65191358904691e-06 | -18.57% | -15.66% | 0.84x | ❌ |
| `python_version` | 1.1767295329581407e-06 | 1.3671712565439658e-06 | -16.18% | -13.93% | 0.86x | ❌ |
