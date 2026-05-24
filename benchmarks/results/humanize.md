#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.446481731416783e-06 | 2.6324344998004994e-06 | 40.80% | 68.91% | 1.69x | ✅ |
| `humanize_bytes[empty]` | 1.1414561113648342e-06 | 8.45826453292686e-07 | 25.90% | 34.95% | 1.35x | ✅ |
| `humanize_bytes[long]` | 4.1889307039996386e-06 | 2.436321685643367e-06 | 41.84% | 71.94% | 1.72x | ✅ |
| `humanize_bytes[short]` | 1.5253308746254519e-06 | 1.113295401806558e-06 | 27.01% | 37.01% | 1.37x | ✅ |
| `humanize_hash[32-bytes]` | 4.733859870539322e-06 | 2.696549619351006e-06 | 43.04% | 75.55% | 1.76x | ✅ |
| `humanize_hash[empty]` | 1.3323418520394138e-06 | 8.65906140524013e-07 | 35.01% | 53.87% | 1.54x | ✅ |
| `humanize_hash[long]` | 4.537605475686966e-06 | 2.5255179775199013e-06 | 44.34% | 79.67% | 1.80x | ✅ |
| `humanize_hash[short]` | 1.7278729849819158e-06 | 1.1206120445207776e-06 | 35.14% | 54.19% | 1.54x | ✅ |
| `humanize_hexstr[empty]` | 1.8894480122641218e-06 | 6.716100517047513e-07 | 64.45% | 181.33% | 2.81x | ✅ |
| `humanize_hexstr[short-0x]` | 4.805555933119698e-06 | 2.49143412928164e-06 | 48.16% | 92.88% | 1.93x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.034882579526764e-06 | 2.0597957274618113e-06 | 48.95% | 95.89% | 1.96x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.75345215796274e-06 | 2.5555648350322916e-06 | 46.24% | 86.00% | 1.86x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.026131873373409e-06 | 2.0858216193000942e-06 | 48.19% | 93.02% | 1.93x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.1254586812578255e-05 | 2.494680248629585e-05 | 20.18% | 25.28% | 1.25x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.8366014868688615e-05 | 3.024568091611605e-05 | 21.17% | 26.85% | 1.27x | ✅ |
| `humanize_integer_sequence[empty]` | 8.675742479140129e-07 | 5.911667530664836e-07 | 31.86% | 46.76% | 1.47x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.7387937419468146e-05 | 3.822775930659057e-05 | 19.33% | 23.96% | 1.24x | ✅ |
| `humanize_integer_sequence[single]` | 2.7407197716768698e-05 | 2.148748215681266e-05 | 21.60% | 27.55% | 1.28x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.205286818189068e-05 | 3.353321749731881e-05 | 20.26% | 25.41% | 1.25x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.905677757240695e-05 | 6.887024733711857e-05 | 0.27% | 0.27% | 1.00x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9132597513954123e-05 | 1.7532612608628e-05 | 8.36% | 9.13% | 1.09x | ✅ |
| `humanize_seconds[negative]` | 2.3934694825871886e-05 | 1.449238015268536e-05 | 39.45% | 65.15% | 1.65x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.785884866935737e-05 | 1.693879180825194e-05 | 39.20% | 64.47% | 1.64x | ✅ |
| `humanize_seconds[one-hour]` | 1.8150553405737052e-05 | 1.5932767676325512e-05 | 12.22% | 13.92% | 1.14x | ✅ |
| `humanize_seconds[one-minute]` | 1.8448875595197892e-05 | 1.6515376063488168e-05 | 10.48% | 11.71% | 1.12x | ✅ |
| `humanize_seconds[one-second]` | 1.9377041658025856e-05 | 1.733146790785164e-05 | 10.56% | 11.80% | 1.12x | ✅ |
| `humanize_seconds[zero]` | 8.343170005108505e-07 | 7.338205511499595e-07 | 12.05% | 13.69% | 1.14x | ✅ |
| `humanize_wei[ether]` | 2.8913666665864707e-05 | 2.6442846058021973e-05 | 8.55% | 9.34% | 1.09x | ✅ |
| `humanize_wei[gwei]` | 2.8331919863788168e-05 | 2.6479398152288945e-05 | 6.54% | 7.00% | 1.07x | ✅ |
| `humanize_wei[wei]` | 2.799029210443071e-05 | 2.5734306775608874e-05 | 8.06% | 8.77% | 1.09x | ✅ |
| `humanize_wei[zero]` | 5.1363107240921045e-06 | 3.2294999967567745e-06 | 37.12% | 59.04% | 1.59x | ✅ |
| `is_ipfs_uri[empty]` | 1.875099227302181e-05 | 1.923403037739895e-05 | -2.58% | -2.51% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.352253669894288e-05 | 3.36243123234534e-05 | -0.30% | -0.30% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.108844909226259e-05 | 3.186195789547676e-05 | -2.49% | -2.43% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.456511014313894e-05 | 3.380831605015408e-05 | 2.19% | 2.24% | 1.02x | ✅ |
