"""
Module with functions that helps with dealing with formulas and reporting its results.
"""

from typing import Dict, Union

# from types import Numbers


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

    return {"direction": direction, "strength": strength}


def input_handler(inpt: str) -> Numbers:
    """
    Allows user to make input easier.

    Instead of fulfilling vector with comma-separated numbers,
    one can just write it as a string.

    Example:
    instead of: average([1, 6.2, 6, 3, 12, 5.4, 9])
    one can write: average("1 6.2 6 3 12 5.4 9")

    For me that's simply faster.
    """
    return [int(x) if float(x).is_integer() else float(x) for x in inpt.split(" ")]


h = input_handler


def report_calculation(data: Union[Numbers, str]) -> dict:
    """
    Performs all steps required to calculate coefficient of variation of the
    given vector.
    """
    if isinstance(data, str):
        data = input_handler(data)

    return {
        "average": average(data),
        "variance": variance(data),
        "standard_deviation": standard_deviation(data),
        "coefficient_of_variation": coefficient_of_variation(data),
    }


def report_calculations(xs: Union[Numbers, str], ys: Union[Numbers, str]) -> dict:
    """
    Performs all steps required to calculate Pearson linear correlation coefficient
    between two vectors.

    :TODO: allow function process more than two vectors
    """

    def validate(coll: Union[Numbers, str]) -> Numbers:
        if isinstance(coll, str):
            return input_handler(coll)

    xs, ys = [validate(coll) for coll in [xs, ys]]

    return {
        # todo: rewrite that to minimize the boilerplate
        "xs": {
            "average": average(xs),
            "variance": variance(xs),
            "standard_deviation": standard_deviation(xs),
        },
        "ys": {
            "average": average(ys),
            "variance": variance(ys),
            "standard_deviation": standard_deviation(ys),
        },
        "covariance": covariance(xs, ys),
        "pearson_correlation_coefficient": pearson_correlation_coefficient(xs, ys),
    }
