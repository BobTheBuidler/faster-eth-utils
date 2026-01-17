#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.616941527470849e-06 | 8.786275886720763e-06 | -15.35% | -13.31% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.643367710089561e-06 | 8.695984539222378e-06 | -13.77% | -12.10% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.646938630430953e-06 | 8.646806001971684e-06 | -13.08% | -11.56% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 1.0018191346998733e-06 | 9.941625347584204e-07 | 0.76% | 0.77% | 1.01x | ✅ |
| `apply_formatter_if[condition-true]` | 1.198432951398143e-06 | 1.4104484550071805e-06 | -17.69% | -15.03% | 0.85x | ❌ |
| `apply_formatter_to_array[empty]` | 4.775047738143366e-06 | 4.8332551366908696e-06 | -1.22% | -1.20% | 0.99x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.950409447223481e-06 | 6.14221718190415e-06 | -3.22% | -3.12% | 0.97x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.216304386415091e-06 | 5.376531698305987e-06 | -3.07% | -2.98% | 0.97x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0563127808487073e-05 | 5.301856089669628e-06 | 49.81% | 99.23% | 1.99x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0764725869570102e-05 | 4.749004211896261e-06 | 55.88% | 126.67% | 2.27x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.496956060517493e-06 | 5.684926246489527e-06 | 33.09% | 49.46% | 1.49x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.961665070983292e-06 | 6.0703392876540314e-06 | 32.26% | 47.63% | 1.48x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.753091243415993e-06 | 6.560069119133261e-06 | 32.74% | 48.67% | 1.49x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.006026005657856e-05 | 7.028982474665241e-06 | 30.13% | 43.13% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.487225465076162e-05 | 8.448818524118311e-06 | 43.19% | 76.03% | 1.76x | ✅ |
| `apply_key_map[single-key]` | 1.7825532808418346e-05 | 1.0471799521979518e-05 | 41.25% | 70.22% | 1.70x | ✅ |
| `apply_key_map[two-keys]` | 2.0784642348915005e-05 | 1.2043040091752429e-05 | 42.06% | 72.59% | 1.73x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9366953898540476e-05 | 1.1407334234121785e-05 | 41.10% | 69.78% | 1.70x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5998667799830067e-06 | 1.5657196412963714e-06 | 2.13% | 2.18% | 1.02x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2023727516740136e-06 | 1.9090290598327426e-06 | 13.32% | 15.37% | 1.15x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00038444446499786027 | 0.0013512257182238655 | -251.47% | -71.55% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005574110649523185 | 0.0015924374338117634 | -185.68% | -65.00% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00046062783687115296 | 0.0016815454141411823 | -265.06% | -72.61% | 0.27x | ❌ |
