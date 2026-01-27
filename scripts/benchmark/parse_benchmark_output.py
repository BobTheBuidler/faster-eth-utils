import json
from pathlib import (
    Path,
)
from typing import (
    Any,
)


RESULTS_DIR = Path(__file__).resolve().parents[2] / "benchmarks" / "results"


def parse_benchmark_output() -> dict[str, dict[str, float]]:
    """
    Parses the benchmark output from pytest-benchmark and returns a nested dictionary.
    """
    stats = json.loads((RESULTS_DIR / "results.json").read_text())
    results = {}

    for entry in stats["benchmarks"]:
        name = entry["name"].replace("test_", "").replace("benchmark_", "")
        name = name.replace("Test", "")
        name = name.replace("__", ".")
        module, function = name.split(".")

        results.setdefault(module, {})
        results[module][function] = entry["stats"]["mean"] * 1000000

    return results
