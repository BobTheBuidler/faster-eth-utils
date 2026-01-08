#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.192012941124257e-06 | 2.8129127576025638e-06 | 32.90% | 49.03% | 1.49x | ✅ |
| `humanize_bytes[empty]` | 1.116480293787355e-06 | 8.161470092355073e-07 | 26.90% | 36.80% | 1.37x | ✅ |
| `humanize_bytes[long]` | 4.019694266468282e-06 | 2.6312735034179585e-06 | 34.54% | 52.77% | 1.53x | ✅ |
| `humanize_bytes[short]` | 1.4789147741304267e-06 | 1.153001302985566e-06 | 22.04% | 28.27% | 1.28x | ✅ |
| `humanize_hash[32-bytes]` | 4.479393466276848e-06 | 2.8123406482684284e-06 | 37.22% | 59.28% | 1.59x | ✅ |
| `humanize_hash[empty]` | 1.3586563475077627e-06 | 8.395424378498127e-07 | 38.21% | 61.83% | 1.62x | ✅ |
| `humanize_hash[long]` | 4.266237655994074e-06 | 2.6580064648577076e-06 | 37.70% | 60.51% | 1.61x | ✅ |
| `humanize_hash[short]` | 1.6904169276557645e-06 | 1.1491442592768505e-06 | 32.02% | 47.10% | 1.47x | ✅ |
| `humanize_hexstr[empty]` | 1.8668589088368305e-06 | 6.32328661318207e-07 | 66.13% | 195.24% | 2.95x | ✅ |
| `humanize_hexstr[short-0x]` | 4.5483194962127015e-06 | 2.4873399403788164e-06 | 45.31% | 82.86% | 1.83x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.805047036430484e-06 | 2.042132176865362e-06 | 46.33% | 86.33% | 1.86x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.5733707771530075e-06 | 2.6012673028965286e-06 | 43.12% | 75.81% | 1.76x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.792532726457032e-06 | 1.9780955780452477e-06 | 47.84% | 91.73% | 1.92x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.063249417441887e-05 | 2.3813141754158298e-05 | 22.26% | 28.64% | 1.29x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.7510196141571286e-05 | 2.9589658914889377e-05 | 21.12% | 26.77% | 1.27x | ✅ |
| `humanize_integer_sequence[empty]` | 9.090945494748063e-07 | 6.010369711047236e-07 | 33.89% | 51.25% | 1.51x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.6154281130038295e-05 | 3.7410776806993787e-05 | 18.94% | 23.37% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.6492221133388842e-05 | 1.989926307360227e-05 | 24.89% | 33.13% | 1.33x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.1017020363650135e-05 | 3.311374322199993e-05 | 19.27% | 23.87% | 1.24x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.845098870595944e-05 | 6.723553225151692e-05 | 1.78% | 1.81% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9157041666630446e-05 | 1.7876654356953818e-05 | 6.68% | 7.16% | 1.07x | ✅ |
| `humanize_seconds[negative]` | 2.3771382983483008e-05 | 1.781662206419573e-05 | 25.05% | 33.42% | 1.33x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7772727593903232e-05 | 1.986455197804526e-05 | 28.47% | 39.81% | 1.40x | ✅ |
| `humanize_seconds[one-hour]` | 1.8129205150599195e-05 | 1.655266981263649e-05 | 8.70% | 9.52% | 1.10x | ✅ |
| `humanize_seconds[one-minute]` | 1.827282126206396e-05 | 1.7411993730134323e-05 | 4.71% | 4.94% | 1.05x | ✅ |
| `humanize_seconds[one-second]` | 1.908826588299783e-05 | 1.7823867556782878e-05 | 6.62% | 7.09% | 1.07x | ✅ |
| `humanize_seconds[zero]` | 8.958333450810117e-07 | 6.786408394100743e-07 | 24.24% | 32.00% | 1.32x | ✅ |
| `humanize_wei[ether]` | 2.7183386837720436e-05 | 2.7570181306166415e-05 | -1.42% | -1.40% | 0.99x | ❌ |
| `humanize_wei[gwei]` | 2.722424296992293e-05 | 2.7172938915345903e-05 | 0.19% | 0.19% | 1.00x | ✅ |
| `humanize_wei[wei]` | 2.685331761611388e-05 | 2.6597553757685014e-05 | 0.95% | 0.96% | 1.01x | ✅ |
| `humanize_wei[zero]` | 4.7917670266479735e-06 | 4.004957198253685e-06 | 16.42% | 19.65% | 1.20x | ✅ |
| `is_ipfs_uri[empty]` | 1.839889885757616e-05 | 1.8728695055853233e-05 | -1.79% | -1.76% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.3205552503354263e-05 | 3.325301550788331e-05 | -0.14% | -0.14% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.105015656702884e-05 | 3.173277212194916e-05 | -2.20% | -2.15% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.396377824132338e-05 | 3.375145807706146e-05 | 0.63% | 0.63% | 1.01x | ✅ |
