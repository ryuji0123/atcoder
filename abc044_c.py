def solve():
    X = max([A] + x)
    y = [x[i] - A for i in range(N)]
    dp = [[0 for _ in range(2 * N * X + 1)] for _ in range(N + 1)]
    for j in range(N + 1):
        for t in range(2 * N * X + 1):
            if j == 0 and t == N * X:
                dp[j][t] = 1
            elif 1 <= j and (t - y[j - 1] < 0 or 2 * N * X < t - y[j - 1]):
                dp[j][t] = dp[j - 1][t]
            elif 1 <= j and 0 <= t - y[j - 1] <= 2 * N * X:
                dp[j][t] = dp[j - 1][t] + dp[j - 1][t - y[j - 1]]
            else:
                dp[j][t] = 0
    print(dp[N][N * X] - 1)
                
    # dp = [[[0] * (N * X + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    # for j in range(N + 1):
    #     for k in range(N + 1):
    #         for s in range(N * X + 1):
    #             if j == k == s == 0:
    #                 dp[j][k][s] = 1
    #             elif 1 <= j and s < x[j- 1]:
    #                 dp[j][k][s] = dp[j - 1][k][s]
    #             elif 1 <= j and 1 <= k and x[j - 1] <= s:
    #                 dp[j][k][s] = dp[j - 1][k][s] + dp[j - 1][k - 1][s - x[j - 1]]
    #             else:
    #                 dp[j][k][s] = 0
    # print(sum([dp[N][k][k * A] for k in range(1, N + 1)]))


N, A = map(int, input().split())
x = list(map(int, input().split()))
solve()
