#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.132649677945809e-06 | 2.753882609202183e-06 | 33.36% | 50.07% | 1.50x | ✅ |
| `humanize_bytes[empty]` | 1.1640454870655247e-06 | 8.3769127598865e-07 | 28.04% | 38.96% | 1.39x | ✅ |
| `humanize_bytes[long]` | 3.963146556242839e-06 | 2.5473266044008178e-06 | 35.72% | 55.58% | 1.56x | ✅ |
| `humanize_bytes[short]` | 1.6894903672782543e-06 | 1.2100182491645398e-06 | 28.38% | 39.63% | 1.40x | ✅ |
| `humanize_hash[32-bytes]` | 4.359603545583002e-06 | 2.793254972972871e-06 | 35.93% | 56.08% | 1.56x | ✅ |
| `humanize_hash[empty]` | 1.400508575667961e-06 | 8.6853491857944e-07 | 37.98% | 61.25% | 1.61x | ✅ |
| `humanize_hash[long]` | 4.162529591439143e-06 | 2.565671462640072e-06 | 38.36% | 62.24% | 1.62x | ✅ |
| `humanize_hash[short]` | 1.7405015405093438e-06 | 1.2414056391734788e-06 | 28.68% | 40.20% | 1.40x | ✅ |
| `humanize_hexstr[empty]` | 1.947019346828349e-06 | 6.314295308266966e-07 | 67.57% | 208.35% | 3.08x | ✅ |
| `humanize_hexstr[short-0x]` | 4.729158294447778e-06 | 2.4903037542321315e-06 | 47.34% | 89.90% | 1.90x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.9941869407617235e-06 | 2.0602179964691553e-06 | 48.42% | 93.87% | 1.94x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.709590141351977e-06 | 2.5382207630104364e-06 | 46.11% | 85.55% | 1.86x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.969128892576385e-06 | 2.0487018943501133e-06 | 48.38% | 93.74% | 1.94x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.070300483889337e-05 | 2.4122915535088955e-05 | 21.43% | 27.28% | 1.27x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.7203024894237085e-05 | 2.8648949406225302e-05 | 22.99% | 29.86% | 1.30x | ✅ |
| `humanize_integer_sequence[empty]` | 8.597672515629552e-07 | 5.683348198456536e-07 | 33.90% | 51.28% | 1.51x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.6193946662586804e-05 | 3.5764890854273676e-05 | 22.58% | 29.16% | 1.29x | ✅ |
| `humanize_integer_sequence[single]` | 2.680783593554447e-05 | 1.993152546971135e-05 | 25.65% | 34.50% | 1.34x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0583729279381676e-05 | 3.199094925480021e-05 | 21.17% | 26.86% | 1.27x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.615142590340751e-05 | 6.444612276922279e-05 | 2.58% | 2.65% | 1.03x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.86737998371553e-05 | 1.5663117180167265e-05 | 16.12% | 19.22% | 1.19x | ✅ |
| `humanize_seconds[negative]` | 2.296660614123718e-05 | 1.3682031795351967e-05 | 40.43% | 67.86% | 1.68x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.668483701165822e-05 | 1.5956806537112055e-05 | 40.20% | 67.23% | 1.67x | ✅ |
| `humanize_seconds[one-hour]` | 1.7700100024357913e-05 | 1.4431558661664824e-05 | 18.47% | 22.65% | 1.23x | ✅ |
| `humanize_seconds[one-minute]` | 1.7901863189928186e-05 | 1.5133174186045825e-05 | 15.47% | 18.30% | 1.18x | ✅ |
| `humanize_seconds[one-second]` | 1.8718113088096934e-05 | 1.5811511808598e-05 | 15.53% | 18.38% | 1.18x | ✅ |
| `humanize_seconds[zero]` | 8.296219884115195e-07 | 7.052970118073447e-07 | 14.99% | 17.63% | 1.18x | ✅ |
| `humanize_wei[ether]` | 2.6944647936754744e-05 | 2.6437022930266926e-05 | 1.88% | 1.92% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.667437239968791e-05 | 2.540351120891912e-05 | 4.76% | 5.00% | 1.05x | ✅ |
| `humanize_wei[wei]` | 2.66960243944463e-05 | 2.5596197044973017e-05 | 4.12% | 4.30% | 1.04x | ✅ |
| `humanize_wei[zero]` | 4.871950686839788e-06 | 3.485155290127538e-06 | 28.46% | 39.79% | 1.40x | ✅ |
| `is_ipfs_uri[empty]` | 1.814633230935393e-05 | 1.8270471565640225e-05 | -0.68% | -0.68% | 0.99x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.2499804779062044e-05 | 3.227629011146288e-05 | 0.69% | 0.69% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.009619326337789e-05 | 3.0410819209898422e-05 | -1.05% | -1.03% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.2925768233225055e-05 | 3.255349071298204e-05 | 1.13% | 1.14% | 1.01x | ✅ |
