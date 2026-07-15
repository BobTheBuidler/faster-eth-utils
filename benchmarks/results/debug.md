#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2707474967999929 | 0.2569060989999912 | 5.11% | 5.39% | 1.05x | ✅ |
| `pip_freeze` | 0.2513383480000016 | 0.2545186889999854 | -1.27% | -1.25% | 0.99x | ❌ |
| `platform_info` | 3.0716807920769516e-06 | 3.258356959954178e-06 | -6.08% | -5.73% | 0.94x | ❌ |
| `python_version` | 1.165578019897836e-06 | 1.3418120774494593e-06 | -15.12% | -13.13% | 0.87x | ❌ |
