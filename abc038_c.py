def solve():
    ret = val = cur = 0
    for a in A:
        val = val + 1 if cur < a else 1
        ret += val
        cur = a
    print(ret)


N = input()
A = list(map(int, input().split()))
solve()
