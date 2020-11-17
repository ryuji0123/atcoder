def solve():
    m = (A[N // 2] + A[N // 2 - 1]) // 2 if N % 2 == 0 else A[N // 2]
    print(sum([abs(a - m) for a in A]))


N = int(input())
A = list(map(int, input().split()))
A = sorted([a - (idx + 1) for idx, a in enumerate(A)])
solve()
