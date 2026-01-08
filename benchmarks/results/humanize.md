#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.200926884065073e-06 | 2.7689614634875684e-06 | 34.09% | 51.71% | 1.52x | ✅ |
| `humanize_bytes[empty]` | 1.1347252380182078e-06 | 8.124267004157315e-07 | 28.40% | 39.67% | 1.40x | ✅ |
| `humanize_bytes[long]` | 4.013207230113809e-06 | 2.5637601596118173e-06 | 36.12% | 56.54% | 1.57x | ✅ |
| `humanize_bytes[short]` | 1.4722027843928615e-06 | 1.1202400729227689e-06 | 23.91% | 31.42% | 1.31x | ✅ |
| `humanize_hash[32-bytes]` | 4.466900627748958e-06 | 2.7850830266538606e-06 | 37.65% | 60.39% | 1.60x | ✅ |
| `humanize_hash[empty]` | 1.3729521575670062e-06 | 8.497645246230939e-07 | 38.11% | 61.57% | 1.62x | ✅ |
| `humanize_hash[long]` | 4.2491375677107234e-06 | 2.6047625233482967e-06 | 38.70% | 63.13% | 1.63x | ✅ |
| `humanize_hash[short]` | 1.6216625227640365e-06 | 1.1350053560343555e-06 | 30.01% | 42.88% | 1.43x | ✅ |
| `humanize_hexstr[empty]` | 1.8603341432915613e-06 | 6.354761906325266e-07 | 65.84% | 192.75% | 2.93x | ✅ |
| `humanize_hexstr[short-0x]` | 4.492473424360365e-06 | 2.551583662497776e-06 | 43.20% | 76.07% | 1.76x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.764460007401755e-06 | 2.0712664315958494e-06 | 44.98% | 81.75% | 1.82x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.573658846463008e-06 | 2.5541931512779334e-06 | 44.15% | 79.06% | 1.79x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.767703954788396e-06 | 2.103782325062979e-06 | 44.16% | 79.09% | 1.79x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0401285069353034e-05 | 2.422895904946002e-05 | 20.30% | 25.47% | 1.25x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.687104638759994e-05 | 2.971305053938723e-05 | 19.41% | 24.09% | 1.24x | ✅ |
| `humanize_integer_sequence[empty]` | 9.060664230904888e-07 | 5.896818492014298e-07 | 34.92% | 53.65% | 1.54x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.537167839262137e-05 | 3.7290924730839086e-05 | 17.81% | 21.67% | 1.22x | ✅ |
| `humanize_integer_sequence[single]` | 2.643597063717587e-05 | 2.0171054743799443e-05 | 23.70% | 31.06% | 1.31x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.010215924462739e-05 | 3.431358085310483e-05 | 14.43% | 16.87% | 1.17x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.704777896279938e-05 | 6.673517627033872e-05 | 0.47% | 0.47% | 1.00x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9031255554700585e-05 | 1.802305778550388e-05 | 5.30% | 5.59% | 1.06x | ✅ |
| `humanize_seconds[negative]` | 2.3713213362472375e-05 | 1.7922190735199328e-05 | 24.42% | 32.31% | 1.32x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.751676014350195e-05 | 2.0037484308684195e-05 | 27.18% | 37.33% | 1.37x | ✅ |
| `humanize_seconds[one-hour]` | 1.810883784866355e-05 | 1.7364158893143236e-05 | 4.11% | 4.29% | 1.04x | ✅ |
| `humanize_seconds[one-minute]` | 1.8128272949043152e-05 | 1.735797783993169e-05 | 4.25% | 4.44% | 1.04x | ✅ |
| `humanize_seconds[one-second]` | 1.8844060041259814e-05 | 1.7956389021155728e-05 | 4.71% | 4.94% | 1.05x | ✅ |
| `humanize_seconds[zero]` | 8.92537312575215e-07 | 6.645057402640043e-07 | 25.55% | 34.32% | 1.34x | ✅ |
| `humanize_wei[ether]` | 2.7248141282467354e-05 | 2.702751538322138e-05 | 0.81% | 0.82% | 1.01x | ✅ |
| `humanize_wei[gwei]` | 2.7513363381810264e-05 | 2.6533722222007603e-05 | 3.56% | 3.69% | 1.04x | ✅ |
| `humanize_wei[wei]` | 2.6817300455000053e-05 | 2.615305971218303e-05 | 2.48% | 2.54% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.818946734416937e-06 | 4.156350858624922e-06 | 13.75% | 15.94% | 1.16x | ✅ |
| `is_ipfs_uri[empty]` | 1.850764333958286e-05 | 1.8899545416652848e-05 | -2.12% | -2.07% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.285783724223545e-05 | 3.293426990875897e-05 | -0.23% | -0.23% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.089120755227633e-05 | 3.115234902929318e-05 | -0.85% | -0.84% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.373057609379135e-05 | 3.3340861074104105e-05 | 1.16% | 1.17% | 1.01x | ✅ |
