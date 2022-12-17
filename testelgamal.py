import unittest

from order import order
from primitiveroot import primitive_root
from bsgs import bsgs


class TestElgamal(unittest.TestCase):
    def test_order(self):
        # test Order that 5^6 mod 7 is 1
        self.assertEqual(order(5, 7, 6), 1)

    def test_primitive_root(self):
        self.assertEqual(primitive_root(37), 2)
        self.assertEqual(primitive_root(7919), 7)
        self.assertEqual(primitive_root(7), 3)

    def test_bsgs(self):
        self.assertEqual(bsgs(2, 16, 37), 4)



if __name__ == '__main__':
    unittest.main()