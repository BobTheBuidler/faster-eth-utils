#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08862520375000926 | 0.08009738531248445 | 9.62% | 10.65% | 1.11x | ✅ |
| `name_from_chain_id` | 7.012907927170602e-06 | 6.109083625267029e-06 | 12.89% | 14.79% | 1.15x | ✅ |
| `network_from_chain_id` | 6.934362272311141e-06 | 6.020330874058597e-06 | 13.18% | 15.18% | 1.15x | ✅ |
| `short_name_from_chain_id` | 6.953825422594498e-06 | 6.1102077328896455e-06 | 12.13% | 13.81% | 1.14x | ✅ |
