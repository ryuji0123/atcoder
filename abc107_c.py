def solve():
    ret = float('inf')
    for idx in range(N + 1 - K):
        if x[idx] * x[idx + K - 1] < 0:
            ret = min(ret, 2 * min(abs(x[idx]), abs(x[idx + K - 1])) + max(abs(x[idx]), abs(x[idx + K - 1])))
        else:
            ret = min(ret, max(abs(x[idx]), abs(x[idx + K - 1])))
    print(ret)


N, K = map(int, input().split())
x = list(map(int, input().split()))
solve()
