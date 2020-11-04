# time: O(N)
# space: O(N)
from collections import defaultdict


def solve():
    ref = defaultdict(int)
    ret = 0
    for k in s:
        ret += ref[k]
        ref[k] += 1
    print(ret)


N = int(input())
s = []
for _ in range(N):
    s.append(str(sorted(input())))
solve()
