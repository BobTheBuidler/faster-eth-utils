#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.09202175718749572 | 0.08060588593752271 | 12.41% | 14.16% | 1.14x | ✅ |
| `name_from_chain_id` | 6.967905305274802e-06 | 6.71048976598378e-06 | 3.69% | 3.84% | 1.04x | ✅ |
| `network_from_chain_id` | 6.967840668786074e-06 | 6.360691249275636e-06 | 8.71% | 9.55% | 1.10x | ✅ |
| `short_name_from_chain_id` | 6.8242780228206616e-06 | 6.017646035895739e-06 | 11.82% | 13.40% | 1.13x | ✅ |
