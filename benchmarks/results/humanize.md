#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.4170305830653874e-06 | 2.523356090945481e-06 | 42.87% | 75.05% | 1.75x | ✅ |
| `humanize_bytes[empty]` | 1.1177613285988928e-06 | 8.112172768380942e-07 | 27.42% | 37.79% | 1.38x | ✅ |
| `humanize_bytes[long]` | 4.1598388808366915e-06 | 2.328002782635405e-06 | 44.04% | 78.69% | 1.79x | ✅ |
| `humanize_bytes[short]` | 1.5002896320499795e-06 | 1.0591802079520786e-06 | 29.40% | 41.65% | 1.42x | ✅ |
| `humanize_hash[32-bytes]` | 4.679512220664244e-06 | 2.5922154705676657e-06 | 44.61% | 80.52% | 1.81x | ✅ |
| `humanize_hash[empty]` | 1.3158092661808395e-06 | 8.290692286105587e-07 | 36.99% | 58.71% | 1.59x | ✅ |
| `humanize_hash[long]` | 4.482729771061019e-06 | 2.410979704526371e-06 | 46.22% | 85.93% | 1.86x | ✅ |
| `humanize_hash[short]` | 1.7273342955343767e-06 | 1.0690297614904299e-06 | 38.11% | 61.58% | 1.62x | ✅ |
| `humanize_hexstr[empty]` | 1.8809297873527268e-06 | 7.083290372601528e-07 | 62.34% | 165.54% | 2.66x | ✅ |
| `humanize_hexstr[short-0x]` | 4.80159476546686e-06 | 2.567755904927729e-06 | 46.52% | 87.00% | 1.87x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.05636178967583e-06 | 2.1514145809406273e-06 | 46.96% | 88.54% | 1.89x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.81495825895982e-06 | 2.452316087067417e-06 | 49.07% | 96.34% | 1.96x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.041618783300775e-06 | 2.0299408938201763e-06 | 49.77% | 99.10% | 1.99x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.1079327052955944e-05 | 2.4709208146923735e-05 | 20.50% | 25.78% | 1.26x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.7299664451351284e-05 | 2.982809459834272e-05 | 20.03% | 25.05% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 8.768701428941619e-07 | 5.699683970191991e-07 | 35.00% | 53.85% | 1.54x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.623821377284444e-05 | 3.7268826487997855e-05 | 19.40% | 24.07% | 1.24x | ✅ |
| `humanize_integer_sequence[single]` | 2.7025017734100165e-05 | 2.0517776237454794e-05 | 24.08% | 31.72% | 1.32x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0963642924393297e-05 | 3.326944264757377e-05 | 18.78% | 23.13% | 1.23x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.887140357895187e-05 | 6.817256667570515e-05 | 1.01% | 1.03% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.925342234065957e-05 | 1.66936245325487e-05 | 13.30% | 15.33% | 1.15x | ✅ |
| `humanize_seconds[negative]` | 2.389169696495859e-05 | 1.383043064999648e-05 | 42.11% | 72.75% | 1.73x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.778267547455253e-05 | 1.593788617964011e-05 | 42.63% | 74.32% | 1.74x | ✅ |
| `humanize_seconds[one-hour]` | 1.8134944673415362e-05 | 1.4905540577558061e-05 | 17.81% | 21.67% | 1.22x | ✅ |
| `humanize_seconds[one-minute]` | 1.8526994775587467e-05 | 1.561977737668345e-05 | 15.69% | 18.61% | 1.19x | ✅ |
| `humanize_seconds[one-second]` | 1.903319642084831e-05 | 1.63001963172935e-05 | 14.36% | 16.77% | 1.17x | ✅ |
| `humanize_seconds[zero]` | 8.077666304824927e-07 | 6.692414793938158e-07 | 17.15% | 20.70% | 1.21x | ✅ |
| `humanize_wei[ether]` | 2.8636964644858748e-05 | 2.6818521573531848e-05 | 6.35% | 6.78% | 1.07x | ✅ |
| `humanize_wei[gwei]` | 2.8489702874029217e-05 | 2.6530160136288404e-05 | 6.88% | 7.39% | 1.07x | ✅ |
| `humanize_wei[wei]` | 2.827283757050805e-05 | 2.6094821440446904e-05 | 7.70% | 8.35% | 1.08x | ✅ |
| `humanize_wei[zero]` | 5.10216528711442e-06 | 3.206072839829779e-06 | 37.16% | 59.14% | 1.59x | ✅ |
| `is_ipfs_uri[empty]` | 1.8544084163277934e-05 | 1.89500343455592e-05 | -2.19% | -2.14% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.3303947151953794e-05 | 3.357230978563376e-05 | -0.81% | -0.80% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.119689014875067e-05 | 3.1783137273160955e-05 | -1.88% | -1.84% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.425424135963881e-05 | 3.415643546485624e-05 | 0.29% | 0.29% | 1.00x | ✅ |
