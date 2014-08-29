import unittest
import math
import time

def isPentagonal(n):
    return ((math.sqrt(24*n+1)+1) / 6).is_integer()

def pentagonal(n):
    return (n*(3*n-1))/2

start_time = time.time()

i = 1
found = False
while not found:
   second = pentagonal(i)
   for j in range(i-1, 1, -1):
       first = pentagonal(j)
       if isPentagonal(second - first) and isPentagonal(first + second):
           result = (first, second)
           found = True
           break
   i += 1
print(result[1] - result[0])
print(time.time() - start_time)

class PentagonTests(unittest.TestCase):


    def test_pentagon_test(self):
        self.assertTrue(isPentagonal(1))
        self.assertTrue(isPentagonal(5))
        self.assertTrue(isPentagonal(12))
        self.assertTrue(isPentagonal(22))
        self.assertTrue(isPentagonal(35))
        self.assertFalse(isPentagonal(0))
        self.assertFalse(isPentagonal(2))
        self.assertFalse(isPentagonal(3))
        self.assertFalse(isPentagonal(7))
        self.assertFalse(isPentagonal(118))
        self.assertFalse(isPentagonal(9))

if __name__ == "__main__":
    unittest.main()
