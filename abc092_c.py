def solve():
    def costFromLeftAndRight(N, A):
        B = [0] + A + [0]
        N += 2
        L = [0] * N
        R = [0] * N
        for idx in range(1, N):
            L[idx] = L[idx - 1] + abs(B[idx] - B[idx - 1])
            R[N - 1 - idx] = R[N - idx] + abs(B[N - 1 - idx] - B[N - idx])
        return L, R, B, N

    L, R, B, LN = costFromLeftAndRight(N, A)
    for i in range(1, LN - 1):
        print(L[i - 1] + abs(B[i - 1] - B[i + 1]) + R[i + 1])


N = int(input())
A = list(map(int, input().split()))
solve()
