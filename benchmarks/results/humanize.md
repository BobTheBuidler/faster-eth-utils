#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.396071138214241e-06 | 2.590595578722623e-06 | 41.07% | 69.69% | 1.70x | ✅ |
| `humanize_bytes[empty]` | 1.2202042602664293e-06 | 8.344786596488124e-07 | 31.61% | 46.22% | 1.46x | ✅ |
| `humanize_bytes[long]` | 4.191028381086749e-06 | 2.3812277563255483e-06 | 43.18% | 76.00% | 1.76x | ✅ |
| `humanize_bytes[short]` | 1.6000988834828596e-06 | 1.0586435504844149e-06 | 33.84% | 51.15% | 1.51x | ✅ |
| `humanize_hash[32-bytes]` | 4.7244714078341855e-06 | 2.635396138277759e-06 | 44.22% | 79.27% | 1.79x | ✅ |
| `humanize_hash[empty]` | 1.4005334007576625e-06 | 8.46787019211938e-07 | 39.54% | 65.39% | 1.65x | ✅ |
| `humanize_hash[long]` | 4.430486509349607e-06 | 2.41865370650208e-06 | 45.41% | 83.18% | 1.83x | ✅ |
| `humanize_hash[short]` | 1.8371084456666105e-06 | 1.0969617030738021e-06 | 40.29% | 67.47% | 1.67x | ✅ |
| `humanize_hexstr[empty]` | 1.98641204075943e-06 | 6.657743354710424e-07 | 66.48% | 198.36% | 2.98x | ✅ |
| `humanize_hexstr[short-0x]` | 4.812348306355584e-06 | 2.42439759182217e-06 | 49.62% | 98.50% | 1.98x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.089743417447736e-06 | 1.9977019470956304e-06 | 51.15% | 104.72% | 2.05x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.8678231280874725e-06 | 2.491971490578502e-06 | 48.81% | 95.34% | 1.95x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.052979822832314e-06 | 1.992952100301272e-06 | 50.83% | 103.37% | 2.03x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.2736431244965945e-05 | 2.5113211414365135e-05 | 23.29% | 30.36% | 1.30x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.832626993356607e-05 | 3.0476311649898834e-05 | 20.48% | 25.76% | 1.26x | ✅ |
| `humanize_integer_sequence[empty]` | 8.584988954486034e-07 | 5.728558396172051e-07 | 33.27% | 49.86% | 1.50x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.752794265390586e-05 | 3.795827188337082e-05 | 20.13% | 25.21% | 1.25x | ✅ |
| `humanize_integer_sequence[single]` | 2.7699377600970376e-05 | 2.107971868450382e-05 | 23.90% | 31.40% | 1.31x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.218294384759625e-05 | 3.397234500477617e-05 | 19.46% | 24.17% | 1.24x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.868874004940842e-05 | 6.649601906227926e-05 | 3.19% | 3.30% | 1.03x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.920428656753016e-05 | 1.6612085187017918e-05 | 13.50% | 15.60% | 1.16x | ✅ |
| `humanize_seconds[negative]` | 2.4030224208779406e-05 | 1.4106504495397266e-05 | 41.30% | 70.35% | 1.70x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7889909646467326e-05 | 1.641915820217798e-05 | 41.13% | 69.86% | 1.70x | ✅ |
| `humanize_seconds[one-hour]` | 1.843169805751062e-05 | 1.533678934196509e-05 | 16.79% | 20.18% | 1.20x | ✅ |
| `humanize_seconds[one-minute]` | 1.848003889938237e-05 | 1.6061452807059817e-05 | 13.09% | 15.06% | 1.15x | ✅ |
| `humanize_seconds[one-second]` | 1.9405002433789032e-05 | 1.6489901418086e-05 | 15.02% | 17.68% | 1.18x | ✅ |
| `humanize_seconds[zero]` | 8.651813676303233e-07 | 8.327965405750552e-07 | 3.74% | 3.89% | 1.04x | ✅ |
| `humanize_wei[ether]` | 2.8562147237958627e-05 | 2.7188237499178772e-05 | 4.81% | 5.05% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.85741676905318e-05 | 2.6794096990748486e-05 | 6.23% | 6.64% | 1.07x | ✅ |
| `humanize_wei[wei]` | 2.81430289328677e-05 | 2.6372784966787288e-05 | 6.29% | 6.71% | 1.07x | ✅ |
| `humanize_wei[zero]` | 5.133873930607682e-06 | 3.1940560037196043e-06 | 37.78% | 60.73% | 1.61x | ✅ |
| `is_ipfs_uri[empty]` | 1.864186770124009e-05 | 1.8806153708940523e-05 | -0.88% | -0.87% | 0.99x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.336072250688074e-05 | 3.327138155161625e-05 | 0.27% | 0.27% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.103551074810502e-05 | 3.13319010186648e-05 | -0.96% | -0.95% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.386995287226341e-05 | 3.316199287254045e-05 | 2.09% | 2.13% | 1.02x | ✅ |
