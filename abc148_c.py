from math import gcd


def solve():
    print(A * B // gcd(A, B))


A, B = map(int, input().split())
solve()
