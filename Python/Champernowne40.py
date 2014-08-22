from functools import reduce

__author__ = 'Linoor'

if __name__ == "__main__":
    c = '0'
    for i in range(1, 1000001):
        c += str(i)
    result = reduce(lambda x, y: x * y, (map(int, [c[1], c[10], c[100], c[1000], c[10000], c[100000], c[1000000]])))
    print(result)
