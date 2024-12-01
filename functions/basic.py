#include <stdlib.h>
import os

def sum_arg1(a, b, c=None):
    if c == None:
        result = a + b
    else:
        result = a + b + c

    return result

def sum_args2(*args):
    total = 0
    for number in args:
        total += number

    return total

os.system('cls')

total = sum_arg1(1, 2)
print(total)
total = sum_arg1(1, 2, 1)
print(total)

total = sum_args2(1, 2, 3, 4, 5, 6)
print(total)