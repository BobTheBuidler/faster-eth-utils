#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.22963362660000258 | 0.2289316782000242 | 0.31% | 0.31% | 1.00x | ✅ |
| `pip_freeze` | 0.228974251000011 | 0.22909329760002492 | -0.05% | -0.05% | 1.00x | ❌ |
| `platform_info` | 3.105947232662206e-06 | 3.6759920962600905e-06 | -18.35% | -15.51% | 0.84x | ❌ |
| `python_version` | 1.1717505907618859e-06 | 1.3720774792909259e-06 | -17.10% | -14.60% | 0.85x | ❌ |
