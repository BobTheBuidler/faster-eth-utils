#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.07151124100000743 | 0.0863630098666628 | -20.77% | -17.20% | 0.83x | ❌ |
| `name_from_chain_id` | 6.289770135457247e-06 | 7.210962607819748e-06 | -14.65% | -12.77% | 0.87x | ❌ |
| `network_from_chain_id` | 6.297477326822213e-06 | 6.551926308431444e-06 | -4.04% | -3.88% | 0.96x | ❌ |
| `short_name_from_chain_id` | 6.420550259103459e-06 | 6.394056040183761e-06 | 0.41% | 0.41% | 1.00x | ✅ |
