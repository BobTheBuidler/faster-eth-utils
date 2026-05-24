#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.07038600839998707 | 0.08798377100000986 | -25.00% | -20.00% | 0.80x | ❌ |
| `name_from_chain_id` | 6.731144189060573e-06 | 6.7942632074854815e-06 | -0.94% | -0.93% | 0.99x | ❌ |
| `network_from_chain_id` | 6.642851533868819e-06 | 6.596889203944508e-06 | 0.69% | 0.70% | 1.01x | ✅ |
| `short_name_from_chain_id` | 6.888853710654083e-06 | 6.670272852497731e-06 | 3.17% | 3.28% | 1.03x | ✅ |
