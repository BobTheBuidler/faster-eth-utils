#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.13011494560001893 | 0.06429588006249887 | 50.59% | 102.37% | 2.02x | ✅ |
| `name_from_chain_id` | 4.930089292728423e-06 | 6.453404407245332e-06 | -30.90% | -23.60% | 0.76x | ❌ |
| `network_from_chain_id` | 4.940268794178977e-06 | 6.319659412207936e-06 | -27.92% | -21.83% | 0.78x | ❌ |
| `short_name_from_chain_id` | 4.932866851557356e-06 | 6.3611149200634045e-06 | -28.95% | -22.45% | 0.78x | ❌ |
