#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.201688991234385e-06 | 2.6213660254076104e-06 | 37.61% | 60.29% | 1.60x | ✅ |
| `humanize_bytes[empty]` | 1.1211285844419552e-06 | 8.145796803676258e-07 | 27.34% | 37.63% | 1.38x | ✅ |
| `humanize_bytes[long]` | 4.053134437225093e-06 | 2.4188924741498887e-06 | 40.32% | 67.56% | 1.68x | ✅ |
| `humanize_bytes[short]` | 1.4750414805703551e-06 | 1.0875716479364544e-06 | 26.27% | 35.63% | 1.36x | ✅ |
| `humanize_hash[32-bytes]` | 4.4400162759414785e-06 | 2.656737553313148e-06 | 40.16% | 67.12% | 1.67x | ✅ |
| `humanize_hash[empty]` | 1.3503201667741397e-06 | 8.852843168595471e-07 | 34.44% | 52.53% | 1.53x | ✅ |
| `humanize_hash[long]` | 4.259065136043823e-06 | 2.4402103171342327e-06 | 42.71% | 74.54% | 1.75x | ✅ |
| `humanize_hash[short]` | 1.712254684607091e-06 | 1.1855271944535325e-06 | 30.76% | 44.43% | 1.44x | ✅ |
| `humanize_hexstr[empty]` | 1.8499303191170638e-06 | 6.299147197899937e-07 | 65.95% | 193.68% | 2.94x | ✅ |
| `humanize_hexstr[short-0x]` | 4.503957289953328e-06 | 2.518025862778729e-06 | 44.09% | 78.87% | 1.79x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.7624872209044908e-06 | 2.023894361609192e-06 | 46.21% | 85.90% | 1.86x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.52611543506148e-06 | 2.5678746700252956e-06 | 43.27% | 76.26% | 1.76x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.7727936608312713e-06 | 2.057225292663995e-06 | 45.47% | 83.39% | 1.83x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.14919580758456e-05 | 2.492689607258061e-05 | 20.85% | 26.34% | 1.26x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.795320577058308e-05 | 3.069112601970062e-05 | 19.13% | 23.66% | 1.24x | ✅ |
| `humanize_integer_sequence[empty]` | 9.1722132131633e-07 | 5.813701948919798e-07 | 36.62% | 57.77% | 1.58x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.750705680830341e-05 | 3.8914444165948786e-05 | 18.09% | 22.08% | 1.22x | ✅ |
| `humanize_integer_sequence[single]` | 2.69482812296712e-05 | 2.0491794596188934e-05 | 23.96% | 31.51% | 1.32x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.1743786108322165e-05 | 3.430898718500494e-05 | 17.81% | 21.67% | 1.22x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.657931798207245e-05 | 6.649027404825675e-05 | 0.13% | 0.13% | 1.00x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8927684917903802e-05 | 1.6180226436714974e-05 | 14.52% | 16.98% | 1.17x | ✅ |
| `humanize_seconds[negative]` | 2.399361215210932e-05 | 1.3772027863285883e-05 | 42.60% | 74.22% | 1.74x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.767683752779367e-05 | 1.6202870503694832e-05 | 41.46% | 70.81% | 1.71x | ✅ |
| `humanize_seconds[one-hour]` | 1.790733692703402e-05 | 1.4730563459407589e-05 | 17.74% | 21.57% | 1.22x | ✅ |
| `humanize_seconds[one-minute]` | 1.8286886521095175e-05 | 1.549790355258781e-05 | 15.25% | 18.00% | 1.18x | ✅ |
| `humanize_seconds[one-second]` | 1.9127656076813958e-05 | 1.6823290595232656e-05 | 12.05% | 13.70% | 1.14x | ✅ |
| `humanize_seconds[zero]` | 8.922350651730308e-07 | 8.188522050551798e-07 | 8.22% | 8.96% | 1.09x | ✅ |
| `humanize_wei[ether]` | 2.730375540137808e-05 | 2.6086720739735943e-05 | 4.46% | 4.67% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.689458270694781e-05 | 2.5531996833498216e-05 | 5.07% | 5.34% | 1.05x | ✅ |
| `humanize_wei[wei]` | 2.6679761982485057e-05 | 2.5299639956804325e-05 | 5.17% | 5.46% | 1.05x | ✅ |
| `humanize_wei[zero]` | 4.738570295498847e-06 | 3.696100045795294e-06 | 22.00% | 28.20% | 1.28x | ✅ |
| `is_ipfs_uri[empty]` | 1.823044888975397e-05 | 1.8688860425472646e-05 | -2.51% | -2.45% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.2642071532071726e-05 | 3.24465563134323e-05 | 0.60% | 0.60% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.0327965329587465e-05 | 3.090974715611632e-05 | -1.92% | -1.88% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.319154351739005e-05 | 3.283969743335808e-05 | 1.06% | 1.07% | 1.01x | ✅ |
