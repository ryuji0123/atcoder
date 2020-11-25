from itertools import product


REPEAT = 10


def solve():
    ret = float('-inf')
    for bits in product(range(2), repeat=REPEAT):
        if sum(bits) == 0:
            continue

        val = 0
        for i in range(N):
            c = sum([bits[t] * F[i][t] for t in range(REPEAT)])
            val += P[i][c] 
        ret = max(ret, val)
    print(ret)


N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
solve()
