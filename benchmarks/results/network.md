#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09950675926667524 | 0.09032280839997688 | 9.23% | 10.17% | 1.10x | ✅ |
| `name_from_chain_id` | 6.901058181893916e-06 | 5.994172687904758e-06 | 13.14% | 15.13% | 1.15x | ✅ |
| `network_from_chain_id` | 6.884615807545608e-06 | 6.051168290549264e-06 | 12.11% | 13.77% | 1.14x | ✅ |
| `short_name_from_chain_id` | 6.848952306069566e-06 | 6.1709715119398216e-06 | 9.90% | 10.99% | 1.11x | ✅ |
