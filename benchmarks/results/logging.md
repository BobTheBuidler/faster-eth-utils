#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021544143808283666 | 0.00021648858389323913 | -0.49% | -0.48% | 1.00x | ❌ |
| `get_logger` | 4.874190630313209e-05 | 4.524268422648789e-05 | 7.18% | 7.73% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.2991183116730156e-06 | 1.2136413757797514e-06 | 6.58% | 7.04% | 1.07x | ✅ |
