# time: O(N)
# space: O(N)

def solve():
    MOD = pow(10, 9) + 7
    dp = [1] + [0] * N
    for i in range(1, N + 1):
        if i in a:
            dp[i] = float('inf')
        else:
            if 0 <= i - 1 and dp[i - 1] != float('inf'):
                dp[i] = (dp[i] + dp[i - 1]) % MOD
            if 0 <= i - 2 and dp[i - 2] != float('inf'):
                dp[i] = (dp[i] + dp[i - 2]) % MOD
    print(dp[-1])


N, M = map(int, input().split())
a = set()
for _ in range(M):
    a.add(int(input()))
solve()
