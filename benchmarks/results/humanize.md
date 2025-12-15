#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.054692230162976e-06 | 2.630322788203022e-06 | 35.13% | 54.15% | 1.54x | ✅ |
| `humanize_bytes[empty]` | 1.1130495361056425e-06 | 8.060124600480026e-07 | 27.59% | 38.09% | 1.38x | ✅ |
| `humanize_bytes[long]` | 3.840162613530592e-06 | 2.415393655231114e-06 | 37.10% | 58.99% | 1.59x | ✅ |
| `humanize_bytes[short]` | 1.4773992889696717e-06 | 1.0873267067113862e-06 | 26.40% | 35.87% | 1.36x | ✅ |
| `humanize_hash[32-bytes]` | 4.312501230546922e-06 | 2.65397022085495e-06 | 38.46% | 62.49% | 1.62x | ✅ |
| `humanize_hash[empty]` | 1.3394796144176565e-06 | 8.18140777473098e-07 | 38.92% | 63.72% | 1.64x | ✅ |
| `humanize_hash[long]` | 4.095433017728011e-06 | 2.440346308931434e-06 | 40.41% | 67.82% | 1.68x | ✅ |
| `humanize_hash[short]` | 1.68019647881534e-06 | 1.1103256662970016e-06 | 33.92% | 51.32% | 1.51x | ✅ |
| `humanize_hexstr[empty]` | 1.7801035385983939e-06 | 5.724323333662404e-07 | 67.84% | 210.97% | 3.11x | ✅ |
| `humanize_hexstr[short-0x]` | 4.477226511347377e-06 | 2.270604743990379e-06 | 49.29% | 97.18% | 1.97x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.8047147162725335e-06 | 1.8287684275838332e-06 | 51.93% | 108.05% | 2.08x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.575044264369588e-06 | 2.311084314950645e-06 | 49.48% | 97.96% | 1.98x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.8014403317162036e-06 | 1.8311368870236881e-06 | 51.83% | 107.60% | 2.08x | ✅ |
| `humanize_integer_sequence[consecutive]` | 2.853560634310148e-05 | 2.197479100382603e-05 | 22.99% | 29.86% | 1.30x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.428648972149842e-05 | 2.7057565207804755e-05 | 21.08% | 26.72% | 1.27x | ✅ |
| `humanize_integer_sequence[empty]` | 7.867807964453693e-07 | 5.256854010673947e-07 | 33.19% | 49.67% | 1.50x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.206390584794097e-05 | 3.4857024685537694e-05 | 17.13% | 20.68% | 1.21x | ✅ |
| `humanize_integer_sequence[single]` | 2.4792837994035697e-05 | 1.8725194113995458e-05 | 24.47% | 32.40% | 1.32x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.72790294776664e-05 | 3.0494519792867287e-05 | 18.20% | 22.25% | 1.22x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.268364849911284e-05 | 6.390301310974871e-05 | -1.95% | -1.91% | 0.98x | ❌ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8402468040491646e-05 | 1.7489225509978893e-05 | 4.96% | 5.22% | 1.05x | ✅ |
| `humanize_seconds[negative]` | 2.3602696751076396e-05 | 1.69923987293324e-05 | 28.01% | 38.90% | 1.39x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.8292120646015682e-05 | 1.9824530025910872e-05 | 29.93% | 42.71% | 1.43x | ✅ |
| `humanize_seconds[one-hour]` | 1.751409761777741e-05 | 1.6346635722578236e-05 | 6.67% | 7.14% | 1.07x | ✅ |
| `humanize_seconds[one-minute]` | 1.7614546209672735e-05 | 1.7064443556434334e-05 | 3.12% | 3.22% | 1.03x | ✅ |
| `humanize_seconds[one-second]` | 1.8378439632791166e-05 | 1.7481539590989123e-05 | 4.88% | 5.13% | 1.05x | ✅ |
| `humanize_seconds[zero]` | 7.505945310004322e-07 | 5.78530605618079e-07 | 22.92% | 29.74% | 1.30x | ✅ |
| `humanize_wei[ether]` | 2.6161851520938822e-05 | 2.6479368363301666e-05 | -1.21% | -1.20% | 0.99x | ❌ |
| `humanize_wei[gwei]` | 2.584668417015341e-05 | 2.608010422326284e-05 | -0.90% | -0.90% | 0.99x | ❌ |
| `humanize_wei[wei]` | 2.5487970699484265e-05 | 2.530890981103504e-05 | 0.70% | 0.71% | 1.01x | ✅ |
| `humanize_wei[zero]` | 4.720769061001644e-06 | 4.0872888059927e-06 | 13.42% | 15.50% | 1.15x | ✅ |
| `is_ipfs_uri[empty]` | 1.6273268563062124e-05 | 1.7133879671925485e-05 | -5.29% | -5.02% | 0.95x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.046418994770711e-05 | 3.1782721909683645e-05 | -4.33% | -4.15% | 0.96x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 2.862099143814231e-05 | 2.9555846683865154e-05 | -3.27% | -3.16% | 0.97x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.09985121674969e-05 | 3.2123965947315384e-05 | -3.63% | -3.50% | 0.96x | ❌ |
