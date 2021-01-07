def solve():
    d = sorted([(idx, s[::-1]) for idx, s in enumerate(S)], key=lambda x: x[1])
    for idx, _ in d:
        print(S[idx])

N = int(input())
S = [input() for _ in range(N)]
solve()
