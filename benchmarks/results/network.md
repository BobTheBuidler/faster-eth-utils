#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0888404936250069 | 0.0800038365624971 | 9.95% | 11.05% | 1.11x | ✅ |
| `name_from_chain_id` | 6.7514403560934274e-06 | 6.528210127455561e-06 | 3.31% | 3.42% | 1.03x | ✅ |
| `network_from_chain_id` | 6.717287086011746e-06 | 6.102366883201858e-06 | 9.15% | 10.08% | 1.10x | ✅ |
| `short_name_from_chain_id` | 6.846820590950856e-06 | 6.021660482374559e-06 | 12.05% | 13.70% | 1.14x | ✅ |
