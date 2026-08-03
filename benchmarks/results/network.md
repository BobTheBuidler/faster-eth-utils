#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.07235308979998081 | 0.07197489042855361 | 0.52% | 0.53% | 1.01x | ✅ |
| `name_from_chain_id` | 6.4379423098898385e-06 | 6.624743228561203e-06 | -2.90% | -2.82% | 0.97x | ❌ |
| `network_from_chain_id` | 6.342626715633143e-06 | 6.3950668914627665e-06 | -0.83% | -0.82% | 0.99x | ❌ |
| `short_name_from_chain_id` | 6.397403120121543e-06 | 6.58386450016168e-06 | -2.91% | -2.83% | 0.97x | ❌ |
