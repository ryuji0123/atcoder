def solve():
    ret = [0] * (N + 1)
    for l, r in A:
        ret[l - 1] += 1
        ret[r] -= 1
    cur = 0
    for idx in range(N):
        cur += ret[idx]
        print(cur % 2, end='')
    print()


N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(Q)]
solve()
