"""
parse_codspeed_output.py

Extracts per-function benchmark timings from CodSpeed/pytest-codspeed output.
Parses the output text file, finds all test function results, and writes a JSON file
mapping function names to their mean execution time, unit, and standard deviation.

Usage:
    python parse_codspeed_output.py <codspeed_output.txt> [output.json]
"""

import re
import json
import sys
from typing import Dict, Any

def parse_codspeed_output(text: str) -> Dict[str, Any]:
    """
    Parses CodSpeed/pytest-codspeed output and extracts per-function timings.
    Returns a dict: {function_name: {"mean": float, "unit": str, ...}}
    """
    results = {}
    # Example line: test_func_name ... 123 ns ± 4 ns
    pattern = re.compile(r"^(test_[\w\d_]+).*?([0-9.]+)\s*(ns|us|ms|s)\s*±\s*([0-9.]+)\s*(ns|us|ms|s)", re.MULTILINE)
    for match in pattern.finditer(text):
        func = match.group(1)
        mean = float(match.group(2))
        unit = match.group(3)
        stddev = float(match.group(4))
        stddev_unit = match.group(5)
        results[func] = {
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
