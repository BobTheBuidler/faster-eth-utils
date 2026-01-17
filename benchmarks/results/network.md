#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09138137281249215 | 0.08011801768748938 | 12.33% | 14.06% | 1.14x | ✅ |
| `name_from_chain_id` | 6.994097652178183e-06 | 6.302001553200892e-06 | 9.90% | 10.98% | 1.11x | ✅ |
| `network_from_chain_id` | 6.961061196385928e-06 | 6.357431169766297e-06 | 8.67% | 9.49% | 1.09x | ✅ |
| `short_name_from_chain_id` | 6.994267951556488e-06 | 6.949106672935087e-06 | 0.65% | 0.65% | 1.01x | ✅ |
