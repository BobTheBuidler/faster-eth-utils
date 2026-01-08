#### [faster_eth_utils.currency](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/faster_eth_utils/currency.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/benchmarks/test_currency_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `from_wei[1-ether]` | 2.4529534835202027e-05 | 2.4385923447767155e-05 | 0.59% | 0.59% | 1.01x | ✅ |
| `from_wei[1-gwei]` | 2.3951778659359272e-05 | 2.400515060394904e-05 | -0.22% | -0.22% | 1.00x | ❌ |
| `from_wei[max]` | 2.6290075193327226e-05 | 2.5559988974854454e-05 | 2.78% | 2.86% | 1.03x | ✅ |
| `from_wei[zero]` | 2.5761252514859208e-06 | 2.1345807551224213e-06 | 17.14% | 20.69% | 1.21x | ✅ |
| `from_wei_decimals[100M-8dec]` | 2.8478512825441096e-05 | 3.0555436114941714e-05 | -7.29% | -6.80% | 0.93x | ❌ |
| `from_wei_decimals[max]` | 3.0283619252381562e-05 | 3.185086372136116e-05 | -5.18% | -4.92% | 0.95x | ❌ |
| `from_wei_decimals[zero]` | 7.2059234859676135e-06 | 7.2322298422333606e-06 | -0.37% | -0.36% | 1.00x | ❌ |
| `to_wei[1-ether]` | 3.249590641540291e-05 | 2.8697718605573548e-05 | 11.69% | 13.24% | 1.13x | ✅ |
| `to_wei[1.5-ether]` | 4.002515468154093e-05 | 3.637724308879731e-05 | 9.11% | 10.03% | 1.10x | ✅ |
| `to_wei[2str-ether]` | 3.2640604956216875e-05 | 2.9564246370735103e-05 | 9.42% | 10.41% | 1.10x | ✅ |
| `to_wei[max]` | 3.852728801490582e-05 | 3.4128794115999097e-05 | 11.42% | 12.89% | 1.13x | ✅ |
| `to_wei[zero]` | 9.381601014352305e-06 | 5.738028858334713e-06 | 38.84% | 63.50% | 1.63x | ✅ |
| `to_wei_decimals[1-8dec]` | 3.749594786305286e-05 | 3.339388087619705e-05 | 10.94% | 12.28% | 1.12x | ✅ |
| `to_wei_decimals[1.5-8dec]` | 4.432743492676915e-05 | 4.094160077025466e-05 | 7.64% | 8.27% | 1.08x | ✅ |
| `to_wei_decimals[2str-8dec]` | 3.708168459361017e-05 | 3.423006334231034e-05 | 7.69% | 8.33% | 1.08x | ✅ |
| `to_wei_decimals[max]` | 4.3557436753402605e-05 | 3.917597850714254e-05 | 10.06% | 11.18% | 1.11x | ✅ |
| `to_wei_decimals[zero]` | 1.3903452288950964e-05 | 1.0513030647015339e-05 | 24.39% | 32.25% | 1.32x | ✅ |
