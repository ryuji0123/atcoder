def solve():
    N = len(s)
    if N != len(t):
        print(-1)
        return
    idx = N
    while 0 <= idx:
        if s[idx: ] + s[: idx] == t:
            print(N - idx)
            return
        idx -= 1
    print(-1)


s = input()
t = input()
solve()
