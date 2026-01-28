#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09335188862499422 | 0.07950656493749975 | 14.83% | 17.41% | 1.17x | ✅ |
| `name_from_chain_id` | 6.9079143725073545e-06 | 6.807302232981306e-06 | 1.46% | 1.48% | 1.01x | ✅ |
| `network_from_chain_id` | 6.928978104644071e-06 | 6.439404065230849e-06 | 7.07% | 7.60% | 1.08x | ✅ |
| `short_name_from_chain_id` | 6.94530644327583e-06 | 6.221782865574192e-06 | 10.42% | 11.63% | 1.12x | ✅ |
