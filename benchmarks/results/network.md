#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08953803212499167 | 0.08266744312501828 | 7.67% | 8.31% | 1.08x | ✅ |
| `name_from_chain_id` | 7.027752891828172e-06 | 6.71493872573941e-06 | 4.45% | 4.66% | 1.05x | ✅ |
| `network_from_chain_id` | 7.1882994262264726e-06 | 6.501274849182763e-06 | 9.56% | 10.57% | 1.11x | ✅ |
| `short_name_from_chain_id` | 6.994532681440007e-06 | 6.166613672928168e-06 | 11.84% | 13.43% | 1.13x | ✅ |
