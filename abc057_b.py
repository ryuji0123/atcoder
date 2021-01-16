def solve():
    ret = [1] * N
    for i, (a, b) in enumerate(A):
        m = float('inf')
        for j, (c, d) in enumerate(B):
            dist = abs(c - a) + abs(d - b)
            if dist < m:
                ret[i] = j + 1
                m = dist
    for r in ret:
        print(r)


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(M)]
solve()
