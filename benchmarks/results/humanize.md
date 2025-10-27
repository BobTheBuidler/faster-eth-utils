#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.220673620887578e-06 | 2.777614071953265e-06 | 34.19% | 51.95% | 1.52x | ✅ |
| `humanize_bytes[empty]` | 1.2638651925532758e-06 | 9.496516295055657e-07 | 24.86% | 33.09% | 1.33x | ✅ |
| `humanize_bytes[long]` | 4.005668493189921e-06 | 2.58790511947038e-06 | 35.39% | 54.78% | 1.55x | ✅ |
| `humanize_bytes[short]` | 1.4831683096926955e-06 | 1.160104427962376e-06 | 21.78% | 27.85% | 1.28x | ✅ |
| `humanize_hash[32-bytes]` | 4.5016429073531155e-06 | 2.8435175029248153e-06 | 36.83% | 58.31% | 1.58x | ✅ |
| `humanize_hash[empty]` | 1.4225151797731749e-06 | 8.646894131175838e-07 | 39.21% | 64.51% | 1.65x | ✅ |
| `humanize_hash[long]` | 4.3198458995198905e-06 | 2.6439882675859506e-06 | 38.79% | 63.38% | 1.63x | ✅ |
| `humanize_hash[short]` | 1.7040198625836656e-06 | 1.2842855093335832e-06 | 24.63% | 32.68% | 1.33x | ✅ |
| `humanize_hexstr[empty]` | 1.9183311052398386e-06 | 6.834401239604987e-07 | 64.37% | 180.69% | 2.81x | ✅ |
| `humanize_hexstr[short-0x]` | 4.770423162063323e-06 | 2.4895822696323865e-06 | 47.81% | 91.62% | 1.92x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.964534334234552e-06 | 2.0148796314515e-06 | 49.18% | 96.76% | 1.97x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.7659114382157805e-06 | 2.5435600018319826e-06 | 46.63% | 87.37% | 1.87x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.983279446310367e-06 | 2.0175342779931663e-06 | 49.35% | 97.43% | 1.97x | ✅ |
| `humanize_integer_sequence[consecutive]` | 2.999093786508239e-05 | 2.371837844039015e-05 | 20.91% | 26.45% | 1.26x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.59243296421502e-05 | 2.8686892692427624e-05 | 20.15% | 25.23% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 9.396755998845486e-07 | 6.177181779789534e-07 | 34.26% | 52.12% | 1.52x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.353333645741781e-05 | 3.6161456492704695e-05 | 16.93% | 20.39% | 1.20x | ✅ |
| `humanize_integer_sequence[single]` | 2.593018571020986e-05 | 1.9840312243575227e-05 | 23.49% | 30.69% | 1.31x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.896903303918355e-05 | 3.206735039775345e-05 | 17.71% | 21.52% | 1.22x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.819831406650892e-05 | 6.73655519723416e-05 | 1.22% | 1.24% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8647523320580768e-05 | 1.702828269763072e-05 | 8.68% | 9.51% | 1.10x | ✅ |
| `humanize_seconds[negative]` | 2.3693927456261108e-05 | 1.6908900463100366e-05 | 28.64% | 40.13% | 1.40x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.708314981175809e-05 | 1.8954243724799794e-05 | 30.01% | 42.89% | 1.43x | ✅ |
| `humanize_seconds[one-hour]` | 1.7465903267719833e-05 | 1.5753058594984394e-05 | 9.81% | 10.87% | 1.11x | ✅ |
| `humanize_seconds[one-minute]` | 1.7730134530686773e-05 | 1.6539713695699475e-05 | 6.71% | 7.20% | 1.07x | ✅ |
| `humanize_seconds[one-second]` | 1.8570428888973524e-05 | 1.690879196790009e-05 | 8.95% | 9.83% | 1.10x | ✅ |
| `humanize_seconds[zero]` | 8.94493611070487e-07 | 6.536545521673511e-07 | 26.92% | 36.85% | 1.37x | ✅ |
| `humanize_wei[ether]` | 2.7277041831080205e-05 | 2.6791053605841708e-05 | 1.78% | 1.81% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.6922027430096396e-05 | 2.6434576337521484e-05 | 1.81% | 1.84% | 1.02x | ✅ |
| `humanize_wei[wei]` | 2.6741241185992212e-05 | 2.5946771641093845e-05 | 2.97% | 3.06% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.910537232173445e-06 | 4.239153814799466e-06 | 13.67% | 15.84% | 1.16x | ✅ |
| `is_ipfs_uri[empty]` | 1.8059429895654344e-05 | 1.857699775857684e-05 | -2.87% | -2.79% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.3079056397218567e-05 | 3.309767768121713e-05 | -0.06% | -0.06% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.111274998874781e-05 | 3.131417997200278e-05 | -0.65% | -0.64% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.402252569545725e-05 | 3.366769963425958e-05 | 1.04% | 1.05% | 1.01x | ✅ |
