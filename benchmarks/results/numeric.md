#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.34570427438605e-05 | 6.806322044067067e-05 | 7.34% | 7.92% | 1.08x | ✅ |
| `clamp[at-lower]` | 7.416058168312916e-05 | 6.71701118108667e-05 | 9.43% | 10.41% | 1.10x | ✅ |
| `clamp[at-upper]` | 7.404122370031118e-05 | 6.574971147520088e-05 | 11.20% | 12.61% | 1.13x | ✅ |
| `clamp[below-lower]` | 6.829511688854109e-05 | 5.897789276402927e-05 | 13.64% | 15.80% | 1.16x | ✅ |
| `clamp[within-bounds]` | 7.367730003642772e-05 | 6.744183324306995e-05 | 8.46% | 9.25% | 1.09x | ✅ |
