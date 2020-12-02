from collections import Counter


def solve():
    counters = [Counter(s) for s in S]
    cur = counters[0]
    for counter in counters[1: ]:
        for k in cur.keys():
            cur[k] = min(cur[k], counter[k])
    print(''.join(sorted([e * c for e, c in cur.items()])))


N = int(input())
S = [input() for _ in range(N)]
solve()
