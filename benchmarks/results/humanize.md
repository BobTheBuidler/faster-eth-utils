#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.201083901923976e-06 | 2.678926341738801e-06 | 36.23% | 56.82% | 1.57x | ✅ |
| `humanize_bytes[empty]` | 1.1013803265800763e-06 | 9.223857542635734e-07 | 16.25% | 19.41% | 1.19x | ✅ |
| `humanize_bytes[long]` | 4.040383929676069e-06 | 2.45887669364326e-06 | 39.14% | 64.32% | 1.64x | ✅ |
| `humanize_bytes[short]` | 1.45695239226892e-06 | 1.1692001437014699e-06 | 19.75% | 24.61% | 1.25x | ✅ |
| `humanize_hash[32-bytes]` | 4.502961104117477e-06 | 2.713111501011757e-06 | 39.75% | 65.97% | 1.66x | ✅ |
| `humanize_hash[empty]` | 1.3998613298205352e-06 | 8.271185744001889e-07 | 40.91% | 69.25% | 1.69x | ✅ |
| `humanize_hash[long]` | 4.250566814559434e-06 | 2.5020273526505535e-06 | 41.14% | 69.88% | 1.70x | ✅ |
| `humanize_hash[short]` | 1.7017233564711093e-06 | 1.1304305249093354e-06 | 33.57% | 50.54% | 1.51x | ✅ |
| `humanize_hexstr[empty]` | 1.8682755050806392e-06 | 6.447104470966982e-07 | 65.49% | 189.79% | 2.90x | ✅ |
| `humanize_hexstr[short-0x]` | 4.527019301449101e-06 | 2.4708449727318612e-06 | 45.42% | 83.22% | 1.83x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.7683125710442502e-06 | 2.0054193756376896e-06 | 46.78% | 87.91% | 1.88x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.564126800496556e-06 | 2.4873875039294206e-06 | 45.50% | 83.49% | 1.83x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.746233613974072e-06 | 1.9854943855420144e-06 | 47.00% | 88.68% | 1.89x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0476184581256574e-05 | 2.47322359366135e-05 | 18.85% | 23.22% | 1.23x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.6755018330274076e-05 | 3.015586685399584e-05 | 17.95% | 21.88% | 1.22x | ✅ |
| `humanize_integer_sequence[empty]` | 9.273931265022586e-07 | 5.90671397299774e-07 | 36.31% | 57.01% | 1.57x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.521731829593946e-05 | 3.791056965120776e-05 | 16.16% | 19.27% | 1.19x | ✅ |
| `humanize_integer_sequence[single]` | 2.6417751276110226e-05 | 2.0383940854480673e-05 | 22.84% | 29.60% | 1.30x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.02544709407141e-05 | 3.353106794823564e-05 | 16.70% | 20.05% | 1.20x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.886675852015415e-05 | 6.65439725708267e-05 | 3.37% | 3.49% | 1.03x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.900943192574086e-05 | 1.8413241005898704e-05 | 3.14% | 3.24% | 1.03x | ✅ |
| `humanize_seconds[negative]` | 2.3341652850766085e-05 | 1.845108951166634e-05 | 20.95% | 26.51% | 1.27x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7604439915996397e-05 | 2.0362327381367203e-05 | 26.24% | 35.57% | 1.36x | ✅ |
| `humanize_seconds[one-hour]` | 1.786860925965493e-05 | 1.6854568521744115e-05 | 5.67% | 6.02% | 1.06x | ✅ |
| `humanize_seconds[one-minute]` | 1.8349874409372017e-05 | 1.7792334868335554e-05 | 3.04% | 3.13% | 1.03x | ✅ |
| `humanize_seconds[one-second]` | 1.914908838125095e-05 | 1.8316219716118396e-05 | 4.35% | 4.55% | 1.05x | ✅ |
| `humanize_seconds[zero]` | 8.800736120558565e-07 | 6.784191463004898e-07 | 22.91% | 29.72% | 1.30x | ✅ |
| `humanize_wei[ether]` | 2.7096489853574404e-05 | 2.656304503756995e-05 | 1.97% | 2.01% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.6836388730573916e-05 | 2.590648151220232e-05 | 3.47% | 3.59% | 1.04x | ✅ |
| `humanize_wei[wei]` | 2.6802501968181294e-05 | 2.5621259484329454e-05 | 4.41% | 4.61% | 1.05x | ✅ |
| `humanize_wei[zero]` | 4.751817045331375e-06 | 3.626560253954155e-06 | 23.68% | 31.03% | 1.31x | ✅ |
| `is_ipfs_uri[empty]` | 1.854828014316643e-05 | 1.9097485896577897e-05 | -2.96% | -2.88% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.3527711724286365e-05 | 3.340312007674283e-05 | 0.37% | 0.37% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.113227276885358e-05 | 3.184256600681081e-05 | -2.28% | -2.23% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3982961103359375e-05 | 3.370848698280906e-05 | 0.81% | 0.81% | 1.01x | ✅ |
