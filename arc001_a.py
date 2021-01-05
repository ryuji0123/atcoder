from collections import Counter

def solve():
    counter = Counter(S)
    vals = list(counter.most_common())
    print(vals[0][1], vals[-1][1] if 2 <= len(vals) else 0)


N = input()
S = input()
solve()
