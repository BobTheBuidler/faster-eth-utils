#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.163260251199825e-06 | 2.7346380218970623e-06 | 34.31% | 52.24% | 1.52x | ✅ |
| `humanize_bytes[empty]` | 1.1945144441069665e-06 | 8.223661657609856e-07 | 31.15% | 45.25% | 1.45x | ✅ |
| `humanize_bytes[long]` | 3.982821319948197e-06 | 2.5493458398221584e-06 | 35.99% | 56.23% | 1.56x | ✅ |
| `humanize_bytes[short]` | 1.501444234558481e-06 | 1.2141066240135416e-06 | 19.14% | 23.67% | 1.24x | ✅ |
| `humanize_hash[32-bytes]` | 4.3740752774145805e-06 | 2.736890326484275e-06 | 37.43% | 59.82% | 1.60x | ✅ |
| `humanize_hash[empty]` | 1.3846593703782248e-06 | 8.724878064328992e-07 | 36.99% | 58.70% | 1.59x | ✅ |
| `humanize_hash[long]` | 4.196636523233285e-06 | 2.587018266920625e-06 | 38.35% | 62.22% | 1.62x | ✅ |
| `humanize_hash[short]` | 1.7090146847142861e-06 | 1.2687552082539813e-06 | 25.76% | 34.70% | 1.35x | ✅ |
| `humanize_hexstr[empty]` | 1.9209768226464055e-06 | 6.520263764915734e-07 | 66.06% | 194.62% | 2.95x | ✅ |
| `humanize_hexstr[short-0x]` | 4.68816638720595e-06 | 2.5558572755178125e-06 | 45.48% | 83.43% | 1.83x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.931027605490194e-06 | 2.1167536164072264e-06 | 46.15% | 85.71% | 1.86x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.754012355075319e-06 | 2.56206109093013e-06 | 46.11% | 85.55% | 1.86x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.99689288687463e-06 | 2.071588943017183e-06 | 48.17% | 92.94% | 1.93x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.1256324560778034e-05 | 2.3791741169146645e-05 | 23.88% | 31.37% | 1.31x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.687994139602717e-05 | 2.8754502816160585e-05 | 22.03% | 28.26% | 1.28x | ✅ |
| `humanize_integer_sequence[empty]` | 8.521306210990349e-07 | 6.731072712773605e-07 | 21.01% | 26.60% | 1.27x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.621661651729735e-05 | 3.5970399895555746e-05 | 22.17% | 28.49% | 1.28x | ✅ |
| `humanize_integer_sequence[single]` | 2.6905771735220332e-05 | 1.9840290291860757e-05 | 26.26% | 35.61% | 1.36x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.093848095499699e-05 | 3.216920779301705e-05 | 21.42% | 27.26% | 1.27x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.579492787996737e-05 | 6.501060444273903e-05 | 1.19% | 1.21% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9019250470039378e-05 | 1.585892958472627e-05 | 16.62% | 19.93% | 1.20x | ✅ |
| `humanize_seconds[negative]` | 2.3185901977318907e-05 | 1.3473084328586207e-05 | 41.89% | 72.09% | 1.72x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.690927989780914e-05 | 1.5985071560749236e-05 | 40.60% | 68.34% | 1.68x | ✅ |
| `humanize_seconds[one-hour]` | 1.8162782848742486e-05 | 1.4742769113483086e-05 | 18.83% | 23.20% | 1.23x | ✅ |
| `humanize_seconds[one-minute]` | 1.816335989460046e-05 | 1.5255067056288548e-05 | 16.01% | 19.06% | 1.19x | ✅ |
| `humanize_seconds[one-second]` | 1.910683179769561e-05 | 1.588913997218468e-05 | 16.84% | 20.25% | 1.20x | ✅ |
| `humanize_seconds[zero]` | 8.398625141131406e-07 | 8.041034700357177e-07 | 4.26% | 4.45% | 1.04x | ✅ |
| `humanize_wei[ether]` | 2.704109790632059e-05 | 2.5705494100546267e-05 | 4.94% | 5.20% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.6910708347613528e-05 | 2.5364655813778273e-05 | 5.75% | 6.10% | 1.06x | ✅ |
| `humanize_wei[wei]` | 2.6880247085975148e-05 | 2.4986669063198257e-05 | 7.04% | 7.58% | 1.08x | ✅ |
| `humanize_wei[zero]` | 4.831963886130502e-06 | 3.4978624490306e-06 | 27.61% | 38.14% | 1.38x | ✅ |
| `is_ipfs_uri[empty]` | 1.808143656535391e-05 | 1.849219887092211e-05 | -2.27% | -2.22% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.212737128452659e-05 | 3.220606825296541e-05 | -0.24% | -0.24% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 2.9783374193033766e-05 | 3.014277692200224e-05 | -1.21% | -1.19% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.273841358564418e-05 | 3.244032209689424e-05 | 0.91% | 0.92% | 1.01x | ✅ |
