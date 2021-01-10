def solve():
    rate = 0
    for v in R[-K: ]:
        rate = (rate + v) / 2
    print(rate)


N, K = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
solve()
