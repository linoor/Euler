__author__ = 'linoor'

import unittest
import math
import itertools

def is_prime(n):
    if n == 1:
        return False
    else:
        if n < 4:
            return True
        else:
            if n % 2 == 0:
                return False
            else:
                if n < 9:
                    return True
                else:
                    if n % 3 == 0:
                        return False
                    else:
                        r = math.floor(math.sqrt(n))
                        f = 5
                        while f <= r:
                            if n % f == 0:
                                return False
                            if n % (f+2) == 0:
                                return False
                            f += 6
                        return True

def sieve():

    D = {}
    for q in itertools.count(2):
        p = D.pop(q, None)
        if p is None:
            yield q
            D[q*q] = q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p

def primes_less_than(n):

    return list(itertools.takewhile(lambda p: p < n, sieve()))

class Test(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(21))

    def test_sieve(self):
        self.assertEqual([2,3,5,7,11,13], primes_less_than(15))

if __name__ == "__main__":
    unittest.main()