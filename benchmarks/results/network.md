#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.07385082399998737 | 0.09470709307142654 | -28.24% | -22.02% | 0.78x | ❌ |
| `name_from_chain_id` | 6.2628595414705305e-06 | 6.204070115445831e-06 | 0.94% | 0.95% | 1.01x | ✅ |
| `network_from_chain_id` | 6.226092393245203e-06 | 6.16275705372646e-06 | 1.02% | 1.03% | 1.01x | ✅ |
| `short_name_from_chain_id` | 6.141207968480507e-06 | 6.546209934686229e-06 | -6.59% | -6.19% | 0.94x | ❌ |
