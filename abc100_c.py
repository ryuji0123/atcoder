def solve():
    ret = 0
    for a in A:
        while a % 2 == 0:
            a //= 2
            ret += 1
    print(ret)


N = input()
A = list(map(int, input().split()))
solve()
