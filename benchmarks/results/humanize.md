#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.216389637759392e-06 | 2.7080021059081464e-06 | 35.77% | 55.70% | 1.56x | ✅ |
| `humanize_bytes[empty]` | 1.1295804317116663e-06 | 8.085073152537129e-07 | 28.42% | 39.71% | 1.40x | ✅ |
| `humanize_bytes[long]` | 4.039805135148155e-06 | 2.4917583099224687e-06 | 38.32% | 62.13% | 1.62x | ✅ |
| `humanize_bytes[short]` | 1.4849912786337002e-06 | 1.0737078235686667e-06 | 27.70% | 38.30% | 1.38x | ✅ |
| `humanize_hash[32-bytes]` | 4.485372262520027e-06 | 2.7455094228041963e-06 | 38.79% | 63.37% | 1.63x | ✅ |
| `humanize_hash[empty]` | 1.3771088359008442e-06 | 8.294311051212677e-07 | 39.77% | 66.03% | 1.66x | ✅ |
| `humanize_hash[long]` | 4.270115173600687e-06 | 2.4825292496173228e-06 | 41.86% | 72.01% | 1.72x | ✅ |
| `humanize_hash[short]` | 1.7208120641399483e-06 | 1.090603794434744e-06 | 36.62% | 57.79% | 1.58x | ✅ |
| `humanize_hexstr[empty]` | 1.8804269135794871e-06 | 6.495952765086199e-07 | 65.45% | 189.48% | 2.89x | ✅ |
| `humanize_hexstr[short-0x]` | 4.5316588625189316e-06 | 2.5070035484872553e-06 | 44.68% | 80.76% | 1.81x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.7956995388049707e-06 | 2.0312864136356445e-06 | 46.48% | 86.86% | 1.87x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.5889144841363366e-06 | 2.504720086036971e-06 | 45.42% | 83.21% | 1.83x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.7869232551682583e-06 | 2.023198256433511e-06 | 46.57% | 87.18% | 1.87x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0493463864106178e-05 | 2.4638721864705144e-05 | 19.20% | 23.76% | 1.24x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.672259544816738e-05 | 3.0328642590379858e-05 | 17.41% | 21.08% | 1.21x | ✅ |
| `humanize_integer_sequence[empty]` | 9.33869080576396e-07 | 5.612897556245999e-07 | 39.90% | 66.38% | 1.66x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.536973215614777e-05 | 3.814816077389167e-05 | 15.92% | 18.93% | 1.19x | ✅ |
| `humanize_integer_sequence[single]` | 2.6821830016965487e-05 | 2.0475365317573975e-05 | 23.66% | 31.00% | 1.31x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.008323212188022e-05 | 3.4026904491513834e-05 | 15.11% | 17.80% | 1.18x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.700611562190097e-05 | 6.58595882107394e-05 | 1.71% | 1.74% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8747015292272208e-05 | 1.67721504254763e-05 | 10.53% | 11.77% | 1.12x | ✅ |
| `humanize_seconds[negative]` | 2.345092345152666e-05 | 1.4016386544143642e-05 | 40.23% | 67.31% | 1.67x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.725908861845144e-05 | 1.6567424017690594e-05 | 39.22% | 64.53% | 1.65x | ✅ |
| `humanize_seconds[one-hour]` | 1.7938277375946386e-05 | 1.5602842398539895e-05 | 13.02% | 14.97% | 1.15x | ✅ |
| `humanize_seconds[one-minute]` | 1.8091119429015763e-05 | 1.60166446710416e-05 | 11.47% | 12.95% | 1.13x | ✅ |
| `humanize_seconds[one-second]` | 1.8769972843228687e-05 | 1.6705899773930974e-05 | 11.00% | 12.36% | 1.12x | ✅ |
| `humanize_seconds[zero]` | 8.775470408222305e-07 | 6.852452679039034e-07 | 21.91% | 28.06% | 1.28x | ✅ |
| `humanize_wei[ether]` | 2.7026861973503176e-05 | 2.596319409316701e-05 | 3.94% | 4.10% | 1.04x | ✅ |
| `humanize_wei[gwei]` | 2.6823025278856015e-05 | 2.6244825079387067e-05 | 2.16% | 2.20% | 1.02x | ✅ |
| `humanize_wei[wei]` | 2.6570251625655833e-05 | 2.634704992459689e-05 | 0.84% | 0.85% | 1.01x | ✅ |
| `humanize_wei[zero]` | 4.8574558489119246e-06 | 3.670248807677116e-06 | 24.44% | 32.35% | 1.32x | ✅ |
| `is_ipfs_uri[empty]` | 1.8278800847260652e-05 | 1.8758067110956548e-05 | -2.62% | -2.55% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.260729318003071e-05 | 3.275243814511714e-05 | -0.45% | -0.44% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.03269359773176e-05 | 3.088550500154936e-05 | -1.84% | -1.81% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.324595439662781e-05 | 3.276233730846151e-05 | 1.45% | 1.48% | 1.01x | ✅ |
