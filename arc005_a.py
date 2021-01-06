from collections import Counter


def solve():
    counter = Counter(w)
    keys = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']
    print(sum([counter[k] for k in keys]))


N = input()
w = list(input()[: -1].split())
solve()
