import math
import unittest

class Solution():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __repr__(self):
        return r'{{{0}, {1}, {2}}}'.format(self.a, self.b, self.c)

    def __eq__(self, other):
        items1 = [self.a, self.b, self.c]
        items2 = [other.a, other.b, other.c]

        return all([i in items1 for i in items2]) and all([i in items2 for i in items1])

def solutions(perimeter):
    sols = []
    p = perimeter
    for b in range(1, round(p/2)):
        a = int((2*p*b - p*p) / (2*b - 2*p))
        c = int(math.sqrt(a*a + b*b))
        solution = Solution(a, b, c)
        if solution.a + solution.b + solution.c == p:
            sols.append(solution)
    seen = []
    for s in sols:
        if s not in seen:
            seen.append(s)
    return seen

def number_of_sols(sols):
    return len(sols)

class SolutionsTests(unittest.TestCase):


    def test_equality(self):
        self.assertTrue(Solution(1,2,3) == Solution(3,2,1))

    def test_solution(self):
        self.assertEqual([Solution(20, 48, 52), Solution(24, 45, 51), Solution(30, 40, 50)], solutions(120))

    def test_number_of_solutions(self):
        self.assertEqual(number_of_sols(solutions(120)), 3)

if __name__ == "__main__":
    # unittest.main()
    max, p = 0, 0
    for i in range(1, 1000):
        number = number_of_sols(solutions(i))
        if number > max:
            max = number
            p = i
    print(max, p)
    print(solutions(840))
