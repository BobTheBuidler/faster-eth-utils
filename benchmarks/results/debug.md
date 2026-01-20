#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2295842832000062 | 0.22952930259999677 | 0.02% | 0.02% | 1.00x | ✅ |
| `pip_freeze` | 0.22824101460000748 | 0.23177631960002146 | -1.55% | -1.53% | 0.98x | ❌ |
| `platform_info` | 3.0953734165139603e-06 | 3.720441495807618e-06 | -20.19% | -16.80% | 0.83x | ❌ |
| `python_version` | 1.2365800641912016e-06 | 1.3770196753154306e-06 | -11.36% | -10.20% | 0.90x | ❌ |
