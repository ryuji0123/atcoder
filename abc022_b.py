from collections import Counter


def solve():
    counter = Counter(A)
    print(sum([c - 1 for c in counter.values()]))


N = int(input())
A = [input() for _ in range(N)]
solve()
