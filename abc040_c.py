def solve():
    dp = [0] + [float('inf') for _ in range(N - 1)]
    for i in range(1, N):
        tmp = [dp[j] + abs(A[i] - A[j]) for j in [i - 1, i - 2] if 0 <= j]
        dp[i] = min(tmp)
    print(dp[N - 1])

N = int(input())
A = list(map(int, input().split()))
solve()
