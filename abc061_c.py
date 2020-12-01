from collections import Counter


def solve():
    counter = Counter()
    for a, b in A:
        counter[a] += b
    keys = sorted(counter.keys())
    c = 0
    idx = 0
    while True:
        if K <= c + counter[keys[idx]]:
            print(keys[idx])
            return
        c += counter[keys[idx]]
        idx += 1


N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
solve()
