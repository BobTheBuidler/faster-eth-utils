#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08899710599997661 | 0.07870747518751386 | 11.56% | 13.07% | 1.13x | ✅ |
| `name_from_chain_id` | 6.863890133427724e-06 | 6.26016686864455e-06 | 8.80% | 9.64% | 1.10x | ✅ |
| `network_from_chain_id` | 6.958916632183616e-06 | 6.287137159338514e-06 | 9.65% | 10.68% | 1.11x | ✅ |
| `short_name_from_chain_id` | 6.988234630810513e-06 | 6.187497234749154e-06 | 11.46% | 12.94% | 1.13x | ✅ |
