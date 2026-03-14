#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09042419818751313 | 0.07950366881248883 | 12.08% | 13.74% | 1.14x | ✅ |
| `name_from_chain_id` | 6.51075195943106e-06 | 6.199892429295565e-06 | 4.77% | 5.01% | 1.05x | ✅ |
| `network_from_chain_id` | 6.504426790968412e-06 | 6.349242327187466e-06 | 2.39% | 2.44% | 1.02x | ✅ |
| `short_name_from_chain_id` | 6.565785492403138e-06 | 6.355415618851983e-06 | 3.20% | 3.31% | 1.03x | ✅ |
