__author__ = 'linoor'

import unittest
from primes import primes_less_than
from collections import defaultdict
import itertools as it

def get_rotations(n):

    n = str(n)
    result = [n]
    rotation = n
    while True:
        rotation = move_digits_left(rotation)
        if rotation == n:
            break
        result.append(rotation)
    result = map(int, result)
    result = [x for x in result if len(str(x)) == len(n)]
    return result

def move_digits_left(n):
    n_str = str(n)
    return n_str[1:]+n_str[0]

def circular_primes(limit):

    result = []
    primes = primes_less_than(limit)
    primes_dict = defaultdict(bool)
    for p in primes:
        primes_dict[p] = True

    count = 0
    for p in primes:
        if p in result:
            continue
        rotations = get_rotations(p)
        if all([primes_dict[x] == True for x in rotations]):
            for r in rotations:
                result.append(r)
    return sorted(result)


def main():

    print(len(circular_primes(1000000)))

class Test(unittest.TestCase):


    def test_get_rotations(self):
        self.assertEqual(get_rotations(197), [197, 971, 719])
        self.assertEqual(get_rotations(2), [2])
        self.assertEqual(get_rotations(101), [101, 110])
        self.assertEqual(get_rotations(97), [97, 79])
        self.assertEqual(get_rotations(11), [11])
        self.assertEqual(get_rotations(131), [131, 311, 113])

    def test_move_digits_left(self):
        self.assertEqual(move_digits_left(101), '011')
        self.assertEqual(move_digits_left(197), '971')
        self.assertEqual(move_digits_left(131), '311')
        self.assertEqual(move_digits_left(11), '11')
        self.assertEqual(move_digits_left(17), '71')
        self.assertEqual(move_digits_left(5432), '4325')
        self.assertEqual(move_digits_left(345463), '454633')

    def test_example(self):
        self.assertEqual(circular_primes(100), [2,3,5,7,11,13,17,31,37,71,73,79,97])
        self.assertEqual(len(circular_primes(100)), 13)
        self.assertEqual(len(circular_primes(102)), 13)

if __name__ == "__main__":
    #unittest.main()
    main()
