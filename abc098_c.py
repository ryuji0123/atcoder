def solve():
    lw, lc = [0] * (N + 1), 0
    re, rc = [0] * (N + 1), 0
    for idx in range(1, N + 1):
        lc += S[idx - 1] == 'W'
        lw[idx] = lc

        rc += S[N - idx] == 'E'
        re[N - idx] = rc
    
    ret = float('inf')
    for idx in range(N):
        ret = min(ret, lw[idx] + re[idx + 1])
    print(ret)


N = int(input())
S = input()
solve()
