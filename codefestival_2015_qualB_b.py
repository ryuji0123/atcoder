from collections import Counter


def solve():
    counter = Counter(A)
    items = counter.most_common()
    print(items[0][0] if N // 2 < items[0][1] else '?')


N, _ = map(int, input().split())
A = list(map(int, input().split()))
solve()
