#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.074813611250003 | 0.07680822529409718 | -2.67% | -2.60% | 0.97x | ❌ |
| `name_from_chain_id` | 7.04074760226392e-06 | 6.137969533316037e-06 | 12.82% | 14.71% | 1.15x | ✅ |
| `network_from_chain_id` | 6.902294102596962e-06 | 6.187834933964525e-06 | 10.35% | 11.55% | 1.12x | ✅ |
| `short_name_from_chain_id` | 7.047981966729143e-06 | 6.236730446642331e-06 | 11.51% | 13.01% | 1.13x | ✅ |
