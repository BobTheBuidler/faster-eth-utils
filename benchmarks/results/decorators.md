#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2269782761516413e-05 | 2.4412823194830135e-05 | -98.97% | -49.74% | 0.50x | ❌ |
| `replace_exceptions[no-exception]` | 1.6402463340218546e-06 | 1.4974588186266258e-06 | 8.71% | 9.54% | 1.10x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.517216912247629e-06 | 1.4563806109956609e-05 | -70.99% | -41.52% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.4465980593825644e-06 | 2.292403973788985e-06 | 6.30% | 6.73% | 1.07x | ✅ |
| `return_arg_type[int-pos0]` | 2.414185051684121e-06 | 2.2372557348371492e-06 | 7.33% | 7.91% | 1.08x | ✅ |
| `return_arg_type[int-pos1]` | 2.3416565466895624e-06 | 2.1655839558065943e-06 | 7.52% | 8.13% | 1.08x | ✅ |
| `return_arg_type[str-pos0]` | 3.119880427841551e-06 | 2.8425173057749406e-06 | 8.89% | 9.76% | 1.10x | ✅ |
| `return_arg_type[str-pos1]` | 3.079842050037466e-06 | 2.8437335242529846e-06 | 7.67% | 8.30% | 1.08x | ✅ |
