#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.10417610191666427 | 0.09738423118747619 | 6.52% | 6.97% | 1.07x | ✅ |
| `name_from_chain_id` | 6.2139930861298085e-06 | 6.666761349076941e-06 | -7.29% | -6.79% | 0.93x | ❌ |
| `network_from_chain_id` | 6.133384362509526e-06 | 6.248213486958317e-06 | -1.87% | -1.84% | 0.98x | ❌ |
| `short_name_from_chain_id` | 6.206733753337529e-06 | 6.525128194145969e-06 | -5.13% | -4.88% | 0.95x | ❌ |
