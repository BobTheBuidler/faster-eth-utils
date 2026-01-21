#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2389584609999929 | 0.23928332980000278 | -0.14% | -0.14% | 1.00x | ❌ |
| `pip_freeze` | 0.2414297458000192 | 0.24517360440000857 | -1.55% | -1.53% | 0.98x | ❌ |
| `platform_info` | 3.059237008981744e-06 | 3.932762872837743e-06 | -28.55% | -22.21% | 0.78x | ❌ |
| `python_version` | 1.249314800884367e-06 | 1.399335755267069e-06 | -12.01% | -10.72% | 0.89x | ❌ |
