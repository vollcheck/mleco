from itertools import combinations
from math import sqrt

from typing import List, Union

from types import Numbers


def average(xs: Numbers) -> float:
    """
    Calculates an arithmetic average.
    """
    return sum(xs) / len(xs)


def variance(xs: Numbers) -> float:
    """
    Calculates a variance.
    """
    avg = average(xs)
    return sum((x - avg) ** 2 for x in xs) / len(xs)


def standard_deviation(data: Numbers) -> float:
    return sqrt(variance(data))


def coefficient_of_variation(
    data: Numbers, in_percents: bool = False
) -> Union[str, float]:
    cfc = abs(standard_deviation(data) / average(data))

    if in_percents:
        return f"{cfc*100:.2f}%"
    return cfc


def covariance(xs: Numbers, ys: Numbers, *args) -> float:
    assert len(xs) == len(ys), "Different-length collections"
    xs_avg, ys_avg = average(xs), average(ys)
    return sum((x - xs_avg) * (y - ys_avg) for x, y in zip(xs, ys)) / len(xs)


def covariance_m(*colls) -> List[float]:
    """
    Function for calculating covariance for more than two collections.
    """

    assert len(colls) > 1, "Too few collections"
    assert all(len(c) == len(colls[0]) for c in colls), "Wrong length of one of the collections"

    averages: List[float] = [average(coll) for coll in colls]

    colls_with_averages = zip(colls, averages)

    # pairs are being made in greedy-per-collection manner:
    # given x1, x2, x3 collections,
    # it will exhaust x1, later x2 and eventually x3
    # x1-x2, x1-x3, x2-x3
    # also, how it would look like in the matrices?
    pairs = combinations(colls, 2)

    for idx, coll in enumerate(colls):
        pass


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


def pearson_correlation_coefficient(xs: Numbers, ys: Numbers) -> float:
    """
    Calculates Pearson linear correlation coefficient.
    """

    # TODO: write implementation for more than one explanatory variable
    #       also do we need matrices?

    return covariance(xs, ys) / (standard_deviation(xs) * standard_deviation(ys))


def hellwig(*colls):
    # To be implemented
    pass
