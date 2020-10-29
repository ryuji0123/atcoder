from collections import deque


def solve():
    stack = deque([s for s in range(10)])
    while stack:
        val = stack.popleft()
        if len(str(val)) == N:
            val = str(val)
            if all([val[s[i]] == c[i] for i in range(M)]):
                print(val)
                return
            continue
        if val == 0:
            continue
        for v in range(10):
            stack.append(val * 10 + v)
    print(-1)


N, M = map(int, input().split())
s, c = [], []
for _ in range(M):
    tmp = list(input().split())
    s.append(int(tmp[0]) - 1)
    c.append(tmp[1])
solve()
