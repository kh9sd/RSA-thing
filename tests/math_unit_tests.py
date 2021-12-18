import unittest
from personal_math import *


class MathTests(unittest.TestCase):
    def test_gcf(self):
        self.assertEqual(gcf(4, 5), 1)
        self.assertEqual(gcf(4, 2), 2)
        self.assertEqual(gcf(10, 15), 5)

    def test_ext_euc_alg(self):
        self.assertEqual(ext_euc_alg(4, 5), (-1, 1))
        self.assertEqual(ext_euc_alg(64, 35), (-6, 11))
        self.assertEqual(ext_euc_alg(4, 2), (0, 1))
        self.assertEqual(ext_euc_alg(2, 2), (0, 1))

    def test_modular_inv(self):
        self.assertEqual(modular_inv(3, 26), 9)
        self.assertEqual(modular_inv(4, 5), 4)
        self.assertEqual(modular_inv(1, 6), 1)
        self.assertEqual(modular_inv(63, 65), 32)

    def test_chinese_rem(self):
        self.assertEqual(chinese_rem_thrm([5, 8, 35],
                                                               [29, 41, 37]),
                                 26453)
        self.assertEqual(chinese_rem_thrm([4, 12, 0],
                                                               [11, 13, 5]),
                                675)


if __name__ == '__main__':
    unittest.main()
