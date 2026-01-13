from typing import Type, Union

import pytest

from faster_eth_utils import (
    combomethod,
)


@pytest.fixture()
def Getter() -> type["_Getter"]:
    class _Getter:
        val = 1

        @combomethod
        def get(combo: Union[type["_Getter"], "_Getter"]) -> str:
            if isinstance(combo, type):
                return f"{combo.val} by class"
            elif isinstance(combo, _Getter):
                return f"{combo.val} by instance"
            else:
                raise TypeError("Unreachable, unless you really monkey around")

    return _Getter


def test_class_access(Getter: type["_Getter"]) -> None:
    assert Getter.get() == "1 by class"


def test_instance_access(Getter: type["_Getter"]) -> None:
    getter = Getter()
    getter.val = 2
    assert getter.get() == "2 by instance"
