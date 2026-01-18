#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09026871306250683 | 0.07883431850000022 | 12.67% | 14.50% | 1.15x | ✅ |
| `name_from_chain_id` | 7.02563521948622e-06 | 6.748746101934972e-06 | 3.94% | 4.10% | 1.04x | ✅ |
| `network_from_chain_id` | 6.920832634215594e-06 | 6.300005637580938e-06 | 8.97% | 9.85% | 1.10x | ✅ |
| `short_name_from_chain_id` | 6.997888928405898e-06 | 6.204618164817105e-06 | 11.34% | 12.79% | 1.13x | ✅ |
