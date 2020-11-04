def solve():
    ret = 0
    for i in range(N - 1, -1, -1):
        for j in range(i  +1, i - 1, -1):
            if A[j] <= B[i]:
                ret += A[j]
                B[i] -= A[j]
                A[j] = 0
            else:
                ret += B[i]
                A[j] -= B[i]
                B[i] = 0
    print(ret)


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
solve()
