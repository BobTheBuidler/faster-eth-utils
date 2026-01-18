#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.201612352876896e-06 | 2.6298181409050403e-06 | 37.41% | 59.77% | 1.60x | ✅ |
| `humanize_bytes[empty]` | 1.0970706740896656e-06 | 7.93503879299511e-07 | 27.67% | 38.26% | 1.38x | ✅ |
| `humanize_bytes[long]` | 4.015969020640772e-06 | 2.415338722688158e-06 | 39.86% | 66.27% | 1.66x | ✅ |
| `humanize_bytes[short]` | 1.4454825087261684e-06 | 1.0846816512892169e-06 | 24.96% | 33.26% | 1.33x | ✅ |
| `humanize_hash[32-bytes]` | 4.4767471496551915e-06 | 2.6724719676735486e-06 | 40.30% | 67.51% | 1.68x | ✅ |
| `humanize_hash[empty]` | 1.3410176583846746e-06 | 8.246883506936589e-07 | 38.50% | 62.61% | 1.63x | ✅ |
| `humanize_hash[long]` | 4.227381334367479e-06 | 2.4559852514782113e-06 | 41.90% | 72.13% | 1.72x | ✅ |
| `humanize_hash[short]` | 1.6766120074957254e-06 | 1.1879019048250842e-06 | 29.15% | 41.14% | 1.41x | ✅ |
| `humanize_hexstr[empty]` | 1.8664455737620386e-06 | 6.470300113578999e-07 | 65.33% | 188.46% | 2.88x | ✅ |
| `humanize_hexstr[short-0x]` | 4.521551934288554e-06 | 2.4304900979076126e-06 | 46.25% | 86.03% | 1.86x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.7798050799113898e-06 | 1.9874510853485104e-06 | 47.42% | 90.18% | 1.90x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.611539697480597e-06 | 2.4635946768709296e-06 | 46.58% | 87.19% | 1.87x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.770352855175568e-06 | 2.01740874568231e-06 | 46.49% | 86.89% | 1.87x | ✅ |
| `humanize_integer_sequence[consecutive]` | 2.9908690807445216e-05 | 2.4296879063159713e-05 | 18.76% | 23.10% | 1.23x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.6889490343487174e-05 | 3.0048305750438677e-05 | 18.55% | 22.77% | 1.23x | ✅ |
| `humanize_integer_sequence[empty]` | 9.063901327259321e-07 | 5.72230356095265e-07 | 36.87% | 58.40% | 1.58x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.5217148295515906e-05 | 3.8111906599317816e-05 | 15.71% | 18.64% | 1.19x | ✅ |
| `humanize_integer_sequence[single]` | 2.594144188597825e-05 | 2.0337146766940227e-05 | 21.60% | 27.56% | 1.28x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.021919534114559e-05 | 3.372509818375482e-05 | 16.15% | 19.26% | 1.19x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.680183299390924e-05 | 6.597487833121085e-05 | 1.24% | 1.25% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8998687562782066e-05 | 1.830340176235728e-05 | 3.66% | 3.80% | 1.04x | ✅ |
| `humanize_seconds[negative]` | 2.358006175767517e-05 | 1.760951049092998e-05 | 25.32% | 33.91% | 1.34x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.731602995174883e-05 | 2.003017674915198e-05 | 26.67% | 36.37% | 1.36x | ✅ |
| `humanize_seconds[one-hour]` | 1.789457374038548e-05 | 1.672908446474155e-05 | 6.51% | 6.97% | 1.07x | ✅ |
| `humanize_seconds[one-minute]` | 1.808841124036868e-05 | 1.7552254064385684e-05 | 2.96% | 3.05% | 1.03x | ✅ |
| `humanize_seconds[one-second]` | 1.8933007543999276e-05 | 1.8175029517570505e-05 | 4.00% | 4.17% | 1.04x | ✅ |
| `humanize_seconds[zero]` | 8.923507088886444e-07 | 8.003709979094648e-07 | 10.31% | 11.49% | 1.11x | ✅ |
| `humanize_wei[ether]` | 2.700414144661337e-05 | 2.6307892154293215e-05 | 2.58% | 2.65% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.6799808728828346e-05 | 2.5894654664170432e-05 | 3.38% | 3.50% | 1.03x | ✅ |
| `humanize_wei[wei]` | 2.664006200936828e-05 | 2.5241174950638365e-05 | 5.25% | 5.54% | 1.06x | ✅ |
| `humanize_wei[zero]` | 4.797284198408134e-06 | 3.6582641770837285e-06 | 23.74% | 31.14% | 1.31x | ✅ |
| `is_ipfs_uri[empty]` | 1.825715579367967e-05 | 1.865356744701346e-05 | -2.17% | -2.13% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.277887098586284e-05 | 3.2292634049814424e-05 | 1.48% | 1.51% | 1.02x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.016621875760657e-05 | 3.081780365223372e-05 | -2.16% | -2.11% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.333816221506527e-05 | 3.296229471397943e-05 | 1.13% | 1.14% | 1.01x | ✅ |
