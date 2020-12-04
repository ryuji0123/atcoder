def solve():
    d, m = divmod(x, 11)
    print(2 * d + m // 6 + (m % 6 != 0))

x = int(input())
solve()
