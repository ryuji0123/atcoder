from collections import defaultdict


def solve():
    ref = defaultdict(int)
    for a in A:
        ref[a] += 1
    for i in range(1, N + 1):
        print(ref.get(i, 0))


N = int(input())
A = map(int, input().split())
solve()
