def solve():
    N = max(2 * X, 2 * Y)
    ret = float('inf')
    for i in range(N + 1):
        ret = min(ret, A * max(0, X - i // 2) + B * max(0, Y - i // 2) + C * i)
    print(ret)


A, B, C, X, Y = map(int, input().split())
solve()
