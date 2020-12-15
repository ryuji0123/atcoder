def solve():
    ret = set()
    for a in A:
        while a % 2 == 0:
            a //= 2
        ret.add(a)
    print(len(ret))


N = input()
A = list(map(int, input().split()))
solve()
