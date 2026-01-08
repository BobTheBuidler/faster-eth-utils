#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.195559206312389e-06 | 2.7289806935082437e-06 | 34.96% | 53.74% | 1.54x | ✅ |
| `humanize_bytes[empty]` | 1.0918745632723016e-06 | 8.154199998269698e-07 | 25.32% | 33.90% | 1.34x | ✅ |
| `humanize_bytes[long]` | 4.013027982957501e-06 | 2.5527161307406676e-06 | 36.39% | 57.21% | 1.57x | ✅ |
| `humanize_bytes[short]` | 1.4490094937247164e-06 | 1.121507863786382e-06 | 22.60% | 29.20% | 1.29x | ✅ |
| `humanize_hash[32-bytes]` | 4.465541106943984e-06 | 2.774312772308675e-06 | 37.87% | 60.96% | 1.61x | ✅ |
| `humanize_hash[empty]` | 1.322272447702766e-06 | 8.256115869721042e-07 | 37.56% | 60.16% | 1.60x | ✅ |
| `humanize_hash[long]` | 4.203648065086245e-06 | 2.57130292397773e-06 | 38.83% | 63.48% | 1.63x | ✅ |
| `humanize_hash[short]` | 1.6851276101992446e-06 | 1.1291002941864996e-06 | 33.00% | 49.25% | 1.49x | ✅ |
| `humanize_hexstr[empty]` | 1.8481591209713417e-06 | 6.21650612989392e-07 | 66.36% | 197.30% | 2.97x | ✅ |
| `humanize_hexstr[short-0x]` | 4.510346376268385e-06 | 2.52217416506103e-06 | 44.08% | 78.83% | 1.79x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.767773406066532e-06 | 2.06682878298316e-06 | 45.14% | 82.30% | 1.82x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.566818274741915e-06 | 2.4828839288063005e-06 | 45.63% | 83.93% | 1.84x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.7706419139935597e-06 | 2.060148941102863e-06 | 45.36% | 83.03% | 1.83x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0376823001577345e-05 | 2.397581268169407e-05 | 21.07% | 26.70% | 1.27x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.674942483234277e-05 | 2.9423208333224677e-05 | 19.94% | 24.90% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 8.96289817465724e-07 | 5.74527588876864e-07 | 35.90% | 56.00% | 1.56x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.53504257932044e-05 | 3.73888812200122e-05 | 17.56% | 21.29% | 1.21x | ✅ |
| `humanize_integer_sequence[single]` | 2.6371709015606404e-05 | 2.0258502976350597e-05 | 23.18% | 30.18% | 1.30x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.039718757578211e-05 | 3.281375448448956e-05 | 18.77% | 23.11% | 1.23x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.657011498546072e-05 | 6.624987326849583e-05 | 0.48% | 0.48% | 1.00x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9025179033101852e-05 | 1.7803969884856285e-05 | 6.42% | 6.86% | 1.07x | ✅ |
| `humanize_seconds[negative]` | 2.3689129469848084e-05 | 1.7523906338318674e-05 | 26.03% | 35.18% | 1.35x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7677231966203362e-05 | 1.9756413584601342e-05 | 28.62% | 40.09% | 1.40x | ✅ |
| `humanize_seconds[one-hour]` | 1.7817978573634067e-05 | 1.6533288981965357e-05 | 7.21% | 7.77% | 1.08x | ✅ |
| `humanize_seconds[one-minute]` | 1.8065993835794186e-05 | 1.7284911802161175e-05 | 4.32% | 4.52% | 1.05x | ✅ |
| `humanize_seconds[one-second]` | 1.8949289946266948e-05 | 1.7780355743872703e-05 | 6.17% | 6.57% | 1.07x | ✅ |
| `humanize_seconds[zero]` | 8.805933451362529e-07 | 6.42484643818174e-07 | 27.04% | 37.06% | 1.37x | ✅ |
| `humanize_wei[ether]` | 2.6853460977661433e-05 | 2.6685974617025552e-05 | 0.62% | 0.63% | 1.01x | ✅ |
| `humanize_wei[gwei]` | 2.675235365086016e-05 | 2.6270798954268085e-05 | 1.80% | 1.83% | 1.02x | ✅ |
| `humanize_wei[wei]` | 2.6655632576963807e-05 | 2.5930783298668197e-05 | 2.72% | 2.80% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.853430627147685e-06 | 4.151302418873973e-06 | 14.47% | 16.91% | 1.17x | ✅ |
| `is_ipfs_uri[empty]` | 1.8384199367553572e-05 | 1.885168629707138e-05 | -2.54% | -2.48% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.270107121487959e-05 | 3.267084543120307e-05 | 0.09% | 0.09% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.0501043516670886e-05 | 3.1056186198270603e-05 | -1.82% | -1.79% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3285817295074267e-05 | 3.31627652183992e-05 | 0.37% | 0.37% | 1.00x | ✅ |
