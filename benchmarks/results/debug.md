#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.24753246719999425 | 0.24851722120000658 | -0.40% | -0.40% | 1.00x | ❌ |
| `pip_freeze` | 0.2606838319999952 | 0.25222119759998807 | 3.25% | 3.36% | 1.03x | ✅ |
| `platform_info` | 2.9423993985708783e-06 | 3.33717904609297e-06 | -13.42% | -11.83% | 0.88x | ❌ |
| `python_version` | 1.1580915170632988e-06 | 1.3768003550373592e-06 | -18.89% | -15.89% | 0.84x | ❌ |
