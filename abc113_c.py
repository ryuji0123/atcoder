# time: O(NlogN)
# space: O(N)
from collections import defaultdict


def solve():
    ret = ['' for _ in range(M)]
    for k in ref.keys():
        ref[k].sort(key=lambda x: x[1])
        p = str(k).zfill(6)
        for x, (i, _) in enumerate(ref[k]):
            ret[i] = p + str(x + 1).zfill(6)

    for i in range(M):
        print(ret[i])


N, M = map(int, input().split())
ref = defaultdict(list) 
p_y = []
for i in range(M):
    p_y.append(list(map(int, input().split())))
    ref[p_y[-1][0]].append([i, p_y[-1][1]])
solve()
