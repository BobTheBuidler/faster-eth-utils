#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0878156997499957 | 0.08180473549999334 | 6.84% | 7.35% | 1.07x | ✅ |
| `name_from_chain_id` | 7.095996874262669e-06 | 6.608246709424908e-06 | 6.87% | 7.38% | 1.07x | ✅ |
| `network_from_chain_id` | 7.069423497290679e-06 | 6.314945048715776e-06 | 10.67% | 11.95% | 1.12x | ✅ |
| `short_name_from_chain_id` | 6.965353370320911e-06 | 6.741258588399545e-06 | 3.22% | 3.32% | 1.03x | ✅ |
