#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0941207972499889 | 0.08226851662500678 | 12.59% | 14.41% | 1.14x | ✅ |
| `name_from_chain_id` | 6.862165650665346e-06 | 6.1904264265638554e-06 | 9.79% | 10.85% | 1.11x | ✅ |
| `network_from_chain_id` | 6.957758967481994e-06 | 6.160000240427356e-06 | 11.47% | 12.95% | 1.13x | ✅ |
| `short_name_from_chain_id` | 6.764624741587724e-06 | 6.034620791912952e-06 | 10.79% | 12.10% | 1.12x | ✅ |
