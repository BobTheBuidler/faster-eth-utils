#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08600479492856396 | 0.09112884006249544 | -5.96% | -5.62% | 0.94x | ❌ |
| `name_from_chain_id` | 7.135907826677258e-06 | 6.372926869097189e-06 | 10.69% | 11.97% | 1.12x | ✅ |
| `network_from_chain_id` | 7.15934074179616e-06 | 6.145706564500672e-06 | 14.16% | 16.49% | 1.16x | ✅ |
| `short_name_from_chain_id` | 7.041487043624545e-06 | 6.408456281482284e-06 | 8.99% | 9.88% | 1.10x | ✅ |
