from math import sqrt

from typing import List, Union


Number = Union[int, float]


def average(data: List[Number]) -> float:
    """
    Calculates an arithmetic average.
    """
    return sum(data)/len(data)


def variance(data: List[Number]) -> float:
    """
    Calculates a variance.
    """
    avg = average(data)
    return sum((x-avg)**2 for x in data)/len(data)


def standard_deviation(data: List[Number]) -> float:
    return sqrt(variance(data))


def coefficient_of_variation(
    data: List[Number], in_percents: bool = False
) -> Union[str, float]:
    cov = standard_deviation(data)/average(data)
    if in_percents:
        return f'{cov*100:.2f}%'
    return cov


def handler(inpt: str) -> List[Number]:
    """
    Allows user to make input easier.

    Instead of fulfilling vector with comma-separated numbers,
    one can just write it as a string.

    Example:
    instead of: average([1, 6.2, 6, 3, 12, 5.4, 9])
    one can write: average("1 6.2 6 3 12 5.4 9")

    For me that's simply faster.
    """
    return [
        int(x) if float(x).is_integer else float(x)
        for x in inpt.split(" ")
    ]


h = handler
