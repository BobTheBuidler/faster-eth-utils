#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09003390253845876 | 0.08498297306249825 | 5.61% | 5.94% | 1.06x | ✅ |
| `name_from_chain_id` | 6.957552525232784e-06 | 6.520681026561255e-06 | 6.28% | 6.70% | 1.07x | ✅ |
| `network_from_chain_id` | 6.970355706588611e-06 | 6.137029587104957e-06 | 11.96% | 13.58% | 1.14x | ✅ |
| `short_name_from_chain_id` | 6.9863224908247e-06 | 6.483483399842973e-06 | 7.20% | 7.76% | 1.08x | ✅ |
