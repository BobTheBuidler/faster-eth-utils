#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0706808330000058 | 0.08818411313332793 | -24.76% | -19.85% | 0.80x | ❌ |
| `name_from_chain_id` | 6.42989032685663e-06 | 6.758690185446236e-06 | -5.11% | -4.86% | 0.95x | ❌ |
| `network_from_chain_id` | 6.469181909774725e-06 | 6.748441214682261e-06 | -4.32% | -4.14% | 0.96x | ❌ |
| `short_name_from_chain_id` | 6.454077891965491e-06 | 6.649413216363211e-06 | -3.03% | -2.94% | 0.97x | ❌ |
