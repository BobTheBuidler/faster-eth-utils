#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0745288417142709 | 0.09013708971429375 | -20.94% | -17.32% | 0.83x | ❌ |
| `name_from_chain_id` | 6.585935593719285e-06 | 6.47331170252171e-06 | 1.71% | 1.74% | 1.02x | ✅ |
| `network_from_chain_id` | 6.620062940473483e-06 | 6.745857960696079e-06 | -1.90% | -1.86% | 0.98x | ❌ |
| `short_name_from_chain_id` | 6.567266987462591e-06 | 6.644152984583796e-06 | -1.17% | -1.16% | 0.99x | ❌ |
