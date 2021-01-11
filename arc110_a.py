from math import gcd


def solve():
    ret = 1
    for i in range(2, N + 1):
        ret = ret * i // gcd(ret, i)
    print(ret + 1)


N = int(input())
solve()
