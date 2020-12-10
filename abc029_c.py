from itertools import product


def solve():
    for v in product(['a', 'b', 'c'], repeat=N):
        print(''.join(v))


N = int(input())
solve()
