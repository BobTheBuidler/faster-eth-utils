#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021363533524116558 | 0.00021418532875569835 | -0.26% | -0.26% | 1.00x | ❌ |
| `get_logger` | 4.7550242592062314e-05 | 4.415664251295257e-05 | 7.14% | 7.69% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.361972407834833e-06 | 1.2143449452185835e-06 | 10.84% | 12.16% | 1.12x | ✅ |
