#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.181283313093829e-06 | 2.4920674155703423e-06 | 40.40% | 67.78% | 1.68x | ✅ |
| `humanize_bytes[empty]` | 1.137544415318711e-06 | 8.756787370097889e-07 | 23.02% | 29.90% | 1.30x | ✅ |
| `humanize_bytes[long]` | 3.955356744692123e-06 | 2.315602871714048e-06 | 41.46% | 70.81% | 1.71x | ✅ |
| `humanize_bytes[short]` | 1.4609327046546126e-06 | 1.1923971722949004e-06 | 18.38% | 22.52% | 1.23x | ✅ |
| `humanize_hash[32-bytes]` | 4.33983430197938e-06 | 2.4981645885101094e-06 | 42.44% | 73.72% | 1.74x | ✅ |
| `humanize_hash[empty]` | 1.396364653907354e-06 | 8.635714505118194e-07 | 38.16% | 61.70% | 1.62x | ✅ |
| `humanize_hash[long]` | 4.205830697237985e-06 | 2.271747563104302e-06 | 45.99% | 85.14% | 1.85x | ✅ |
| `humanize_hash[short]` | 1.6869581025736625e-06 | 1.1457503328145953e-06 | 32.08% | 47.24% | 1.47x | ✅ |
| `humanize_hexstr[empty]` | 2.0147539732892266e-06 | 6.600848273646291e-07 | 67.24% | 205.23% | 3.05x | ✅ |
| `humanize_hexstr[short-0x]` | 4.78419298358151e-06 | 2.24260107764165e-06 | 53.12% | 113.33% | 2.13x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.988243767300225e-06 | 1.8601444438106e-06 | 53.36% | 114.41% | 2.14x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.879578065545654e-06 | 2.2545205528133445e-06 | 53.80% | 116.44% | 2.16x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.988762001562038e-06 | 1.834215752815382e-06 | 54.02% | 117.46% | 2.17x | ✅ |
| `humanize_integer_sequence[consecutive]` | 2.9774687062563974e-05 | 2.4430927515349838e-05 | 17.95% | 21.87% | 1.22x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.614353704880808e-05 | 2.911198812145777e-05 | 19.45% | 24.15% | 1.24x | ✅ |
| `humanize_integer_sequence[empty]` | 8.382530076041485e-07 | 6.17755455963885e-07 | 26.30% | 35.69% | 1.36x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.422365207253597e-05 | 3.6299086016697745e-05 | 17.92% | 21.83% | 1.22x | ✅ |
| `humanize_integer_sequence[single]` | 2.6755041902372347e-05 | 2.0399785796486276e-05 | 23.75% | 31.15% | 1.31x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.915649088884466e-05 | 3.25105928136996e-05 | 16.97% | 20.44% | 1.20x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 3.5247683113257925e-05 | 3.2495727533204626e-05 | 7.81% | 8.47% | 1.08x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 2.0517340758196478e-05 | 1.8599448429449236e-05 | 9.35% | 10.31% | 1.10x | ✅ |
| `humanize_seconds[negative]` | 2.7540051807427127e-05 | 1.7898166450019716e-05 | 35.01% | 53.87% | 1.54x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 3.2565435752394824e-05 | 1.9972469392999927e-05 | 38.67% | 63.05% | 1.63x | ✅ |
| `humanize_seconds[one-hour]` | 1.9958432278244736e-05 | 1.8271657717361926e-05 | 8.45% | 9.23% | 1.09x | ✅ |
| `humanize_seconds[one-minute]` | 1.9802432038827505e-05 | 1.787237588732869e-05 | 9.75% | 10.80% | 1.11x | ✅ |
| `humanize_seconds[one-second]` | 2.0553796671138762e-05 | 1.8548537597664836e-05 | 9.76% | 10.81% | 1.11x | ✅ |
| `humanize_seconds[zero]` | 1.2700675715271723e-06 | 1.0979136341954095e-06 | 13.55% | 15.68% | 1.16x | ✅ |
| `humanize_wei[ether]` | 2.6782099935196134e-05 | 2.5461472388782915e-05 | 4.93% | 5.19% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.647009333558937e-05 | 2.4739963800012775e-05 | 6.54% | 6.99% | 1.07x | ✅ |
| `humanize_wei[wei]` | 2.618868208074089e-05 | 2.4169863381202972e-05 | 7.71% | 8.35% | 1.08x | ✅ |
| `humanize_wei[zero]` | 4.714956928929039e-06 | 3.786259884114341e-06 | 19.70% | 24.53% | 1.25x | ✅ |
| `is_ipfs_uri[empty]` | 1.3840620216738573e-05 | 1.4064734738696892e-05 | -1.62% | -1.59% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 1.7130908005237622e-05 | 1.626813163436755e-05 | 5.04% | 5.30% | 1.05x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 1.4474734289587582e-05 | 1.4664012404867156e-05 | -1.31% | -1.29% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 1.75701721393243e-05 | 1.634739668678151e-05 | 6.96% | 7.48% | 1.07x | ✅ |
