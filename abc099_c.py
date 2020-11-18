from math import log


def solve():
    coins = sorted([1] + [pow(6, i) for i in range(1, int(log(N, 6) + 2))] + [pow(9, i) for i in range(1, int(log(N, 9) + 2))])
    lc = len(coins)
    dp = [0] + [float('inf')] * N
    for i in range(1, N + 1):
        idx = 0
        while idx < lc and coins[idx] <= i:
            dp[i] = min(dp[i], dp[i - coins[idx]] + 1)
            idx += 1
    print(dp[-1])


N = int(input())
solve()
