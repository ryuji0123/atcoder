def solve(K):
    MOD = K
    a = 7
    for i in range(K):
        if a % MOD == 0:
            print(i + 1)
            return
        a = (10 * a + 7 ) % MOD
    print(-1)


solve(int(input()))
