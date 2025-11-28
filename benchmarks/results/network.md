#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0905216260909056 | 0.08255016537501447 | 8.81% | 9.66% | 1.10x | ✅ |
| `name_from_chain_id` | 7.074578658954528e-06 | 6.243778778259907e-06 | 11.74% | 13.31% | 1.13x | ✅ |
| `network_from_chain_id` | 7.053378147767479e-06 | 6.1750051771955035e-06 | 12.45% | 14.22% | 1.14x | ✅ |
| `short_name_from_chain_id` | 7.048713796639746e-06 | 6.208779019926023e-06 | 11.92% | 13.53% | 1.14x | ✅ |
