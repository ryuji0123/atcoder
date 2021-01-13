def solve():
    ret = B // 4 - A // 4
    ret -= B // 100 - A // 100
    ret += B // 400 - A // 400
    print(ret)


A, B = map(int, input().split())
A -= 1
solve()
