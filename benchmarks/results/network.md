#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09376145317647196 | 0.0774548643529409 | 17.39% | 21.05% | 1.21x | ✅ |
| `name_from_chain_id` | 5.598609526977525e-06 | 5.725258317464037e-06 | -2.26% | -2.21% | 0.98x | ❌ |
| `network_from_chain_id` | 5.594524914049656e-06 | 5.731119160379419e-06 | -2.44% | -2.38% | 0.98x | ❌ |
| `short_name_from_chain_id` | 5.595143004882662e-06 | 5.982905094976906e-06 | -6.93% | -6.48% | 0.94x | ❌ |
