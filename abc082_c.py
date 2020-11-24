from collections import Counter


def solve():
    counter = Counter(A)
    print(sum([c - e if e <= c else c for e, c in counter.items()]))


N = input()
A = list(map(int, input().split()))
solve()
