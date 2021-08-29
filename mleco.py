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
    cfc = standard_deviation(data)/average(data)
    if in_percents:
        return f'{cfc*100:.2f}%'
    return cfc


def covariance(xs: List[Number], ys: List[Number]) -> float:
    assert len(xs) == len(ys)
    xs_avg, ys_avg = average(xs), average(ys)
    return sum((x - xs_avg)*(y - ys_avg) for x, y in zip(xs, ys))/len(xs)


def pearson_correlation_coefficient(xs: List[Number], ys: List[Number]) -> float:
    """
    Calculates Pearson linear correlation coefficient.
    """
    return covariance(xs, ys) / (variance(xs) * variance(ys))


def input_handler(inpt: str) -> List[Number]:
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


h = input_handler


def report_calculations(data: Union[List[Number], str]) -> dict:
    if isinstance(data, str):
        data = input_handler(data)

    return {
        "average": average(data),
        "variance": variance(data),
        "standard_deviation": standard_deviation(data),
        "coefficient_of_variation": coefficient_of_variation(data),
    }
