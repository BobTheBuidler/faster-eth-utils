#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.24824085520001518 | 0.2431080149999957 | 2.07% | 2.11% | 1.02x | ✅ |
| `pip_freeze` | 0.24971260499999062 | 0.24771601879999708 | 0.80% | 0.81% | 1.01x | ✅ |
| `platform_info` | 2.9038066878584677e-06 | 3.281958762613955e-06 | -13.02% | -11.52% | 0.88x | ❌ |
| `python_version` | 1.1335438206275218e-06 | 1.4572362622579148e-06 | -28.56% | -22.21% | 0.78x | ❌ |
