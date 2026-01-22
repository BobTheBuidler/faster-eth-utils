#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0971368411874991 | 0.07852875329412842 | 19.16% | 23.70% | 1.24x | ✅ |
| `name_from_chain_id` | 5.608208385983364e-06 | 5.754003220149317e-06 | -2.60% | -2.53% | 0.97x | ❌ |
| `network_from_chain_id` | 5.641418687658727e-06 | 5.929435989068293e-06 | -5.11% | -4.86% | 0.95x | ❌ |
| `short_name_from_chain_id` | 5.561086949251215e-06 | 5.994596282528594e-06 | -7.80% | -7.23% | 0.93x | ❌ |
