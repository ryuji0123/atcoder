from collections import deque

def solve(N, X, Y):
    ret = [0] * N
    already_used = [[False for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        already_used[i][i] = True
        reached = [False for _ in range(N + 1)]
        reached[i] = True
        stack = deque([[i, 0]])

        while stack:
            node, step = stack.popleft()
            if 1 <= step and not already_used[i][node]:
               ret[step] += 1
            already_used[i][node], already_used[node][i] = True, True

            for x in [node + 1, node - 1]:
                if 0 < x < N + 1 and not reached[x]:
                    stack.append([x, step + 1])
                    reached[x] = True
            if node == X and not reached[Y]:
                stack.append([Y, step + 1])
                reached[x] = True
            if node == Y and not reached[X]:
                stack.append([X, step + 1])
                reached[x] = True
    return ret

if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    for r in solve(N, X, Y)[1:]:
        print(r)