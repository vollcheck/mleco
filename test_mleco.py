import mleco


test_data = [1, 6, 6, 3, 12, 5, 9]


def test_average(data):
    assert mleco.average(data) == 6


def test_variance(data):
    assert mleco.variance(data) == 11.428571428571429


def test_standard_deviation(data):
    assert mleco.standard_deviation(data) == 3.3806170189140663


def test_coefficient_of_variation_default(data):
    assert mleco.coefficient_of_variation(data) == 0.563436169819011


def test_coefficient_of_variation_in_percents(data):
    assert mleco.coefficient_of_variation(data, in_percents=True) == "56.34%"
