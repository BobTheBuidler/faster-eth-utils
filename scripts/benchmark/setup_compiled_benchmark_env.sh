#!/usr/bin/env bash
set -euo pipefail

requirements_file="${1:?usage: setup_compiled_benchmark_env.sh <requirements-file>}"

python -m pip install --upgrade pip

mapfile -t wheels < <(find wheelhouse -maxdepth 1 -type f -name '*.whl' | sort)
if [[ "${#wheels[@]}" -ne 1 ]]; then
  echo "Expected exactly 1 wheel in wheelhouse/, found ${#wheels[@]}." >&2
  ls -al wheelhouse ||:
  exit 1
fi

wheel_path="${wheels[0]}"
echo "Installing compiled wheel: ${wheel_path}"
python -m pip install "${wheel_path}" -r "${requirements_file}"

# Force imports to resolve from the installed package.
rm -rf faster_eth_utils

python - <<'PY'
import importlib
import importlib.machinery

MODULES_TO_VERIFY = [
    "faster_eth_utils.abi",
    "faster_eth_utils.address",
    "faster_eth_utils.conversions",
    "faster_eth_utils.crypto",
]

ext_suffixes = tuple(importlib.machinery.EXTENSION_SUFFIXES)
errors = []

for module_name in MODULES_TO_VERIFY:
    module = importlib.import_module(module_name)
    module_file = getattr(module, "__file__", None)
    if not module_file:
        errors.append(f"{module_name}: missing __file__")
        continue

    normalized = module_file.replace("\\", "/")
    if not normalized.endswith(ext_suffixes):
        errors.append(
            f"{module_name}: expected compiled extension suffix {ext_suffixes}, got {module_file}"
        )
    if "/site-packages/" not in normalized:
        errors.append(f"{module_name}: expected site-packages import path, got {module_file}")

if errors:
    raise SystemExit("Compiled environment validation failed:\n- " + "\n- ".join(errors))

print("Compiled environment validation passed for:", ", ".join(MODULES_TO_VERIFY))
PY
