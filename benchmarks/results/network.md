#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09386079668750114 | 0.08061374506250729 | 14.11% | 16.43% | 1.16x | ✅ |
| `name_from_chain_id` | 7.0258467669974755e-06 | 6.2133205048584214e-06 | 11.56% | 13.08% | 1.13x | ✅ |
| `network_from_chain_id` | 6.854362031459891e-06 | 6.009103392482243e-06 | 12.33% | 14.07% | 1.14x | ✅ |
| `short_name_from_chain_id` | 6.864961622089754e-06 | 6.8514723948743624e-06 | 0.20% | 0.20% | 1.00x | ✅ |
