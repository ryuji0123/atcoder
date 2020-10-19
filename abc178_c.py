MOD = pow(10, 9) + 7

def p(b, n):
    return pow(b, n, MOD)

def solve(N):
    print((p(10, N) - 2 * p(9, N) + p(8, N)) % MOD)


N = int(input())
solve(N)
