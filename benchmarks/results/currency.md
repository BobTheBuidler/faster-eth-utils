#### [faster_eth_utils.currency](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/currency.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_currency_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `from_wei[1-ether]` | 2.42586944741995e-05 | 2.4764940558183833e-05 | -2.09% | -2.04% | 0.98x | ❌ |
| `from_wei[1-gwei]` | 2.388923530391896e-05 | 2.4285090104767545e-05 | -1.66% | -1.63% | 0.98x | ❌ |
| `from_wei[max]` | 2.6091593545213428e-05 | 2.650609700504191e-05 | -1.59% | -1.56% | 0.98x | ❌ |
| `from_wei[zero]` | 2.497362893310742e-06 | 2.7663154927607927e-06 | -10.77% | -9.72% | 0.90x | ❌ |
| `from_wei_decimals[100M-8dec]` | 2.845871305393239e-05 | 2.8833158886988798e-05 | -1.32% | -1.30% | 0.99x | ❌ |
| `from_wei_decimals[max]` | 3.072794024370695e-05 | 3.0418040135076336e-05 | 1.01% | 1.02% | 1.01x | ✅ |
| `from_wei_decimals[zero]` | 7.492593834255169e-06 | 7.3768189014136715e-06 | 1.55% | 1.57% | 1.02x | ✅ |
| `to_wei[1-ether]` | 3.2133997260167206e-05 | 3.146011936878175e-05 | 2.10% | 2.14% | 1.02x | ✅ |
| `to_wei[1.5-ether]` | 3.9874667726198855e-05 | 3.97050828337507e-05 | 0.43% | 0.43% | 1.00x | ✅ |
| `to_wei[2str-ether]` | 3.2383101271303184e-05 | 3.2077651786463355e-05 | 0.94% | 0.95% | 1.01x | ✅ |
| `to_wei[max]` | 3.847350585862753e-05 | 3.713594689279821e-05 | 3.48% | 3.60% | 1.04x | ✅ |
| `to_wei[zero]` | 9.319943964299668e-06 | 8.365314044396466e-06 | 10.24% | 11.41% | 1.11x | ✅ |
| `to_wei_decimals[1-8dec]` | 3.709039020564242e-05 | 3.485369618336993e-05 | 6.03% | 6.42% | 1.06x | ✅ |
| `to_wei_decimals[1.5-8dec]` | 4.46158681985751e-05 | 4.291075991993194e-05 | 3.82% | 3.97% | 1.04x | ✅ |
| `to_wei_decimals[2str-8dec]` | 3.683940808357784e-05 | 3.5634741375212934e-05 | 3.27% | 3.38% | 1.03x | ✅ |
| `to_wei_decimals[max]` | 4.293353805682715e-05 | 4.156247325977715e-05 | 3.19% | 3.30% | 1.03x | ✅ |
| `to_wei_decimals[zero]` | 1.3474167831871676e-05 | 1.2400356502865131e-05 | 7.97% | 8.66% | 1.09x | ✅ |
