def solve():
    if Y % 400 == 0:
        ret = 'YES'
    elif Y % 100 == 0:
        ret = 'NO'
    elif Y % 4 == 0:
        ret = 'YES'
    else:
        ret = 'NO'
    print(ret)


Y = int(input())
solve()
