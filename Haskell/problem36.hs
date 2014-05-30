import Numeric
import Data.Char

isPalindrome x = x == reverse x

toBinary x = showIntAtBase 2 intToDigit x ""

palindromes = [ x | x <- [1..1000000], isPalindrome(show x), isPalindrome(toBinary x)]

problem_36 = sum palindromes