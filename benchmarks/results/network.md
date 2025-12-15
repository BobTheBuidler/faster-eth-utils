#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.1001706824375006 | 0.0839301973749933 | 16.21% | 19.35% | 1.19x | ✅ |
| `name_from_chain_id` | 5.564425649025631e-06 | 5.847554243073685e-06 | -5.09% | -4.84% | 0.95x | ❌ |
| `network_from_chain_id` | 5.569690430137927e-06 | 5.750672626226681e-06 | -3.25% | -3.15% | 0.97x | ❌ |
| `short_name_from_chain_id` | 5.562733312332282e-06 | 5.79960450887516e-06 | -4.26% | -4.08% | 0.96x | ❌ |
