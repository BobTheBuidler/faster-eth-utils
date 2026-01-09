#### [faster_eth_utils.currency](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/faster_eth_utils/currency.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/benchmarks/test_currency_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `from_wei[1-ether]` | 2.4058246854031325e-05 | 2.3856821555627195e-05 | 0.84% | 0.84% | 1.01x | ✅ |
| `from_wei[1-gwei]` | 2.37058934134928e-05 | 2.3940794085980664e-05 | -0.99% | -0.98% | 0.99x | ❌ |
| `from_wei[max]` | 2.5533367414033474e-05 | 2.5309536515452485e-05 | 0.88% | 0.88% | 1.01x | ✅ |
| `from_wei[zero]` | 2.478421359993946e-06 | 2.058679586420217e-06 | 16.94% | 20.39% | 1.20x | ✅ |
| `from_wei_decimals[100M-8dec]` | 2.793847294640053e-05 | 2.8644681447199988e-05 | -2.53% | -2.47% | 0.98x | ❌ |
| `from_wei_decimals[max]` | 2.981661143572102e-05 | 3.022719994896726e-05 | -1.38% | -1.36% | 0.99x | ❌ |
| `from_wei_decimals[zero]` | 7.232595889196171e-06 | 7.31441126355718e-06 | -1.13% | -1.12% | 0.99x | ❌ |
| `to_wei[1-ether]` | 3.1721913818152994e-05 | 2.804554355747464e-05 | 11.59% | 13.11% | 1.13x | ✅ |
| `to_wei[1.5-ether]` | 3.9403811380382995e-05 | 3.582126993996724e-05 | 9.09% | 10.00% | 1.10x | ✅ |
| `to_wei[2str-ether]` | 3.212395546780168e-05 | 2.872320756532895e-05 | 10.59% | 11.84% | 1.12x | ✅ |
| `to_wei[max]` | 3.7308920190481283e-05 | 3.379609250857475e-05 | 9.42% | 10.39% | 1.10x | ✅ |
| `to_wei[zero]` | 9.15591772581693e-06 | 5.760368554584796e-06 | 37.09% | 58.95% | 1.59x | ✅ |
| `to_wei_decimals[1-8dec]` | 3.7266254996092965e-05 | 3.285237391757054e-05 | 11.84% | 13.44% | 1.13x | ✅ |
| `to_wei_decimals[1.5-8dec]` | 4.446950888458535e-05 | 4.096273690906376e-05 | 7.89% | 8.56% | 1.09x | ✅ |
| `to_wei_decimals[2str-8dec]` | 3.736473791951859e-05 | 3.380927438546433e-05 | 9.52% | 10.52% | 1.11x | ✅ |
| `to_wei_decimals[max]` | 4.244942475446479e-05 | 3.8877007834240025e-05 | 8.42% | 9.19% | 1.09x | ✅ |
| `to_wei_decimals[zero]` | 1.3376800483088804e-05 | 1.0406898549342596e-05 | 22.20% | 28.54% | 1.29x | ✅ |
