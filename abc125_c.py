from math import gcd


def solve():
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    for idx in range(1, N + 1):
        L[idx] = gcd(L[idx - 1], A[idx - 1])
        R[N - idx] = gcd(R[N + 1 - idx], A[N - idx])
    print(max([gcd(L[idx], R[idx + 1]) for idx in range(N)]))


N = int(input())
A = list(map(int, input().split()))
solve()
