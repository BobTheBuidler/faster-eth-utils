#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23830231439999353 | 0.23801095880000958 | 0.12% | 0.12% | 1.00x | ✅ |
| `pip_freeze` | 0.23589354300000878 | 0.23569468279998773 | 0.08% | 0.08% | 1.00x | ✅ |
| `platform_info` | 3.101339050581589e-06 | 3.434649246325935e-06 | -10.75% | -9.70% | 0.90x | ❌ |
| `python_version` | 1.183809062007689e-06 | 1.1555322359370443e-06 | 2.39% | 2.45% | 1.02x | ✅ |
