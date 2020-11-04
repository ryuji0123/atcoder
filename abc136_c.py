def solve():
    for i in range(N - 2, -1, -1):
        if A[i + 1] < A[i] - 1:
            print('No')
            return
        if A[i + 1] == A[i] - 1:
            A[i] -= 1
    print('Yes')

N = int(input())
A = list(map(int, input().split()))
solve()
