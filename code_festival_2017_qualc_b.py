from itertools import product


def solve():
    ret = 0
    for bins in product([0, 1, -1], repeat=N):
        ret += any([(A[i] + bins[i]) % 2 == 0 for i in range(N)])
    print(ret)


N = int(input())
A = list(map(int, input().split()))
solve()
