#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08365663546666534 | 0.08584789468748966 | -2.62% | -2.55% | 0.97x | ❌ |
| `name_from_chain_id` | 7.309135623241224e-06 | 6.3730874126877515e-06 | 12.81% | 14.69% | 1.15x | ✅ |
| `network_from_chain_id` | 7.030613920180673e-06 | 6.402815398638567e-06 | 8.93% | 9.81% | 1.10x | ✅ |
| `short_name_from_chain_id` | 7.119481075205888e-06 | 6.393438570748224e-06 | 10.20% | 11.36% | 1.11x | ✅ |
