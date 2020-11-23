def solve():
    ret = 1
    i = X
    while 2 * i <= Y:
        i *= 2
        ret += 1
    print(ret)


X,Y = map(int, input().split())
solve()
