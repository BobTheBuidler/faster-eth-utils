#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08204119749997776 | 0.08054842900000547 | 1.82% | 1.85% | 1.02x | ✅ |
| `name_from_chain_id` | 7.160975404104513e-06 | 6.26033938448929e-06 | 12.58% | 14.39% | 1.14x | ✅ |
| `network_from_chain_id` | 7.216641848608394e-06 | 7.160561753508896e-06 | 0.78% | 0.78% | 1.01x | ✅ |
| `short_name_from_chain_id` | 7.190332866025938e-06 | 6.24350465571396e-06 | 13.17% | 15.17% | 1.15x | ✅ |
