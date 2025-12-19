#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.245081010636548e-06 | 2.7672133695256187e-06 | 34.81% | 53.41% | 1.53x | ✅ |
| `humanize_bytes[empty]` | 1.1417557914299237e-06 | 8.110510852514485e-07 | 28.96% | 40.77% | 1.41x | ✅ |
| `humanize_bytes[long]` | 4.059460484347637e-06 | 2.600217489191833e-06 | 35.95% | 56.12% | 1.56x | ✅ |
| `humanize_bytes[short]` | 1.4922605865425018e-06 | 1.1399274719137547e-06 | 23.61% | 30.91% | 1.31x | ✅ |
| `humanize_hash[32-bytes]` | 4.460410921794175e-06 | 2.8050610914833988e-06 | 37.11% | 59.01% | 1.59x | ✅ |
| `humanize_hash[empty]` | 1.3537442585534116e-06 | 8.388209225292944e-07 | 38.04% | 61.39% | 1.61x | ✅ |
| `humanize_hash[long]` | 4.262667823363399e-06 | 2.6329655249305194e-06 | 38.23% | 61.90% | 1.62x | ✅ |
| `humanize_hash[short]` | 1.6874994029040568e-06 | 1.2580719009686436e-06 | 25.45% | 34.13% | 1.34x | ✅ |
| `humanize_hexstr[empty]` | 1.892351698914153e-06 | 7.369971356094641e-07 | 61.05% | 156.77% | 2.57x | ✅ |
| `humanize_hexstr[short-0x]` | 4.581453428146069e-06 | 2.4782656991255356e-06 | 45.91% | 84.87% | 1.85x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.83328127343614e-06 | 2.1481489894024325e-06 | 43.96% | 78.45% | 1.78x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.578491041241528e-06 | 2.468928328223221e-06 | 46.08% | 85.44% | 1.85x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.7202094861795327e-06 | 2.055536846833832e-06 | 44.75% | 80.98% | 1.81x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.017850594155076e-05 | 2.3798725307893005e-05 | 21.14% | 26.81% | 1.27x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.6916259614574796e-05 | 2.912741596886518e-05 | 21.10% | 26.74% | 1.27x | ✅ |
| `humanize_integer_sequence[empty]` | 9.18365080181112e-07 | 5.852160345486389e-07 | 36.28% | 56.93% | 1.57x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.5813313033083446e-05 | 3.6626237852129036e-05 | 20.05% | 25.08% | 1.25x | ✅ |
| `humanize_integer_sequence[single]` | 2.6648278761635164e-05 | 1.968573798890838e-05 | 26.13% | 35.37% | 1.35x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0348072162439314e-05 | 3.257000714950727e-05 | 19.28% | 23.88% | 1.24x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.73018107389497e-05 | 6.622477126592234e-05 | 1.60% | 1.63% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9173724497882868e-05 | 1.8122052527860215e-05 | 5.48% | 5.80% | 1.06x | ✅ |
| `humanize_seconds[negative]` | 2.3610300115853548e-05 | 1.8095239318812118e-05 | 23.36% | 30.48% | 1.30x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7543213421775553e-05 | 1.9965142405309193e-05 | 27.51% | 37.96% | 1.38x | ✅ |
| `humanize_seconds[one-hour]` | 1.8241529660297233e-05 | 1.6823071178107213e-05 | 7.78% | 8.43% | 1.08x | ✅ |
| `humanize_seconds[one-minute]` | 1.8447813066293425e-05 | 1.7524088597376116e-05 | 5.01% | 5.27% | 1.05x | ✅ |
| `humanize_seconds[one-second]` | 1.9315808435458477e-05 | 1.8089035624383762e-05 | 6.35% | 6.78% | 1.07x | ✅ |
| `humanize_seconds[zero]` | 8.874943258093852e-07 | 6.80005249136937e-07 | 23.38% | 30.51% | 1.31x | ✅ |
| `humanize_wei[ether]` | 2.6981642693883042e-05 | 2.6662525549037052e-05 | 1.18% | 1.20% | 1.01x | ✅ |
| `humanize_wei[gwei]` | 2.6885968222374862e-05 | 2.652391645182277e-05 | 1.35% | 1.37% | 1.01x | ✅ |
| `humanize_wei[wei]` | 2.68053798564876e-05 | 2.602820938523866e-05 | 2.90% | 2.99% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.800554628382789e-06 | 4.174491102607266e-06 | 13.04% | 15.00% | 1.15x | ✅ |
| `is_ipfs_uri[empty]` | 1.8441233633757264e-05 | 1.8924590454884978e-05 | -2.62% | -2.55% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.28324388756029e-05 | 3.301590853656274e-05 | -0.56% | -0.56% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.0435167736835986e-05 | 3.129832025502193e-05 | -2.84% | -2.76% | 0.97x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.4049504218918136e-05 | 3.3319757338594666e-05 | 2.14% | 2.19% | 1.02x | ✅ |
