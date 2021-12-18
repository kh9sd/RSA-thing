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

    def test_binary_list(self):
        self.assertEqual(num_to_binary_list(19), [1, 0, 0, 1, 1])
        self.assertEqual(num_to_binary_list(123), [1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(num_to_binary_list(32), [1, 0, 0, 0, 0, 0])
        self.assertEqual(num_to_binary_list(31), [1, 1, 1, 1, 1])
        self.assertEqual(num_to_binary_list(1), [1])

    def test_mod_expo(self):
        self.assertEqual(mod_expo(11,3,19), 1)
        self.assertEqual(mod_expo(11, 1, 19), 11)
        self.assertEqual(mod_expo(11, 2, 19), 7)
        self.assertEqual(mod_expo(11, 4, 19), 11)
        self.assertEqual(mod_expo(72, 84, 64), 0)
        self.assertEqual(mod_expo(73, 84, 64), 33)
        self.assertEqual(mod_expo(71, 84, 64), 33)
        self.assertEqual(mod_expo(19, 24, 34), 1)



if __name__ == '__main__':
    unittest.main()
