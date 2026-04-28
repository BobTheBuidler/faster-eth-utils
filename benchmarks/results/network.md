#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08952036231250204 | 0.07965770656250726 | 11.02% | 12.38% | 1.12x | ✅ |
| `name_from_chain_id` | 6.180823785040539e-06 | 6.622779000121557e-06 | -7.15% | -6.67% | 0.93x | ❌ |
| `network_from_chain_id` | 6.17774228367048e-06 | 7.03600726823353e-06 | -13.89% | -12.20% | 0.88x | ❌ |
| `short_name_from_chain_id` | 6.201269987206379e-06 | 7.344975700299635e-06 | -18.44% | -15.57% | 0.84x | ❌ |
