#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.155703795794867e-06 | 2.530545261341664e-06 | 39.11% | 64.22% | 1.64x | ✅ |
| `humanize_bytes[empty]` | 1.1440270091344284e-06 | 8.370032136262386e-07 | 26.84% | 36.68% | 1.37x | ✅ |
| `humanize_bytes[long]` | 3.9534443089031475e-06 | 2.3282949964705906e-06 | 41.11% | 69.80% | 1.70x | ✅ |
| `humanize_bytes[short]` | 1.4696962028210261e-06 | 1.139119657841414e-06 | 22.49% | 29.02% | 1.29x | ✅ |
| `humanize_hash[32-bytes]` | 4.4754188183611035e-06 | 2.5991485579786277e-06 | 41.92% | 72.19% | 1.72x | ✅ |
| `humanize_hash[empty]` | 1.3789675275338862e-06 | 8.563347951639278e-07 | 37.90% | 61.03% | 1.61x | ✅ |
| `humanize_hash[long]` | 4.184284446982142e-06 | 2.358618312238558e-06 | 43.63% | 77.40% | 1.77x | ✅ |
| `humanize_hash[short]` | 1.6622363822121148e-06 | 1.1338149534719972e-06 | 31.79% | 46.61% | 1.47x | ✅ |
| `humanize_hexstr[empty]` | 1.8739550214734897e-06 | 6.355764382225763e-07 | 66.08% | 194.84% | 2.95x | ✅ |
| `humanize_hexstr[short-0x]` | 4.731649597796996e-06 | 2.381011826582144e-06 | 49.68% | 98.72% | 1.99x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.967078717078334e-06 | 1.967489851788397e-06 | 50.40% | 101.63% | 2.02x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.7069503399377895e-06 | 2.423679941231498e-06 | 48.51% | 94.21% | 1.94x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.946512914006322e-06 | 1.9945753543444054e-06 | 49.46% | 97.86% | 1.98x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0674106876787014e-05 | 2.397491116046643e-05 | 21.84% | 27.94% | 1.28x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.686397230813502e-05 | 2.9226421466532418e-05 | 20.72% | 26.13% | 1.26x | ✅ |
| `humanize_integer_sequence[empty]` | 9.280076000004331e-07 | 5.656371811079799e-07 | 39.05% | 64.06% | 1.64x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.519880944704239e-05 | 3.645728153068933e-05 | 19.34% | 23.98% | 1.24x | ✅ |
| `humanize_integer_sequence[single]` | 2.6831655040810965e-05 | 2.011532456729614e-05 | 25.03% | 33.39% | 1.33x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.026670955313893e-05 | 3.2686932817899786e-05 | 18.82% | 23.19% | 1.23x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.784181073570534e-05 | 6.63845702625179e-05 | 2.15% | 2.20% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9163778781098918e-05 | 1.7877593540476606e-05 | 6.71% | 7.19% | 1.07x | ✅ |
| `humanize_seconds[negative]` | 2.4153763911112583e-05 | 1.7430864280111195e-05 | 27.83% | 38.57% | 1.39x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.8182980652270562e-05 | 1.982170521209129e-05 | 29.67% | 42.18% | 1.42x | ✅ |
| `humanize_seconds[one-hour]` | 1.82378140284737e-05 | 1.6774791433407114e-05 | 8.02% | 8.72% | 1.09x | ✅ |
| `humanize_seconds[one-minute]` | 1.8204926004051708e-05 | 1.72962350102363e-05 | 4.99% | 5.25% | 1.05x | ✅ |
| `humanize_seconds[one-second]` | 1.911211626284642e-05 | 1.7838057956681823e-05 | 6.67% | 7.14% | 1.07x | ✅ |
| `humanize_seconds[zero]` | 8.867479881006484e-07 | 6.414394665540656e-07 | 27.66% | 38.24% | 1.38x | ✅ |
| `humanize_wei[ether]` | 2.720929442071021e-05 | 2.6572956063378113e-05 | 2.34% | 2.39% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.688620349056451e-05 | 2.6175059313730603e-05 | 2.65% | 2.72% | 1.03x | ✅ |
| `humanize_wei[wei]` | 2.677890851862789e-05 | 2.586693401766051e-05 | 3.41% | 3.53% | 1.04x | ✅ |
| `humanize_wei[zero]` | 4.85590113790415e-06 | 4.182130623519662e-06 | 13.88% | 16.11% | 1.16x | ✅ |
| `is_ipfs_uri[empty]` | 1.8298784209675994e-05 | 1.867520186685402e-05 | -2.06% | -2.02% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.2855341266417485e-05 | 3.291571839387512e-05 | -0.18% | -0.18% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.078598482928662e-05 | 3.1222280453670006e-05 | -1.42% | -1.40% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3972356305168474e-05 | 3.311741875926636e-05 | 2.52% | 2.58% | 1.03x | ✅ |
