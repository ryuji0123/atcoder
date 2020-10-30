def solve():
    print(sum(sorted(H, reverse=True)[K: ]))


N, K = map(int, input().split())
H = list(map(int, input().split()))
solve()
