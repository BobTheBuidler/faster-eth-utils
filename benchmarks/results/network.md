#### [faster_eth_utils.network](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/faster_eth_utils/network.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/benchmarks/test_network_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `initialize_network_objects` | 0.08912301218750684 | 0.0793914296874938 | 10.92% | 12.26% | 1.12x | ✅ |
| `name_from_chain_id` | 6.9867889729867044e-06 | 6.6082643330975265e-06 | 5.42% | 5.73% | 1.06x | ✅ |
| `network_from_chain_id` | 6.9010309265159585e-06 | 6.080033295427504e-06 | 11.90% | 13.50% | 1.14x | ✅ |
| `short_name_from_chain_id` | 6.768299707520752e-06 | 6.033853914045527e-06 | 10.85% | 12.17% | 1.12x | ✅ |
