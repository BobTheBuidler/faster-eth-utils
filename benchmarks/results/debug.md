#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2533640942000034 | 0.2519549186000177 | 0.56% | 0.56% | 1.01x | ✅ |
| `pip_freeze` | 0.24611282540000728 | 0.2539163462000033 | -3.17% | -3.07% | 0.97x | ❌ |
| `platform_info` | 3.0148211378808857e-06 | 3.2073164870841777e-06 | -6.38% | -6.00% | 0.94x | ❌ |
| `python_version` | 1.2378862995479545e-06 | 1.3205084110680354e-06 | -6.67% | -6.26% | 0.94x | ❌ |
