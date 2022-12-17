import unittest

from exgcd import exgcd
from RSA import pick_e
from bbs import bbs
from euler_phi import euler_phi
from fastexp import fastexp
from gcd import gcd
from isprime import is_prime
from modinverse import modInverse
from pollardRho import pollardRho


class TestRSA(unittest.TestCase):
    def test_gcd(self):
        # bbs random s and n are 977 and 46883
        self.assertEqual(gcd(977,46883), 1)

    def test_exgcd(self):
        self.assertEqual(exgcd(63,57),(3,-9,10))

    def test_pollardRho(self):
        self.assertEqual(pollardRho(646184512626547),5057989)

    def test_fastexp(self):
        self.assertEqual(fastexp(2,5,7),4)

    def test_phi(self):
        self.assertEqual(euler_phi(46883),46440)

    def test_modinverse(self):
        self.assertEqual(modInverse(17,3120),2753)

    def test_miller_rabin(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(100))

        # test p,q in example
        self.assertTrue(is_prime(173))
        self.assertTrue(is_prime(271))

        # pollardRho factorization large number 646184512626547 get 5057989 and try prime test
        self.assertTrue(is_prime(5057989))
        self.assertTrue(is_prime(127755223))

        # 182096120426651 is the decimal number converted by Blum-Blum-Shub Pseudorandom Number Generator
        self.assertTrue(is_prime(182096120426651))


    def test_bbs(self):
        self.assertTrue(bbs(977),182096120426651)

    def test_e(self):
        self.assertTrue(gcd(pick_e(46440),46440),1)

    def test_d(self):
        self.assertTrue(modInverse(pick_e(46440),46440),1)

if __name__ == '__main__':
    unittest.main()