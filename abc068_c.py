from collections import defaultdict


def solve():
    for b in neighborhoods[1]:
        if N in neighborhoods[b]:
            print('POSSIBLE')
            return
    print('IMPOSSIBLE')


N, M = map(int, input().split())
neighborhoods = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    neighborhoods[a].add(b)
    neighborhoods[b].add(a)
solve()
