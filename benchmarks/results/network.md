#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.06268999920000624 | 0.06242714149999529 | 0.42% | 0.42% | 1.00x | ✅ |
| `name_from_chain_id` | 7.241966756254061e-06 | 6.4777321072431505e-06 | 10.55% | 11.80% | 1.12x | ✅ |
| `network_from_chain_id` | 7.176774225714199e-06 | 6.447352826977539e-06 | 10.16% | 11.31% | 1.11x | ✅ |
| `short_name_from_chain_id` | 7.262764791749096e-06 | 6.43857875374806e-06 | 11.35% | 12.80% | 1.13x | ✅ |
