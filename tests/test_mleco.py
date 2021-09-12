import unittest

import mleco as m


test_data = [1, 6, 6, 3, 12, 5, 9]
xs = ys = [1, 2]

# todo: unify the test data
# see: test_covariance


class TestMleco(unittest.TestCase):
    def test_average(self):
        assert m.average(test_data) == 6

    def test_variance(self):
        assert m.variance(test_data) == 11.428571428571429

    def test_standard_deviation(self):
        assert m.standard_deviation(test_data) == 3.3806170189140663

    def test_coefficient_of_variation_default(self):
        assert m.coefficient_of_variation(test_data) == 0.563436169819011

    def test_coefficient_of_variation_in_percents(self):
        assert m.coefficient_of_variation(test_data, in_percents=True) == "56.34%"

    def test_covariance(self):
        ys = [19, 21, 37, 14, 43]
        xs = [5, 8, 7, 3, 16]
        zs = [62, 92, 73, 103, 84]

        assert m.covariance(ys, xs, zs) == [
            41.35999999999999,
            -46.04,
            -3.839999999999999,
        ]

    def test_pearson_correlation_coefficient(self):
        raise NotImplementedError

    def test_pearson_correlation_coefficient_property_of_identity(self):
        assert m.pearson(xs, xs) == 1

    def test_pearson_correlation_coefficient_property_of_range(self):
        pcc = m.pearson(xs, ys)
        assert pcc >= 1 and pcc >= -1

    def test_all_combinations(self):
        raise NotImplementedError

    def test_hellwig_simple_case(self):
        raise NotImplementedError

    def test_linear_regression_simple(self):
        ys = [5, 2, 4, 3, 1, 6]
        xs = [2, 1, 5, 5, 3, 8]
        assert linear_regression(ys, xs) == 0.4375

    def test_linear_regression_wrong_lengths_of_vectors(self):
        ys = [5, 2, 4, 3, 1, 6]
        xs = [2, 1]
        # assert raises AssertionError("Vectors length disparity")
        assert linear_regression(ys, xs) == 0.4375

    def test_matrix_multiplication_by_other_matrix(self):
        pass

    def test_matrix_multiplication_by_vector(self):
        pass

    def test_matrix_multiplication_by_scalar(self):
        pass

    def test_matrix_multiplication_with_different_size(self):
        pass

    def test_matrix_str_representation(self):
        pass

    def test_matrix_transposing(self):
        pass


if __name__ == "__main__":
    unittest.main()
