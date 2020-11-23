def solve():
    for i in range(N + 1):
        for j in range(N + 1 - i):
            k = N - i - j
            if Y == 10000 * i + 5000 * j + k * 1000:
                print(i, j, k)
                return
    print(-1, -1, -1)

N, Y = map(int, input().split())
solve()
