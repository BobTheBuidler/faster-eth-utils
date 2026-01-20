#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.250170520186314e-06 | 2.655990479094101e-06 | 37.51% | 60.02% | 1.60x | ✅ |
| `humanize_bytes[empty]` | 1.1244066935471153e-06 | 9.300873347204004e-07 | 17.28% | 20.89% | 1.21x | ✅ |
| `humanize_bytes[long]` | 4.019691890272529e-06 | 2.458227968532412e-06 | 38.85% | 63.52% | 1.64x | ✅ |
| `humanize_bytes[short]` | 1.4674587861821588e-06 | 1.175051582940735e-06 | 19.93% | 24.88% | 1.25x | ✅ |
| `humanize_hash[32-bytes]` | 4.443612490527664e-06 | 2.693492838700402e-06 | 39.39% | 64.98% | 1.65x | ✅ |
| `humanize_hash[empty]` | 1.3507203618796917e-06 | 8.184915943488032e-07 | 39.40% | 65.03% | 1.65x | ✅ |
| `humanize_hash[long]` | 4.284203790689294e-06 | 2.499033126908229e-06 | 41.67% | 71.43% | 1.71x | ✅ |
| `humanize_hash[short]` | 1.7020207468936937e-06 | 1.1003085332073706e-06 | 35.35% | 54.69% | 1.55x | ✅ |
| `humanize_hexstr[empty]` | 1.872507501412013e-06 | 6.698510226239268e-07 | 64.23% | 179.54% | 2.80x | ✅ |
| `humanize_hexstr[short-0x]` | 4.550345768310188e-06 | 2.4272928158405433e-06 | 46.66% | 87.47% | 1.87x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.803891651348216e-06 | 1.958692733712184e-06 | 48.51% | 94.21% | 1.94x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.679350264561899e-06 | 2.4742737062234107e-06 | 47.12% | 89.12% | 1.89x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.8378360949616236e-06 | 1.9581810307054596e-06 | 48.98% | 95.99% | 1.96x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0343946198246742e-05 | 2.46005462869079e-05 | 18.93% | 23.35% | 1.23x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.7157277745425004e-05 | 3.004129753620481e-05 | 19.15% | 23.69% | 1.24x | ✅ |
| `humanize_integer_sequence[empty]` | 9.204960463656104e-07 | 5.747791520694785e-07 | 37.56% | 60.15% | 1.60x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.570420397606325e-05 | 3.7971479672075124e-05 | 16.92% | 20.36% | 1.20x | ✅ |
| `humanize_integer_sequence[single]` | 2.638554930533902e-05 | 2.0550708208431493e-05 | 22.11% | 28.39% | 1.28x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.029115679876293e-05 | 3.3761383434841845e-05 | 16.21% | 19.34% | 1.19x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.76427673520931e-05 | 6.634405089537449e-05 | 1.92% | 1.96% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9146670206655313e-05 | 1.8532264707624287e-05 | 3.21% | 3.32% | 1.03x | ✅ |
| `humanize_seconds[negative]` | 2.3871323068345604e-05 | 1.7575280075678243e-05 | 26.37% | 35.82% | 1.36x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7797424642963105e-05 | 2.0026775119528713e-05 | 27.95% | 38.80% | 1.39x | ✅ |
| `humanize_seconds[one-hour]` | 1.836496390918642e-05 | 1.699407529637419e-05 | 7.46% | 8.07% | 1.08x | ✅ |
| `humanize_seconds[one-minute]` | 1.8535909875047703e-05 | 1.784475912700045e-05 | 3.73% | 3.87% | 1.04x | ✅ |
| `humanize_seconds[one-second]` | 1.9303761117352962e-05 | 1.8635273679019192e-05 | 3.46% | 3.59% | 1.04x | ✅ |
| `humanize_seconds[zero]` | 8.868903996452098e-07 | 6.777753011988233e-07 | 23.58% | 30.85% | 1.31x | ✅ |
| `humanize_wei[ether]` | 2.733228708168209e-05 | 2.5974243197793595e-05 | 4.97% | 5.23% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.690305256624915e-05 | 2.5575388004191576e-05 | 4.93% | 5.19% | 1.05x | ✅ |
| `humanize_wei[wei]` | 2.6895464182472342e-05 | 2.5287497872099335e-05 | 5.98% | 6.36% | 1.06x | ✅ |
| `humanize_wei[zero]` | 4.78979125653018e-06 | 3.589263897967228e-06 | 25.06% | 33.45% | 1.33x | ✅ |
| `is_ipfs_uri[empty]` | 1.845159391764848e-05 | 1.885048109052356e-05 | -2.16% | -2.12% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.280360503839266e-05 | 3.288215562508491e-05 | -0.24% | -0.24% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.0821604191851954e-05 | 3.088716077221718e-05 | -0.21% | -0.21% | 1.00x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.37564527384065e-05 | 3.3096808045102004e-05 | 1.95% | 1.99% | 1.02x | ✅ |
