#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.07213587680000728 | 0.0889143733571294 | -23.26% | -18.87% | 0.81x | ❌ |
| `name_from_chain_id` | 6.278858831225921e-06 | 6.610124159915279e-06 | -5.28% | -5.01% | 0.95x | ❌ |
| `network_from_chain_id` | 6.3603489860092635e-06 | 6.4220238939355486e-06 | -0.97% | -0.96% | 0.99x | ❌ |
| `short_name_from_chain_id` | 6.246662464692994e-06 | 6.399302238532483e-06 | -2.44% | -2.39% | 0.98x | ❌ |
