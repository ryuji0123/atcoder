def solve():
    a, b, n = x, y, N
    ret = n
    while a <= n:
        div = n // a
        ret += b * div
        n = b * div + n % a
    print(ret)


x, y, N = map(int, input().split())
solve()
