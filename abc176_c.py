def solve(N, A):
    ret = 0
    M = A[0]
    for a in A[1: ]:
        if M <= a:
            M = a
        else:
            ret += M - a
    print(ret)


N = int(input())
A = list(map(int, input().split()))
solve(N, A)
