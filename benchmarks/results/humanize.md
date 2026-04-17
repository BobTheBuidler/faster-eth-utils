#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.17500086309669e-06 | 2.691704379935004e-06 | 35.53% | 55.11% | 1.55x | ✅ |
| `humanize_bytes[empty]` | 1.1752285186412392e-06 | 8.128352742647207e-07 | 30.84% | 44.58% | 1.45x | ✅ |
| `humanize_bytes[long]` | 3.956811644030961e-06 | 2.4980692175339284e-06 | 36.87% | 58.39% | 1.58x | ✅ |
| `humanize_bytes[short]` | 1.4909238783287962e-06 | 1.1901062785586067e-06 | 20.18% | 25.28% | 1.25x | ✅ |
| `humanize_hash[32-bytes]` | 4.373434860948984e-06 | 2.7374368145761338e-06 | 37.41% | 59.76% | 1.60x | ✅ |
| `humanize_hash[empty]` | 1.4007229440338623e-06 | 8.377015700949512e-07 | 40.20% | 67.21% | 1.67x | ✅ |
| `humanize_hash[long]` | 4.167380699181223e-06 | 2.5382993683116803e-06 | 39.09% | 64.18% | 1.64x | ✅ |
| `humanize_hash[short]` | 1.7227461254270856e-06 | 1.3132612969674728e-06 | 23.77% | 31.18% | 1.31x | ✅ |
| `humanize_hexstr[empty]` | 1.9419867343304734e-06 | 6.744494510372369e-07 | 65.27% | 187.94% | 2.88x | ✅ |
| `humanize_hexstr[short-0x]` | 4.671893071420521e-06 | 2.6112220971232425e-06 | 44.11% | 78.92% | 1.79x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.923098701773273e-06 | 2.236714469650864e-06 | 42.99% | 75.40% | 1.75x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.757406633357058e-06 | 2.6692557635463034e-06 | 43.89% | 78.23% | 1.78x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.95439862958635e-06 | 2.3023308506161545e-06 | 41.78% | 71.76% | 1.72x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.045108292536454e-05 | 2.3652095872849417e-05 | 22.33% | 28.75% | 1.29x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.674495540363193e-05 | 2.887229459644638e-05 | 21.43% | 27.27% | 1.27x | ✅ |
| `humanize_integer_sequence[empty]` | 8.952755620014186e-07 | 5.688776707993172e-07 | 36.46% | 57.38% | 1.57x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.5956577960655157e-05 | 3.629042804739308e-05 | 21.03% | 26.64% | 1.27x | ✅ |
| `humanize_integer_sequence[single]` | 2.665651096262868e-05 | 1.981310864623268e-05 | 25.67% | 34.54% | 1.35x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.023581626153361e-05 | 3.203577386842954e-05 | 20.38% | 25.60% | 1.26x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.780544903761776e-05 | 6.55530514040512e-05 | 3.32% | 3.44% | 1.03x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8763334036756005e-05 | 1.583640150088493e-05 | 15.60% | 18.48% | 1.18x | ✅ |
| `humanize_seconds[negative]` | 2.3110611584271525e-05 | 1.3158040010472667e-05 | 43.06% | 75.64% | 1.76x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.6968452043297248e-05 | 1.535971158508871e-05 | 43.05% | 75.58% | 1.76x | ✅ |
| `humanize_seconds[one-hour]` | 1.7945662245626117e-05 | 1.4479924482464287e-05 | 19.31% | 23.93% | 1.24x | ✅ |
| `humanize_seconds[one-minute]` | 1.8020188436300255e-05 | 1.5117841546296944e-05 | 16.11% | 19.20% | 1.19x | ✅ |
| `humanize_seconds[one-second]` | 1.8888149417467876e-05 | 1.5715076574606002e-05 | 16.80% | 20.19% | 1.20x | ✅ |
| `humanize_seconds[zero]` | 8.253728333339284e-07 | 7.93344324314605e-07 | 3.88% | 4.04% | 1.04x | ✅ |
| `humanize_wei[ether]` | 2.7373623843397178e-05 | 2.577871884807411e-05 | 5.83% | 6.19% | 1.06x | ✅ |
| `humanize_wei[gwei]` | 2.7109203038800603e-05 | 2.515492136397661e-05 | 7.21% | 7.77% | 1.08x | ✅ |
| `humanize_wei[wei]` | 2.7089289211827183e-05 | 2.4745715194500947e-05 | 8.65% | 9.47% | 1.09x | ✅ |
| `humanize_wei[zero]` | 4.778708521319668e-06 | 3.1628279553509007e-06 | 33.81% | 51.09% | 1.51x | ✅ |
| `is_ipfs_uri[empty]` | 1.8318797621316478e-05 | 1.8997982863203464e-05 | -3.71% | -3.58% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.2512584831361e-05 | 3.2695711833623876e-05 | -0.56% | -0.56% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.0310598404516747e-05 | 3.090214475227304e-05 | -1.95% | -1.91% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3258549642234185e-05 | 3.294755802753623e-05 | 0.94% | 0.94% | 1.01x | ✅ |
