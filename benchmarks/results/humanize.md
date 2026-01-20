#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.1919395045201864e-06 | 2.746693320767541e-06 | 34.48% | 52.62% | 1.53x | ✅ |
| `humanize_bytes[empty]` | 1.1152778324348953e-06 | 9.255740773280535e-07 | 17.01% | 20.50% | 1.20x | ✅ |
| `humanize_bytes[long]` | 4.003742301243444e-06 | 2.460753205437141e-06 | 38.54% | 62.70% | 1.63x | ✅ |
| `humanize_bytes[short]` | 1.4541994731422129e-06 | 1.1564665944757958e-06 | 20.47% | 25.75% | 1.26x | ✅ |
| `humanize_hash[32-bytes]` | 4.448450395545947e-06 | 2.757260763431611e-06 | 38.02% | 61.34% | 1.61x | ✅ |
| `humanize_hash[empty]` | 1.3275004320292257e-06 | 8.020693765936931e-07 | 39.58% | 65.51% | 1.66x | ✅ |
| `humanize_hash[long]` | 4.256294140060422e-06 | 2.400959763087168e-06 | 43.59% | 77.27% | 1.77x | ✅ |
| `humanize_hash[short]` | 1.6285106770113467e-06 | 1.1372762976788812e-06 | 30.16% | 43.19% | 1.43x | ✅ |
| `humanize_hexstr[empty]` | 1.852765526253421e-06 | 6.292025924977116e-07 | 66.04% | 194.46% | 2.94x | ✅ |
| `humanize_hexstr[short-0x]` | 4.486055806106186e-06 | 2.4168247868481034e-06 | 46.13% | 85.62% | 1.86x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.7619337190870885e-06 | 1.995816391061403e-06 | 46.95% | 88.49% | 1.88x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.640989800756192e-06 | 2.404670008306816e-06 | 48.19% | 93.00% | 1.93x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.7653169756371505e-06 | 2.028512555986445e-06 | 46.13% | 85.62% | 1.86x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.045831500553297e-05 | 2.4282757828492063e-05 | 20.28% | 25.43% | 1.25x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.704243495735835e-05 | 2.9618753083962927e-05 | 20.04% | 25.06% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 9.06105176078798e-07 | 5.794464713609494e-07 | 36.05% | 56.37% | 1.56x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.549656143400386e-05 | 3.756031426810711e-05 | 17.44% | 21.13% | 1.21x | ✅ |
| `humanize_integer_sequence[single]` | 2.6530925774548454e-05 | 2.0318695317178547e-05 | 23.42% | 30.57% | 1.31x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.033958473820107e-05 | 3.303706409453293e-05 | 18.10% | 22.10% | 1.22x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.676386125635295e-05 | 6.695677243924832e-05 | -0.29% | -0.29% | 1.00x | ❌ |
| `humanize_seconds[fifty-nine-seconds]` | 1.898516445255216e-05 | 1.8463586355498097e-05 | 2.75% | 2.82% | 1.03x | ✅ |
| `humanize_seconds[negative]` | 2.3632947431526794e-05 | 1.780791182446546e-05 | 24.65% | 32.71% | 1.33x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.769458479496486e-05 | 2.0317049906196023e-05 | 26.64% | 36.31% | 1.36x | ✅ |
| `humanize_seconds[one-hour]` | 1.7956763763992588e-05 | 1.69957421100545e-05 | 5.35% | 5.65% | 1.06x | ✅ |
| `humanize_seconds[one-minute]` | 1.8290724132393066e-05 | 1.7850713321738578e-05 | 2.41% | 2.46% | 1.02x | ✅ |
| `humanize_seconds[one-second]` | 1.9154428156231193e-05 | 1.8350276837679996e-05 | 4.20% | 4.38% | 1.04x | ✅ |
| `humanize_seconds[zero]` | 8.933357263667289e-07 | 6.941510285934699e-07 | 22.30% | 28.69% | 1.29x | ✅ |
| `humanize_wei[ether]` | 2.7007021722393328e-05 | 2.5948245205312096e-05 | 3.92% | 4.08% | 1.04x | ✅ |
| `humanize_wei[gwei]` | 2.6643607828889264e-05 | 2.5689202625834745e-05 | 3.58% | 3.72% | 1.04x | ✅ |
| `humanize_wei[wei]` | 2.675653775779551e-05 | 2.5271941308945737e-05 | 5.55% | 5.87% | 1.06x | ✅ |
| `humanize_wei[zero]` | 4.8152488620922255e-06 | 3.6812228878565444e-06 | 23.55% | 30.81% | 1.31x | ✅ |
| `is_ipfs_uri[empty]` | 1.8463170983066985e-05 | 1.9311143188025095e-05 | -4.59% | -4.39% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.268089839283043e-05 | 3.283396917398849e-05 | -0.47% | -0.47% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.060817650019886e-05 | 3.115791406289815e-05 | -1.80% | -1.76% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3509130611303396e-05 | 3.324165176094841e-05 | 0.80% | 0.80% | 1.01x | ✅ |
