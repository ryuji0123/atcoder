def solve():
    sref, tref = {}, {}
    for idx in range(N):
        if (S[idx] in sref and sref[S[idx]] != T[idx]) or (T[idx] in tref and tref[T[idx]] != S[idx]):
            print('No')
            return
        sref[S[idx]] = T[idx]
        tref[T[idx]] = S[idx]
    print('Yes')



S = input()
T = input()
N = len(S)
solve()
