# rime: O(NlogN)
# space: O(1)
import bisect


def solve():
    lx = rx = X
    p.sort()
    while True:
        idx = bisect.bisect_left(p, lx)
        if N <= idx or lx != p[idx]:
            print(lx)
            return
        idx = bisect.bisect_left(p, rx)
        if N <= idx or rx != p[idx]:
            print(rx)
            return
        lx -= 1
        rx += 1


X, N = map(int, input().split())
p = list(map(int, input().split()))
solve()
