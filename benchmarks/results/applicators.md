#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.30329201694255e-06 | 8.1204117159498e-06 | -11.19% | -10.06% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.378192184296261e-06 | 8.319855119081975e-06 | -12.76% | -11.32% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.347561617070955e-06 | 8.279778427033132e-06 | -12.69% | -11.26% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.458360715593153e-07 | 1.014141684495339e-06 | -7.22% | -6.74% | 0.93x | ❌ |
| `apply_formatter_if[condition-true]` | 1.2261391505097638e-06 | 1.4415378999828996e-06 | -17.57% | -14.94% | 0.85x | ❌ |
| `apply_formatter_to_array[empty]` | 4.506257918554955e-06 | 4.617797760955802e-06 | -2.48% | -2.42% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.67280373963347e-06 | 5.922065887703901e-06 | -4.39% | -4.21% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 4.909031021949093e-06 | 5.116068783391787e-06 | -4.22% | -4.05% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0199229634566067e-05 | 4.66574882812422e-06 | 54.25% | 118.60% | 2.19x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.914022486868255e-06 | 4.263779747124652e-06 | 56.99% | 132.52% | 2.33x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.390710930497053e-06 | 5.296752509839247e-06 | 36.87% | 58.41% | 1.58x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.625309250835077e-06 | 5.783555623424839e-06 | 32.95% | 49.14% | 1.49x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.097552388826254e-06 | 6.173235753347475e-06 | 32.14% | 47.37% | 1.47x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.608797917388954e-06 | 6.48366901874139e-06 | 32.52% | 48.20% | 1.48x | ✅ |
| `apply_key_map[empty]` | 1.4403276628217168e-05 | 8.551211380300569e-06 | 40.63% | 68.44% | 1.68x | ✅ |
| `apply_key_map[single-key]` | 1.696884656806628e-05 | 9.986982415885674e-06 | 41.15% | 69.91% | 1.70x | ✅ |
| `apply_key_map[two-keys]` | 1.9017189209491717e-05 | 1.1298709934607994e-05 | 40.59% | 68.31% | 1.68x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8540161875692804e-05 | 1.1204338728673433e-05 | 39.57% | 65.47% | 1.65x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6009166807862782e-06 | 1.4593477662116223e-06 | 8.84% | 9.70% | 1.10x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.048973692977365e-06 | 1.9141873780638387e-06 | 6.58% | 7.04% | 1.07x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0002976003909421145 | 0.0009925112458333274 | -233.50% | -70.02% | 0.30x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.00044771615234192333 | 0.0013739325417308362 | -206.88% | -67.41% | 0.33x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00035339841345674827 | 0.0010969143798008924 | -210.39% | -67.78% | 0.32x | ❌ |
