#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.22934245968656e-06 | 2.811356540584083e-06 | 33.53% | 50.44% | 1.50x | ✅ |
| `humanize_bytes[empty]` | 1.1099251417655704e-06 | 8.068032356016786e-07 | 27.31% | 37.57% | 1.38x | ✅ |
| `humanize_bytes[long]` | 4.058007427937656e-06 | 2.658257119195451e-06 | 34.49% | 52.66% | 1.53x | ✅ |
| `humanize_bytes[short]` | 1.482511740508954e-06 | 1.2188986209147437e-06 | 17.78% | 21.63% | 1.22x | ✅ |
| `humanize_hash[32-bytes]` | 4.466731317261776e-06 | 2.8212564533259344e-06 | 36.84% | 58.32% | 1.58x | ✅ |
| `humanize_hash[empty]` | 1.3426297953408849e-06 | 8.178874215848676e-07 | 39.08% | 64.16% | 1.64x | ✅ |
| `humanize_hash[long]` | 4.246970334336008e-06 | 2.654940567048325e-06 | 37.49% | 59.96% | 1.60x | ✅ |
| `humanize_hash[short]` | 1.6851221209164096e-06 | 1.1325394352831559e-06 | 32.79% | 48.79% | 1.49x | ✅ |
| `humanize_hexstr[empty]` | 1.8606849402245836e-06 | 6.180641877582555e-07 | 66.78% | 201.05% | 3.01x | ✅ |
| `humanize_hexstr[short-0x]` | 4.494868870357527e-06 | 2.4929349757542123e-06 | 44.54% | 80.30% | 1.80x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.762580458559614e-06 | 1.9458531148162474e-06 | 48.28% | 93.36% | 1.93x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.549861015323634e-06 | 2.469430597378663e-06 | 45.73% | 84.25% | 1.84x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.7809192485523574e-06 | 1.946218174939266e-06 | 48.53% | 94.27% | 1.94x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0277068307073016e-05 | 2.4070532953514418e-05 | 20.50% | 25.78% | 1.26x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.6604078031869185e-05 | 2.9385374932937494e-05 | 19.72% | 24.57% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 9.016999212030126e-07 | 5.827821776692175e-07 | 35.37% | 54.72% | 1.55x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.57271917289889e-05 | 3.7047369499308123e-05 | 18.98% | 23.43% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.656186068684108e-05 | 1.9969838537071798e-05 | 24.82% | 33.01% | 1.33x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.028268169957785e-05 | 3.275293412387313e-05 | 18.69% | 22.99% | 1.23x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.70842678850507e-05 | 6.606709823447347e-05 | 1.52% | 1.54% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9231093070162863e-05 | 1.7935213419755254e-05 | 6.74% | 7.23% | 1.07x | ✅ |
| `humanize_seconds[negative]` | 2.4219671337468265e-05 | 1.7845624122276365e-05 | 26.32% | 35.72% | 1.36x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.751408088670995e-05 | 2.002458663549777e-05 | 27.22% | 37.40% | 1.37x | ✅ |
| `humanize_seconds[one-hour]` | 1.7982036438039016e-05 | 1.6754764219866506e-05 | 6.82% | 7.32% | 1.07x | ✅ |
| `humanize_seconds[one-minute]` | 1.8489244235305884e-05 | 1.7478696473507496e-05 | 5.47% | 5.78% | 1.06x | ✅ |
| `humanize_seconds[one-second]` | 1.9103834928356883e-05 | 1.8654110622182538e-05 | 2.35% | 2.41% | 1.02x | ✅ |
| `humanize_seconds[zero]` | 8.919153456423692e-07 | 6.62339089979959e-07 | 25.74% | 34.66% | 1.35x | ✅ |
| `humanize_wei[ether]` | 2.728051597125551e-05 | 2.713995571807162e-05 | 0.52% | 0.52% | 1.01x | ✅ |
| `humanize_wei[gwei]` | 2.6885846609265637e-05 | 2.662854641622103e-05 | 0.96% | 0.97% | 1.01x | ✅ |
| `humanize_wei[wei]` | 2.6886417270422106e-05 | 2.581181853824222e-05 | 4.00% | 4.16% | 1.04x | ✅ |
| `humanize_wei[zero]` | 4.828679282619282e-06 | 4.147376705365167e-06 | 14.11% | 16.43% | 1.16x | ✅ |
| `is_ipfs_uri[empty]` | 1.829000263071592e-05 | 1.8982724205322297e-05 | -3.79% | -3.65% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.257695890930598e-05 | 3.255567619458435e-05 | 0.07% | 0.07% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.0366396660655982e-05 | 3.112866317612468e-05 | -2.51% | -2.45% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.362828819777108e-05 | 3.299417144472903e-05 | 1.89% | 1.92% | 1.02x | ✅ |
