#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.3867375594273225e-06 | 2.654907159774704e-06 | 39.48% | 65.23% | 1.65x | ✅ |
| `humanize_bytes[empty]` | 1.233340432941595e-06 | 8.399473819698865e-07 | 31.90% | 46.84% | 1.47x | ✅ |
| `humanize_bytes[long]` | 4.1653312887835975e-06 | 2.464700178533208e-06 | 40.83% | 69.00% | 1.69x | ✅ |
| `humanize_bytes[short]` | 1.620879590614267e-06 | 1.0682488293985836e-06 | 34.09% | 51.73% | 1.52x | ✅ |
| `humanize_hash[32-bytes]` | 4.597931453368325e-06 | 2.669973064968608e-06 | 41.93% | 72.21% | 1.72x | ✅ |
| `humanize_hash[empty]` | 1.3907630598629172e-06 | 8.542357447555237e-07 | 38.58% | 62.81% | 1.63x | ✅ |
| `humanize_hash[long]` | 4.416074475699949e-06 | 2.478600132928379e-06 | 43.87% | 78.17% | 1.78x | ✅ |
| `humanize_hash[short]` | 1.81670706235316e-06 | 1.197479580271516e-06 | 34.09% | 51.71% | 1.52x | ✅ |
| `humanize_hexstr[empty]` | 1.9373148126149375e-06 | 6.642854991569808e-07 | 65.71% | 191.64% | 2.92x | ✅ |
| `humanize_hexstr[short-0x]` | 4.805678699280391e-06 | 2.4186359833532244e-06 | 49.67% | 98.69% | 1.99x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.0425975310290165e-06 | 2.0814642943916996e-06 | 48.51% | 94.22% | 1.94x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.8815587237068535e-06 | 2.4036584110382837e-06 | 50.76% | 103.09% | 2.03x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.070956772070472e-06 | 1.9824141072248202e-06 | 51.30% | 105.35% | 2.05x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.1105214522954394e-05 | 2.513942099801114e-05 | 19.18% | 23.73% | 1.24x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.768815230532649e-05 | 3.05246327196763e-05 | 19.01% | 23.47% | 1.23x | ✅ |
| `humanize_integer_sequence[empty]` | 8.664159808947256e-07 | 5.692686244911739e-07 | 34.30% | 52.20% | 1.52x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.6779025730778484e-05 | 3.784935939334479e-05 | 19.09% | 23.59% | 1.24x | ✅ |
| `humanize_integer_sequence[single]` | 2.7286324948360123e-05 | 2.123104472953908e-05 | 22.19% | 28.52% | 1.29x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.152674059498424e-05 | 3.415859116962321e-05 | 17.74% | 21.57% | 1.22x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.863842247699283e-05 | 6.663739876541512e-05 | 2.92% | 3.00% | 1.03x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9115788831661893e-05 | 1.6617904074367534e-05 | 13.07% | 15.03% | 1.15x | ✅ |
| `humanize_seconds[negative]` | 2.400842316926563e-05 | 1.377481903250828e-05 | 42.63% | 74.29% | 1.74x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.8195225848789015e-05 | 1.5933427152940634e-05 | 43.49% | 76.96% | 1.77x | ✅ |
| `humanize_seconds[one-hour]` | 1.8163317441537536e-05 | 1.5174501614892412e-05 | 16.46% | 19.70% | 1.20x | ✅ |
| `humanize_seconds[one-minute]` | 1.8222494941661473e-05 | 1.585532802176728e-05 | 12.99% | 14.93% | 1.15x | ✅ |
| `humanize_seconds[one-second]` | 1.9102668933940583e-05 | 1.6590830419257503e-05 | 13.15% | 15.14% | 1.15x | ✅ |
| `humanize_seconds[zero]` | 8.91991225426686e-07 | 7.234738869826893e-07 | 18.89% | 23.29% | 1.23x | ✅ |
| `humanize_wei[ether]` | 2.8742722181301963e-05 | 2.7524103230120682e-05 | 4.24% | 4.43% | 1.04x | ✅ |
| `humanize_wei[gwei]` | 2.848861181252916e-05 | 2.7220629762657838e-05 | 4.45% | 4.66% | 1.05x | ✅ |
| `humanize_wei[wei]` | 2.8417831053596656e-05 | 2.6751603979368125e-05 | 5.86% | 6.23% | 1.06x | ✅ |
| `humanize_wei[zero]` | 5.071298482819614e-06 | 3.3164652705899364e-06 | 34.60% | 52.91% | 1.53x | ✅ |
| `is_ipfs_uri[empty]` | 1.884607144552106e-05 | 1.8815687023401336e-05 | 0.16% | 0.16% | 1.00x | ✅ |
| `is_ipfs_uri[invalid-cid]` | 3.319731475071475e-05 | 3.335938115017184e-05 | -0.49% | -0.49% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.146541657046433e-05 | 3.1897797752480784e-05 | -1.37% | -1.36% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.406097490907765e-05 | 3.362407592336494e-05 | 1.28% | 1.30% | 1.01x | ✅ |
