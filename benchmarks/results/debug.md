#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2388307673999975 | 0.24048782419998815 | -0.69% | -0.69% | 0.99x | ❌ |
| `pip_freeze` | 0.24067130239998277 | 0.24120799440000837 | -0.22% | -0.22% | 1.00x | ❌ |
| `platform_info` | 3.0715154633226213e-06 | 3.4656159161793156e-06 | -12.83% | -11.37% | 0.89x | ❌ |
| `python_version` | 1.1345477689119036e-06 | 1.270784442754841e-06 | -12.01% | -10.72% | 0.89x | ❌ |
