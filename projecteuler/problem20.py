# PROBLEM 20

# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
import sys


def factorial(num):
    x = int(num)
    if x < 0:
        print 'Invalid Input!'
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def sum_digits(num):
    result = expand(num)
    total = 0
    for l in result:
        total += int(l)
    return total


def expand(num):
    return str(num)


def solve(num):
    return sum_digits(factorial(num))


num = sys.argv[1]
print ('The sum of all digits of the factorial result is: ' + str(solve(num)))

