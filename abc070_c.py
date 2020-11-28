from functools import reduce
from math import gcd


def lcm_base(x, y):
    return (x * y) // gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def solve():
    print(lcm_list(T))


N = int(input())
T = [int(input()) for _ in range(N)]
solve()
