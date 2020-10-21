def solve(X, K, D):
    if K * D < abs(X):
        print(abs(X) - K * D)
        return
    div = abs(X) // D
    print(abs(X) - div * D if (K - div) % 2 == 0 else D * (div + 1) - abs(X))



solve(*map(int, input().split()))
