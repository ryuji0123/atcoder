def solve():
    cur = sum(A[: K])
    ret = cur
    for idx in range(K, N):
        cur += -A[idx - K] + A[idx]
        ret += cur
    print(ret)


N, K = map(int, input().split())
A = list(map(int, input().split()))
solve()
