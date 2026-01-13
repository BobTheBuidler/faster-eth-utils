#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09252342462499996 | 0.08148727174999237 | 11.93% | 13.54% | 1.14x | ✅ |
| `name_from_chain_id` | 6.95613930596249e-06 | 6.736299498089753e-06 | 3.16% | 3.26% | 1.03x | ✅ |
| `network_from_chain_id` | 6.944289152467802e-06 | 6.105687192485361e-06 | 12.08% | 13.73% | 1.14x | ✅ |
| `short_name_from_chain_id` | 6.984678096575078e-06 | 6.1915187180855125e-06 | 11.36% | 12.81% | 1.13x | ✅ |
