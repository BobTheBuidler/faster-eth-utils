#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09502149713332907 | 0.07848086556250067 | 17.41% | 21.08% | 1.21x | ✅ |
| `name_from_chain_id` | 7.020990267402356e-06 | 6.270362930189096e-06 | 10.69% | 11.97% | 1.12x | ✅ |
| `network_from_chain_id` | 6.960634150483324e-06 | 6.229636462248143e-06 | 10.50% | 11.73% | 1.12x | ✅ |
| `short_name_from_chain_id` | 6.90330070937593e-06 | 5.949123353455663e-06 | 13.82% | 16.04% | 1.16x | ✅ |
