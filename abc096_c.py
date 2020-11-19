def solve():
    for i in range(H):
        for j in range(W):
            if s[i][j] == '#' and all([s[x][y] == '.' for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] if 0 <= x < H and 0 <= y < W]):
                print('No')
                return
    print('Yes')


H, W = map(int, input().split())
s = []
for _ in range(H):
    s.append(input())
solve()
