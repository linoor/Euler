__author__ = 'linoor'

import unittest
import itertools


def is_palindrome(list):
    return str(list) == str(list)[::-1]


def get_palindromes(digits):
    k = digits
    return [int(''.join(map(str, (([x] + list(ys) + [z] + list(ys)[::-1] + [x]) if k % 2
                                  else ([x] + list(ys) + list(ys)[::-1] + [x])))))
            for x in range(1, 10)
            for ys in itertools.permutations(range(10), k / 2 - 1)
            for z in (range(10) if k % 2 else (None,))]


def main():
    palindromes = [x for x in range(1, 10)]
    for i in range(2, 7):
        palindromes.extend(get_palindromes(i))
    result = sum([x for x in palindromes if is_palindrome(bin(x)[2:])])
    print(result)


class Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(bin(585)[2:]))

        self.assertTrue(is_palindrome(101))
        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome("kajak"))
        self.assertTrue(is_palindrome(34343))
        self.assertTrue(is_palindrome(585))
        self.assertTrue(is_palindrome(1001001001))
        self.assertFalse(is_palindrome(1011001001))
        self.assertFalse(is_palindrome(1021001001))
        self.assertFalse(is_palindrome(10))
        self.assertFalse(is_palindrome("wut"))
        self.assertFalse(is_palindrome(211))


if __name__ == "__main__":
    #unittest.main()
    main()
