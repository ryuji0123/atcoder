def solve():
    r = r2 - r1
    c = c2 - c1
    if (r, c) == (0, 0):
        ret = 0
    elif r == c or r == -c:
        ret = 1
    elif abs(r) + abs(c) <= 3:
        ret = 1
    elif (r ^ c ^ 1) & 1:
        ret = 2
    elif abs(r) + abs(c) <= 6:
        ret = 2
    elif abs(r + c) <= 3 or abs(r - c) <= 3:
        ret = 2
    else:
        ret = 3

    print(ret)


r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
solve()
