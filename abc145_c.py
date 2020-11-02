from itertools import permutations
from math import sqrt

def solve():
    perms = permutations(range(N))
    ret = count = 0
    for perm in perms:
        count += 1
        for i, j in zip(perm, perm[1: ]):
            ret += sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
    print(ret / count)


N = int(input())
x, y = [], []
for _ in range(N):
    tmp = list(map(int, input().split()))
    x.append(tmp[0])
    y.append(tmp[1])
solve()
