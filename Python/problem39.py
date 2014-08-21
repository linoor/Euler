import math
import unittest
from collections import namedtuple

class Solution():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c =

    def __eq__(self, other):
        items1 = [self.a, self.b, self.c]
        items2 = [other.a, other.b, other.c]
        return all([i in items2 for ic in items1]) and all([i in items1 for i in items2])

    def __hash__(self):
        return hash()

# Solution = namedtuple('Solution', 'a b c')

def solutions(perimeter):
    sols = []
    p = perimeter
    for b in range(1, p/2):
        a = (2*p*b - p*p) / (2*b - 2*p)
        c = int(math.sqrt(a*a + b*b))
        solution = Solution(a, b, c)
        if sum([solution.a, solution.b, solution.c]) == p:
            sols.append(solution)
    return list(set(sols))

def checkEqual(l1, l2):
    return len(l1) == len(l2) and sorted(l1) == sorted(l2)

class SolutionsTests(unittest.TestCase):


    def test_solution(self):
        print(solutions(120))
        self.assertTrue(checkEqual([Solution(20, 48, 52), Solution(24, 45, 51), (30, 40, 50)], solutions(120)))

if __name__ == "__main__":
    unittest.main()