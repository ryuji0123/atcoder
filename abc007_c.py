from collections import deque


def solve():
    used = [[False for _ in range(C)] for _ in range(R)]
    stack = deque([(sx, sy, 0)])
    while stack:
        x, y, step = stack.popleft()
        if x == gx  and y == gy:
            print(step)
            return

        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= i < R and 0 <= j < C and not used[i][j] and c[i][j] == '.':
                stack.append([i, j, step + 1])
                used[i][j] = True


R, C = map(int, input().split())
tmp = list(map(int, input().split()))
sx, sy = tmp[0] - 1, tmp[1] - 1
tmp = list(map(int, input().split()))
gx, gy = tmp[0] - 1, tmp[1] - 1
c = [input() for _ in range(R)]
solve()
