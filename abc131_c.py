from math import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)


def solve():
    l = lcm(C, D)
    ret = B - A + 1
    ret -= B // C - (A - 1) // C
    ret -= B // D - (A - 1) // D
    ret += B // l - (A - 1) // l
    print(ret)



A, B, C, D = map(int, input().split())
solve()
