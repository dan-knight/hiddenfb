from itertools import chain
from typing import List, Sequence, TypeVar, cast

T = TypeVar("T")


def flatten(rows: Sequence[List[T] | T]) -> List[T]:
    """
    Recursively flattens a list of a given type.
    """
    flattened = chain.from_iterable(
        [cast(List[T], x) if isinstance(x, list) else [x] for x in rows]
    )
    return list(flattened)
