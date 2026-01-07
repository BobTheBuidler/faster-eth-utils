#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09049511193748572 | 0.07894643187498929 | 12.76% | 14.63% | 1.15x | ✅ |
| `name_from_chain_id` | 6.962444230815382e-06 | 6.20046336263255e-06 | 10.94% | 12.29% | 1.12x | ✅ |
| `network_from_chain_id` | 7.086019670593704e-06 | 6.123371919972462e-06 | 13.59% | 15.72% | 1.16x | ✅ |
| `short_name_from_chain_id` | 7.055714451355992e-06 | 7.239138360804061e-06 | -2.60% | -2.53% | 0.97x | ❌ |
