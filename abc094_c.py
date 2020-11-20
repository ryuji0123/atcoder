def solve():
    A = sorted(X)
    midx = N // 2
    for x in X:
        print(A[-midx] if x < A[-midx] else A[-1-midx])


N = int(input())
X = list(map(int, input().split()))
solve()
