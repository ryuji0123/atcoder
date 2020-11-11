# time: O(4^N)
# space: O(4^N)

from itertools import product


def solve():
    ret = float('inf')
    for p in product(range(4),repeat=N):
        tmp = [0, 0, 0]
        cost = 0
        for i, v in enumerate(p):
            if v == 3:
                continue
            cost += (0 < tmp[v]) * 10
            tmp[v] += l[i]
        if any([t == 0 for t in tmp]):
            continue
        ret = min([ret, cost + sum(abs(tmp[idx] - target[idx]) for idx in range(3))])
    print(ret)


N, A, B, C = map(int, input().split())
target = sorted([A, B, C])
l = []
for _ in range(N):
    l.append(int(input()))
solve()
