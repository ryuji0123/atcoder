from math import gcd


def solve():
    dists = [abs(X - xi) for xi in x]
    g = 0
    for d in dists:
        g = gcd(g, d)
    print(g)



N, X = map(int, input().split())
x = list(map(int, input().split()))
solve()
