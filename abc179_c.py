def solve(N):
    ret = 0
    for a in range(1, N):
        ret += (N - 1) // a
    print(ret)


N = int(input())
solve(N)
