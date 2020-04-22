from collections import deque

def bfs(start, maze, H, W):
    max_step = 0
    used = [[False for _ in range(W)] for _ in range(H)]
    start_x, start_y = start
    used[start_x][start_y] = True
    stack = deque([[start, 0]])
    while stack:
        (i, j), step = stack.popleft()
        if maze[i][j] == '#':
            continue
        max_step = max(max_step, step)
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < H and 0 <= y < W and not used[x][y]:
                stack.append([(x, y), step + 1])
                used[x][y] = True
    return max_step

if __name__ == '__main__':
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(list(input()))
    ret = 0
    for i in range(H):
        for j in range(W):
            ret = max(ret, bfs((i, j), S, H, W))
    print(ret)