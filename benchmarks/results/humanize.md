#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.2171009219226985e-06 | 2.7065790079726444e-06 | 35.82% | 55.81% | 1.56x | ✅ |
| `humanize_bytes[empty]` | 1.0861858965640743e-06 | 8.329753656701032e-07 | 23.31% | 30.40% | 1.30x | ✅ |
| `humanize_bytes[long]` | 3.991642443985229e-06 | 2.5353786129426806e-06 | 36.48% | 57.44% | 1.57x | ✅ |
| `humanize_bytes[short]` | 1.4494537221775958e-06 | 1.1360436698901672e-06 | 21.62% | 27.59% | 1.28x | ✅ |
| `humanize_hash[32-bytes]` | 4.4617899833759725e-06 | 2.683625614139655e-06 | 39.85% | 66.26% | 1.66x | ✅ |
| `humanize_hash[empty]` | 1.3509535148059646e-06 | 8.077357914108881e-07 | 40.21% | 67.25% | 1.67x | ✅ |
| `humanize_hash[long]` | 4.271106804011548e-06 | 2.4951199903129604e-06 | 41.58% | 71.18% | 1.71x | ✅ |
| `humanize_hash[short]` | 1.695527298290477e-06 | 1.0971737178373818e-06 | 35.29% | 54.54% | 1.55x | ✅ |
| `humanize_hexstr[empty]` | 1.8428259075629108e-06 | 6.207672750638292e-07 | 66.31% | 196.86% | 2.97x | ✅ |
| `humanize_hexstr[short-0x]` | 4.511986815443616e-06 | 2.523306915033809e-06 | 44.08% | 78.81% | 1.79x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.790447085366467e-06 | 2.076118094668868e-06 | 45.23% | 82.57% | 1.83x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.5672010664904544e-06 | 2.520136715364788e-06 | 44.82% | 81.23% | 1.81x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.746995615861905e-06 | 2.0818813481804663e-06 | 44.44% | 79.98% | 1.80x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0598090593567635e-05 | 2.4349179612182535e-05 | 20.42% | 25.66% | 1.26x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.698676427844555e-05 | 2.9656277136488104e-05 | 19.82% | 24.72% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 9.568681633679745e-07 | 5.772262560860607e-07 | 39.68% | 65.77% | 1.66x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.6049509912551045e-05 | 3.754513310563722e-05 | 18.47% | 22.65% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.6638191004854892e-05 | 2.0096614854028767e-05 | 24.56% | 32.55% | 1.33x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.061489666408705e-05 | 3.319789867679162e-05 | 18.26% | 22.34% | 1.22x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.752994723462221e-05 | 6.68929912509703e-05 | 0.94% | 0.95% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.932402031659906e-05 | 1.8209784635403814e-05 | 5.77% | 6.12% | 1.06x | ✅ |
| `humanize_seconds[negative]` | 2.3684989544817397e-05 | 1.7649611185780456e-05 | 25.48% | 34.20% | 1.34x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.78444835189697e-05 | 2.033579056648824e-05 | 26.97% | 36.92% | 1.37x | ✅ |
| `humanize_seconds[one-hour]` | 1.8086491346684984e-05 | 1.6881979704741818e-05 | 6.66% | 7.13% | 1.07x | ✅ |
| `humanize_seconds[one-minute]` | 1.806026732676793e-05 | 1.7539060906907243e-05 | 2.89% | 2.97% | 1.03x | ✅ |
| `humanize_seconds[one-second]` | 1.905726475384024e-05 | 1.8302160929888422e-05 | 3.96% | 4.13% | 1.04x | ✅ |
| `humanize_seconds[zero]` | 8.569237702153291e-07 | 6.41590864331521e-07 | 25.13% | 33.56% | 1.34x | ✅ |
| `humanize_wei[ether]` | 2.751814060007323e-05 | 2.673369261989966e-05 | 2.85% | 2.93% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.7016810101540405e-05 | 2.6438580060150405e-05 | 2.14% | 2.19% | 1.02x | ✅ |
| `humanize_wei[wei]` | 2.694541955208885e-05 | 2.579429858661731e-05 | 4.27% | 4.46% | 1.04x | ✅ |
| `humanize_wei[zero]` | 4.782770247245828e-06 | 3.5122161897781113e-06 | 26.57% | 36.18% | 1.36x | ✅ |
| `is_ipfs_uri[empty]` | 1.827402204489447e-05 | 1.8970508457017653e-05 | -3.81% | -3.67% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.28099095411112e-05 | 3.304966742650553e-05 | -0.73% | -0.73% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.075532321488594e-05 | 3.125051283752653e-05 | -1.61% | -1.58% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3479645626931375e-05 | 3.3544524529689935e-05 | -0.19% | -0.19% | 1.00x | ❌ |
