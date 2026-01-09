from pathlib import Path


def test_import_and_version():
    import faster_eth_utils

    assert isinstance(faster_eth_utils.__version__, str)


def test_compiled_c_sources_exist_for_submodules():
    compiled_modules = [
        "abi",
        "address",
        "applicators",
        "conversions",
        "crypto",
        "currency",
        "debug",
        "decorators",
        "encoding",
        "exceptions",
        "functional",
        "hexadecimal",
        "humanize",
        "module_loading",
        "network",
        "numeric",
        "toolz",
        "types",
        "units",
    ]
    repo_root = Path(__file__).resolve().parents[2]
    build_dir = repo_root / "build" / "faster_eth_utils"

    assert build_dir.is_dir(), (
        "Expected the mypyc build output directory to exist at "
        f"{build_dir!s}."
    )

    missing_sources = [
        module for module in compiled_modules if not (build_dir / f"{module}.c").exists()
    ]

    assert not missing_sources, (
        "Expected C sources for compiled submodules. Missing: "
        f"{', '.join(sorted(missing_sources))}."
    )
