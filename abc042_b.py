def solve():
    print(''.join(sorted(S)))


N, L = map(int, input().split())
S = [input() for _ in range(N)]
solve()
