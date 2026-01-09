#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.223023856375351e-06 | 2.6718218003301348e-06 | 36.73% | 58.06% | 1.58x | ✅ |
| `humanize_bytes[empty]` | 1.1018487446925456e-06 | 7.946964654953119e-07 | 27.88% | 38.65% | 1.39x | ✅ |
| `humanize_bytes[long]` | 4.009327686329488e-06 | 2.444826296394698e-06 | 39.02% | 63.99% | 1.64x | ✅ |
| `humanize_bytes[short]` | 1.4781590523639362e-06 | 1.2545922000408847e-06 | 15.12% | 17.82% | 1.18x | ✅ |
| `humanize_hash[32-bytes]` | 4.462468758430447e-06 | 2.63754051611366e-06 | 40.90% | 69.19% | 1.69x | ✅ |
| `humanize_hash[empty]` | 1.3337480832152398e-06 | 8.321820346604414e-07 | 37.61% | 60.27% | 1.60x | ✅ |
| `humanize_hash[long]` | 4.274740808853843e-06 | 2.482165476687045e-06 | 41.93% | 72.22% | 1.72x | ✅ |
| `humanize_hash[short]` | 1.6870584684301841e-06 | 1.236367792368311e-06 | 26.71% | 36.45% | 1.36x | ✅ |
| `humanize_hexstr[empty]` | 1.900913727746844e-06 | 6.297587620464481e-07 | 66.87% | 201.85% | 3.02x | ✅ |
| `humanize_hexstr[short-0x]` | 4.478141032116004e-06 | 2.4380902556458295e-06 | 45.56% | 83.67% | 1.84x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.755448470448673e-06 | 2.019499295022649e-06 | 46.22% | 85.96% | 1.86x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.538555057283265e-06 | 2.500814164580262e-06 | 44.90% | 81.48% | 1.81x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.7677156324183046e-06 | 2.1216139436602033e-06 | 43.69% | 77.59% | 1.78x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0077366169911294e-05 | 2.3871559364697213e-05 | 20.63% | 26.00% | 1.26x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.678966698046963e-05 | 2.9358536381840903e-05 | 20.20% | 25.31% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 9.180895145415056e-07 | 5.903265208456185e-07 | 35.70% | 55.52% | 1.56x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.5795317863193934e-05 | 3.693084381266747e-05 | 19.36% | 24.00% | 1.24x | ✅ |
| `humanize_integer_sequence[single]` | 2.5983461855307114e-05 | 1.98790873346021e-05 | 23.49% | 30.71% | 1.31x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0484017320045694e-05 | 3.26331419596715e-05 | 19.39% | 24.06% | 1.24x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.736208269377617e-05 | 6.635458632942087e-05 | 1.50% | 1.52% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9266358573838805e-05 | 1.750315119272357e-05 | 9.15% | 10.07% | 1.10x | ✅ |
| `humanize_seconds[negative]` | 2.3868879038089947e-05 | 1.73000488219884e-05 | 27.52% | 37.97% | 1.38x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7781756966151647e-05 | 1.9586456189978766e-05 | 29.50% | 41.84% | 1.42x | ✅ |
| `humanize_seconds[one-hour]` | 1.7958194944544702e-05 | 1.6366615756439027e-05 | 8.86% | 9.72% | 1.10x | ✅ |
| `humanize_seconds[one-minute]` | 1.832979018303166e-05 | 1.703111506331229e-05 | 7.09% | 7.63% | 1.08x | ✅ |
| `humanize_seconds[one-second]` | 1.888449814845184e-05 | 1.7472560346306293e-05 | 7.48% | 8.08% | 1.08x | ✅ |
| `humanize_seconds[zero]` | 8.950273655549537e-07 | 6.664096627690874e-07 | 25.54% | 34.31% | 1.34x | ✅ |
| `humanize_wei[ether]` | 2.698856398887805e-05 | 2.6151896411335806e-05 | 3.10% | 3.20% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.678110735000881e-05 | 2.5806577879723528e-05 | 3.64% | 3.78% | 1.04x | ✅ |
| `humanize_wei[wei]` | 2.6698693409398098e-05 | 2.5375229813916727e-05 | 4.96% | 5.22% | 1.05x | ✅ |
| `humanize_wei[zero]` | 4.854893432649913e-06 | 3.441911200880147e-06 | 29.10% | 41.05% | 1.41x | ✅ |
| `is_ipfs_uri[empty]` | 1.846077359893723e-05 | 1.8639191289540003e-05 | -0.97% | -0.96% | 0.99x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.2807580164652417e-05 | 3.259217301389692e-05 | 0.66% | 0.66% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.0607302079721284e-05 | 3.0997727150326966e-05 | -1.28% | -1.26% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.346827960810219e-05 | 3.329891802151202e-05 | 0.51% | 0.51% | 1.01x | ✅ |
