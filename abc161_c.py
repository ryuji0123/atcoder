def solve():
    m = N % K
    print(min(m, K - m))


N, K = map(int, input().split())
solve()
