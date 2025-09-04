"""
compare_codspeed_results.py

Compares the two implementations in each benchmark group from a single CodSpeed results JSON file.
For each group (e.g., "abi_to_signature"), finds both implementations (e.g., "test_abi_to_signature" and "test_faster_abi_to_signature"),
computes the percent change in mean execution time, and writes a diff JSON file summarizing the results.

Assumes benchmark function names are paired by group and "faster" prefix.

Usage:
    python compare_codspeed_results.py <results.json> [output.json]
"""

import json
import sys
import re
from collections import defaultdict
from typing import Any, Dict

def get_group_name(test_name: str) -> str:
    # Extract group from test name, e.g., test_foo, test_faster_foo -> group: foo
    m = re.match(r"test_faster_(.+)", test_name)
    if m:
        return m.group(1)
    m = re.match(r"test_(.+)", test_name)
    if m:
        return m.group(1)
    return test_name

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python compare_codspeed_results.py <results.json> [output.json]")
        sys.exit(1)
    results_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "codspeed_diff.json"

    with open(results_path, "r") as f:
        results = json.load(f)

    # Group by group name
    groups: Dict[str, Dict[str, Any]] = defaultdict(dict)
    for test_name, data in results.items():
        group = get_group_name(test_name)
        if test_name.startswith("test_faster_"):
            groups[group]["faster"] = data
        elif test_name.startswith("test_"):
            groups[group]["reference"] = data

    diff = {}
    for group, impls in groups.items():
        ref = impls.get("reference")
        fast = impls.get("faster")
        if ref and fast:
            mean_ref = ref["mean"]
            mean_fast = fast["mean"]
            percent = ((mean_ref - mean_fast) / mean_ref) * 100 if mean_ref != 0 else 0.0
            diff[group] = {
                "reference_mean": mean_ref,
                "faster_mean": mean_fast,
                "unit": ref["unit"],
                "percent_change": percent,
                "reference": "test_" + group,
                "faster": "test_faster_" + group
            }
        else:
            diff[group] = {
                "note": f"Missing implementation(s): {list(impls.keys())}"
            }

    with open(output_path, "w") as f:
        json.dump(diff, f, indent=2)
    print(f"Diff written to {output_path}")

if __name__ == "__main__":
    main()
