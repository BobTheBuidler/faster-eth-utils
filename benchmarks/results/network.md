#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0799612040666678 | 0.08609676129412278 | -7.67% | -7.13% | 0.93x | ❌ |
| `name_from_chain_id` | 5.601198464920872e-06 | 5.580518420699844e-06 | 0.37% | 0.37% | 1.00x | ✅ |
| `network_from_chain_id` | 5.592571972167199e-06 | 5.60518952851906e-06 | -0.23% | -0.23% | 1.00x | ❌ |
| `short_name_from_chain_id` | 5.5890924689561805e-06 | 5.644678537358084e-06 | -0.99% | -0.98% | 0.99x | ❌ |
