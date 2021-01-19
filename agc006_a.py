def solve():
    idx = 0
    while idx < N:
        if s[idx: ] == t[: N - idx]:
            print(N + idx)
            return
        idx += 1
    print(2 * N)


N = int(input())
s = input()
t = input()
solve()
