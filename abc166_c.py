# time: O(N + M)
# space: O(M)
from collections import defaultdict


def solve():
    print(sum([
        len(ref.get(i, [])) == 0 or all([H[j] < H[i] for j in ref[i]]) for i in range(N)
        ]))


N, M = map(int, input().split())
H = list(map(int, input().split()))
ref = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    ref[a - 1].append(b - 1)
    ref[b - 1].append(a - 1)

solve()
