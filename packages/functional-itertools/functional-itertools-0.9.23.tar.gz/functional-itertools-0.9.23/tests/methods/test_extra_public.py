from __future__ import annotations

from itertools import permutations
from typing import Any
from typing import Dict
from typing import List
from typing import Type

from hypothesis import given
from hypothesis.strategies import integers
from hypothesis.strategies import lists
from pytest import mark

from functional_itertools import CDict
from functional_itertools import CIterable
from functional_itertools import CList
from tests.strategies import Case
from tests.strategies import CASES
from tests.test_utilities import sum_varargs


@mark.parametrize("case", CASES)
@mark.parametrize("kwargs", [{}, {"parallel": True, "processes": 1}])
@given(x=lists(integers()), xs=lists(lists(integers())))
def test_map_dict(case: Case, x: List[int], xs: List[List[int]], kwargs: Dict[str, Any]) -> None:
    y = case.cls(x).map_dict(sum_varargs, *xs, **kwargs)
    assert isinstance(y, CDict)
    z = case.cast(x)
    if xs:
        keys = zip(z, *xs)
    else:
        keys = z
    assert y == dict(zip(keys, map(sum_varargs, z, *xs)))


@given(x=lists(integers()))
def test_pipe(x: List[int]) -> None:
    y = CIterable(x).pipe(permutations, r=2)
    assert isinstance(y, CIterable)
    assert list(y) == list(permutations(x, r=2))


@mark.parametrize("cls", [CIterable, CList])
@given(x=lists(integers(), min_size=1))
def test_unzip(cls: Type, x: List[int]) -> None:
    indices, ints = cls(x).enumerate().unzip()
    assert isinstance(indices, cls)
    assert list(indices) == list(range(len(x)))
    assert isinstance(ints, cls)
    assert list(ints) == x
