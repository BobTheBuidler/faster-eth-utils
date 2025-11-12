#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.271224041424849e-06 | 2.687626509018242e-06 | 37.08% | 58.92% | 1.59x | ✅ |
| `humanize_bytes[empty]` | 1.1762210878999327e-06 | 8.776072784208744e-07 | 25.39% | 34.03% | 1.34x | ✅ |
| `humanize_bytes[long]` | 4.080045099809834e-06 | 2.4151075297807192e-06 | 40.81% | 68.94% | 1.69x | ✅ |
| `humanize_bytes[short]` | 1.5150136589065701e-06 | 1.1144966189818322e-06 | 26.44% | 35.94% | 1.36x | ✅ |
| `humanize_hash[32-bytes]` | 4.527848863078253e-06 | 2.6913264225969675e-06 | 40.56% | 68.24% | 1.68x | ✅ |
| `humanize_hash[empty]` | 1.5242684653143848e-06 | 8.907113163899428e-07 | 41.56% | 71.13% | 1.71x | ✅ |
| `humanize_hash[long]` | 4.456946023033782e-06 | 2.478347959828466e-06 | 44.39% | 79.84% | 1.80x | ✅ |
| `humanize_hash[short]` | 1.7023251361005633e-06 | 1.1131923582978776e-06 | 34.61% | 52.92% | 1.53x | ✅ |
| `humanize_hexstr[empty]` | 1.8768333036393044e-06 | 7.60200796076706e-07 | 59.50% | 146.89% | 2.47x | ✅ |
| `humanize_hexstr[short-0x]` | 4.728374613704359e-06 | 2.4033450580353387e-06 | 49.17% | 96.74% | 1.97x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.943711582561618e-06 | 2.0247587218560138e-06 | 48.66% | 94.77% | 1.95x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.763484923537131e-06 | 2.424644411577683e-06 | 49.10% | 96.46% | 1.96x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.983231185121483e-06 | 1.9941865567567463e-06 | 49.94% | 99.74% | 2.00x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0240007600856825e-05 | 2.3688493150788642e-05 | 21.67% | 27.66% | 1.28x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.664199505491031e-05 | 2.8688108908919874e-05 | 21.71% | 27.73% | 1.28x | ✅ |
| `humanize_integer_sequence[empty]` | 9.548868783030885e-07 | 6.49746075134945e-07 | 31.96% | 46.96% | 1.47x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.422392404453878e-05 | 3.602315800040265e-05 | 18.54% | 22.77% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.806188888233436e-05 | 1.9787713596301246e-05 | 29.49% | 41.81% | 1.42x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.977860783506407e-05 | 3.215283328391201e-05 | 19.17% | 23.72% | 1.24x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.886226795022102e-05 | 6.646896839279407e-05 | 3.48% | 3.60% | 1.04x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.88349141133004e-05 | 1.6939288068180876e-05 | 10.06% | 11.19% | 1.11x | ✅ |
| `humanize_seconds[negative]` | 2.4153254472406885e-05 | 1.7010960206186445e-05 | 29.57% | 41.99% | 1.42x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7915682147372276e-05 | 1.8940951884104923e-05 | 32.15% | 47.38% | 1.47x | ✅ |
| `humanize_seconds[one-hour]` | 1.7808621043569337e-05 | 1.553383054373655e-05 | 12.77% | 14.64% | 1.15x | ✅ |
| `humanize_seconds[one-minute]` | 1.812893272715077e-05 | 1.633524045822412e-05 | 9.89% | 10.98% | 1.11x | ✅ |
| `humanize_seconds[one-second]` | 1.886878536877899e-05 | 1.691299072942316e-05 | 10.37% | 11.56% | 1.12x | ✅ |
| `humanize_seconds[zero]` | 8.988843951269148e-07 | 6.823294998072901e-07 | 24.09% | 31.74% | 1.32x | ✅ |
| `humanize_wei[ether]` | 2.737617434853965e-05 | 2.718702133406187e-05 | 0.69% | 0.70% | 1.01x | ✅ |
| `humanize_wei[gwei]` | 2.7328839992239346e-05 | 2.638265601334355e-05 | 3.46% | 3.59% | 1.04x | ✅ |
| `humanize_wei[wei]` | 2.701328661402691e-05 | 2.595231586845373e-05 | 3.93% | 4.09% | 1.04x | ✅ |
| `humanize_wei[zero]` | 4.9268039997751366e-06 | 4.288618397629403e-06 | 12.95% | 14.88% | 1.15x | ✅ |
| `is_ipfs_uri[empty]` | 1.8331872005170015e-05 | 1.869700108985176e-05 | -1.99% | -1.95% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.342179191446231e-05 | 3.3340002785114644e-05 | 0.24% | 0.25% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.095215021414214e-05 | 3.156859060812449e-05 | -1.99% | -1.95% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.4036084205478986e-05 | 3.35300841258366e-05 | 1.49% | 1.51% | 1.02x | ✅ |
