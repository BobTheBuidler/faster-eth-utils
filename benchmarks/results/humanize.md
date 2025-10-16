#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.24408551614347e-06 | 2.6038410635169628e-06 | 38.65% | 62.99% | 1.63x | ✅ |
| `humanize_bytes[empty]` | 1.1743816393308957e-06 | 8.704588175480272e-07 | 25.88% | 34.92% | 1.35x | ✅ |
| `humanize_bytes[long]` | 3.962553291430839e-06 | 2.394210205066979e-06 | 39.58% | 65.51% | 1.66x | ✅ |
| `humanize_bytes[short]` | 1.4934857043644078e-06 | 1.2058198864997379e-06 | 19.26% | 23.86% | 1.24x | ✅ |
| `humanize_hash[32-bytes]` | 4.446948237722765e-06 | 2.6195968807860538e-06 | 41.09% | 69.76% | 1.70x | ✅ |
| `humanize_hash[empty]` | 1.5214952633254528e-06 | 8.742873058864778e-07 | 42.54% | 74.03% | 1.74x | ✅ |
| `humanize_hash[long]` | 4.232543625042862e-06 | 2.4232041448929025e-06 | 42.75% | 74.67% | 1.75x | ✅ |
| `humanize_hash[short]` | 1.6950783997097075e-06 | 1.1133834730422895e-06 | 34.32% | 52.25% | 1.52x | ✅ |
| `humanize_hexstr[empty]` | 1.8820591506278274e-06 | 6.760299722735101e-07 | 64.08% | 178.40% | 2.78x | ✅ |
| `humanize_hexstr[short-0x]` | 4.670036821814919e-06 | 2.4334563662667273e-06 | 47.89% | 91.91% | 1.92x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.999562170834364e-06 | 2.0422813589989075e-06 | 48.94% | 95.84% | 1.96x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.7115542772591006e-06 | 2.4832760449911894e-06 | 47.29% | 89.73% | 1.90x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.99876255295371e-06 | 2.017189945427054e-06 | 49.55% | 98.23% | 1.98x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.06821458616112e-05 | 2.3714778905519395e-05 | 22.71% | 29.38% | 1.29x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.63851626521808e-05 | 2.885331984159497e-05 | 20.70% | 26.10% | 1.26x | ✅ |
| `humanize_integer_sequence[empty]` | 9.510715596392419e-07 | 6.301268603086889e-07 | 33.75% | 50.93% | 1.51x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.412046281215948e-05 | 3.5837592998115634e-05 | 18.77% | 23.11% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.6772758366145378e-05 | 2.0006570707150915e-05 | 25.27% | 33.82% | 1.34x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.006640311096523e-05 | 3.2056200200987433e-05 | 19.99% | 24.99% | 1.25x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.738622427354026e-05 | 6.575731524223038e-05 | 2.42% | 2.48% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8961673873141238e-05 | 1.717324531265398e-05 | 9.43% | 10.41% | 1.10x | ✅ |
| `humanize_seconds[negative]` | 2.399645453074112e-05 | 1.7278584953829447e-05 | 28.00% | 38.88% | 1.39x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7860826027090293e-05 | 1.9184563033651584e-05 | 31.14% | 45.23% | 1.45x | ✅ |
| `humanize_seconds[one-hour]` | 1.7798788986770914e-05 | 1.5960631695381933e-05 | 10.33% | 11.52% | 1.12x | ✅ |
| `humanize_seconds[one-minute]` | 1.817738558872102e-05 | 1.6705839599729103e-05 | 8.10% | 8.81% | 1.09x | ✅ |
| `humanize_seconds[one-second]` | 1.8838378233392145e-05 | 1.7211740017946994e-05 | 8.63% | 9.45% | 1.09x | ✅ |
| `humanize_seconds[zero]` | 8.694923197891667e-07 | 6.814575925647004e-07 | 21.63% | 27.59% | 1.28x | ✅ |
| `humanize_wei[ether]` | 2.754240813106996e-05 | 2.7795179899318645e-05 | -0.92% | -0.91% | 0.99x | ❌ |
| `humanize_wei[gwei]` | 2.7267768343933374e-05 | 2.7434450307068908e-05 | -0.61% | -0.61% | 0.99x | ❌ |
| `humanize_wei[wei]` | 2.7160278834243578e-05 | 2.6994749027512946e-05 | 0.61% | 0.61% | 1.01x | ✅ |
| `humanize_wei[zero]` | 4.904387085336764e-06 | 4.235942865634705e-06 | 13.63% | 15.78% | 1.16x | ✅ |
| `is_ipfs_uri[empty]` | 1.8315532772282122e-05 | 1.8688372475512972e-05 | -2.04% | -2.00% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.2606918878417914e-05 | 3.258256511898315e-05 | 0.07% | 0.07% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.0418972298593698e-05 | 3.0795081286387654e-05 | -1.24% | -1.22% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.41764707565347e-05 | 3.3077831511560394e-05 | 3.21% | 3.32% | 1.03x | ✅ |
