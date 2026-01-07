#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08943214237499575 | 0.08006063793749973 | 10.48% | 11.71% | 1.12x | ✅ |
| `name_from_chain_id` | 6.720782767329463e-06 | 6.219034100529767e-06 | 7.47% | 8.07% | 1.08x | ✅ |
| `network_from_chain_id` | 6.870930623891876e-06 | 6.064105524656576e-06 | 11.74% | 13.30% | 1.13x | ✅ |
| `short_name_from_chain_id` | 6.888324037541651e-06 | 6.589266472767609e-06 | 4.34% | 4.54% | 1.05x | ✅ |
