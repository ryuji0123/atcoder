from math import log


def solve():
    A, B = int(log(N, 3)) + 2, int(log(N, 5)) + 2
    for i in range(A):
        for j in range(B):
            if 3 ** i + 5 ** j == N:
                print(i, j)
                return
    print(-1)


N = int(input())
solve()
