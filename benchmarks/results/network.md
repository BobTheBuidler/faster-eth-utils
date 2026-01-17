#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09066544999999593 | 0.07877987718750035 | 13.11% | 15.09% | 1.15x | ✅ |
| `name_from_chain_id` | 6.789383521411143e-06 | 6.57513986650964e-06 | 3.16% | 3.26% | 1.03x | ✅ |
| `network_from_chain_id` | 6.8577923162722e-06 | 6.0340569741512356e-06 | 12.01% | 13.65% | 1.14x | ✅ |
| `short_name_from_chain_id` | 6.827604162441497e-06 | 6.148887905809705e-06 | 9.94% | 11.04% | 1.11x | ✅ |
