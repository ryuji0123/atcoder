def solve():
    A, B = [], []
    for s in S:
        if s % 10 == 0:
            B.append(s)
        else:
            A.append(s)
    if len(A) == 0:
        print(0)
    else:
        sum_ = sum(A)
        sum_ -= sorted(A)[0] * (sum_ % 10 == 0)
        print(sum_ + sum(B))


N = int(input())
S = [int(input()) for _ in range(N)]
solve()
