from collections import Counter


def solve():
    counter = Counter(A)
    print(sum([c % 2 == 1 for e, c in counter.items()]))


N = int(input())
A = [int(input()) for _ in range(N)]
solve()
