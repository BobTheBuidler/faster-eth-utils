#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.357394733953207e-06 | 2.6412517210802277e-06 | 39.38% | 64.97% | 1.65x | ✅ |
| `humanize_bytes[empty]` | 1.1614741415542807e-06 | 8.330364878384291e-07 | 28.28% | 39.43% | 1.39x | ✅ |
| `humanize_bytes[long]` | 4.094006535890779e-06 | 2.43483658155003e-06 | 40.53% | 68.14% | 1.68x | ✅ |
| `humanize_bytes[short]` | 1.5577580500343984e-06 | 1.0930528931112723e-06 | 29.83% | 42.51% | 1.43x | ✅ |
| `humanize_hash[32-bytes]` | 4.537535158960835e-06 | 2.5869555397277044e-06 | 42.99% | 75.40% | 1.75x | ✅ |
| `humanize_hash[empty]` | 1.3513985300689043e-06 | 8.210962986293173e-07 | 39.24% | 64.58% | 1.65x | ✅ |
| `humanize_hash[long]` | 4.3393745428737125e-06 | 2.398565657570646e-06 | 44.73% | 80.92% | 1.81x | ✅ |
| `humanize_hash[short]` | 1.7223924688686255e-06 | 1.0950730710635473e-06 | 36.42% | 57.29% | 1.57x | ✅ |
| `humanize_hexstr[empty]` | 1.9103684306604676e-06 | 6.785806315664757e-07 | 64.48% | 181.52% | 2.82x | ✅ |
| `humanize_hexstr[short-0x]` | 4.744001931943478e-06 | 2.462510898142499e-06 | 48.09% | 92.65% | 1.93x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.992352018192002e-06 | 2.025667884845313e-06 | 49.26% | 97.09% | 1.97x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.8540746939150355e-06 | 2.453972048321826e-06 | 49.45% | 97.80% | 1.98x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.0168171604075506e-06 | 1.9993567507435246e-06 | 50.23% | 100.91% | 2.01x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.205717654800805e-05 | 2.5005634303704097e-05 | 22.00% | 28.20% | 1.28x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.761772708992736e-05 | 3.054287307797943e-05 | 18.81% | 23.16% | 1.23x | ✅ |
| `humanize_integer_sequence[empty]` | 8.330704505248962e-07 | 5.820910960957576e-07 | 30.13% | 43.12% | 1.43x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.704982078021774e-05 | 3.7737188284884125e-05 | 19.79% | 24.68% | 1.25x | ✅ |
| `humanize_integer_sequence[single]` | 2.72003888224448e-05 | 2.088226944028825e-05 | 23.23% | 30.26% | 1.30x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.139011769957777e-05 | 3.367206546373094e-05 | 18.65% | 22.92% | 1.23x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.84116919709956e-05 | 6.808683826443848e-05 | 0.47% | 0.48% | 1.00x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9260619574378356e-05 | 1.6829969042360448e-05 | 12.62% | 14.44% | 1.14x | ✅ |
| `humanize_seconds[negative]` | 2.4576887517073932e-05 | 1.3998507093131424e-05 | 43.04% | 75.57% | 1.76x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.8330914474700206e-05 | 1.687582924947979e-05 | 40.43% | 67.88% | 1.68x | ✅ |
| `humanize_seconds[one-hour]` | 1.830572070451028e-05 | 1.5651262684693235e-05 | 14.50% | 16.96% | 1.17x | ✅ |
| `humanize_seconds[one-minute]` | 1.8591202283921908e-05 | 1.617461216272415e-05 | 13.00% | 14.94% | 1.15x | ✅ |
| `humanize_seconds[one-second]` | 1.9333392466123147e-05 | 1.6814634227840722e-05 | 13.03% | 14.98% | 1.15x | ✅ |
| `humanize_seconds[zero]` | 8.672143137091617e-07 | 8.317871033014187e-07 | 4.09% | 4.26% | 1.04x | ✅ |
| `humanize_wei[ether]` | 2.7651485651608084e-05 | 2.668897522648177e-05 | 3.48% | 3.61% | 1.04x | ✅ |
| `humanize_wei[gwei]` | 2.747193942256052e-05 | 2.575670629127062e-05 | 6.24% | 6.66% | 1.07x | ✅ |
| `humanize_wei[wei]` | 2.741947307286715e-05 | 2.540428225229451e-05 | 7.35% | 7.93% | 1.08x | ✅ |
| `humanize_wei[zero]` | 4.857747791423561e-06 | 3.221469150272197e-06 | 33.68% | 50.79% | 1.51x | ✅ |
| `is_ipfs_uri[empty]` | 1.8803716730140193e-05 | 1.903526687328015e-05 | -1.23% | -1.22% | 0.99x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.333677153742471e-05 | 3.3576877883991364e-05 | -0.72% | -0.72% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.123608131676979e-05 | 3.1865284226451844e-05 | -2.01% | -1.97% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.4211706870466045e-05 | 3.403710312199652e-05 | 0.51% | 0.51% | 1.01x | ✅ |
