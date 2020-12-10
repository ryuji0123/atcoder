def solve():
    print(sum(['0' not in c for c in S.split('+')]))


S = input()
solve()
