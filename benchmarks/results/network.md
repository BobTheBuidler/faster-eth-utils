#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.07983739387499966 | 0.0856425315882448 | -7.27% | -6.78% | 0.93x | ❌ |
| `name_from_chain_id` | 7.1309060602856756e-06 | 6.437140434115731e-06 | 9.73% | 10.78% | 1.11x | ✅ |
| `network_from_chain_id` | 7.1899095302543284e-06 | 6.215581098184686e-06 | 13.55% | 15.68% | 1.16x | ✅ |
| `short_name_from_chain_id` | 7.037382610784131e-06 | 6.342062298514947e-06 | 9.88% | 10.96% | 1.11x | ✅ |
