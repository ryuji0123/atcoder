def solve():
    bins = bin(X)[2: ].zfill(N)[:: -1]
    print(sum([int(bins[i]) * a[i] for i in range(N)]))


N, X = map(int, input().split())
a = list(map(int, input().split()))
solve()
