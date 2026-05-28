#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.0766190984615535 | 0.09248116949999842 | -20.70% | -17.15% | 0.83x | ❌ |
| `name_from_chain_id` | 6.482499564648577e-06 | 6.40859810380113e-06 | 1.14% | 1.15% | 1.01x | ✅ |
| `network_from_chain_id` | 6.469605901077656e-06 | 6.160421317439948e-06 | 4.78% | 5.02% | 1.05x | ✅ |
| `short_name_from_chain_id` | 6.441921262820798e-06 | 6.79357782574013e-06 | -5.46% | -5.18% | 0.95x | ❌ |
