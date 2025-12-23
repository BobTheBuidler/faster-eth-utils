#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2097244199756182e-05 | 2.392185084886044e-05 | -97.75% | -49.43% | 0.51x | ❌ |
| `replace_exceptions[no-exception]` | 1.6441129442972736e-06 | 1.5035324467765918e-06 | 8.55% | 9.35% | 1.09x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.413592103532773e-06 | 1.4653530598020014e-05 | -74.16% | -42.58% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.487532686911565e-06 | 2.370732840649317e-06 | 4.70% | 4.93% | 1.05x | ✅ |
| `return_arg_type[int-pos0]` | 2.3910968085148462e-06 | 2.250143804756074e-06 | 5.89% | 6.26% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.3437821144629213e-06 | 2.1705293481647568e-06 | 7.39% | 7.98% | 1.08x | ✅ |
| `return_arg_type[str-pos0]` | 3.0729018584227787e-06 | 2.791715599057366e-06 | 9.15% | 10.07% | 1.10x | ✅ |
| `return_arg_type[str-pos1]` | 3.0392415338047917e-06 | 2.7906911003429058e-06 | 8.18% | 8.91% | 1.09x | ✅ |
