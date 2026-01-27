import json
from collections import (
    defaultdict,
)
from pathlib import (
    Path,
)
from typing import (
    Any,
)

from .parse_benchmark_output import (
    parse_benchmark_output,
)


RESULTS_DIR = Path(__file__).resolve().parents[2] / "benchmarks" / "results"


def generate_benchmark_markdown(results: dict[str, dict[str, float]]) -> None:
    for module, functions in results.items():
        if module == "_root":
            continue
        lines = [
            f"# {module.title()}\n",
            "",
        ]

        table = [
            "| Function | Average |",
            "| --- | --- |",
        ]
        for function, avg in functions.items():
            table.append(f"| `{function}` | `{avg:.2f} us` |")

        lines.append("\n".join(table))
        lines.append("")

        (RESULTS_DIR / f"{module}.md").write_text("\n".join(lines))


if __name__ == "__main__":
    results = parse_benchmark_output()
    generate_benchmark_markdown(results)
