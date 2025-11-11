#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.224363916668112e-06 | 2.5450387511725756e-06 | 39.75% | 65.98% | 1.66x | ✅ |
| `humanize_bytes[empty]` | 1.173490172343636e-06 | 8.706203660731701e-07 | 25.81% | 34.79% | 1.35x | ✅ |
| `humanize_bytes[long]` | 4.0149858160217305e-06 | 2.4104205889909946e-06 | 39.96% | 66.57% | 1.67x | ✅ |
| `humanize_bytes[short]` | 1.492239958483999e-06 | 1.092619368732763e-06 | 26.78% | 36.57% | 1.37x | ✅ |
| `humanize_hash[32-bytes]` | 4.465909557772967e-06 | 2.691401294355122e-06 | 39.73% | 65.93% | 1.66x | ✅ |
| `humanize_hash[empty]` | 1.4189711185087254e-06 | 8.743987340405753e-07 | 38.38% | 62.28% | 1.62x | ✅ |
| `humanize_hash[long]` | 4.328762409332338e-06 | 2.4644877188761294e-06 | 43.07% | 75.65% | 1.76x | ✅ |
| `humanize_hash[short]` | 1.6334102402877799e-06 | 1.0888153756910978e-06 | 33.34% | 50.02% | 1.50x | ✅ |
| `humanize_hexstr[empty]` | 1.8398084343987338e-06 | 7.599199858036223e-07 | 58.70% | 142.11% | 2.42x | ✅ |
| `humanize_hexstr[short-0x]` | 4.653281598530123e-06 | 2.3904349008064397e-06 | 48.63% | 94.66% | 1.95x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.998256141547068e-06 | 1.9854263527993958e-06 | 50.34% | 101.38% | 2.01x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.778219124644261e-06 | 2.345820163650471e-06 | 50.91% | 103.69% | 2.04x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.97868560953202e-06 | 1.9883104274501712e-06 | 50.03% | 100.10% | 2.00x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0632642993131986e-05 | 2.372526288329916e-05 | 22.55% | 29.11% | 1.29x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.660411273674827e-05 | 2.8638479259367593e-05 | 21.76% | 27.81% | 1.28x | ✅ |
| `humanize_integer_sequence[empty]` | 9.507595299271109e-07 | 6.289578423020148e-07 | 33.85% | 51.16% | 1.51x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.506655110519591e-05 | 3.593640598974896e-05 | 20.26% | 25.41% | 1.25x | ✅ |
| `humanize_integer_sequence[single]` | 2.6974217423091737e-05 | 1.9812608451584238e-05 | 26.55% | 36.15% | 1.36x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.961956867806302e-05 | 3.167163980858406e-05 | 20.06% | 25.09% | 1.25x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.797020809307017e-05 | 6.643948162958885e-05 | 2.25% | 2.30% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8670739062612947e-05 | 1.7414361346985597e-05 | 6.73% | 7.21% | 1.07x | ✅ |
| `humanize_seconds[negative]` | 2.395751380402352e-05 | 1.7761597174666133e-05 | 25.86% | 34.88% | 1.35x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7695853505836768e-05 | 1.9758096835649423e-05 | 28.66% | 40.17% | 1.40x | ✅ |
| `humanize_seconds[one-hour]` | 1.7816514551521827e-05 | 1.6138540921542144e-05 | 9.42% | 10.40% | 1.10x | ✅ |
| `humanize_seconds[one-minute]` | 1.8121816255136675e-05 | 1.6781259489820294e-05 | 7.40% | 7.99% | 1.08x | ✅ |
| `humanize_seconds[one-second]` | 1.872533608759205e-05 | 1.7303297322565277e-05 | 7.59% | 8.22% | 1.08x | ✅ |
| `humanize_seconds[zero]` | 8.869723231833739e-07 | 6.72999392277567e-07 | 24.12% | 31.79% | 1.32x | ✅ |
| `humanize_wei[ether]` | 2.6995849364831582e-05 | 2.6569185329385877e-05 | 1.58% | 1.61% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.66079879603309e-05 | 2.583747274865752e-05 | 2.90% | 2.98% | 1.03x | ✅ |
| `humanize_wei[wei]` | 2.660756161236944e-05 | 2.5531722239828212e-05 | 4.04% | 4.21% | 1.04x | ✅ |
| `humanize_wei[zero]` | 4.867426506594293e-06 | 4.191913534574675e-06 | 13.88% | 16.11% | 1.16x | ✅ |
| `is_ipfs_uri[empty]` | 1.781385375956661e-05 | 1.8486760757207334e-05 | -3.78% | -3.64% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.266625362232093e-05 | 3.2657580216258464e-05 | 0.03% | 0.03% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.119892949579585e-05 | 3.087620828635784e-05 | 1.03% | 1.05% | 1.01x | ✅ |
| `is_ipfs_uri[valid-cidv0]` | 3.368190282494793e-05 | 3.3342907842999385e-05 | 1.01% | 1.02% | 1.01x | ✅ |
