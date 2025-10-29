#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.222619104617101e-06 | 2.7075063973566277e-06 | 35.88% | 55.96% | 1.56x | ✅ |
| `humanize_bytes[empty]` | 1.1653298790454716e-06 | 8.653912609733946e-07 | 25.74% | 34.66% | 1.35x | ✅ |
| `humanize_bytes[long]` | 4.018672599013307e-06 | 2.3711439015668255e-06 | 41.00% | 69.48% | 1.69x | ✅ |
| `humanize_bytes[short]` | 1.478722548266588e-06 | 1.1223732579058532e-06 | 24.10% | 31.75% | 1.32x | ✅ |
| `humanize_hash[32-bytes]` | 4.542946631066864e-06 | 2.716092766163253e-06 | 40.21% | 67.26% | 1.67x | ✅ |
| `humanize_hash[empty]` | 1.4040996410355914e-06 | 8.79796622906398e-07 | 37.34% | 59.59% | 1.60x | ✅ |
| `humanize_hash[long]` | 4.201195615753379e-06 | 2.4251676421722838e-06 | 42.27% | 73.23% | 1.73x | ✅ |
| `humanize_hash[short]` | 1.7054923048699552e-06 | 1.2162779669792548e-06 | 28.68% | 40.22% | 1.40x | ✅ |
| `humanize_hexstr[empty]` | 1.915322420710924e-06 | 6.798258900988649e-07 | 64.51% | 181.74% | 2.82x | ✅ |
| `humanize_hexstr[short-0x]` | 4.680313488888067e-06 | 2.3939118417257668e-06 | 48.85% | 95.51% | 1.96x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.983382995153835e-06 | 1.964064275677655e-06 | 50.69% | 102.81% | 2.03x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.735893080410554e-06 | 2.3843046448194494e-06 | 49.65% | 98.63% | 1.99x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.985271680124943e-06 | 1.9247320439120036e-06 | 51.70% | 107.06% | 2.07x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0538396703582545e-05 | 2.3628116544601794e-05 | 22.63% | 29.25% | 1.29x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.6678526065996974e-05 | 2.9404830108580227e-05 | 19.83% | 24.74% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 9.432951689425467e-07 | 6.254187674724061e-07 | 33.70% | 50.83% | 1.51x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.48170171278331e-05 | 3.5957954977879966e-05 | 19.77% | 24.64% | 1.25x | ✅ |
| `humanize_integer_sequence[single]` | 2.6720946543049204e-05 | 1.9960747596777448e-05 | 25.30% | 33.87% | 1.34x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.012114675083723e-05 | 3.1999445601972316e-05 | 20.24% | 25.38% | 1.25x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.882750845435045e-05 | 6.66334155250228e-05 | 3.19% | 3.29% | 1.03x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8963491301174122e-05 | 1.707752728598412e-05 | 9.95% | 11.04% | 1.11x | ✅ |
| `humanize_seconds[negative]` | 2.3944063648797685e-05 | 1.6884168089737282e-05 | 29.48% | 41.81% | 1.42x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.768470007594091e-05 | 1.8951223445859768e-05 | 31.55% | 46.08% | 1.46x | ✅ |
| `humanize_seconds[one-hour]` | 1.7899564369625912e-05 | 1.62464003437531e-05 | 9.24% | 10.18% | 1.10x | ✅ |
| `humanize_seconds[one-minute]` | 1.7942814360857474e-05 | 1.6416101062434324e-05 | 8.51% | 9.30% | 1.09x | ✅ |
| `humanize_seconds[one-second]` | 1.897925047455246e-05 | 1.6975471157779135e-05 | 10.56% | 11.80% | 1.12x | ✅ |
| `humanize_seconds[zero]` | 8.916693472693706e-07 | 6.83361331358798e-07 | 23.36% | 30.48% | 1.30x | ✅ |
| `humanize_wei[ether]` | 2.7627980003475748e-05 | 2.7298029771101635e-05 | 1.19% | 1.21% | 1.01x | ✅ |
| `humanize_wei[gwei]` | 2.762615607756499e-05 | 2.689663345316283e-05 | 2.64% | 2.71% | 1.03x | ✅ |
| `humanize_wei[wei]` | 2.7121568680634972e-05 | 2.6468488617169987e-05 | 2.41% | 2.47% | 1.02x | ✅ |
| `humanize_wei[zero]` | 4.85538172281072e-06 | 4.163649654884085e-06 | 14.25% | 16.61% | 1.17x | ✅ |
| `is_ipfs_uri[empty]` | 1.8344406901014794e-05 | 1.8740758149849358e-05 | -2.16% | -2.11% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.2776872802886774e-05 | 3.309932461112193e-05 | -0.98% | -0.97% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.067842665227262e-05 | 3.106807921388381e-05 | -1.27% | -1.25% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.384230882758388e-05 | 3.3343825310080716e-05 | 1.47% | 1.49% | 1.01x | ✅ |
