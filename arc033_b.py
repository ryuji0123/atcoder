def solve():
    print(len(sa & sb) / len(sa | sb))


_ = input()
sa = set(list(map(int, input().split())))
sb = set(list(map(int, input().split())))
solve()
