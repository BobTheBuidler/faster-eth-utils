#### [faster_eth_utils.currency](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/currency.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_currency_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `from_wei[1-ether]` | 2.4065426871980903e-05 | 2.4502555060071372e-05 | -1.82% | -1.78% | 0.98x | ❌ |
| `from_wei[1-gwei]` | 2.36435861349146e-05 | 2.4086642251408925e-05 | -1.87% | -1.84% | 0.98x | ❌ |
| `from_wei[max]` | 2.58151310527882e-05 | 2.5837070661667598e-05 | -0.08% | -0.08% | 1.00x | ❌ |
| `from_wei[zero]` | 2.5263919269675338e-06 | 2.6407532565927774e-06 | -4.53% | -4.33% | 0.96x | ❌ |
| `from_wei_decimals[100M-8dec]` | 2.799356789884074e-05 | 2.8196551653624127e-05 | -0.73% | -0.72% | 0.99x | ❌ |
| `from_wei_decimals[max]` | 3.001308035870315e-05 | 3.0049925445444988e-05 | -0.12% | -0.12% | 1.00x | ❌ |
| `from_wei_decimals[zero]` | 7.367745562773075e-06 | 7.236153706443468e-06 | 1.79% | 1.82% | 1.02x | ✅ |
| `to_wei[1-ether]` | 3.183551811290308e-05 | 3.077384534918388e-05 | 3.33% | 3.45% | 1.03x | ✅ |
| `to_wei[1.5-ether]` | 3.9117194821214145e-05 | 3.84056509158363e-05 | 1.82% | 1.85% | 1.02x | ✅ |
| `to_wei[2str-ether]` | 3.210966271913302e-05 | 3.1599351163690086e-05 | 1.59% | 1.61% | 1.02x | ✅ |
| `to_wei[max]` | 3.773025707047305e-05 | 3.640746597155352e-05 | 3.51% | 3.63% | 1.04x | ✅ |
| `to_wei[zero]` | 9.151642982299771e-06 | 8.029185616316205e-06 | 12.27% | 13.98% | 1.14x | ✅ |
| `to_wei_decimals[1-8dec]` | 3.656914560880431e-05 | 3.438100508036144e-05 | 5.98% | 6.36% | 1.06x | ✅ |
| `to_wei_decimals[1.5-8dec]` | 4.3669724362126546e-05 | 4.169039201429902e-05 | 4.53% | 4.75% | 1.05x | ✅ |
| `to_wei_decimals[2str-8dec]` | 3.6531183827047266e-05 | 3.4929068636775114e-05 | 4.39% | 4.59% | 1.05x | ✅ |
| `to_wei_decimals[max]` | 4.271788207818289e-05 | 4.066179551490336e-05 | 4.81% | 5.06% | 1.05x | ✅ |
| `to_wei_decimals[zero]` | 1.3423431940681044e-05 | 1.2215329678615476e-05 | 9.00% | 9.89% | 1.10x | ✅ |
