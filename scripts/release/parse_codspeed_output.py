"""
parse_codspeed_output.py

Extracts per-function benchmark timings from CodSpeed/pytest-codspeed output.
Parses the output text file, finds all test function results, and writes a JSON file
mapping submodules (benchmark files) to their test functions and results.

Usage:
    python parse_codspeed_output.py <codspeed_output.txt> [output.json]
"""

import re
import json
import sys
from collections import defaultdict
from typing import Dict, Any, DefaultDict


def parse_codspeed_output(text: str) -> Dict[str, Dict[str, Any]]:
    """
    Parses CodSpeed/pytest-codspeed output and extracts per-function timings,
    grouped by submodule (benchmark file).
    Returns a dict: {submodule: {function_name: {...}}}
    """
    results: DefaultDict[str, Dict[str, Any]] = defaultdict(dict)
    # Example line: benchmarks/test_abi_benchmarks.py::test_abi_to_signature ... 123 ns ± 4 ns
    pattern = re.compile(
        r"^(benchmarks/[a-zA-Z0-9_]+_benchmarks\.py)::(test_[\w\d_]+).*?([0-9.]+)\s*(ns|us|ms|s)\s*±\s*([0-9.]+)\s*(ns|us|ms|s)",
        re.MULTILINE
    )
    for match in pattern.finditer(text):
        submodule = match.group(1)
        func = match.group(2)
        mean = float(match.group(3))
        unit = match.group(4)
        stddev = float(match.group(5))
        stddev_unit = match.group(6)
        results[submodule][func] = {
            "mean": mean,
            "unit": unit,
            "stddev": stddev,
            "stddev_unit": stddev_unit
        }
    return results

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python parse_codspeed_output.py <codspeed_output.txt> [output.json]")
        sys.exit(1)
    infile = sys.argv[1]
    outfile = sys.argv[2] if len(sys.argv) > 2 else "codspeed_results.json"
    with open(infile, "r") as f:
        text = f.read()
    results = parse_codspeed_output(text)
    with open(outfile, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Parsed results written to {outfile}")

if __name__ == "__main__":
    main()
