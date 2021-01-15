def solve():
    s = S
    for l, r in orders:
        a, b = l - 1, r - 1
        s = s[: a] + s[a: b + 1][:: -1] + s[b + 1: ]
    print(s)


S = input()
N = int(input())
orders = [list(map(int, input().split())) for _ in range(N)]
solve()
