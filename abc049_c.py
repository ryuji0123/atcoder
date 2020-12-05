def solve():
    N = len(S)
    dp = [True] + [False for _ in range(N)]
    for i in range(1, N + 1):
        for t in T:
            if len(t) <= i and dp[i - len(t)] and S[i - len(t): i] == t:
                dp[i] = True
    print('YES' if dp[N] else 'NO')


S = input()
T = ['dream', 'dreamer', 'erase', 'eraser']
solve()
