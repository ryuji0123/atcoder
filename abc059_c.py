def calc(mod):
    ret = cur = 0
    for idx, a in enumerate(A):
        cur += a
        if idx % 2 == mod:
            if cur <= 0:
                ret += -cur + 1
                cur = 1
        else:
            if 0 <= cur:
                ret += cur + 1
                cur = -1
    return ret


def solve():
    print(min([calc(mod) for mod in range(2)]))


N = int(input())
A = list(map(int, input().split()))
solve()
