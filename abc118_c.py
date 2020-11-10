from math import gcd


def solve():
    g = 0
    for a in A:
        g = gcd(g, a)
    print(g)


N = input()
A = list(map(int, input().split()))
solve()
