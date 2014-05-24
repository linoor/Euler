__author__ = 'linoor'

__author__ = 'linoor'

import unittest
from fractions import Fraction
from operator import mul

def last_digit(n):
    return n % 10

def common_digits(denominator, numerator):
    return [x for x in set(str(numerator)) & set(str(denominator))]

def remove_digits(number, digits):
    number = str(number)

    for digit in digits:
        number = number.replace(str(digit), '')

    if number == '':
        return None

    return int(number)

def is_curious_fraction(numerator, denominator):

    if last_digit(numerator) == 0 or last_digit(denominator) == 0:
        return False

    common_digs = common_digits(numerator, denominator)

    new_num = remove_digits(numerator, common_digs)
    new_denom = remove_digits(denominator, common_digs)

    if not new_num or not new_denom:
        return False

    # reduced by Fraction class, guaranteed to be well reduced
    reduced = Fraction(numerator, denominator)

    changed = new_num != numerator or new_denom != denominator

    new_fraction = Fraction(new_num, new_denom)

    return new_fraction == reduced and changed

def main():

    fractions = []
    for i in range(10, 101):
        for j in range(10, 101):
            if i > j:
                continue
            if is_curious_fraction(i, j):
                fractions.append((i, j))

    print(fractions)
    assert len(fractions) == 4

    result = reduce(mul, [Fraction(x, y) for x, y in fractions], 1)
    print(result)

class Test(unittest.TestCase):


    def test_last_digit(self):

        self.assertEqual(last_digit(99), 9)
        self.assertEqual(last_digit(90), 0)
        self.assertEqual(last_digit(127), 7)
        self.assertEqual(last_digit(32), 2)
        self.assertEqual(last_digit(1), 1)

    def test_remove_common_digits(self):

        self.assertEqual(5, remove_digits(59, [9]))
        self.assertEqual(5, remove_digits(59, [9, 4]))
        self.assertEqual(4, remove_digits(49, [9]))
        self.assertEqual(8, remove_digits(98, [9]))
        self.assertNotEqual(48, remove_digits(48, [9, 4]))
        self.assertEqual(None, remove_digits(98, [9, 8]))

    def test_common_digits(self):

        self.assertEqual(['9'], common_digits(49, 98))
        self.assertEqual(['9', '5'], common_digits(495, 598))
        self.assertNotEqual(['8'], common_digits(43, 34))

    def test_curious_fractions(self):

        self.assertTrue(is_curious_fraction(49, 98))
        self.assertFalse(is_curious_fraction(10, 12))
        self.assertFalse(is_curious_fraction(12, 13))
        self.assertFalse(is_curious_fraction(30, 50))

if __name__ == '__main__':
    #unittest.main()
    main()
