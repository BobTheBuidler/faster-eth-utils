#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.193034542131889e-06 | 2.5975092228887357e-06 | 38.05% | 61.43% | 1.61x | ✅ |
| `humanize_bytes[empty]` | 1.1068086757994451e-06 | 7.956780424329599e-07 | 28.11% | 39.10% | 1.39x | ✅ |
| `humanize_bytes[long]` | 3.972082334542752e-06 | 2.4086003880890514e-06 | 39.36% | 64.91% | 1.65x | ✅ |
| `humanize_bytes[short]` | 1.492937749448714e-06 | 1.0970216721056956e-06 | 26.52% | 36.09% | 1.36x | ✅ |
| `humanize_hash[32-bytes]` | 4.451524548260551e-06 | 2.6379384793839225e-06 | 40.74% | 68.75% | 1.69x | ✅ |
| `humanize_hash[empty]` | 1.3622413493156083e-06 | 8.158791751111582e-07 | 40.11% | 66.97% | 1.67x | ✅ |
| `humanize_hash[long]` | 4.27923791353114e-06 | 2.4443868005552913e-06 | 42.88% | 75.06% | 1.75x | ✅ |
| `humanize_hash[short]` | 1.6944681410389087e-06 | 1.2199136063956832e-06 | 28.01% | 38.90% | 1.39x | ✅ |
| `humanize_hexstr[empty]` | 1.8720194654965451e-06 | 6.379854248334497e-07 | 65.92% | 193.43% | 2.93x | ✅ |
| `humanize_hexstr[short-0x]` | 4.53308992863306e-06 | 2.3809532586722856e-06 | 47.48% | 90.39% | 1.90x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.766347257589027e-06 | 1.995977880213281e-06 | 47.00% | 88.70% | 1.89x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.577054428131851e-06 | 2.45397137789771e-06 | 46.39% | 86.52% | 1.87x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.7504658525311423e-06 | 1.9997740165151177e-06 | 46.68% | 87.54% | 1.88x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0140801210049874e-05 | 2.4489285312055657e-05 | 18.75% | 23.08% | 1.23x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.6579275356792194e-05 | 2.9744490781920565e-05 | 18.68% | 22.98% | 1.23x | ✅ |
| `humanize_integer_sequence[empty]` | 8.953717853511133e-07 | 5.626881254148948e-07 | 37.16% | 59.12% | 1.59x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.564895783974075e-05 | 3.713552163964061e-05 | 18.65% | 22.93% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.676121364631456e-05 | 2.0146154262610444e-05 | 24.72% | 32.84% | 1.33x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0779376238071924e-05 | 3.278003240056798e-05 | 19.62% | 24.40% | 1.24x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.750497199835769e-05 | 6.642960014334672e-05 | 1.59% | 1.62% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8997411595008847e-05 | 1.7977074494676545e-05 | 5.37% | 5.68% | 1.06x | ✅ |
| `humanize_seconds[negative]` | 2.3725702259864668e-05 | 1.7477687275370518e-05 | 26.33% | 35.75% | 1.36x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.759717684078419e-05 | 1.979882529343041e-05 | 28.26% | 39.39% | 1.39x | ✅ |
| `humanize_seconds[one-hour]` | 1.8100040369095212e-05 | 1.685324947112151e-05 | 6.89% | 7.40% | 1.07x | ✅ |
| `humanize_seconds[one-minute]` | 1.831578905417508e-05 | 1.7455643725521555e-05 | 4.70% | 4.93% | 1.05x | ✅ |
| `humanize_seconds[one-second]` | 1.9054295131799368e-05 | 1.807605072560896e-05 | 5.13% | 5.41% | 1.05x | ✅ |
| `humanize_seconds[zero]` | 8.898907188509637e-07 | 6.626014317181986e-07 | 25.54% | 34.30% | 1.34x | ✅ |
| `humanize_wei[ether]` | 2.741862939732454e-05 | 2.675977593607338e-05 | 2.40% | 2.46% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.6855031841947403e-05 | 2.6490940018702034e-05 | 1.36% | 1.37% | 1.01x | ✅ |
| `humanize_wei[wei]` | 2.6702810179344026e-05 | 2.5910856371150192e-05 | 2.97% | 3.06% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.779371074692211e-06 | 4.022909531718564e-06 | 15.83% | 18.80% | 1.19x | ✅ |
| `is_ipfs_uri[empty]` | 1.824761640649362e-05 | 1.8761415574722006e-05 | -2.82% | -2.74% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.268630500117999e-05 | 3.292761332821714e-05 | -0.74% | -0.73% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.0656456533201006e-05 | 3.1187199242081504e-05 | -1.73% | -1.70% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.318680735966059e-05 | 3.335673455989712e-05 | -0.51% | -0.51% | 0.99x | ❌ |
