#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1621874228682728e-05 | 2.4492560834877432e-05 | -110.75% | -52.55% | 0.47x | ❌ |
| `replace_exceptions[no-exception]` | 1.5070094938671745e-06 | 1.5449972387725342e-06 | -2.52% | -2.46% | 0.98x | ❌ |
| `replace_exceptions[unmapped-exception]` | 8.326286872082038e-06 | 1.4885913323253317e-05 | -78.78% | -44.07% | 0.56x | ❌ |
| `return_arg_type[float-pos0]` | 2.41400305920613e-06 | 2.2320515433403805e-06 | 7.54% | 8.15% | 1.08x | ✅ |
| `return_arg_type[int-pos0]` | 2.3276550527913572e-06 | 2.129957813312803e-06 | 8.49% | 9.28% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 2.2670971575069103e-06 | 2.0853280488055964e-06 | 8.02% | 8.72% | 1.09x | ✅ |
| `return_arg_type[str-pos0]` | 2.9232704016278197e-06 | 2.998090515463304e-06 | -2.56% | -2.50% | 0.98x | ❌ |
| `return_arg_type[str-pos1]` | 2.92134143071716e-06 | 2.9561584394522845e-06 | -1.19% | -1.18% | 0.99x | ❌ |
