def solve():
    B = sorted([(idx + 1, a) for idx, a in enumerate(A)], key=lambda x: -x[1])
    for idx, _ in B:
        print(idx)


N = input()
A = list(map(int, input().split()))
solve()
