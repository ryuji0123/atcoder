def solve():
    ret = K[::] + [K[-1]]
    for i in range(1, N - 1):
        ret[i] = min(K[i - 1], K[i])
    print(' '.join([str(r) for r in ret]))


N = int(input())
K = list(map(int, input().split()))
solve()
