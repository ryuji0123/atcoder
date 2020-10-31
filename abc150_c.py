from itertools import permutations


def solve():
    p = list(permutations(list(range(1, N + 1))))
    print(abs(p.index(P) - p.index(Q)))


N = int(input())
P = tuple(list(map(int, input().split())))
Q = tuple(list(map(int, input().split())))
solve()
