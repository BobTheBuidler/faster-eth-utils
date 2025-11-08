#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08244565785714388 | 0.0628604261999726 | 23.76% | 31.16% | 1.31x | ✅ |
| `name_from_chain_id` | 7.024081274197744e-06 | 6.456160528246006e-06 | 8.09% | 8.80% | 1.09x | ✅ |
| `network_from_chain_id` | 7.039564026147237e-06 | 6.262033925861096e-06 | 11.05% | 12.42% | 1.12x | ✅ |
| `short_name_from_chain_id` | 7.174509430093542e-06 | 6.223992973997859e-06 | 13.25% | 15.27% | 1.15x | ✅ |
