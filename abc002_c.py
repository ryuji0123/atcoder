def solve():
    x1, y1 = A[2] - A[0], A[3] - A[1]
    x2, y2 = A[4] - A[0], A[5] - A[1]
    print(abs(x1 * y2 - x2 * y1) / 2)


A = list(map(int, input().split()))
solve()
