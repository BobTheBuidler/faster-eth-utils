"""
compare_codspeed_results.py

Refactored: Compares the two implementations in each benchmark group from a pytest-benchmark parsed results JSON file.
For each group (e.g., "abi_to_signature"), finds both implementations
(e.g., "test_abi_to_signature" and "test_faster_abi_to_signature"), computes the percent change
in mean execution time, and writes a diff JSON file summarizing the results.

Usage:
    python compare_codspeed_results.py <results.json> [output.json]
"""

import json
import sys
import re
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

def compare_group(group_results: Dict[str, Any]) -> Dict[str, Any]:
    # Find reference and faster implementations in the group
    ref = None
    fast = None
    for func_name, data in group_results.items():
        if func_name.startswith("test_faster_"):
            fast = data
        elif func_name.startswith("test_"):
            ref = data

    if ref and fast:
        mean_ref = ref["mean"]
        mean_fast = fast["mean"]
        percent = ((mean_ref - mean_fast) / mean_ref) * 100 if mean_ref != 0 else 0.0
        return {
            "reference_mean": mean_ref,
            "faster_mean": mean_fast,
            "unit": ref["unit"],
            "percent_change": percent,
            "reference": [k for k in group_results if k.startswith("test_") and not k.startswith("test_faster_")][0],
            "faster": [k for k in group_results if k.startswith("test_faster_")][0]
        }
    else:
        return {
            "note": f"Missing implementation(s): {['reference' if not ref else '', 'faster' if not fast else '']}"
        }

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python compare_codspeed_results.py <results.json> [output.json]")
        sys.exit(1)
    results_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "codspeed_diff.json"

    with open(results_path, "r") as f:
        results = json.load(f)

    # results: {group: {function_name: {...}}}
    diff_by_group = {}
    for group, group_results in results.items():
        diff_by_group[group] = compare_group(group_results)

    with open(output_path, "w") as f:
        json.dump(diff_by_group, f, indent=2)
    print(f"Diff written to {output_path}")

if __name__ == "__main__":
    main()
