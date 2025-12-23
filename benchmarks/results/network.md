#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08989525943750465 | 0.081744819249991 | 9.07% | 9.97% | 1.10x | ✅ |
| `name_from_chain_id` | 6.878071557431586e-06 | 6.274614281978704e-06 | 8.77% | 9.62% | 1.10x | ✅ |
| `network_from_chain_id` | 7.1053473807239945e-06 | 6.3824393077439554e-06 | 10.17% | 11.33% | 1.11x | ✅ |
| `short_name_from_chain_id` | 6.995846576320434e-06 | 6.08917538081696e-06 | 12.96% | 14.89% | 1.15x | ✅ |
