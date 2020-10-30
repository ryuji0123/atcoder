def solve():
    ret = 0
    m = float('inf')
    for p in P:
        m = min(m, p)
        ret += p <= m
    print(ret)


N = int(input())
P = list(map(int, input().split()))
solve()
