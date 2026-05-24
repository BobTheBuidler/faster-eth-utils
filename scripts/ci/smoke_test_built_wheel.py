from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
BUILD_DIR = PROJECT_ROOT / "build"
DIST_DIR = PROJECT_ROOT / "dist"
WHEEL_PATTERN = "faster_eth_utils-*.whl"
PACKAGE_IMPORT = "faster_eth_utils"


def run_python(*args: str, cwd: Path = PROJECT_ROOT) -> None:
    subprocess.run((sys.executable, *args), cwd=cwd, check=True)


def clean_build_artifacts() -> None:
    for path in (BUILD_DIR, DIST_DIR):
        if path.exists():
            shutil.rmtree(path)


def find_built_wheel() -> Path:
    wheels = sorted(DIST_DIR.glob(WHEEL_PATTERN))
    if len(wheels) == 1:
        return wheels[0]

    found = ", ".join(wheel.name for wheel in wheels) or "none"
    raise SystemExit(
        f"Expected exactly one {WHEEL_PATTERN} in {DIST_DIR}, found {found}."
    )


def main() -> None:
    clean_build_artifacts()
    run_python("-m", "build")

    wheel = find_built_wheel()
    print(f"Installing wheel: {wheel.name}")
    run_python(
        "-m",
        "pip",
        "install",
        "--upgrade",
        str(wheel),
        "--progress-bar",
        "off",
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        run_python("-c", f"import {PACKAGE_IMPORT}", cwd=Path(tmpdir))


if __name__ == "__main__":
    main()
