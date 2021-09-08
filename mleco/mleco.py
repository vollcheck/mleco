from functools import lru_cache
from itertools import combinations
from math import sqrt

from typing import List, Union

from mleco.types import Numbers


@lru_cache
def average(xs: Numbers) -> float:
    """
    Calculates an arithmetic average.
    """
    return sum(xs) / len(xs)


@lru_cache
def variance(xs: Numbers) -> float:
    """
    Calculates a variance.
    """
    avg = average(xs)
    return sum((x - avg) ** 2 for x in xs) / len(xs)


@lru_cache
def standard_deviation(data: Numbers) -> float:
    return sqrt(variance(data))


def coefficient_of_variation(
    data: Numbers, in_percents: bool = False
) -> Union[str, float]:
    cfc = abs(standard_deviation(data) / average(data))

    if in_percents:
        return f"{cfc*100:.2f}%"
    return cfc


@lru_cache
def covariance(*colls) -> Union[float, List[float]]:
    """
    Function for calculating covariance for more than two collections.

    It plays around with combinations so that every element has a pair.
    """
    assert len(colls) > 1, "Too few collections"

    ln = len(colls[0])  # length of every collection, presumably
    assert all(len(c) == ln for c in colls), "Different-length collections"

    averages: List[float] = [average(coll) for coll in colls]
    averages_indexes = list(combinations(range(len(colls)), 2))

    pairs = combinations(colls, 2)

    results = []

    for idx, pair in enumerate(pairs):
        f, s = pair
        number_f, number_s = averages_indexes[idx]
        f_avg, s_avg = averages[number_f], averages[number_s]
        cov = sum((x - f_avg) * (y - s_avg) for x, y in zip(f, s)) / ln
        results.append(cov)

    if len(results) == 1:
        return results[0]
    return results


@lru_cache
def pearson(*colls) -> Union[float, List[float]]:
    """
    Calculates Pearson linear correlation coefficient among every combination
    that occurs in the `colls`.
    """
    sd = standard_deviation  # shorten the name for inline usage
    results = [(covariance(*p) / sd(p[0]) * sd(p[1])) for p in combinations(colls, 2)]

    if len(results) == 1:
        return results[0]
    return results


def hellwig(*colls):
    # To be implemented
    pass
