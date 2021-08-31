from math import sqrt

from typing import Dict, List, Union


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


# TODO:
# For allowing calculations of covariance or pcc, we can make combinations
# out of available variables.
#
# from itertools import combinations
# list(map(lambda pair: covariance(*pair), combinations([ys, xs1, xs2], 2)))
# >>> [1208.5, 576.0, 546.0]
#
# list(map(lambda pair: pearson_correlation_coefficient(*pair), combinations([ys, xs1, xs2], 2)))
# [0.9714911154609688, 0.5691548168397905, 0.6446999952267405]


def pearson_correlation_coefficient(xs: List[Number], ys: List[Number]) -> float:
    """
    Calculates Pearson linear correlation coefficient.
    """

    # TODO: write implementation for more than one explanatory variable
    #       also do we need matrices?

    return covariance(xs, ys) / (standard_deviation(xs) * standard_deviation(ys))


def interpret_pcc(pcc: float) -> Dict[str, str]:
    """
    Function returns `pcc` which stands for
    *Pearson linear correlation coefficient*.
    """
    # TODO: make enum with decisions

    direction: str = ""

    if pcc == 0:
        direction = "no correlation"
    elif pcc > 0:
        direction = "positive"
    elif pcc < 0:
        direction = "negative"

    strength = ""

    pcc = abs(pcc)

    if pcc <= 0.2:
        strength = "no correlation or very weak"
    if pcc <= 0.4:
        strength = "weak"
    if pcc <= 0.7:
        strength = "moderate"
    if pcc <= 0.9:
        strength = "strong"
    if pcc <= 1:
        strength = "very strong"

    return {
        "direction": direction,
        "strength": strength
    }



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
