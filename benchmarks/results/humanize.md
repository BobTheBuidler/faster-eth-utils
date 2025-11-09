#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.22151081536122e-06 | 2.6311458730148463e-06 | 37.67% | 60.44% | 1.60x | ✅ |
| `humanize_bytes[empty]` | 1.1912818080767977e-06 | 8.694688666601559e-07 | 27.01% | 37.01% | 1.37x | ✅ |
| `humanize_bytes[long]` | 4.0040898310032284e-06 | 2.4193819373146796e-06 | 39.58% | 65.50% | 1.66x | ✅ |
| `humanize_bytes[short]` | 1.5036592153936483e-06 | 1.0938188307420376e-06 | 27.26% | 37.47% | 1.37x | ✅ |
| `humanize_hash[32-bytes]` | 4.453383954174716e-06 | 2.6901319999905373e-06 | 39.59% | 65.55% | 1.66x | ✅ |
| `humanize_hash[empty]` | 1.4059218452263525e-06 | 8.796319918683909e-07 | 37.43% | 59.83% | 1.60x | ✅ |
| `humanize_hash[long]` | 4.2584350796610606e-06 | 2.4862918010967443e-06 | 41.61% | 71.28% | 1.71x | ✅ |
| `humanize_hash[short]` | 1.68437831278248e-06 | 1.1955592047314107e-06 | 29.02% | 40.89% | 1.41x | ✅ |
| `humanize_hexstr[empty]` | 1.8666895828027684e-06 | 7.661247404713209e-07 | 58.96% | 143.65% | 2.44x | ✅ |
| `humanize_hexstr[short-0x]` | 4.727199587365365e-06 | 2.4450830343232733e-06 | 48.28% | 93.33% | 1.93x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.03785584689468e-06 | 2.0270873314678505e-06 | 49.80% | 99.19% | 1.99x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.741294811869218e-06 | 2.447910042392949e-06 | 48.37% | 93.69% | 1.94x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.131734196703246e-06 | 1.9877045380112594e-06 | 51.89% | 107.86% | 2.08x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0580813319131805e-05 | 2.3608593466972093e-05 | 22.80% | 29.53% | 1.30x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.652277326925088e-05 | 2.8722338669890347e-05 | 21.36% | 27.16% | 1.27x | ✅ |
| `humanize_integer_sequence[empty]` | 9.450398198229233e-07 | 6.170080691263312e-07 | 34.71% | 53.16% | 1.53x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.460532122633127e-05 | 3.580418659540351e-05 | 19.73% | 24.58% | 1.25x | ✅ |
| `humanize_integer_sequence[single]` | 2.6840709831734634e-05 | 1.972306238563826e-05 | 26.52% | 36.09% | 1.36x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.982479224141494e-05 | 3.186816638541155e-05 | 19.98% | 24.97% | 1.25x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.874360946539474e-05 | 6.665225798428624e-05 | 3.04% | 3.14% | 1.03x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.886892741956824e-05 | 1.69657594112741e-05 | 10.09% | 11.22% | 1.11x | ✅ |
| `humanize_seconds[negative]` | 2.4183924702762938e-05 | 1.704330578204101e-05 | 29.53% | 41.90% | 1.42x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7972311603755893e-05 | 1.9109087740386526e-05 | 31.69% | 46.38% | 1.46x | ✅ |
| `humanize_seconds[one-hour]` | 1.777359801278901e-05 | 1.5651137016542118e-05 | 11.94% | 13.56% | 1.14x | ✅ |
| `humanize_seconds[one-minute]` | 1.8220490903219227e-05 | 1.630345010916358e-05 | 10.52% | 11.76% | 1.12x | ✅ |
| `humanize_seconds[one-second]` | 1.8888639641124307e-05 | 1.7023158527685394e-05 | 9.88% | 10.96% | 1.11x | ✅ |
| `humanize_seconds[zero]` | 8.91033214696517e-07 | 6.768814121039877e-07 | 24.03% | 31.64% | 1.32x | ✅ |
| `humanize_wei[ether]` | 2.7535792513987558e-05 | 2.7017894133380382e-05 | 1.88% | 1.92% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.7282434496780048e-05 | 2.6646987138831687e-05 | 2.33% | 2.38% | 1.02x | ✅ |
| `humanize_wei[wei]` | 2.706275185663535e-05 | 2.630383329172718e-05 | 2.80% | 2.89% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.846444963012905e-06 | 4.2390844669692945e-06 | 12.53% | 14.33% | 1.14x | ✅ |
| `is_ipfs_uri[empty]` | 1.8071566087525875e-05 | 1.8643346709962573e-05 | -3.16% | -3.07% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.235639832986379e-05 | 3.256125637309596e-05 | -0.63% | -0.63% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.0182945412014947e-05 | 3.07581438975599e-05 | -1.91% | -1.87% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.359342119006627e-05 | 3.313058341474569e-05 | 1.38% | 1.40% | 1.01x | ✅ |
