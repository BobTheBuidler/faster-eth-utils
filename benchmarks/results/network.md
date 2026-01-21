#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08415578994118157 | 0.07255167050000308 | 13.79% | 15.99% | 1.16x | ✅ |
| `name_from_chain_id` | 6.4825289470518234e-06 | 6.524135656938551e-06 | -0.64% | -0.64% | 0.99x | ❌ |
| `network_from_chain_id` | 6.4530323132528915e-06 | 5.978303934989352e-06 | 7.36% | 7.94% | 1.08x | ✅ |
| `short_name_from_chain_id` | 6.593517509991253e-06 | 5.957622475062826e-06 | 9.64% | 10.67% | 1.11x | ✅ |
