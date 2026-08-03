#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.417971200518755e-06 | 2.5885290166663626e-06 | 41.41% | 70.67% | 1.71x | ✅ |
| `humanize_bytes[empty]` | 1.2309347781594521e-06 | 8.133668347559675e-07 | 33.92% | 51.34% | 1.51x | ✅ |
| `humanize_bytes[long]` | 4.1893924669280555e-06 | 2.379221444600447e-06 | 43.21% | 76.08% | 1.76x | ✅ |
| `humanize_bytes[short]` | 1.6210742002117062e-06 | 1.0465792423080142e-06 | 35.44% | 54.89% | 1.55x | ✅ |
| `humanize_hash[32-bytes]` | 4.617612764832319e-06 | 2.6107290411650796e-06 | 43.46% | 76.87% | 1.77x | ✅ |
| `humanize_hash[empty]` | 1.3982925642672907e-06 | 8.447135469697121e-07 | 39.59% | 65.53% | 1.66x | ✅ |
| `humanize_hash[long]` | 4.4274367883465536e-06 | 2.411179567104987e-06 | 45.54% | 83.62% | 1.84x | ✅ |
| `humanize_hash[short]` | 1.7454555935522706e-06 | 1.0753961133821737e-06 | 38.39% | 62.31% | 1.62x | ✅ |
| `humanize_hexstr[empty]` | 1.9429157320254482e-06 | 6.557198929353125e-07 | 66.25% | 196.30% | 2.96x | ✅ |
| `humanize_hexstr[short-0x]` | 4.82573853271166e-06 | 2.4342854953287967e-06 | 49.56% | 98.24% | 1.98x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.127626437688634e-06 | 2.0177916494178783e-06 | 51.11% | 104.56% | 2.05x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.87909313472446e-06 | 2.5792606619670714e-06 | 47.14% | 89.17% | 1.89x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.074278510758353e-06 | 1.9907534433173183e-06 | 51.14% | 104.66% | 2.05x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.155100943191711e-05 | 2.536802018873994e-05 | 19.60% | 24.37% | 1.24x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.7715710454738965e-05 | 3.025900647902377e-05 | 19.77% | 24.64% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 8.433890795184739e-07 | 5.745518299557435e-07 | 31.88% | 46.79% | 1.47x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.687841278733261e-05 | 3.784178748347772e-05 | 19.28% | 23.88% | 1.24x | ✅ |
| `humanize_integer_sequence[single]` | 2.7384396494865786e-05 | 2.1022800742005888e-05 | 23.23% | 30.26% | 1.30x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.152184139948139e-05 | 3.3694721046724836e-05 | 18.85% | 23.23% | 1.23x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.918736951655455e-05 | 6.773706825139373e-05 | 2.10% | 2.14% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9310310942286537e-05 | 1.6289499279426924e-05 | 15.64% | 18.54% | 1.19x | ✅ |
| `humanize_seconds[negative]` | 2.3948144981754638e-05 | 1.3641138386575139e-05 | 43.04% | 75.56% | 1.76x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7753922667482747e-05 | 1.5823288518560393e-05 | 42.99% | 75.40% | 1.75x | ✅ |
| `humanize_seconds[one-hour]` | 1.8275053437875256e-05 | 1.5069793329677719e-05 | 17.54% | 21.27% | 1.21x | ✅ |
| `humanize_seconds[one-minute]` | 1.8359689870205386e-05 | 1.5595026067594703e-05 | 15.06% | 17.73% | 1.18x | ✅ |
| `humanize_seconds[one-second]` | 1.9356876568434665e-05 | 1.6324528473903363e-05 | 15.67% | 18.58% | 1.19x | ✅ |
| `humanize_seconds[zero]` | 8.83538072679081e-07 | 6.941940058704158e-07 | 21.43% | 27.28% | 1.27x | ✅ |
| `humanize_wei[ether]` | 2.8294912365372793e-05 | 2.714625541501679e-05 | 4.06% | 4.23% | 1.04x | ✅ |
| `humanize_wei[gwei]` | 2.8128945530319635e-05 | 2.697789845769803e-05 | 4.09% | 4.27% | 1.04x | ✅ |
| `humanize_wei[wei]` | 2.7600044745526244e-05 | 2.6490640803994044e-05 | 4.02% | 4.19% | 1.04x | ✅ |
| `humanize_wei[zero]` | 5.065468420033369e-06 | 3.1792869848510436e-06 | 37.24% | 59.33% | 1.59x | ✅ |
| `is_ipfs_uri[empty]` | 1.908645226988092e-05 | 1.9094368703099736e-05 | -0.04% | -0.04% | 1.00x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.427464916324918e-05 | 3.362229515222516e-05 | 1.90% | 1.94% | 1.02x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.236951367334354e-05 | 3.183895924237426e-05 | 1.64% | 1.67% | 1.02x | ✅ |
| `is_ipfs_uri[valid-cidv0]` | 3.504014198678634e-05 | 3.394932910359093e-05 | 3.11% | 3.21% | 1.03x | ✅ |
