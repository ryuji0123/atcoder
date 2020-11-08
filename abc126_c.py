def solve():
    ret = 0
    for i in range(1, N + 1):
        c = i
        prob = 1 / N
        while c < K:
            c *= 2
            prob /= 2
        ret += prob
    print(ret)


N, K = map(int, input().split())
solve()
