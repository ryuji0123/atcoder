def solve():
    X.sort()
    ret = float('inf')
    for p in range(X[0], X[-1] + 1):
        ret = min(ret, sum([(p - x)**2 for x in X]))
    print(ret)


N = int(input())
X = list(map(int, input().split()))
solve()
