#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.222570938260116e-06 | 2.813966892263052e-06 | 33.36% | 50.06% | 1.50x | ✅ |
| `humanize_bytes[empty]` | 1.1102101185615028e-06 | 8.221792968582159e-07 | 25.94% | 35.03% | 1.35x | ✅ |
| `humanize_bytes[long]` | 4.0340676623065334e-06 | 2.6419827554711567e-06 | 34.51% | 52.69% | 1.53x | ✅ |
| `humanize_bytes[short]` | 1.4795851968853081e-06 | 1.1307604357721328e-06 | 23.58% | 30.85% | 1.31x | ✅ |
| `humanize_hash[32-bytes]` | 4.509630319212018e-06 | 2.800765915337454e-06 | 37.89% | 61.01% | 1.61x | ✅ |
| `humanize_hash[empty]` | 1.3551590246490549e-06 | 8.283883533040229e-07 | 38.87% | 63.59% | 1.64x | ✅ |
| `humanize_hash[long]` | 4.299933819595659e-06 | 2.584899547488099e-06 | 39.89% | 66.35% | 1.66x | ✅ |
| `humanize_hash[short]` | 1.7018638022907332e-06 | 1.2385512321216865e-06 | 27.22% | 37.41% | 1.37x | ✅ |
| `humanize_hexstr[empty]` | 1.9038697816785383e-06 | 6.402740928864487e-07 | 66.37% | 197.35% | 2.97x | ✅ |
| `humanize_hexstr[short-0x]` | 4.539754753976121e-06 | 2.45566740068357e-06 | 45.91% | 84.87% | 1.85x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.8223936685001e-06 | 2.0326988582497556e-06 | 46.82% | 88.05% | 1.88x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.589523895523414e-06 | 2.4803822258938385e-06 | 45.96% | 85.03% | 1.85x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.9677462885550195e-06 | 1.9987994369067398e-06 | 49.62% | 98.51% | 1.99x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0603078432227386e-05 | 2.4297889411073275e-05 | 20.60% | 25.95% | 1.26x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.713566677639425e-05 | 2.9594841020450837e-05 | 20.31% | 25.48% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 9.234031332114298e-07 | 5.762028249145319e-07 | 37.60% | 60.26% | 1.60x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.60328584345492e-05 | 3.7340836208866085e-05 | 18.88% | 23.28% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.652188539773415e-05 | 2.0063664495676576e-05 | 24.35% | 32.19% | 1.32x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0532208911423836e-05 | 3.314820503640558e-05 | 18.22% | 22.28% | 1.22x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.814211730365321e-05 | 6.760755518864934e-05 | 0.78% | 0.79% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9465859782025446e-05 | 1.804899965051573e-05 | 7.28% | 7.85% | 1.08x | ✅ |
| `humanize_seconds[negative]` | 2.3741628306994278e-05 | 1.8210832706442042e-05 | 23.30% | 30.37% | 1.30x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7923245413948027e-05 | 1.9831547294292406e-05 | 28.98% | 40.80% | 1.41x | ✅ |
| `humanize_seconds[one-hour]` | 1.815953324577815e-05 | 1.6636229065914997e-05 | 8.39% | 9.16% | 1.09x | ✅ |
| `humanize_seconds[one-minute]` | 1.831364009775129e-05 | 1.7332689001099917e-05 | 5.36% | 5.66% | 1.06x | ✅ |
| `humanize_seconds[one-second]` | 1.8987077402874027e-05 | 1.791555942485035e-05 | 5.64% | 5.98% | 1.06x | ✅ |
| `humanize_seconds[zero]` | 8.954912531816298e-07 | 6.625182015744087e-07 | 26.02% | 35.16% | 1.35x | ✅ |
| `humanize_wei[ether]` | 2.730158064888279e-05 | 2.707534065869358e-05 | 0.83% | 0.84% | 1.01x | ✅ |
| `humanize_wei[gwei]` | 2.7095177068878593e-05 | 2.6605555673191488e-05 | 1.81% | 1.84% | 1.02x | ✅ |
| `humanize_wei[wei]` | 2.706416982992945e-05 | 2.610544178974533e-05 | 3.54% | 3.67% | 1.04x | ✅ |
| `humanize_wei[zero]` | 4.953698687081932e-06 | 4.241740825116884e-06 | 14.37% | 16.78% | 1.17x | ✅ |
| `is_ipfs_uri[empty]` | 1.8324723439455395e-05 | 1.8975285313921252e-05 | -3.55% | -3.43% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.2884501539706405e-05 | 3.376937174729862e-05 | -2.69% | -2.62% | 0.97x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.068764272707413e-05 | 3.129962484755828e-05 | -1.99% | -1.96% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.341012489457816e-05 | 3.351915430296675e-05 | -0.33% | -0.33% | 1.00x | ❌ |
