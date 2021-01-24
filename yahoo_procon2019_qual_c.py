def solve():
    if K - 1 < A or B - A < 2:
        print(1 + K)
        return

    if 1 < A:
        count = A - 1
        ret = A
    else:
        count = 0
        ret = 1
    d, m = divmod(K - count, 2)
    ret += (B - A) * d
    print(ret + (m == 1))



K, A, B = map(int, input().split())
solve()
