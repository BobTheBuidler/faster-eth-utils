#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.2409062602460535e-06 | 2.7191839837994455e-06 | 35.88% | 55.96% | 1.56x | ✅ |
| `humanize_bytes[empty]` | 1.1083682610753468e-06 | 9.166171340300774e-07 | 17.30% | 20.92% | 1.21x | ✅ |
| `humanize_bytes[long]` | 3.981263734013379e-06 | 2.475460208887011e-06 | 37.82% | 60.83% | 1.61x | ✅ |
| `humanize_bytes[short]` | 1.4772367648040824e-06 | 1.1548633324847423e-06 | 21.82% | 27.91% | 1.28x | ✅ |
| `humanize_hash[32-bytes]` | 4.50715519511355e-06 | 2.697200462580106e-06 | 40.16% | 67.10% | 1.67x | ✅ |
| `humanize_hash[empty]` | 1.3694072813078141e-06 | 8.309876162836749e-07 | 39.32% | 64.79% | 1.65x | ✅ |
| `humanize_hash[long]` | 4.254343231632876e-06 | 2.463062463389663e-06 | 42.10% | 72.73% | 1.73x | ✅ |
| `humanize_hash[short]` | 1.714714634695181e-06 | 1.0916798841067907e-06 | 36.33% | 57.07% | 1.57x | ✅ |
| `humanize_hexstr[empty]` | 1.8486913206360138e-06 | 6.346834230916822e-07 | 65.67% | 191.28% | 2.91x | ✅ |
| `humanize_hexstr[short-0x]` | 4.539872636896956e-06 | 2.404073885307422e-06 | 47.05% | 88.84% | 1.89x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.779045926787203e-06 | 1.9847801319666823e-06 | 47.48% | 90.40% | 1.90x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.579803531097191e-06 | 2.4001195778653436e-06 | 47.59% | 90.82% | 1.91x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.789665120891023e-06 | 1.981552087742965e-06 | 47.71% | 91.25% | 1.91x | ✅ |
| `humanize_integer_sequence[consecutive]` | 2.9918971298209343e-05 | 2.474078454744024e-05 | 17.31% | 20.93% | 1.21x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.652754192505382e-05 | 3.0107792557469247e-05 | 17.58% | 21.32% | 1.21x | ✅ |
| `humanize_integer_sequence[empty]` | 8.972723138621095e-07 | 5.636738179047852e-07 | 37.18% | 59.18% | 1.59x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.49040021342828e-05 | 3.817094685559168e-05 | 14.99% | 17.64% | 1.18x | ✅ |
| `humanize_integer_sequence[single]` | 2.6053885137631433e-05 | 2.053961849386984e-05 | 21.16% | 26.85% | 1.27x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.9732231322803684e-05 | 3.408168047316562e-05 | 14.22% | 16.58% | 1.17x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.747364275359722e-05 | 6.607644634768743e-05 | 2.07% | 2.11% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9130674615949608e-05 | 1.8376849860361753e-05 | 3.94% | 4.10% | 1.04x | ✅ |
| `humanize_seconds[negative]` | 2.3481794116529348e-05 | 1.7562636375230336e-05 | 25.21% | 33.70% | 1.34x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7709769487220052e-05 | 2.0022205925899284e-05 | 27.74% | 38.40% | 1.38x | ✅ |
| `humanize_seconds[one-hour]` | 1.7933699560075737e-05 | 1.6826953732886477e-05 | 6.17% | 6.58% | 1.07x | ✅ |
| `humanize_seconds[one-minute]` | 1.8096498343829538e-05 | 1.7647619806234086e-05 | 2.48% | 2.54% | 1.03x | ✅ |
| `humanize_seconds[one-second]` | 1.8877101573087346e-05 | 1.838398100937168e-05 | 2.61% | 2.68% | 1.03x | ✅ |
| `humanize_seconds[zero]` | 8.600787946455101e-07 | 6.870420023423472e-07 | 20.12% | 25.19% | 1.25x | ✅ |
| `humanize_wei[ether]` | 2.7095774181922743e-05 | 2.679813252186694e-05 | 1.10% | 1.11% | 1.01x | ✅ |
| `humanize_wei[gwei]` | 2.669996790398808e-05 | 2.5915878085871445e-05 | 2.94% | 3.03% | 1.03x | ✅ |
| `humanize_wei[wei]` | 2.656387867847843e-05 | 2.5906736361557395e-05 | 2.47% | 2.54% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.842661048837903e-06 | 3.694889413591887e-06 | 23.70% | 31.06% | 1.31x | ✅ |
| `is_ipfs_uri[empty]` | 1.8381317793944056e-05 | 1.872936989987118e-05 | -1.89% | -1.86% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.271089449745448e-05 | 3.270733682764732e-05 | 0.01% | 0.01% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.0443562297603102e-05 | 3.093517555658073e-05 | -1.61% | -1.59% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.34716880866494e-05 | 3.303661364479098e-05 | 1.30% | 1.32% | 1.01x | ✅ |
