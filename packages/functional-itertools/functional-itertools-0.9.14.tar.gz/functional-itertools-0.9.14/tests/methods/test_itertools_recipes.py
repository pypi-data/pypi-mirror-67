from __future__ import annotations

from functools import partial
from itertools import islice
from operator import add
from operator import neg
from sys import maxsize
from typing import Callable
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple

from hypothesis import assume
from hypothesis import given
from hypothesis.strategies import data
from hypothesis.strategies import DataObject
from hypothesis.strategies import integers
from hypothesis.strategies import just
from hypothesis.strategies import none
from hypothesis.strategies import tuples
from more_itertools.recipes import all_equal
from more_itertools.recipes import consume
from more_itertools.recipes import dotproduct
from more_itertools.recipes import first_true
from more_itertools.recipes import flatten
from more_itertools.recipes import grouper
from more_itertools.recipes import iter_except
from more_itertools.recipes import ncycles
from more_itertools.recipes import nth
from more_itertools.recipes import nth_combination
from more_itertools.recipes import padnone
from more_itertools.recipes import pairwise
from more_itertools.recipes import partition
from more_itertools.recipes import powerset
from more_itertools.recipes import prepend
from more_itertools.recipes import quantify
from more_itertools.recipes import repeatfunc
from more_itertools.recipes import roundrobin
from more_itertools.recipes import tabulate
from more_itertools.recipes import tail
from more_itertools.recipes import take
from more_itertools.recipes import unique_everseen
from more_itertools.recipes import unique_justseen
from pytest import mark

from functional_itertools import CIterable
from functional_itertools import CTuple
from tests.strategies import Case
from tests.strategies import CASES
from tests.strategies import combinations_r
from tests.strategies import combinations_x
from tests.strategies import islice_ints
from tests.strategies import permutations_r
from tests.strategies import permutations_x
from tests.strategies import product_repeat
from tests.strategies import product_x
from tests.strategies import product_xs
from tests.strategies import real_iterables
from tests.test_utilities import is_even


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()))
def test_all_equal(case: Case, x: Iterable[int]) -> None:
    y = case.cls(x).all_equal()
    assert isinstance(y, bool)
    assert y == all_equal(x)


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()), n=none() | integers(0, maxsize))
def test_consume(case: Case, x: Iterable[int], n: Optional[int]) -> None:
    y = case.cls(x).consume(n=n)
    assert isinstance(y, case.cls)
    if case.ordered:
        iter_x = iter(x)
        consume(iter_x, n=n)
        assert case.cast(y) == case.cast(iter_x)


@mark.parametrize("case", CASES)
@given(pairs=real_iterables(tuples(integers(), integers()), min_size=1))
def test_dotproduct(case: Case, pairs: Iterable[Tuple[int, int]]) -> None:
    x, y = zip(*pairs)
    z = case.cls(x).dotproduct(y)
    assert isinstance(z, int)
    if case.ordered:
        assert z == dotproduct(x, y)


@mark.parametrize("case", CASES)
@given(
    x=real_iterables(integers()), default=integers(), pred=none() | just(is_even),
)
def test_first_true(
    case: Case, x: Iterable[int], default: int, pred: Optional[Callable[[int], bool]],
) -> None:
    y = case.cls(x).first_true(default=default, pred=pred)
    assert isinstance(y, int)
    if case.ordered:
        assert y == first_true(x, default=default, pred=pred)


@mark.parametrize("case", CASES)
@given(x=real_iterables(real_iterables(integers())))
def test_flatten(case: Case, x: Iterable[Iterable[int]]) -> None:
    y = case.cls(x).flatten()
    assert isinstance(y, case.cls)
    if case.ordered:
        assert case.cast(y) == case.cast(flatten(x))


@mark.parametrize("case", CASES)
@given(
    x=real_iterables(integers()), n=integers(0, 1000), fillvalue=none() | integers(),
)
def test_grouper(case: Case, x: Iterable[int], n: int, fillvalue: Optional[int]) -> None:
    y = case.cls(x).grouper(n, fillvalue=fillvalue)
    assert isinstance(y, case.cls)
    z = list(y)
    for zi in z:
        assert isinstance(zi, CTuple)
    if case.ordered:
        assert case.cast(map(case.cast, z)) == case.cast(
            map(case.cast, grouper(x, n, fillvalue=fillvalue)),
        )


@mark.parametrize("case", CASES)
def test_iter_except(case: Case) -> None:
    def create_adder() -> Callable[[], int]:
        x = set()

        def adder() -> int:
            len_x = len(x)
            if len_x <= 10:
                x.add(len_x)
                return len_x
            else:
                raise ValueError()

        return adder

    y = case.cls.iter_except(create_adder(), ValueError)
    assert isinstance(y, case.cls)
    assert case.cast(y) == case.cast(iter_except(create_adder(), ValueError))


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers(), max_size=10), n=integers(0, 5))
def test_ncycles(case: Case, x: Iterable[int], n: int) -> None:
    y = case.cls(x).ncycles(n)
    assert isinstance(y, case.cls)
    if case.ordered:
        assert case.cast(y) == case.cast(ncycles(x, n))


@mark.parametrize("case", CASES)
@given(
    x=real_iterables(integers()), n=integers(0, maxsize), default=none() | integers(),
)
def test_nth(case: Case, x: Iterable[int], n: int, default: Optional[int]) -> None:
    y = case.cls(x).nth(n, default=default)
    assert isinstance(y, int) or (y is None)
    if case.ordered:
        assert y == nth(x, n, default=default)


@mark.parametrize("case", CASES)
@given(
    data=data(), x=real_iterables(integers(), min_size=2),
)
def test_nth_combination(case: Case, data: DataObject, x: Iterable[int]) -> None:
    r = data.draw(integers(1, len(x) - 1))
    index = data.draw(integers(0, r))
    y = case.cls(x).nth_combination(r, index)
    assert isinstance(y, CTuple)
    if case.ordered:
        assert y == nth_combination(x, r, index)


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()), n=islice_ints)
def test_padnone(case: Case, x: List[int], n: int) -> None:
    y = case.cls(x).padnone()
    assert isinstance(y, CIterable)
    if case.ordered:
        assert case.cast(y[:n]) == case.cast(islice(padnone(x), n))


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()))
def test_pairwise(case: Case, x: Iterable[int]) -> None:
    y = case.cls(x).pairwise()
    assert isinstance(y, case.cls)
    z = case.cast(y)
    for zi in z:
        assert isinstance(zi, CTuple)
        zi0, zi1 = zi
        assert isinstance(zi0, int)
        assert isinstance(zi1, int)
    if case.ordered:
        assert z == case.cast(pairwise(x))


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()))
def test_partition(case: Case, x: Iterable[int]) -> None:
    y = case.cls(x).partition(is_even)
    assert isinstance(y, CTuple)
    assert len(y) == 2
    for yi in y:
        assert isinstance(yi, case.cls)
    for yi, zi in zip(y, partition(is_even, x)):
        assert case.cast(yi) == case.cast(zi)


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()))
def test_powerset(case: Case, x: Iterable[int]) -> None:
    y = case.cls(x).powerset()
    assert isinstance(y, case.cls)
    z = list(y)
    for zi in z:
        assert isinstance(zi, CTuple)
    if case.ordered:
        assert case.cast(map(case.cast, z)) == case.cast(map(case.cast, powerset(x)))


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()), value=integers())
def test_prepend(case: Case, x: Iterable[int], value: int) -> None:
    y = case.cls(x).prepend(value)
    assert isinstance(y, case.cls)
    if case.ordered:
        assert case.cast(y) == case.cast(prepend(value, x))


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()))
def test_quantify(case: Case, x: Iterable[int]) -> None:
    y = case.cls(x).quantify(pred=is_even)
    assert isinstance(y, int)
    assert y == quantify(x, pred=is_even)


@mark.parametrize("case", CASES)
@given(x=combinations_x, r=combinations_r)
def test_random_combination(case: Case, x: Iterable[int], r: int) -> None:
    assume(0 <= r <= len(x))
    assert isinstance(case.cls(x).random_combination(r), CTuple)


@mark.parametrize("case", CASES)
@given(x=combinations_x, r=combinations_r)
def test_random_combination_with_replacement(case: Case, x: Iterable[int], r: int) -> None:
    assert isinstance(case.cls(x).random_combination_with_replacement(r), CTuple)


@mark.parametrize("case", CASES)
@given(x=permutations_x, r=permutations_r)
def test_random_permutation(case: Case, x: Iterable[int], r: Optional[int]) -> None:
    if r is not None:
        assume(0 <= r <= len(x))
    assert isinstance(case.cls(x).random_permutation(r=r), CTuple)


@mark.parametrize("case", CASES)
@given(
    x=product_x, xs=product_xs, repeat=product_repeat,
)
def test_random_product(
    case: Case, x: Iterable[int], xs: Iterable[Iterable[int]], repeat: int,
) -> None:
    assert isinstance(case.cls(x).random_product(*xs, repeat=repeat), CTuple)


@mark.parametrize("case", CASES)
@given(data=data(), n=islice_ints)
def test_repeatfunc(case: Case, data: DataObject, n: int) -> None:
    add1 = partial(add, 1)
    if case.cls is CIterable:
        times = data.draw(none() | integers(0, 10))
    else:
        times = data.draw(integers(0, 10))
    y = case.cls.repeatfunc(add1, times, 0)
    assert isinstance(y, case.cls)
    z = repeatfunc(add1, times, 0)
    if (case.cls is CIterable) and (times is None):
        assert case.cast(y[:n]) == case.cast(islice(z, n))
    else:
        assert case.cast(y) == case.cast(z)


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()), xs=real_iterables(real_iterables(integers())))
def test_roundrobin(case: Case, x: Iterable[int], xs: Iterable[Iterable[int]]) -> None:
    y = case.cls(x).roundrobin(*xs)
    assert isinstance(y, case.cls)
    assert case.cast(y) == case.cast(roundrobin(x, *xs))


@given(start=integers(), n=islice_ints)
def test_tabulate(start: int, n: int) -> None:
    x = CIterable.tabulate(neg, start=start)
    assert isinstance(x, CIterable)
    assert list(islice(x, n)) == list(islice(tabulate(neg, start=start), n))


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()), n=integers(0, maxsize))
def test_tail(case: Case, x: Iterable[int], n: int) -> None:
    y = case.cls(x).tail(n)
    assert isinstance(y, case.cls)
    if case.ordered:
        assert case.cast(y) == case.cast(tail(n, x))


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()), n=integers(0, maxsize))
def test_take(case: Case, x: Iterable[int], n: int) -> None:
    y = case.cls(x).take(n)
    assert isinstance(y, case.cls)
    if case.ordered:
        assert case.cast(y) == case.cast(take(n, x))


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()), key=none() | just(neg))
def test_unique_everseen(
    case: Case, x: Iterable[int], key: Optional[Callable[[int], int]],
) -> None:
    y = case.cls(x).unique_everseen(key=key)
    assert isinstance(y, case.cls)
    if case.ordered:
        assert case.cast(y) == case.cast(unique_everseen(x, key=key))


@mark.parametrize("case", CASES)
@given(x=real_iterables(integers()), key=none() | just(neg))
def test_unique_justseen(
    case: Case, x: Iterable[int], key: Optional[Callable[[int], int]],
) -> None:
    y = case.cls(x).unique_justseen(key=key)
    assert isinstance(y, case.cls)
    if case.ordered:
        assert case.cast(y) == case.cast(unique_justseen(x, key=key))
