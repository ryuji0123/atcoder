def solve():
    print(pow(N // K, 3) + (K % 2 == 0) * pow(N // K + (K // 2 <= N % K), 3))


N, K = map(int, input().split())
solve()
