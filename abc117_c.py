def solve():
    X.sort()
    print(sum(sorted([xj - xi for xi, xj in zip(X, X[1: ])], reverse=True)[N - 1: ]))


N, M = map(int, input().split())
X = list(map(int, input().split()))
solve()
