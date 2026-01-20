#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.517333363848864e-05 | 6.83272329552055e-05 | 9.11% | 10.02% | 1.10x | ✅ |
| `clamp[at-lower]` | 7.162401371188898e-05 | 6.727398827002066e-05 | 6.07% | 6.47% | 1.06x | ✅ |
| `clamp[at-upper]` | 7.088665557153065e-05 | 6.811723475808705e-05 | 3.91% | 4.07% | 1.04x | ✅ |
| `clamp[below-lower]` | 6.916550400360032e-05 | 5.86010431569156e-05 | 15.27% | 18.03% | 1.18x | ✅ |
| `clamp[within-bounds]` | 7.146529262716671e-05 | 6.88583998497354e-05 | 3.65% | 3.79% | 1.04x | ✅ |
