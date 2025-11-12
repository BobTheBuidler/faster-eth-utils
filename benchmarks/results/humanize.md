#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.190119919675274e-06 | 2.6199316166192455e-06 | 37.47% | 59.93% | 1.60x | ✅ |
| `humanize_bytes[empty]` | 1.1660009741996794e-06 | 8.750158150099428e-07 | 24.96% | 33.25% | 1.33x | ✅ |
| `humanize_bytes[long]` | 3.991882857725054e-06 | 2.4086284627523565e-06 | 39.66% | 65.73% | 1.66x | ✅ |
| `humanize_bytes[short]` | 1.4800632812257524e-06 | 1.0911520654254976e-06 | 26.28% | 35.64% | 1.36x | ✅ |
| `humanize_hash[32-bytes]` | 4.533331824755194e-06 | 2.6737430820000535e-06 | 41.02% | 69.55% | 1.70x | ✅ |
| `humanize_hash[empty]` | 1.4139570911677373e-06 | 8.698113068281066e-07 | 38.48% | 62.56% | 1.63x | ✅ |
| `humanize_hash[long]` | 4.247424542023933e-06 | 2.5059000098644682e-06 | 41.00% | 69.50% | 1.69x | ✅ |
| `humanize_hash[short]` | 1.68773696660869e-06 | 1.1021662948147177e-06 | 34.70% | 53.13% | 1.53x | ✅ |
| `humanize_hexstr[empty]` | 1.918398754321451e-06 | 7.571728357635207e-07 | 60.53% | 153.36% | 2.53x | ✅ |
| `humanize_hexstr[short-0x]` | 4.680286329375671e-06 | 2.4275768572356446e-06 | 48.13% | 92.80% | 1.93x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.115306612415252e-06 | 1.9900922333100364e-06 | 51.64% | 106.79% | 2.07x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.798524010382024e-06 | 2.445454217860892e-06 | 49.04% | 96.22% | 1.96x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.130056435939481e-06 | 2.0424200535813402e-06 | 50.55% | 102.21% | 2.02x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0502836203739146e-05 | 2.409042128453995e-05 | 21.02% | 26.62% | 1.27x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.697310925239645e-05 | 2.8910923972228053e-05 | 21.81% | 27.89% | 1.28x | ✅ |
| `humanize_integer_sequence[empty]` | 9.299521631129155e-07 | 6.235290525058189e-07 | 32.95% | 49.14% | 1.49x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.514428533699462e-05 | 3.596613263805151e-05 | 20.33% | 25.52% | 1.26x | ✅ |
| `humanize_integer_sequence[single]` | 2.667354136381843e-05 | 2.0074032412041226e-05 | 24.74% | 32.88% | 1.33x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.965224505801374e-05 | 3.231918103490997e-05 | 18.49% | 22.69% | 1.23x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.87980850129238e-05 | 6.713366820110608e-05 | 2.42% | 2.48% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9024388899366066e-05 | 1.7545416539611704e-05 | 7.77% | 8.43% | 1.08x | ✅ |
| `humanize_seconds[negative]` | 2.3911230689509137e-05 | 1.753385970528605e-05 | 26.67% | 36.37% | 1.36x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7990684898776542e-05 | 1.9715150910810327e-05 | 29.57% | 41.98% | 1.42x | ✅ |
| `humanize_seconds[one-hour]` | 1.7977474874188597e-05 | 1.642538084291928e-05 | 8.63% | 9.45% | 1.09x | ✅ |
| `humanize_seconds[one-minute]` | 1.824496832029545e-05 | 1.6887093579862713e-05 | 7.44% | 8.04% | 1.08x | ✅ |
| `humanize_seconds[one-second]` | 1.8939381618513655e-05 | 1.7519166479230845e-05 | 7.50% | 8.11% | 1.08x | ✅ |
| `humanize_seconds[zero]` | 8.787269656306638e-07 | 6.695700681340183e-07 | 23.80% | 31.24% | 1.31x | ✅ |
| `humanize_wei[ether]` | 2.7431708996313155e-05 | 2.6727618420329926e-05 | 2.57% | 2.63% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.7148323242266658e-05 | 2.6488350376308223e-05 | 2.43% | 2.49% | 1.02x | ✅ |
| `humanize_wei[wei]` | 2.6993626537704284e-05 | 2.6177981489497515e-05 | 3.02% | 3.12% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.933368678993021e-06 | 4.117500737106439e-06 | 16.54% | 19.81% | 1.20x | ✅ |
| `is_ipfs_uri[empty]` | 1.808816942027671e-05 | 1.8521905365000344e-05 | -2.40% | -2.34% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.270589357223733e-05 | 3.276282721894885e-05 | -0.17% | -0.17% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.0709249702030734e-05 | 3.094819909133626e-05 | -0.78% | -0.77% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.373822181757884e-05 | 3.323743234826136e-05 | 1.48% | 1.51% | 1.02x | ✅ |
