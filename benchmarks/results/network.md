#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09428632676470858 | 0.07785321741176056 | 17.43% | 21.11% | 1.21x | ✅ |
| `name_from_chain_id` | 5.560136621082841e-06 | 5.616227157582983e-06 | -1.01% | -1.00% | 0.99x | ❌ |
| `network_from_chain_id` | 5.6028515838735014e-06 | 5.767688648312655e-06 | -2.94% | -2.86% | 0.97x | ❌ |
| `short_name_from_chain_id` | 5.563873596376972e-06 | 5.678981981283522e-06 | -2.07% | -2.03% | 0.98x | ❌ |
