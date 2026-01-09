#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08903868081250721 | 0.0784197789375014 | 11.93% | 13.54% | 1.14x | ✅ |
| `name_from_chain_id` | 7.010712725469595e-06 | 6.468277880483717e-06 | 7.74% | 8.39% | 1.08x | ✅ |
| `network_from_chain_id` | 6.97119438976719e-06 | 6.195619146368433e-06 | 11.13% | 12.52% | 1.13x | ✅ |
| `short_name_from_chain_id` | 6.989267395348108e-06 | 6.305410735266688e-06 | 9.78% | 10.85% | 1.11x | ✅ |
