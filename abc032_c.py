def solve():
    if 0 in S:
        print(N)
        return
    r = ret = 0
    cur = 1 
    for l in range(N):
        while r < N and cur * S[r] <= K:
            cur *= S[r]
            r += 1
        ret = max(ret, r - l)
        if l == r:
            r += 1
        else:
            cur //= S[l]

    print(ret)

N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]
solve()
