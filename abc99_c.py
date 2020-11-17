def solve():
    print(1 + (N - K) // (K - 1) + ((N - K) % (K - 1) != 0))


N, K = map(int, input().split())
A = list(map(int, input().split()))
solve()
