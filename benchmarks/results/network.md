#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.061940568800014265 | 0.06216691833333243 | -0.37% | -0.36% | 1.00x | ❌ |
| `name_from_chain_id` | 6.912563861282915e-06 | 6.295357747511258e-06 | 8.93% | 9.80% | 1.10x | ✅ |
| `network_from_chain_id` | 7.0553378096489325e-06 | 6.132876813984073e-06 | 13.07% | 15.04% | 1.15x | ✅ |
| `short_name_from_chain_id` | 7.1429872888607215e-06 | 6.415372954781041e-06 | 10.19% | 11.34% | 1.11x | ✅ |
