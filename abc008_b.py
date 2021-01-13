from collections import Counter


def solve():
    counter = Counter(S)
    print(counter.most_common(1)[0][0])


N = int(input())
S = [input() for _ in range(N)]
solve()
