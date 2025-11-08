#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23264404099999184 | 0.2315415995999956 | 0.47% | 0.48% | 1.00x | ✅ |
| `pip_freeze` | 0.2309284496000032 | 0.2313899298000024 | -0.20% | -0.20% | 1.00x | ❌ |
| `platform_info` | 3.1547704906237616e-06 | 3.2567828186934236e-06 | -3.23% | -3.13% | 0.97x | ❌ |
| `python_version` | 1.2111080817841707e-06 | 1.2580889686604376e-06 | -3.88% | -3.73% | 0.96x | ❌ |
