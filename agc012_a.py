def solve():
    sorted_A = sorted(A, reverse=True)
    print(sum([sorted_A[idx] for idx in range(1, 2 * N, 2)]))


N = int(input())
A = list(map(int, input().split()))
solve()
