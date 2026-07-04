#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.359655220510663e-06 | 2.548914936729907e-06 | 41.53% | 71.04% | 1.71x | ✅ |
| `humanize_bytes[empty]` | 1.2073433398548018e-06 | 8.307623438063368e-07 | 31.19% | 45.33% | 1.45x | ✅ |
| `humanize_bytes[long]` | 4.144147872152421e-06 | 2.3432153014536156e-06 | 43.46% | 76.86% | 1.77x | ✅ |
| `humanize_bytes[short]` | 1.602555971038956e-06 | 1.0648908761300948e-06 | 33.55% | 50.49% | 1.50x | ✅ |
| `humanize_hash[32-bytes]` | 4.578168053157499e-06 | 2.5398215530487094e-06 | 44.52% | 80.26% | 1.80x | ✅ |
| `humanize_hash[empty]` | 1.3866576944679064e-06 | 8.500003917961419e-07 | 38.70% | 63.14% | 1.63x | ✅ |
| `humanize_hash[long]` | 4.34077882626403e-06 | 2.3559613751095897e-06 | 45.72% | 84.25% | 1.84x | ✅ |
| `humanize_hash[short]` | 1.8143104311337056e-06 | 1.0856220398215968e-06 | 40.16% | 67.12% | 1.67x | ✅ |
| `humanize_hexstr[empty]` | 1.9286948293623917e-06 | 6.533432055085074e-07 | 66.13% | 195.20% | 2.95x | ✅ |
| `humanize_hexstr[short-0x]` | 4.77453706360892e-06 | 2.4603512767470145e-06 | 48.47% | 94.06% | 1.94x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.0601178046298995e-06 | 1.940444505750616e-06 | 52.21% | 109.24% | 2.09x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.929262907507088e-06 | 2.454963474411307e-06 | 50.20% | 100.79% | 2.01x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.183374016489433e-06 | 1.9625624833861386e-06 | 53.09% | 113.16% | 2.13x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.085852925549477e-05 | 2.4199980091415855e-05 | 21.58% | 27.51% | 1.28x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.736286312429554e-05 | 2.9183813699912613e-05 | 21.89% | 28.03% | 1.28x | ✅ |
| `humanize_integer_sequence[empty]` | 8.495548097601535e-07 | 6.102092383550601e-07 | 28.17% | 39.22% | 1.39x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.638305879636951e-05 | 3.660098705665806e-05 | 21.09% | 26.73% | 1.27x | ✅ |
| `humanize_integer_sequence[single]` | 2.700947681504566e-05 | 2.027933186350959e-05 | 24.92% | 33.19% | 1.33x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.1145785815141304e-05 | 3.248249219608198e-05 | 21.06% | 26.67% | 1.27x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.711543302568704e-05 | 6.640188821750567e-05 | 1.06% | 1.07% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8910220469476206e-05 | 1.5758794589638323e-05 | 16.67% | 20.00% | 1.20x | ✅ |
| `humanize_seconds[negative]` | 2.3394522405160553e-05 | 1.3592509852391286e-05 | 41.90% | 72.11% | 1.72x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7045881769674407e-05 | 1.5665187185995084e-05 | 42.08% | 72.65% | 1.73x | ✅ |
| `humanize_seconds[one-hour]` | 1.8017669925222332e-05 | 1.4706504312639322e-05 | 18.38% | 22.51% | 1.23x | ✅ |
| `humanize_seconds[one-minute]` | 1.8037502765364514e-05 | 1.520161265353588e-05 | 15.72% | 18.66% | 1.19x | ✅ |
| `humanize_seconds[one-second]` | 1.86100446113513e-05 | 1.5855889928956146e-05 | 14.80% | 17.37% | 1.17x | ✅ |
| `humanize_seconds[zero]` | 8.868036071211859e-07 | 6.853496567321219e-07 | 22.72% | 29.39% | 1.29x | ✅ |
| `humanize_wei[ether]` | 2.8186310803238727e-05 | 2.6687855969486108e-05 | 5.32% | 5.61% | 1.06x | ✅ |
| `humanize_wei[gwei]` | 2.7986620269672145e-05 | 2.6198891333135706e-05 | 6.39% | 6.82% | 1.07x | ✅ |
| `humanize_wei[wei]` | 2.7633875227733005e-05 | 2.590268504652941e-05 | 6.26% | 6.68% | 1.07x | ✅ |
| `humanize_wei[zero]` | 4.976115895319352e-06 | 3.123940890843602e-06 | 37.22% | 59.29% | 1.59x | ✅ |
| `is_ipfs_uri[empty]` | 1.838887637078958e-05 | 1.834348480575799e-05 | 0.25% | 0.25% | 1.00x | ✅ |
| `is_ipfs_uri[invalid-cid]` | 3.299398870450817e-05 | 3.300031514088722e-05 | -0.02% | -0.02% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.0662432780565744e-05 | 3.157733789685674e-05 | -2.98% | -2.90% | 0.97x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3653113080221576e-05 | 3.330806479113886e-05 | 1.03% | 1.04% | 1.01x | ✅ |
