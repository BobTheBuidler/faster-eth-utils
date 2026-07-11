#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.07114828779999698 | 0.09009578899998262 | -26.63% | -21.03% | 0.79x | ❌ |
| `name_from_chain_id` | 6.555414607343164e-06 | 6.666548944679591e-06 | -1.70% | -1.67% | 0.98x | ❌ |
| `network_from_chain_id` | 6.589203718688364e-06 | 6.821023566765197e-06 | -3.52% | -3.40% | 0.97x | ❌ |
| `short_name_from_chain_id` | 6.674243318063795e-06 | 6.4626406042119955e-06 | 3.17% | 3.27% | 1.03x | ✅ |
