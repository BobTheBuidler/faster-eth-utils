#!/usr/bin/env python
import sys
from typing import List
from setuptools import (
    find_packages,
    setup,
)
try:
    from mypyc.build import mypycify
except ImportError:
    skip_mypyc = True
else:
    skip_mypyc = any(
        cmd in sys.argv
        for cmd in ("sdist", "egg_info", "--name", "--version", "--help", "--help-commands")
    )

if skip_mypyc:
    ext_modules = []
else:
    mypyc_flags = ["--pretty", "--strict"]
    if sys.version_info < (3, 9):
        # We only enable these on the lowest supported Python version
        mypyc_flags.append("--disable-error-code=redundant-cast")
        mypyc_flags.append("--disable-error-code=unused-ignore")
    
    ext_modules = mypycify(
        [
            "faster_eth_utils/abi.py",
            "faster_eth_utils/address.py",
            "faster_eth_utils/applicators.py",
            "faster_eth_utils/conversions.py",
            "faster_eth_utils/crypto.py",
            "faster_eth_utils/currency.py",
            "faster_eth_utils/debug.py",
            "faster_eth_utils/decorators.py",
            "faster_eth_utils/encoding.py",
            "faster_eth_utils/exceptions.py",
            "faster_eth_utils/functional.py",
            "faster_eth_utils/hexadecimal.py",
            "faster_eth_utils/humanize.py",
            "faster_eth_utils/module_loading.py",
            "faster_eth_utils/network.py",
            "faster_eth_utils/numeric.py",
            "faster_eth_utils/toolz.py",
            "faster_eth_utils/types.py",
            "faster_eth_utils/units.py",
            *mypyc_flags,
        ],
        group_name="faster_eth_utils",
        strict_dunder_typing=True,
    )

MYPY_REQUIREMENT = "mypy==1.18.2"
PYTEST_REQUIREMENT = "pytest>=7.0.0"


def read_requirements(path: str) -> List[str]:
    with open(path) as f:
        reqs = set()
        for line in f:
            if stripped := line.strip():
                if not stripped.startswith("#"):
                    if stripped.startswith("-r "):
                        reqs.update(read_requirements(stripped[3:]))
                    else:
                        reqs.add(stripped)
        return sorted(reqs)


extras_require = {
    "dev": read_requirements("requirements-dev.txt"),
    "docs": [
        "sphinx>=6.0.0",
        "sphinx-autobuild>=2021.3.14",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=24,<26",
    ],
    "test": read_requirements("requirements-test.txt"),
    "codspeed": read_requirements("requirements-codspeed.txt"),
    "benchmark": read_requirements("requirements-benchmark.txt"),
}

extras_require["dev"] = (
    extras_require["dev"] + extras_require["docs"] + extras_require["test"]
)


with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="faster-eth-utils",
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version="5.3.20",
    description=(
        """A faster fork of eth-utils: Common utility functions for python code that interacts with Ethereum. Implemented in C"""
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/BobTheBuidler/faster-eth-utils",
    project_urls={
        "Documentation": "https://eth-utils.readthedocs.io/en/stable/",
        "Release Notes": "https://github.com/BobTheBuidler/faster-eth-utils/releases",
        "Issues": "https://github.com/BobTheBuidler/faster-eth-utils/issues",
        "Source - Precompiled (.py)": "https://github.com/BobTheBuidler/faster-eth-utils/tree/master/faster_eth_utils",
        "Source - Compiled (.c)": "https://github.com/BobTheBuidler/faster-eth-utils/tree/master/build",
        "Benchmarks": "https://github.com/BobTheBuidler/faster-eth-utils/tree/master/benchmarks",
        "Benchmarks - Results": "https://github.com/BobTheBuidler/faster-eth-utils/tree/master/benchmarks/results",
        "Original": "https://github.com/ethereum/eth-utils",
    },
    include_package_data=True,
    install_requires=[
        "cchecksum==0.3.8.dev0",
        "eth-hash>=0.3.1",
        "eth-typing==5.2.1",
        "eth-utils==5.3.1",
        "toolz>0.8.2;implementation_name=='pypy'",
        "cytoolz>=0.10.1;implementation_name=='cpython'",
        "pydantic>=2.0.0,<3",
    ],
    python_requires=">=3.8, <4",
    extras_require=extras_require,
    py_modules=["eth_utils"],
    license="MIT",
    license_files=["LICENSE"],
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["scripts", "scripts.*", "tests", "tests.*"]),
    ext_modules=ext_modules,
    package_data={"faster_eth_utils": ["py.typed"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
