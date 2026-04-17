#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0976284970000084 | 0.09425518153334451 | 3.46% | 3.58% | 1.04x | ✅ |
| `name_from_chain_id` | 6.704838698465505e-06 | 6.924363881903606e-06 | -3.27% | -3.17% | 0.97x | ❌ |
| `network_from_chain_id` | 6.669789831986457e-06 | 7.638296082841274e-06 | -14.52% | -12.68% | 0.87x | ❌ |
| `short_name_from_chain_id` | 6.6116443660544944e-06 | 7.821140084213235e-06 | -18.29% | -15.46% | 0.85x | ❌ |
