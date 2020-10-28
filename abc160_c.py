def solve():
    A.sort()
    print(K - max([aj - ai for ai, aj in zip(A, A[1:])] + [A[0] + K - A[-1]]))

K, N = map(int, input().split())
A = list(map(int, input().split()))
solve()
