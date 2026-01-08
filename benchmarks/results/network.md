#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08843157350000297 | 0.07835130525000267 | 11.40% | 12.87% | 1.13x | ✅ |
| `name_from_chain_id` | 7.0027368925947004e-06 | 5.96010796568928e-06 | 14.89% | 17.49% | 1.17x | ✅ |
| `network_from_chain_id` | 6.82833695016474e-06 | 6.44556091366542e-06 | 5.61% | 5.94% | 1.06x | ✅ |
| `short_name_from_chain_id` | 6.9566702814864e-06 | 6.188921352564549e-06 | 11.04% | 12.41% | 1.12x | ✅ |
