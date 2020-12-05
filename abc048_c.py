def cost(A):
    A = A[::]
    ret = 0
    for i in range(N - 1):
        if A[i] + A[i + 1] <= x:
            continue
        if A[i] <= x:
            ret += A[i + 1] - (x - A[i])
            A[i + 1] = x - A[i]
        else:
            ret += A[i + 1] + A[i] - x
            A[i] = x
            A[i + 1] = 0
    return ret


def solve():
    print(min(cost(A), cost(A[::-1])))


N, x = map(int, input().split())
A = list(map(int, input().split()))
solve()
