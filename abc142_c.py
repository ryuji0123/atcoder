def solve():
    for idx, _ in sorted([[i + 1, a] for i, a in enumerate(A)], key=lambda x: x[1]):
        print(idx, end=' ')

N = input()
A = list(map(int, input().split()))
solve()
