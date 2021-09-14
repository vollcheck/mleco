from itertools import combinations
from math import sqrt
from typing import List, Union, Dict

from mleco import Numbers


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


def _all_combinations(*colls) -> List:
    """
    Helper function.

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


def linear_regression(ys: Numbers, xs: Numbers) -> Dict[str, float]:
    """
    Calculates regression for formula with only one variable.
    """
    assert len(xs) == len(ys), "Vectors length disparity"

    xs_avg, ys_avg = average(xs), average(ys)

    a1 = sum((x - xs_avg) * (y - ys_avg) for x, y in zip(xs, ys)) / sum(
        (x - xs_avg) ** 2 for x in xs
    )

    a0 = ys_avg - a1 * xs_avg

    return {"a0": a0, "a1": a1, "model formula": f"^Yt = {a0} + {a1}Xt"}


def multiple_regression(*colls) -> dict:
    """
    Calculates regression for formula with more than one variable.
    """
    pass
