from itertools import combinations
from math import sqrt

from typing import List, Union

Numbers = List[Union[int, float]]


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

    return results[0] if len(results) == 1 else results


def pearson(*colls) -> Union[float, List[float]]:
    """
    Calculates Pearson linear correlation coefficient among every combination
    that occurs in the `colls`.
    """
    assert len(colls) > 1, "Too few collections"

    sd = standard_deviation  # shorten the name for inline usage

    results = [(covariance(*p) / sd(p[0]) * sd(p[1])) for p in combinations(colls, 2)]
    return results[0] if len(results) == 1 else results


def all_combinations(*colls) -> List:
    """
    Given arbitrary number of collections, creates list of every possible
    combination except the ones with duplications within one case.
    """
    return [subset for r in range(len(colls) + 1) for subset in combinations(colls, r)]


def hellwig(vec_r0: Numbers, vec_r: Numbers):
    # all_c = all_combinations(*colls)

    """
    Picks the preferable set of explaining variables by its
    integral indicator of information capacity.

    :param vec_r0: vector cotaining results of Pearson's correlation between
                    Y and explaining variables,
    :param vec_r: matrix containing results of Pearson's correlation among
                    explaining variables themselves.

    :return: [tbd]
    """
    assert len(vec_r0) == len(vec_r), "Matrices' size disparity"

    return


td = [1, 2, 3]

# test data
ys = [19, 21, 37, 14, 43]
xs = [5, 8, 7, 3, 16]
zs = [62, 92, 73, 103, 84]

# test data for minimal examples
# ys = [8, 10, 16, 22, 30, 37]
# xs = [14, 15, 16, 27, 25, 30]
pearson(ys, xs, zs)
