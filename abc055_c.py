def solve():
    if M <= 2 * N:
        ret = M // 2
    else:
        ret = N + (M - 2 * N) // 4
    print(ret)


N, M = map(int, input().split())
solve()
