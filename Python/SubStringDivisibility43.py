__author__ = 'Linoor'
import time
start_time = time.time()

import itertools

def filter_pandigitals(start, end, divisor, pandigitals):
    return list(filter(lambda x: int(x[start-1:end]) % divisor == 0, pandigitals))

pandigitals = range(0,10)
pandigitals = list(map(str, pandigitals))
pandigitals = list(itertools.permutations(pandigitals))
pandigitals = [''.join(i) for i in pandigitals]

pandigitals = filter_pandigitals(8, 10, 17, pandigitals)
pandigitals = filter_pandigitals(7, 9, 13, pandigitals)
pandigitals = filter_pandigitals(6, 8, 11, pandigitals)
pandigitals = filter_pandigitals(5, 7, 7, pandigitals)
pandigitals = filter_pandigitals(4, 6, 5, pandigitals)
pandigitals = filter_pandigitals(3, 5, 3, pandigitals)
pandigitals = filter_pandigitals(2, 4, 2, pandigitals)
print(sum(map(int, pandigitals)))
print(time.time() - start_time)
