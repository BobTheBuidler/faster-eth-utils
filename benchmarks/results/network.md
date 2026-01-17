#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09183636556250008 | 0.08273536656249902 | 9.91% | 11.00% | 1.11x | ✅ |
| `name_from_chain_id` | 6.962176955280216e-06 | 6.654261364917717e-06 | 4.42% | 4.63% | 1.05x | ✅ |
| `network_from_chain_id` | 6.903027214667817e-06 | 6.330589667069073e-06 | 8.29% | 9.04% | 1.09x | ✅ |
| `short_name_from_chain_id` | 6.959080930271926e-06 | 6.528733340874002e-06 | 6.18% | 6.59% | 1.07x | ✅ |
