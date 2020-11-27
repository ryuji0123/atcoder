# time: O(F^2)
# space: O(F^2)
def solve():
    dp = [[False for _ in range(F + 1)] for _ in range(F + 1)]
    dp[0][0] = True
    pa = pb = 0
    for a in range(1, F + 1):
        for b in range(F - a + 1):
            if a * E < 100 * b or F < a + b:
                continue
            for da, db in [(100 * A, 0), (100 * B, 0), (0, C), (0, D)]:
                if 0 <= a - da and 0 <= b - db and dp[a - da][b - db]:
                    dp[a][b] = True
            if dp[a][b] and ((pa == 0 and pb == 0) or (pb * (a + b) < b * (pa + pb))):
                pa, pb = a, b

    print(pa + pb, pb)


A, B, C, D, E, F = map(int, input().split())
solve()
