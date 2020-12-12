MOD = 30

def solve():
    n = N % MOD
    A = list(range(1, 7))
    for i in range(n):
        A[i % 5], A[i % 5 + 1] = A[i % 5 + 1], A[i % 5]
    for a in A:
        print(a, end='')
    print()


N = int(input())
solve()
