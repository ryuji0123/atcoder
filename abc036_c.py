def solve():
    B = sorted(set(A))
    hash_ = {k: idx for idx, k in enumerate(B)}
    for a in A:
        print(hash_[a])


N = int(input())
A = [int(input()) for _ in range(N)]
solve()
