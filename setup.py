#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)
try:
    from mypyc.build import mypycify
except ImportError:
    ext_modules = []
else:
    ext_modules = mypycify(
        [
            "faster_eth_utils/abi.py",
            "faster_eth_utils/address.py",
            #"faster_eth_utils/applicators.py",
            "faster_eth_utils/conversions.py",
            "faster_eth_utils/currency.py",
            "faster_eth_utils/debug.py",
            "faster_eth_utils/decorators.py",
            "faster_eth_utils/encoding.py",
            "faster_eth_utils/exceptions.py",
            "faster_eth_utils/hexadecimal.py",
            "faster_eth_utils/humanize.py",
            "faster_eth_utils/module_loading.py",
            # "faster_eth_utils/network.py", compiled module has no __file__
            "faster_eth_utils/types.py",
            "faster_eth_utils/units.py",
            "--pretty",
            "--install-types",
            "--disable-error-code=attr-defined",
            "--disable-error-code=comparison-overlap",
            "--disable-error-code=typeddict-item",
            "--disable-error-code=assignment",
            "--disable-error-code=type-var",
            "--disable-error-code=no-any-return",
            "--disable-error-code=unused-ignore",
        ],
    )

extras_require = {
    "test": [
        "hypothesis>=4.43.0",
        "pytest>=7.0.0",
        "pytest-xdist>=2.4.0",
        "types-setuptools",
        "mypy==0.971",  # mypy does not follow semver, leave it pinned.
    ],
    "lint": [
        "flake8==3.8.3",  # flake8 claims semver but adds new warnings at minor releases, leave it pinned.
        "isort>=5.11.0",
        "mypy==0.971",  # mypy does not follow semver, leave it pinned.
        "pydocstyle>=5.0.0",
        "black>=23",
        "types-setuptools",
    ],
    "docs": [
        "sphinx>=5.0.0",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=21,<22",
    ],
    "dev": [
        "bumpversion>=0.5.3",
        "pytest-watch>=4.1.0",
        "tox>=4.0.0",
        "build>=0.9.0",
        "wheel",
        "twine",
        "ipython",
        "eth-hash[pycryptodome]",
    ],
}

extras_require["dev"] = (
    extras_require["dev"]
    + extras_require["test"]
    + extras_require["lint"]
    + extras_require["docs"]
)


with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="faster-eth-utils",
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version="2.3.0",
    description=(
        """A fork of eth-utils: Common utility functions for python code that interacts with Ethereum, implemented in C"""
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/BobTheBuidler/eth-utils",
    include_package_data=True,
    install_requires=[
        "cached-property>=1.5.2,<2;python_version<'3.8'",
        "eth-hash>=0.3.1",
        "eth-typing>=3.0.0",
        "toolz>0.8.2;implementation_name=='pypy'",
        "cytoolz>=0.10.1;implementation_name=='cpython'",
    ],
    python_requires=">=3.8,<4",
    extras_require=extras_require,
    py_modules=["eth_utils"],
    license="MIT",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    ext_modules=ext_modules,
    package_data={"faster_eth_utils": ["py.typed"]},
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
