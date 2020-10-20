MOD = pow(10, 9) + 7


def solve(N, A):
    ret = 0
    tmp = A[0] % MOD
    for a in A[1: ]:
        ret = (ret + tmp * a) % MOD
        tmp = (tmp + a) % MOD
    print(ret)


N = int(input())
A = list(map(int, input().split()))
solve(N, A)
