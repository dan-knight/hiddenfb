from typing import List

from hiddenfb.utility.list import flatten


def test__flatten__handles_list_of_single_elements():
    values: List[int] = [1, 2, 3, 4]

    result: List[int] = flatten(values)

    assert result == values


def test__flatten__handles_list_of_lists():
    values: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

    slice_index: int = 3
    input_values: List[List[int]] = [values[:slice_index], values[slice_index:]]

    result: List[int] = flatten(input_values)

    assert result == values


def test__flatten__handles_mixed_elements_and_lists():
    values: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    slice_index: int = 3
    input_values: List[int | List[int]] = values[:slice_index] + [values[slice_index:]]

    result: List[int] = flatten(input_values)

    assert result == values
