#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0711539767999966 | 0.10974635342856638 | -54.24% | -35.17% | 0.65x | ❌ |
| `name_from_chain_id` | 6.098461164545312e-06 | 6.12399902819834e-06 | -0.42% | -0.42% | 1.00x | ❌ |
| `network_from_chain_id` | 6.1286109270916104e-06 | 6.3181458766479324e-06 | -3.09% | -3.00% | 0.97x | ❌ |
| `short_name_from_chain_id` | 6.0826980242952704e-06 | 6.1855973520005856e-06 | -1.69% | -1.66% | 0.98x | ❌ |
