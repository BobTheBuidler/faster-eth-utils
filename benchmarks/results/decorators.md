#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1903415579918596e-05 | 2.3877666843725765e-05 | -100.60% | -50.15% | 0.50x | ❌ |
| `replace_exceptions[no-exception]` | 1.4942538060357998e-06 | 1.4046346554559395e-06 | 6.00% | 6.38% | 1.06x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.487397410065609e-06 | 1.4570176170142347e-05 | -71.67% | -41.75% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.4003560380161808e-06 | 2.100484868113936e-06 | 12.49% | 14.28% | 1.14x | ✅ |
| `return_arg_type[int-pos0]` | 2.352738381115234e-06 | 2.0740212739588912e-06 | 11.85% | 13.44% | 1.13x | ✅ |
| `return_arg_type[int-pos1]` | 2.3009136387469746e-06 | 2.0529111056651727e-06 | 10.78% | 12.08% | 1.12x | ✅ |
| `return_arg_type[str-pos0]` | 2.9496322735997592e-06 | 2.8467120528038676e-06 | 3.49% | 3.62% | 1.04x | ✅ |
| `return_arg_type[str-pos1]` | 2.885768359327614e-06 | 2.782948279938286e-06 | 3.56% | 3.69% | 1.04x | ✅ |
