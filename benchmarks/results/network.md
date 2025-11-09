#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08278545437500284 | 0.08227223668750128 | 0.62% | 0.62% | 1.01x | ✅ |
| `name_from_chain_id` | 7.1194987496336e-06 | 6.3280917727904705e-06 | 11.12% | 12.51% | 1.13x | ✅ |
| `network_from_chain_id` | 7.039723128087882e-06 | 6.088136294946483e-06 | 13.52% | 15.63% | 1.16x | ✅ |
| `short_name_from_chain_id` | 7.101282697743596e-06 | 6.3646923428135216e-06 | 10.37% | 11.57% | 1.12x | ✅ |
