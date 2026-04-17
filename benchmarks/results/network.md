#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09231865220000372 | 0.08255402100000353 | 10.58% | 11.83% | 1.12x | ✅ |
| `name_from_chain_id` | 6.3006622019920205e-06 | 6.698654813566775e-06 | -6.32% | -5.94% | 0.94x | ❌ |
| `network_from_chain_id` | 6.34520897393895e-06 | 7.260488941192954e-06 | -14.42% | -12.61% | 0.87x | ❌ |
| `short_name_from_chain_id` | 6.347008438365067e-06 | 7.223076528140917e-06 | -13.80% | -12.13% | 0.88x | ❌ |
