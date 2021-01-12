def solve():
    s = N[::-1]
    print(sum([0] + [int(s[idx]) for idx in range(1, len(N), 2)]), sum([int(s[idx]) for idx in range(0, len(N), 2)]))


N = input()
solve()
