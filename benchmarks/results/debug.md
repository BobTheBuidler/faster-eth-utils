#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.22612190919999192 | 0.22568425480000087 | 0.19% | 0.19% | 1.00x | ✅ |
| `pip_freeze` | 0.2147026817999972 | 0.21705943319999504 | -1.10% | -1.09% | 0.99x | ❌ |
| `platform_info` | 3.0416410542211826e-06 | 3.5846461542083022e-06 | -17.85% | -15.15% | 0.85x | ❌ |
| `python_version` | 1.098879552052442e-06 | 1.204965354239017e-06 | -9.65% | -8.80% | 0.91x | ❌ |
