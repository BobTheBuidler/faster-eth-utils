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
            "--disable-error-code=str-bytes-safe",
            "--disable-error-code=arg-type",
        ],
    )

extras_require = {
    'test': [
        'hypothesis>=4.43.0,<5.0.0',
        "pytest==5.4.1",
        "pytest-xdist",
        "tox==3.14.6",
    ],
    'lint': [
        'black>=18.6b4,<19',
        "flake8==3.7.9",
        "isort>=4.2.15,<5",
        "mypy==0.720",
        "pydocstyle>=5.0.0,<6",
        'pytest>=3.4.1,<4.0.0',
    ],
    'doc': [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9,<2",
        "towncrier>=19.2.0, <20",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        'wheel>=0.30.0,<1.0.0',
        "twine>=1.13,<2",
        "ipython",
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +  # noqa: W504
    extras_require['test'] +  # noqa: W504
    extras_require['lint'] +  # noqa: W504
    extras_require['doc']
)


with open('./README.md') as readme:
    long_description = readme.read()


setup(
    name="faster-eth-utils",
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='1.10.0',
    description=(
        """A fork of eth-utils: Common utility functions for python code that interacts with Ethereum, implemented in C"""
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='The Ethereum Foundation',
    author_email='snakecharmers@ethereum.org',
    url='https://github.com/ethereum/eth-utils',
    include_package_data=True,
    install_requires=[
        "eth-hash>=0.3.1,<0.4.0",
        "eth-typing>=2.2.1,<3.0.0",
        "toolz>0.8.2,<1;implementation_name=='pypy'",
        "cytoolz>=0.10.1,<1.0.0;implementation_name=='cpython'",
    ],
    python_requires=">=3.8,<4",
    extras_require=extras_require,
    py_modules=['eth_utils'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    ext_modules=ext_modules,
    package_data={"faster_eth_utils": ["py.typed"]},
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
