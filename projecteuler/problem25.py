'''
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

#The answer is F(4782)
'''

from math import *
import sys


def memoize(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]


def F_closed(n):
    assert n > 0, 'A Fibonacci index must be greater than zero.'
    a = (1 + sqrt(5.0)) ** n
    b = (1 - sqrt(5.0)) ** n
    numerator = a - b
    denominator = (2 ** n * sqrt(5))
    result = numerator / denominator
    return result


@memoize
def F(n):
    return n if n < 2 else F(n - 2) + F(n - 1)


def find_first(n_start, n_digits):
    n = n_start
    while True:
        if check_bound(F(n), n_digits):
            break
        else:
            n = n + 1
    return n


def check_bound(num, n_digits):
    bound = (10 ** (n_digits-1))
    if num >= bound:
        return True
    else:
        return False


start_index = int(sys.argv[1])  # The Fibonacci index to start at
n_digits = int(sys.argv[2])  # The number of digits to find
print 'The smallest Fibonacci index with more than '+str(n_digits)+' digits is '+str(find_first(start_index, n_digits))+'.'
