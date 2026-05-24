#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.12854990519999773 | 0.07552777199999484 | 41.25% | 70.20% | 1.70x | ✅ |
| `name_from_chain_id` | 6.453149351214762e-06 | 6.394528981492241e-06 | 0.91% | 0.92% | 1.01x | ✅ |
| `network_from_chain_id` | 6.389379041538224e-06 | 6.430231563536407e-06 | -0.64% | -0.64% | 0.99x | ❌ |
| `short_name_from_chain_id` | 6.370031158935919e-06 | 6.407522454831413e-06 | -0.59% | -0.59% | 0.99x | ❌ |
