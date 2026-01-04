import unittest
import mean_var_std
import numpy as np


class UnitTests(unittest.TestCase):

    def test_calculate(self):
        actual = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        expected = {
            'mean': [3.0, 4.0, 5.0, 4.0],
            'variance': [6.0, 6.0, 6.0, 6.0],
            'standard deviation': [2.449489742783178, 2.449489742783178, 2.449489742783178, 2.449489742783178],
            'max': [6, 7, 8, 8],
            'min': [0, 1, 2, 0],
            'sum': [9, 12, 15, 36]
        }

        for key in expected:
            if isinstance(actual[key][0], float):
                np.testing.assert_almost_equal(actual[key], expected[key])
            else:
                self.assertEqual(actual[key], expected[key])

    def test_calculate_raises_error(self):
        self.assertRaises(ValueError, mean_var_std.calculate, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
