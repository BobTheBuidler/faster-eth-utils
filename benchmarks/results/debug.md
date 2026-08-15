#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23208402380000734 | 0.23166106800000535 | 0.18% | 0.18% | 1.00x | ✅ |
| `pip_freeze` | 0.23146274799998992 | 0.23087538600000243 | 0.25% | 0.25% | 1.00x | ✅ |
| `platform_info` | 3.036564169908287e-06 | 3.2138877425980976e-06 | -5.84% | -5.52% | 0.94x | ❌ |
| `python_version` | 1.2978547029183414e-06 | 1.4708749305746393e-06 | -13.33% | -11.76% | 0.88x | ❌ |
