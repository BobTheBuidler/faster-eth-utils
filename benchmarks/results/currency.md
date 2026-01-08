#### [faster_eth_utils.currency](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/faster_eth_utils/currency.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/benchmarks/test_currency_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `from_wei[1-ether]` | 2.433377964018854e-05 | 2.471686142954209e-05 | -1.57% | -1.55% | 0.98x | ❌ |
| `from_wei[1-gwei]` | 2.4040339427397258e-05 | 2.433673071400837e-05 | -1.23% | -1.22% | 0.99x | ❌ |
| `from_wei[max]` | 2.628266563389171e-05 | 2.619437125245707e-05 | 0.34% | 0.34% | 1.00x | ✅ |
| `from_wei[zero]` | 2.5338860261444817e-06 | 2.6638093680555123e-06 | -5.13% | -4.88% | 0.95x | ❌ |
| `from_wei_decimals[100M-8dec]` | 2.828292182261477e-05 | 2.8574995500243266e-05 | -1.03% | -1.02% | 0.99x | ❌ |
| `from_wei_decimals[max]` | 3.032002848707155e-05 | 3.0219399072932516e-05 | 0.33% | 0.33% | 1.00x | ✅ |
| `from_wei_decimals[zero]` | 7.270297210010963e-06 | 7.071830034563276e-06 | 2.73% | 2.81% | 1.03x | ✅ |
| `to_wei[1-ether]` | 3.184545814112894e-05 | 3.076972024624364e-05 | 3.38% | 3.50% | 1.03x | ✅ |
| `to_wei[1.5-ether]` | 3.923948664654428e-05 | 3.843130114783593e-05 | 2.06% | 2.10% | 1.02x | ✅ |
| `to_wei[2str-ether]` | 3.2311283891732404e-05 | 3.137953266815446e-05 | 2.88% | 2.97% | 1.03x | ✅ |
| `to_wei[max]` | 3.76414369631858e-05 | 3.6979414418805275e-05 | 1.76% | 1.79% | 1.02x | ✅ |
| `to_wei[zero]` | 9.289709575578918e-06 | 8.272457915689995e-06 | 10.95% | 12.30% | 1.12x | ✅ |
| `to_wei_decimals[1-8dec]` | 3.6673501346656165e-05 | 3.424510216309695e-05 | 6.62% | 7.09% | 1.07x | ✅ |
| `to_wei_decimals[1.5-8dec]` | 4.4145029025365226e-05 | 4.231742165629691e-05 | 4.14% | 4.32% | 1.04x | ✅ |
| `to_wei_decimals[2str-8dec]` | 3.688477867889871e-05 | 3.4922630658072764e-05 | 5.32% | 5.62% | 1.06x | ✅ |
| `to_wei_decimals[max]` | 4.2710556767516276e-05 | 4.077516010356791e-05 | 4.53% | 4.75% | 1.05x | ✅ |
| `to_wei_decimals[zero]` | 1.3986861769500364e-05 | 1.2126243225147089e-05 | 13.30% | 15.34% | 1.15x | ✅ |
