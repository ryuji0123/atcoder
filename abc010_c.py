from math import sqrt


def dist(sx, sy, tx, ty):
    return sqrt((sx - tx) ** 2 + (sy - ty) ** 2)


def solve():
    for x, y in A:
        if dist(x, y, tx1, ty1) + dist(tx2, ty2, x, y) <= V * T:
            print('YES')
            return
    print('NO')


tx1, ty1, tx2, ty2, T, V = map(int, input().split())
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
solve()
