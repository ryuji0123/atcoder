from collections import Counter


def solve():
    counter = Counter(A)
    print(sum([c for _, c in counter.most_common()[K: ]]))


N, K = map(int, input().split())
A = list(map(int, input().split()))
solve()
