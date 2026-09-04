#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 3.659067729248798e-06 | 2.3473861985333613e-06 | 35.85% | 55.88% | 1.56x | ✅ |
| `humanize_bytes[empty]` | 8.92566983021454e-07 | 7.599793146448254e-07 | 14.85% | 17.45% | 1.17x | ✅ |
| `humanize_bytes[long]` | 3.4878293950093033e-06 | 2.196312789418718e-06 | 37.03% | 58.80% | 1.59x | ✅ |
| `humanize_bytes[short]` | 1.3627293841744148e-06 | 9.61808109310855e-07 | 29.42% | 41.68% | 1.42x | ✅ |
| `humanize_hash[32-bytes]` | 3.87167107641026e-06 | 2.3506863402603015e-06 | 39.28% | 64.70% | 1.65x | ✅ |
| `humanize_hash[empty]` | 1.1063944762399574e-06 | 7.727554686997482e-07 | 30.16% | 43.18% | 1.43x | ✅ |
| `humanize_hash[long]` | 3.7213212220497183e-06 | 2.211256022749231e-06 | 40.58% | 68.29% | 1.68x | ✅ |
| `humanize_hash[short]` | 1.5545666193706676e-06 | 9.755954122599556e-07 | 37.24% | 59.35% | 1.59x | ✅ |
| `humanize_hexstr[empty]` | 1.6295507973041525e-06 | 6.080900470988314e-07 | 62.68% | 167.98% | 2.68x | ✅ |
| `humanize_hexstr[short-0x]` | 4.1207550594953425e-06 | 2.2358872384294213e-06 | 45.74% | 84.30% | 1.84x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.437831983382687e-06 | 1.8942024142118432e-06 | 44.90% | 81.49% | 1.81x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.1681848947958135e-06 | 2.270344170553504e-06 | 45.53% | 83.59% | 1.84x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.443331298085265e-06 | 1.8401817026639687e-06 | 46.56% | 87.12% | 1.87x | ✅ |
| `humanize_integer_sequence[consecutive]` | 2.5335646657055286e-05 | 2.088673878363706e-05 | 17.56% | 21.30% | 1.21x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.074777530227983e-05 | 2.568028819144581e-05 | 16.48% | 19.73% | 1.20x | ✅ |
| `humanize_integer_sequence[empty]` | 6.842998189285845e-07 | 5.097540773232939e-07 | 25.51% | 34.24% | 1.34x | ✅ |
| `humanize_integer_sequence[mixed]` | 3.81057547263624e-05 | 3.371419995291252e-05 | 11.52% | 13.03% | 1.13x | ✅ |
| `humanize_integer_sequence[single]` | 2.2237359359590527e-05 | 1.7469554114201343e-05 | 21.44% | 27.29% | 1.27x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.371445434469473e-05 | 2.9308642860178306e-05 | 13.07% | 15.03% | 1.15x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 5.7101452114819643e-05 | 5.5014647283934424e-05 | 3.65% | 3.79% | 1.04x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.539972499343415e-05 | 1.4716917401246664e-05 | 4.43% | 4.64% | 1.05x | ✅ |
| `humanize_seconds[negative]` | 1.9296726812238537e-05 | 1.2233763353295904e-05 | 36.60% | 57.73% | 1.58x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.3490033130650364e-05 | 1.46719884248389e-05 | 37.54% | 60.10% | 1.60x | ✅ |
| `humanize_seconds[one-hour]` | 1.4916501727764846e-05 | 1.351368912986168e-05 | 9.40% | 10.38% | 1.10x | ✅ |
| `humanize_seconds[one-minute]` | 1.502862973158376e-05 | 1.413854394662225e-05 | 5.92% | 6.30% | 1.06x | ✅ |
| `humanize_seconds[one-second]` | 1.54131666241151e-05 | 1.466946367147596e-05 | 4.83% | 5.07% | 1.05x | ✅ |
| `humanize_seconds[zero]` | 6.575355684174601e-07 | 7.100494752893882e-07 | -7.99% | -7.40% | 0.93x | ❌ |
| `humanize_wei[ether]` | 2.3770598695023896e-05 | 2.246767409940416e-05 | 5.48% | 5.80% | 1.06x | ✅ |
| `humanize_wei[gwei]` | 2.3500308171045837e-05 | 2.2271033765743406e-05 | 5.23% | 5.52% | 1.06x | ✅ |
| `humanize_wei[wei]` | 2.300454170874582e-05 | 2.1654676409727247e-05 | 5.87% | 6.23% | 1.06x | ✅ |
| `humanize_wei[zero]` | 4.030494879542721e-06 | 2.7611979626746045e-06 | 31.49% | 45.97% | 1.46x | ✅ |
| `is_ipfs_uri[empty]` | 1.4615200559483133e-05 | 1.4693379886650038e-05 | -0.53% | -0.53% | 0.99x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 2.738880651749504e-05 | 2.718716198022602e-05 | 0.74% | 0.74% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 2.5393362894089513e-05 | 2.5362940473664677e-05 | 0.12% | 0.12% | 1.00x | ✅ |
| `is_ipfs_uri[valid-cidv0]` | 2.7880544417855717e-05 | 2.7722135883717418e-05 | 0.57% | 0.57% | 1.01x | ✅ |
