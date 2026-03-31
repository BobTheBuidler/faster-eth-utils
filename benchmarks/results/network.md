#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09058972462499071 | 0.07907737006249249 | 12.71% | 14.56% | 1.15x | ✅ |
| `name_from_chain_id` | 6.47553774806564e-06 | 6.444318913409673e-06 | 0.48% | 0.48% | 1.00x | ✅ |
| `network_from_chain_id` | 6.422771448288637e-06 | 6.349969160135874e-06 | 1.13% | 1.15% | 1.01x | ✅ |
| `short_name_from_chain_id` | 6.592456663373059e-06 | 6.242700292851171e-06 | 5.31% | 5.60% | 1.06x | ✅ |
