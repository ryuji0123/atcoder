def solve():
    ret = 0
    for c in range(9):
        cur = None
        for r in range(N - 1, -1, -1):
            ret += x[r][c] == 'x' or (x[r][c] == 'o' and cur != 'o')
            cur = x[r][c]
    print(ret)


N = int(input())
x = [input() for _ in range(N)]
solve()
