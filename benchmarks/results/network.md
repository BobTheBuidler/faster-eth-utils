#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09088309779998932 | 0.0786357249999945 | 13.48% | 15.57% | 1.16x | ✅ |
| `name_from_chain_id` | 6.9774939259276895e-06 | 6.171954292567006e-06 | 11.54% | 13.05% | 1.13x | ✅ |
| `network_from_chain_id` | 6.972189212472796e-06 | 6.7346974232858835e-06 | 3.41% | 3.53% | 1.04x | ✅ |
| `short_name_from_chain_id` | 6.9718262878938705e-06 | 6.157429144967384e-06 | 11.68% | 13.23% | 1.13x | ✅ |
