def solve():
    print((1900 * M + 100 * (N - M)) * pow(2, M))


N, M = map(int, input().split())
solve()
