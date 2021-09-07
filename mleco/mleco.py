from itertools import combinations
from math import sqrt

from typing import List, Union

from mleco.types import Numbers


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


def covariance(*colls) -> List[float]:
    """
    Function for calculating covariance for more than two collections.

    It play around with combinations so that every element has a pair.
    """
    assert len(colls) > 1, "Too few collections"

    ln = len(colls[0])  # length of every collection, presumably
    assert all(len(c) == ln for c in colls), "Different-length collections"

    # averages: List[float] = [average(coll) for coll in colls]
    # colls_with_averages = zip(colls, averages)

    results = []

    pairs = combinations(colls, 2)
    for pair in pairs:
        f, s = pair  # first and second
        f_avg, s_avg = average(f), average(s)
        cov = sum((f - f_avg) * (s - s_avg) for x, y in zip(f, s)) / ln
        results.append(cov)

    return results


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
