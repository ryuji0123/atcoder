# time: O(E(N + E))
# space: O(N + E)
from collections import defaultdict, deque


def solve():
    ret = 0
    for a, b in edges:
        seen = {n: False for n in range(1, N + 1)}
        seen[1] = True
        stack = deque([1])
        while stack:
            node = stack.pop()
            for n in neighborhoods[node]:
                if not seen[n] and sorted([node, n]) != [a, b]:
                    stack.append(n)
                    seen[n] = True

        ret += any([not is_seen for is_seen in seen.values()])
    print(ret)


neighborhoods = defaultdict(list)
edges = []
N, M = map(int, input().split())
for _ in range(M):
    a, b = map(int, input().split())
    neighborhoods[a].append(b)
    neighborhoods[b].append(a)
    edges.append(sorted([a, b]))
solve()
