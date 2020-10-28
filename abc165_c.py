from collections import deque


def solve():
    stack = deque()
    for i in range(1, M + 1):
        stack.append([i])
    ret = 0
    while stack:
        A = stack.pop()
        if len(A) == N:
            tmp_ret = 0
            for i in range(Q):
                tmp_ret += d[i] * (A[b[i]] - A[a[i]] == c[i])
            ret = max(ret, tmp_ret)
            continue
        for i in range(A[-1], M + 1):
            stack.append(A + [i])
    print(ret)


N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for _ in range(Q):
    tmp = list(map(int, input().split()))
    a.append(tmp[0] - 1)
    b.append(tmp[1] - 1)
    c.append(tmp[2])
    d.append(tmp[3])

solve()
