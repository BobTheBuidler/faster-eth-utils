#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.07479166140000189 | 0.0847743528823444 | -13.35% | -11.78% | 0.88x | ❌ |
| `name_from_chain_id` | 7.117267153552045e-06 | 6.334142606349023e-06 | 11.00% | 12.36% | 1.12x | ✅ |
| `network_from_chain_id` | 7.100435803947743e-06 | 6.304976117900459e-06 | 11.20% | 12.62% | 1.13x | ✅ |
| `short_name_from_chain_id` | 7.174541924123957e-06 | 6.4192691570107195e-06 | 10.53% | 11.77% | 1.12x | ✅ |
