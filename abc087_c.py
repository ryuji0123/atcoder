ROW_NUM = 2


def solve():
    dp = [[A[i][j] for j in range(N)] for i in range(ROW_NUM)]

    for i in range(ROW_NUM):
        for j in range(N):
            for x, y in [(i - 1, j), (i, j - 1)]:
                if 0 <= x < ROW_NUM and 0 <= y < N:
                    dp[i][j] = max(dp[i][j], A[i][j] + dp[x][y])
    print(dp[-1][-1])
                    

N = int(input())
A = [list(map(int, input().split())) for _ in range(ROW_NUM)]
solve()
