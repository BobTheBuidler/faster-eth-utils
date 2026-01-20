#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0920508517500096 | 0.08314451693750868 | 9.68% | 10.71% | 1.11x | ✅ |
| `name_from_chain_id` | 7.0008904524623706e-06 | 6.53957448632157e-06 | 6.59% | 7.05% | 1.07x | ✅ |
| `network_from_chain_id` | 6.982811551379557e-06 | 6.377227815414425e-06 | 8.67% | 9.50% | 1.09x | ✅ |
| `short_name_from_chain_id` | 6.980270017511932e-06 | 6.373314679245429e-06 | 8.70% | 9.52% | 1.10x | ✅ |
